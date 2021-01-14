# -*- coding: utf-8 -*-
###############################################################################
# --- F_03__OTpFunctions.py ---------------------------------------------------
###############################################################################
import os, copy
from operator import itemgetter
import numpy as np
import pandas as pd

import Core.C_00__GenConstants as GC
import Core.F_00__GenFunctions as GF

# --- Functions (general) -----------------------------------------------------
def getPF(sP, sD, sF, sFExt = GC.S_EXT_CSV):
    return GF.joinToPath(os.path.join(sP, sD), sF + '.' + sFExt)

def savePdDfr(dIG, pdDfr, sD, sF, overWr = True, sFExt = GC.S_EXT_CSV):
    sP = getPF(dIG['sPRes'], sD, sF, sFExt = sFExt)
    if not os.path.isfile(sP) and overWr:
        pdDfr.to_csv(sP, sep = dIG['cSep'])
    return sP

def saveAsPdDfr(dIG, dRes, sD, sF, overWr = True, sFExt = GC.S_EXT_CSV):
    sP = getPF(dIG['sPRes'], sD, sF, sFExt = sFExt)
    if not os.path.isfile(sP) or overWr:
        pd.DataFrame(dRes).to_csv(sP, sep = dIG['cSep'])
    return sP

# --- Functions (O_00__Base) --------------------------------------------------
def getDITp(dIG, iTp, lITpU):
    dITp = {}
    if len(lITpU) > 0:
        dITp = copy.deepcopy(dIG[lITpU[0]])     # content of lITpU[0] input
        for iTpU in lITpU[1:]:
            GF.updateDITpDIPlt(dITp, dIG[iTpU]) # updated with iTpU input
    GF.updateDITpDIPlt(dITp, dIG[iTp])          # updated with iTp input
    return dITp

# --- Functions (O_03__Metabolite) --------------------------------------------
def doSinChange(x, dPar):
    if GC.S_PERIOD_CHG in dPar and GC.S_AMPL_CHG in dPar:
        cPeriod, cAmplit = dPar[GC.S_PERIOD_CHG], dPar[GC.S_AMPL_CHG]
        return cAmplit*np.sin(x*2*np.pi/cPeriod)
    else:
        return 0.0

def doStepChange(x, dPar):
    if (GC.S_STEP_T1 in dPar and GC.S_STEP_T2 in dPar and
        GC.S_STEP_V01 in dPar and GC.S_STEP_V12 in dPar and
        GC.S_STEP_V2T in dPar):
        if x < dPar[GC.S_STEP_T1]:
            return dPar[GC.S_STEP_V01]
        elif (x >= dPar[GC.S_STEP_T1] and x < dPar[GC.S_STEP_T2]):
            return dPar[GC.S_STEP_V12]
        else:
            return dPar[GC.S_STEP_V2T]
    else:
        return 0.0

# --- Functions (O_80__Interaction) -------------------------------------------
def doSiteChange(cO, sSpS, lSCpAs, doPyl = True):
    opDone = False
    assert sSpS in cO.dSpS
    cSpS = cO.dSpS[sSpS]
    if doPyl and cSpS.sSPTM == GC.S_NOT_PYL:
        for sCpAs in lSCpAs:
            if sCpAs in cSpS.lPyl:
                cSpS.sSPTM = GC.S_IS_PYL
                opDone = True
                break
    elif not doPyl and cSpS.sSPTM == GC.S_IS_PYL:
        for sCpAs in lSCpAs:
            if sCpAs in cSpS.lDPy:
                cSpS.sSPTM = GC.S_NOT_PYL
                opDone = True
                break
    return opDone

# --- Functions (O_90_Component) ----------------------------------------------
def createLSCp(inpDt, lOAll, sPylDPy = GC.S_DO_PYL):
    lSCp = []
    for cO in lOAll:
        for cSpS in cO.dITp['dInfSpS']:
            for sCp in cO.dITp['dInfSpS'][cSpS][sPylDPy]:
                if sCp not in lSCp:
                    lSCp.append(sCp)
    return sorted(lSCp)

# --- Functions (O_99__System) ------------------------------------------------
def createDCnc(inpFr):
    dCncIni = {}
    for sSMo, dIni in inpFr.dParCnc.items():
        cTp, dPar = dIni[GC.S_INI_CNC_DISTR]
        dCncIni[sSMo] = GF.drawFromDist(cTp, dPar)
    return dCncIni

