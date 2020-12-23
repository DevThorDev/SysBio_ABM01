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

# --- Functions (O_80__Interaction) -------------------------------------------
def doSiteChange(cO, sSpS, sAse, doDePyl = False):
    opDone = False
    assert sSpS in cO.dSpS
    cSpS = cO.dSpS[sSpS]
    if not doDePyl and cSpS.sSPTM == GC.S_NOT_PYL and sAse in cSpS.lPyl:
        cSpS.sSPTM = GC.S_IS_PYL
        opDone = True
    elif doDePyl and cSpS.sSPTM == GC.S_IS_PYL and sAse in cSpS.lDPy:
        cSpS.sSPTM = GC.S_NOT_PYL
        opDone = True
    return opDone

# --- Functions (O_90_Component) ----------------------------------------------
def complLSpec(inpDt, lOAll, sPylDPy = GC.S_DO_PYL):
    lID = []
    for cO in lOAll:
        for cSpS in cO.dITp['dInfSpS']:
            for idTp in cO.dITp['dInfSpS'][cSpS][sPylDPy]:
                if idTp not in lID:
                    lID.append(idTp)
    return sorted(lID)

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
            assert ss in inpFr.dCncChgSMo[sSMo]
            cncChgSMo += inpFr.dCncChgSMo[sSMo][ss]*nO
        # component-distribution-dependent (internal) conc. change
        nCpO = sum(dO['dN'].values())
        cncChgInt = cncChgSMo*dO['tDlt']/nCpO*inpFr.dOthInpV['cncChgScale']
        dO['dCncChgInt'][sSMo] += cncChgInt
        # externally forced conc. change
        cTp, dPar = cD[GC.S_CNC_CHG_MODE]
        if cTp == GC.S_CH_SIN:
            cncChgExt = doSinChange(t, dPar)
        elif cTp == GC.S_CH_STEP:
            pass
        dCncSMo[sSMo] = dO['dCncIni'][sSMo]
        dCncSMo[sSMo] += dO['dCncChgInt'][sSMo] + cncChgExt
        dCncSMo[sSMo] = GF.implMinMax(dCncSMo[sSMo], cncMn, cncMx)

def updateDictH(inpFr, dO, dCncSMo):
    dRUp, sSMoN, p = {}, GC.ID_NO3_1M, GC.P_DUMMY
    # update the reaction rate constants according to the current [NO3-]
    for sRct, wtRct in inpFr.dRct.items():
        # NO3- dependency of incidences of each component
        sRctType, dRctType = inpFr.dTpRct[sRct]
        for sK in dRctType:
            if sK in inpFr.dChgCncDep[sSMoN]:
                dParPSig = inpFr.dChgCncDep[sSMoN][sK]
                p = GF.calcPSigmoidal(dCncSMo[sSMoN], dParPSig)
                break
        dRUp[sRct] = wtRct*p
        # recalculate dH, which contains the h_i (i = 1,... len(dH))
        dO['dH'][sRct] = dRUp[sRct]
        for sCpLHS in GF.partStr(sRct)[0]:
            dO['dH'][sRct] *= dO['dN'][sCpLHS]
        if sRctType in [GC.S_RCT_21, GC.S_RCT_22]:
            dO['dH'][sRct] /= inpFr.dOthInpV['VolC']
    # (?) update the reaction rate constants according to the current [H2PO4-]

def reCalcReactHazards(inpFr, dO, dCncSMo):
    updateDictH(inpFr, dO, dCncSMo)
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

def evolveGillespie(dIG, inpFr, dCncSMo):
    # initialisation
    t, T, tDelta, cTSt = dIG['tStart'], dIG['tMax'], 0, 0
    dO = iniDictOut(inpFr, dCncSMo, t, tDelta)
    reCalcReactHazards(inpFr, dO, dCncSMo)
    while t < T and cTSt < dIG['maxTS']:
        cTSt += 1
        if cTSt >= dIG['minDispTS'] and cTSt%dIG['modDispTS'] == 0:
            print('Reached time step', cTSt, 'at time', round(t, GC.R04))
        # do next event and update time with tToNext
        t += nextEvent(dO, T, cTSt)
        # change the concentrations of the small molecules
        changeCncSMo(inpFr, dO, dCncSMo, t)
        # adapt the re-calc reaction hazards function to current system
        reCalcReactHazards(inpFr, dO, dCncSMo)
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
