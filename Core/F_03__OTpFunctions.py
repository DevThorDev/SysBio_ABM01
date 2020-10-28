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
def doSinChange(x, cPer, cAmpl):
    return cAmpl*np.sin(x*2*np.pi/cPer)

# --- Functions (O_80__Interaction) -------------------------------------------
def doSiteChange(cO, sSpS, sAse, doDePyl = False):
    opDone = False
    assert sSpS in cO.dSpS
    cSpS = cO.dSpS[sSpS]
    if not doDePyl and cSpS.sSPTM == GC.B_NOT_PYL and sAse in cSpS.lPyl:
        cSpS.sSPTM = GC.B_IS_PYL
        opDone = True
    elif doDePyl and cSpS.sSPTM == GC.B_IS_PYL and sAse in cSpS.lDePyl:
        cSpS.sSPTM = GC.B_NOT_PYL
        opDone = True
    return opDone

# --- Functions (O_90_Component) ----------------------------------------------
def complLSpec(inpDt, lOAll, sTp = 'KAs', sD = 'Pyl'):
    lID = []
    for cO in lOAll:
        for cSpS in cO.dITp['dInfSpS']:
            for idTp in GF.getLFromLIt(cO.dITp['dInfSpS'][cSpS][sD]):
                if idTp not in lID:
                    lID.append(idTp)
    return sorted(lID)

# --- Functions (O_99__System) ------------------------------------------------
def createDCnc(dITp):
    dCI = dITp['dConcSMo']['Ini']
    return {s: GF.drawFromDist(dCI[s]['cTp'], dCI[s]['dPar']) for s in dCI}

def iniDictOut(dITp, dCnc, t = 0., tDlt = 0.):
    dO = {'dN': {}, 'dH': {}, 'h': 0., 'tDlt': tDlt, 'dRes': {GC.S_TIME: [t]}}
    for s, cCnc in dCnc.items():
        dO['dRes'][s] = [cCnc]
    for s, k in dITp['dNCpObj'].items():
        dO['dRes'][s] = [k]
        dO['dN'][s] = k
    return dO

def changeConcSMo(dITp, dO, dCncSMo, cID = None, dspI = False):
    if dspI:
        pass
    dMin, dMax = dITp['dConcSMo']['Min'], dITp['dConcSMo']['Max']
    for sSMo in dCncSMo:
        cncCh = 0.
        for s in dO['dN']:
            assert s in dITp['dConcChg'][sSMo]
            cncCh += dITp['dConcChg'][sSMo][s]['absChg']*dO['dN'][s]
        dCncSMo[sSMo] += cncCh*dO['tDlt']/dITp['nCpObj']*dITp['concChgScale']
        dCncSMo[sSMo] = GF.implMinMax(dCncSMo[sSMo], dMin[sSMo], dMax[sSMo])

def updateDictH(dITp, dO, dCncSMo, dspI = False):
    dRRC, dCncCh, dRUp = dITp['dRRC'], dITp['dConcChg'], {}
    sMoN, sMoP = GC.ID_NO3_1M, GC.ID_H2PO4_1M
    # update the reaction rate constants according to the current [NO3-]
    for tS, tRRC in dRRC.items():
        assert len(tS) == len(tRRC)
        for k, s in enumerate(tS):
            p = GF.calcPSigmoidal(dCncSMo[sMoN], dCncCh[tS][sMoN][k])
            dRUp[s] = tRRC[k]*p
            # recalculate dH, which contains the h_i (i = 1,... len(dH))
            dO['dH'][s] = dRUp[s]*dO['dN'][s.split(GC.S_USC)[0]]
    # (?) update the reaction rate constants according to the current [H2PO4-]
    if dspI:
        pass

def reCalcReactHazards(dITp, dO, dCncSMo, dspI = False):
    updateDictH(dITp, dO, dCncSMo, dspI = dspI)
    # h, the sum of the h_i, is the overall reaction hazard
    dO['h'] = sum(dO['dH'].values())
    # sort dH in ascending order for numerical stability
    dO['dH'] = {cK: cV/dO['h'] for cK, cV in
                sorted(dO['dH'].items(), key = itemgetter(1))}
    if dspI:
        pass

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

def nextEvent(dITp, dO, T, cTS):
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

def updateDictOut(dITp, dO, dCnc, t):
    dO['dRes'][GC.S_TIME].append(t)
    for s, cCnc in dCnc.items():
        dO['dRes'][s].append(cCnc)
    for s in dO['dN']:
        dO['dRes'][s].append(dO['dN'][s])

def evolveGillespie(dIG, dITp, dCncSMo):
    t, T, tDelta, cTSt = dIG['tStart'], dIG['tMax'], 0, 0
    dO = iniDictOut(dITp, dCncSMo, t, tDelta)
    while t < T and cTSt <= dIG['maxTS']:
        dspCnd = (cTSt >= dIG['minDispTS'] and cTSt%dIG['modDispTS'] == 0)
        if dspCnd:
            print('Reached time step', cTSt, 'at time', round(t, GC.R04))
        # change the concentrations of the small molecules
        changeConcSMo(dITp, dO, dCncSMo, dspI = dspCnd)
        # adapt the re-calc reaction hazards function to current system
        reCalcReactHazards(dITp, dO, dCncSMo, dspI = dspCnd)
        # do next event and update time with tToNext
        t += nextEvent(dITp, dO, T, cTSt)
        # update the data storage matrix
        if t < T:
            updateDictOut(dITp, dO, dCncSMo, t)
        cTSt += 1
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