def iniDictOut(inpFr, dCnc, t = 0., tDlt = 0.):
    dO = {'dN': {}, 'dH': {}, 'h': 0., 'tDlt': tDlt, 'dCncIni': {},
          'dCncChgInt': {}, 'dRes': {GC.S_TIME: [t]}}
    for s, cCnc in dCnc.items():
        dO['dRes'][s] = [cCnc]
        dO['dCncIni'][s] = cCnc
        dO['dCncChgInt'][s] = 0.
    for s, k in inpFr.dNCpObj.items():
        dO['dRes'][s] = [k]
        dO['dN'][s] = k
    return dO

def changeCncSMo(inpFr, dO, dCncSMo, t, cID = None):
    for sSMo in dCncSMo:
        assert sSMo in inpFr.dParCnc
        cD, cncChgSMo, cncChgExt = inpFr.dParCnc[sSMo], 0., 0.
        cncMn, cncMx = cD[GC.S_CNC_MIN], cD[GC.S_CNC_MAX]
        for s, nO in dO['dN'].items():
            ss = s.replace(GC.S_DASH, '')
            assert ss in inpFr.dSMoCncDepOnCp[sSMo]
            cncChgSMo += inpFr.dSMoCncDepOnCp[sSMo][ss]*nO
        # component-distribution-dependent (internal) conc. change
        nCpO = sum(dO['dN'].values())
        cncChgInt = cncChgSMo*dO['tDlt']/nCpO*inpFr.dOthInpV['cncChgScale']
        dO['dCncChgInt'][sSMo] += cncChgInt
        # externally forced conc. change
        cTp, dPar = cD[GC.S_CNC_CHG_MODE]
        if cTp == GC.S_CH_SIN:
            cncChgExt = doSinChange(t, dPar)
        elif cTp == GC.S_CH_STEP:
            cncChgExt = doStepChange(t, dPar)
        dCncSMo[sSMo] = dO['dCncIni'][sSMo]
        dCncSMo[sSMo] += dO['dCncChgInt'][sSMo] + cncChgExt
        dCncSMo[sSMo] = GF.implMinMax(dCncSMo[sSMo], cncMn, cncMx)

def incorpEnzyme(dICp, dO, lSPyl, lSDPy, sRct, sRctCl, sSpS):
    x, sPylDPy = 0., GC.S_DO_PYL
    if sRctCl in lSPyl:
        sPylDPy = GC.S_DO_PYL
    elif sRctCl in lSDPy:
        sPylDPy = GC.S_DO_DPY
    for sCpAse in dICp[sPylDPy][sSpS]:
        x += dO['dN'][sCpAse]
    dO['dH'][sRct] *= x

def updateDictH(dICp, inpFr, dO, dCncSMo):
    sSMoN, p = GC.ID_NO3_1M, GC.P_DUMMY
    lSPyl, lSDPy = inpFr.dClRct[GC.S_DO_PYL], inpFr.dClRct[GC.S_DO_DPY]
    # update the reaction rate constants according to the current [NO3-]
    for sRct, wtRct in inpFr.dRct.items():
        # NO3- dependency of incidences of each component
        sRctType, sRctClass, _ = inpFr.dTpRct[sRct]
        assert (len(GF.splitStr(sRctClass)) >= 2 and sRctClass in
                inpFr.dCpDepOnSMoCnc[sSMoN])
        b = sRctClass in lSPyl + lSDPy
        sSpS = GF.splitStr(sRctClass)[1]
        dParPSig = inpFr.dCpDepOnSMoCnc[sSMoN][sRctClass]
        p = GF.calcPSigmoidal(dCncSMo[sSMoN], dParPSig)
        # recalculate dH, which contains the h_i (i = 1,... len(dH))
        dO['dH'][sRct] = wtRct*p
        for sCpLHS in GF.partStr(sRct)[0]:
            dO['dH'][sRct] *= dO['dN'][sCpLHS]
        if b:   # check if reaction is (de)phosphorylation
            incorpEnzyme(dICp, dO, lSPyl, lSDPy, sRct, sRctClass, sSpS)
        if (sRctType in GC.L_S_RCT_2ORD or b):
            dO['dH'][sRct] /= inpFr.dOthInpV['VolC']
    # (?) update the reaction rate constants according to the current [H2PO4-]

