# -*- coding: utf-8 -*-
###############################################################################
# --- F_03__OTpFunctions.py ---------------------------------------------------
###############################################################################
import os, copy
import numpy as np
from numpy.random import default_rng as RNG
import pandas as pd

import Core.C_00__GenConstants as GC
import Core.F_00__GenFunctions as GF

# --- Functions (general) -----------------------------------------------------
def getPF(sP, sD, sF, sFExt = GC.S_EXT_CSV):
    return GF.joinToPath(os.path.join(sP, sD), sF + '.' + sFExt)

def savePdDfr(dIG, pdDfr, sD, sF, overWrite = True, sFExt = GC.S_EXT_CSV):
    sP = getPF(dIG['sPRes'], sD, sF, sFExt = sFExt)
    if not os.path.isfile(sP) and overWrite:
        pdDfr.to_csv(sP, sep = dIG['cSep'])
    return sP

def saveAsPdDfr(dIG, dRes, sD, sF, overWrite = True, sFExt = GC.S_EXT_CSV):
    sP = getPF(dIG['sPRes'], sD, sF, sFExt = sFExt)
    if not os.path.isfile(sP) or overWrite:
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
    assert sSpS in cO.dITp['dInfSpS'] and sSpS in cO.dSpS
    dISpS, cSpS = cO.dITp['dInfSpS'][sSpS], cO.dSpS[sSpS]
    if not doDePyl and dISpS['Stat'] == GC.B_NOT_PYL and sAse in cSpS.lPyl:
        dISpS['Stat'] = GC.B_IS_PYL
        opDone = True
    elif doDePyl and dISpS['Stat'] == GC.B_IS_PYL and sAse in cSpS.lDePyl:
        dISpS['Stat'] = GC.B_NOT_PYL
        opDone = True
    if opDone:
        cSpS.sSPTM = dISpS['Stat']
    return opDone

# --- Functions (O_90_State) --------------------------------------------------
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
    dCI = dITp['dConcIni']
    return {s: GF.drawFromDist(dCI[s]['cTp'], dCI[s]['dPar']) for s in dCI}

def iniDictOut(dITp, dCnc, t = 0.):
    dO = {'dN': {}, 'dH': {}, 'h': 0., 'dRes': {GC.S_TIME: [t]}}
    for s, cCnc in dCnc.items():
        dO['dRes'][s] = [cCnc]
    for s, k in dITp['dNStaObj'].items():
        dO['dRes'][s] = [k]
        dO['dN'][s] = k
    return dO

def getSRct(dO):
    uRN, cSum, rIdx = RNG().random(), 0., len(dO['dH']) - 1
    for k, cV in enumerate(dO['dH'].values()):
        cSum += cV
        if uRN < cSum:
            rIdx = k
            break
    return list(dO['dH'])[rIdx]

def eventReactionSys(dO):
    sRct = getSRct(dO)
    # update the numbers of state objects in dO['dN']
    if sRct == 'A_B':
        dO['dN'][GC.S_ST_A_INT_AT5G49770_NRT2P1] -= 1
        dO['dN'][GC.S_ST_B_TRANS_AT5G49770_NRT2P1] += 1
    elif sRct == 'B_C':
        dO['dN'][GC.S_ST_B_TRANS_AT5G49770_NRT2P1] -= 1
        dO['dN'][GC.S_ST_C_INT_NAR2P1_NRT2P1] += 1
    elif sRct == 'C_D':
        dO['dN'][GC.S_ST_C_INT_NAR2P1_NRT2P1] -= 1
        dO['dN'][GC.S_ST_D_TRANS_NAR2P1_NRT2P1] += 1
    elif sRct == 'D_A':
        dO['dN'][GC.S_ST_D_TRANS_NAR2P1_NRT2P1] -= 1
        dO['dN'][GC.S_ST_A_INT_AT5G49770_NRT2P1] += 1
    else:
        print('No reaction occurred!?')
        assert False

def nextEvent(dITp, dO, T, cTS):
    tToNxt = 0
    if dO['h'] > 0:    # otherwise the while-loop ends, see the other case
        # draw the time to the next event from exponential(lambd = 1./h)
        tToNxt = RNG().exponential(1./dO['h'])
        # adapt the event reactions to considered system
        eventReactionSys(dO)
    else:
        # if no reaction is possible, then h becomes 0, therefore stop
        print('The combined reaction hazard is 0 - no reaction possible')
        tToNxt = T - dO['dRes'][GC.S_TIME][cTS]
    return tToNxt

def updateDictOut(dITp, dO, dCnc, t):
    dO['dRes'][GC.S_TIME].append(t)
    for s, cCnc in dCnc.items():
        dO['dRes'][s].append(cCnc)
    for s in dO['dN']:
        dO['dRes'][s].append(dO['dN'][s])
     
# def Gillespie_StateMod(dIG, dITp):
#     t, T, cTSt = dIG['tStart'], dIG['tMax'], 0
#     dO = iniDictOut(dITp, t)
#     while t < T:
#         # adapt the re-calc reaction rate hazards function to current system
#         reCalcReactHazardsCR(dITp, dO)
#         # do next event and update time with tToNext
#         t += nextEvent(dITp, dO, T, cTSt)
#         # update the data storage matrix
#         if t < T:
#             updateDictOut(dITp, dO, t)
#         cTSt += 1
#     return dO['dRes']

# def printSysComp(sCmp = 'Base', lOCmp = []):
#     print('-'*8, sCmp, '-'*8)
#     for cO in lOCmp:
#         s = cO.descO + ' ' + cO.dITp['strCS'] + ' with ID ' + str(cO.idO)
#         if cO.nSpS > 0:
#             s += ' and special sites '
#             s += str(cO.extractLSpecSitesS())
#         if len(cO.sSpS) > 0:
#             s += ' for special site ' + cO.sSpS
#         print(s)

###############################################################################