def reCalcReactHazards(dICp, inpFr, dO, dCncSMo):
    updateDictH(dICp, inpFr, dO, dCncSMo)
    # h, the sum of the h_i, is the overall reaction hazard
    dO['h'] = sum(dO['dH'].values())
    # sort dH in ascending order for numerical stability
    dO['dH'] = {cK: cV/dO['h'] for cK, cV in
                sorted(dO['dH'].items(), key = itemgetter(1))}

def eventReactionSys(dO):
    # get the string consisting of the LHS and RHS of the reaction
    sRct = GF.getSRct(dO['dH'])
    # update the numbers of component objects in dO['dN']
    llSCmp = GF.partStr(sRct)
    assert len(llSCmp) >= 2
    for k, lSCmp in enumerate(llSCmp):
        for sCmp in lSCmp:
            assert sCmp in dO['dN']
            if k == 0:              # left-hand side of the reaction equation
                dO['dN'][sCmp] -= 1
            elif k == 1:            # right-hand side of the reaction equation
                dO['dN'][sCmp] += 1

def nextEvent(dO, T, cTS):
    if dO['h'] > 0:    # otherwise the while-loop ends, see the other case
        # draw the time to the next event from exponential(lambd = 1./h)
        dO['tDlt'] = GF.drawFromDist('exponential', dPar = {'h': dO['h']})
        # adapt the event reactions to considered system
        eventReactionSys(dO)
    else:
        # if no reaction is possible, then h becomes 0, therefore stop
        print('The combined reaction hazard is 0 - no reaction possible')
        dO['tDlt'] = T - dO['dRes'][GC.S_TIME][cTS]
    return dO['tDlt']

def updateDictOut(dO, dCnc, t):
    dO['dRes'][GC.S_TIME].append(t)
    for s, cCnc in dCnc.items():
        dO['dRes'][s].append(cCnc)
    for s, nO in dO['dN'].items():
        dO['dRes'][s].append(nO)

def evolveGillespie(dIG, dICp, inpFr, dCncSMo):
    # initialisation
    t, T, tDelta, cTSt = dIG['tStart'], dIG['tMax'], 0, 0
    dO = iniDictOut(inpFr, dCncSMo, t, tDelta)
    reCalcReactHazards(dICp, inpFr, dO, dCncSMo)
    while t < T and cTSt < dIG['maxTS']:
        cTSt += 1
        if cTSt >= dIG['minDispTS'] and cTSt%dIG['modDispTS'] == 0:
            print('Reached time step', cTSt, 'at time', round(t, GC.R04))
        # do next event and update time with tToNext
        t += nextEvent(dO, T, cTSt)
        # change the concentrations of the small molecules
        changeCncSMo(inpFr, dO, dCncSMo, t)
        # adapt the re-calc reaction hazards function to current system
        reCalcReactHazards(dICp, inpFr, dO, dCncSMo)
        # update the data storage matrix
        updateDictOut(dO, dCncSMo, t)
    return dO['dRes'], dO['dN']

def getPFResEvo(dIG, dITp, sFRs):
    pFRes = getPF(dIG['sPRes'], dITp['sD_Sys'], sFRs, sFExt = GC.S_EXT_CSV)
    if os.path.isfile(pFRes):
        return GF.readCSV(pFRes, iCol = 0)
    return None

def getDPFPltEvo(dIG, dITp, tKey, dMS = None):
    dP = {}
    if dMS is None:
        sF = GC.S_USC.join([str(cEl) for cEl in tKey if cEl is not None])
        dP[getPF(dIG['sPPlt'], dITp['sD_Sys'], sF, sFExt = GC.S_EXT_PDF)] = dMS
    else:
        for sMS, dCp in dMS.items():
            sF = str(tKey[0]) + GC.S_USC + sMS
            if tKey[1] is not None:
                sF +=  GC.S_USC + str(tKey[1])
            pF = getPF(dIG['sPPlt'], dITp['sD_Sys'], sF, sFExt = GC.S_EXT_PDF)
            dP[pF] = (sMS, dCp)
    return dP

###############################################################################
