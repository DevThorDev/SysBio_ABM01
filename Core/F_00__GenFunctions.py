# -*- coding: utf-8 -*-
###############################################################################
# --- F_00__GenFunctions.py ---------------------------------------------------
###############################################################################
import os, copy, time

import numpy as np
from numpy.random import default_rng as RNG
import pandas as pd

import Core.C_00__GenConstants as GC

# --- Functions (Python core) -------------------------------------------------
def startSimu():
    startTime = time.time()
    print('+'*50 + ' START', time.ctime(startTime), '+'*30)
    print('Systems Biology Framework')
    return startTime

def seedRNG(cMode):             # legacy function
    if cMode == GC.M_STOCH:
        np.random.seed()
        print('Seeded RNG.')

def createDir(pF):
    if not os.path.isdir(pF):
        os.mkdir(pF)

def joinToPath(pF = '', sF = 'Dummy.txt'):
    if len(pF) > 0:
        createDir(pF)
        return os.path.join(pF, sF)
    else:
        return sF

def partStr(s0, sSplO = GC.S_USC, sSplI = GC.S_PLUS):
    lSSplRet = [[s0]]
    if sSplO is not None:
        lSSplRet = s0.split(sSplO)
        for k, s1 in enumerate(lSSplRet):
            if sSplI is not None:
                lSSplRet[k] = s1.split(sSplI)
            else:
                lSSplRet[k] = [s1]
    else:
        if sSplI is not None:
            lSSplRet = s0.split(sSplI)
            lSSplRet = [[s1] for s1 in lSSplRet]
    return lSSplRet

def lItToUniqueList(lIt):
    if len(lIt) > 0:
        seAll = set(lIt[0])
        for cIt in lIt[1:]:
            seAll = seAll.union(set(cIt))
        return list(seAll)
    return []

def getLFromLIt(lIt, k = 0):
    return [cIt[k] for cIt in lIt]

def addToDictCt(cD, cK, cCt = 1):
    if cK in cD:
        cD[cK] += cCt
    else:
        cD[cK] = cCt

def addToDictL(cD, cK, cE, lUnique = False):
    if cK in cD:
        if not lUnique or cE not in cD[cK]:
            cD[cK].append(cE)
    else:
        cD[cK] = [cE]

def appendToDictL(cD, lE):
    assert len(lE) == len(cD)
    for i, cK in enumerate(cD):
        cD[cK].append(lE[i])

def implMinMax(x, lowB = 0, upB = 1):
    return min(max(x, lowB), upB)

def calcPSigmoidal(x, dPar):
    pMin, pMax = dPar['prMin'], dPar['prMax']
    B, C, D = dPar['B'], dPar['C'], dPar['D']
    fCh = (B*(B + C)/C*(1/(B + C*np.exp(-D*x)) - 1/(B + C)))
    return pMin + (pMax - pMin)*fCh

def drawFromDist(sDist, dPar, nVal = None):
    if sDist == 'uniform':
        assert 'min' in dPar and 'max' in dPar
        return RNG().uniform(dPar['min'], dPar['max'], nVal)
    elif sDist == 'normal':
        assert 'mean' in dPar and 'sd' in dPar
        return RNG().normal(dPar['min'], dPar['max'], nVal)
    elif sDist == 'exponential':
        assert 'h' in dPar
        return RNG().exponential(1./dPar['h'], nVal)
    else:
        print('WARNING: Option', sDist, 'not implemented. Returning 0...')
        return 0

def getSRct(dH):
    uRN, cSum, rIdx = RNG().random(), 0., len(dH) - 1
    for k, cV in enumerate(dH.values()):
        cSum += cV
        if uRN < cSum:
            rIdx = k
            break
    return list(dH)[rIdx]

def sRct11(lSLHS, lSRHS):
    sLHS, sRHS, lSKeys, dRctTp = lSLHS[0], lSRHS[0], GC.L_S_SPS, {}
    assert len(sLHS) == GC.LEN_S_RCT and len(sLHS) == len(sRHS)
    for k, chLHS in enumerate(sLHS[GC.I_S_RCT_ST_01:]):
        chRHS = sRHS[k + GC.I_S_RCT_ST_01]
        assert chLHS in GC.SET_01_DASH and chRHS in GC.SET_01_DASH
        if chLHS in GC.SET_01 and chRHS in GC.SET_01:
            if chLHS != chRHS:
                if chLHS == '0' and chRHS == '1':
                    dRctTp[lSKeys[k]] = GC.L_DO_PYL_DEPYL[0]    # do Pyl
                else:                           # chLHS == '1' and chRHS == '0'
                    dRctTp[lSKeys[k]] = GC.L_DO_PYL_DEPYL[1]    # do DePyl
    return GC.S_RCT_11, dRctTp

def sRct21(lSLHS, lSRHS):
    ((sLHS1, sLHS2), sRHS) = (lSLHS, lSRHS[0])
    dRctTp, sK, s01LHS, s01RHS = {}, None, '', ''
    assert (len(sLHS1) == GC.LEN_S_RCT and len(sLHS1) == len(sLHS2) and
            len(sLHS1) == len(sRHS))
    assert (sLHS1[0] in GC.L_S_LSK and sLHS2[0] in GC.L_S_LSK and
            sRHS[0] in GC.L_S_LSK and sRHS[1] in GC.L_S_LSK)
    assert sRHS[0] == sLHS1[0] and sRHS[1] == sLHS2[0]
    assert sRHS[2] in GC.L_S_IT
    if sRHS[0] == GC.S_L and sRHS[1] == GC.S_S and sRHS[2] == GC.S_I:
        sK = GC.S_FRM_L_S_LSI
    elif sRHS[0] == GC.S_L and sRHS[1] == GC.S_S and sRHS[2] == GC.S_T:
        sK = GC.S_FRM_L_S_LST
    elif sRHS[0] == GC.S_L and sRHS[1] == GC.S_K and sRHS[2] == GC.S_I:
        sK = GC.S_FRM_L_K_LKI
    elif sRHS[0] == GC.S_L and sRHS[1] == GC.S_K and sRHS[2] == GC.S_T:
        sK = GC.S_FRM_L_K_LKT
    for k, chRHS in enumerate(sRHS[GC.I_S_RCT_ST_01:]):
        if sLHS1[k] in GC.SET_01 and sLHS2[k] not in GC.SET_01:
            s01LHS += sLHS1[k]
        elif sLHS2[k] in GC.SET_01 and sLHS1[k] not in GC.SET_01:
            s01LHS += sLHS2[k]
        elif sLHS1[k] in GC.SET_01 and sLHS2[k] in GC.SET_01:
            print('ERROR: Position', k + GC.I_S_RCT_ST_01, ': LHS string 1 is',
                  sLHS1[k], 'while LHS string 2 is', sLHS2[k])
        if chRHS in GC.SET_01:
            s01RHS += chRHS
    if sK is not None and s01LHS == s01RHS:
        dRctTp[sK] = s01LHS
    else:
        print('ERROR: Key is', sK, 'while LHS 01-string is', s01LHS, 'but RHS',
              '01-string is', s01RHS)
    return GC.S_RCT_21, dRctTp

def analyseSRct(sRct = 'L--10--+K----01_LKI1001'):
    lSSplRct = partStr(sRct)
    assert len(lSSplRct) == 2       # a valid reaction
    if len(lSSplRct[0]) == 1 and len(lSSplRct[1]) == 1:
        return sRct11(lSSplRct[0],lSSplRct[1])
    elif len(lSSplRct[0]) == 2 and len(lSSplRct[1]) == 1:
        pass
    elif len(lSSplRct[0]) == 1 and len(lSSplRct[1]) == 2:
        pass
    elif len(lSSplRct[0]) == 2 and len(lSSplRct[1]) == 2:
        pass
    else:
        print('Reaction type with more than two reactants or products not',
              'implemented. Number of reactants is', len(lSSplRct[0]),
              'while number of products is', len(lSSplRct[1]))

def updateDITpDIPlt(dITpC, dITpU, lKSpc = [GC.S_D_PLT]):
    for cKSpc in lKSpc:
        if cKSpc in dITpC and cKSpc in dITpU:
            dISpcC, dISpcU = dITpC[cKSpc], dITpU[cKSpc]
            for cKSub in dISpcC:
                if cKSub in dISpcU:
                    dSubC, dSubU = dISpcC[cKSub], dISpcU[cKSub]
                    dSubC.update(dSubU)
            for cKSub in dISpcU:
                if cKSub not in dISpcC:
                    dISpcC[cKSub] = copy.deepcopy(dISpcU[cKSub])
        elif cKSpc not in dITpC and cKSpc in dITpU:
            dITpC[cKSpc] = copy.deepcopy(dITpU[cKSpc])
    dITpURed = {cK: cV for cK, cV in dITpU.items() if cK not in lKSpc}
    dITpC.update(dITpURed)

def printElapsedTimeSim(stT, cT, sPre = 'Time'):
    # calculate and display elapsed time 
    elT = round(cT - stT, GC.R04)
    print(sPre, 'elapsed:', elT, 'seconds, this is', round(elT/60, GC.R04),
          'minutes or', round(elT/3600, GC.R04), 'hours or',
          round(elT/(3600*24), GC.R04), 'days.')

def showElapsedTime(startTime):
    print('-'*80)
    printElapsedTimeSim(startTime, time.time(), 'Time')
    print('+'*3 + ' Current time:', time.ctime(time.time()), '+'*3)
    print('-'*80)

def endSimu(startTime):
    print('-'*80)
    printElapsedTimeSim(startTime, time.time(), 'Total time')
    print('*'*20 + ' DONE', time.ctime(time.time()), '*'*20)

# --- Functions (Pandas) ------------------------------------------------------
def readCSV(pF, sepD = GC.SEP_STD, iCol = None, dDtype = None):
    return pd.read_csv(pF, sep = sepD, index_col = iCol, dtype = dDtype)

def iniPdDfr(data = None, lSNmC = [], lSNmR = [], shape = (0, 0)):
    assert len(shape) == 2
    nR, nC = shape
    if len(lSNmC) == 0:
        if len(lSNmR) == 0:
            if data is None:
                return pd.DataFrame(np.zeros(shape))
            else:
                return pd.DataFrame(data)
        else:
            if data is None:
                return pd.DataFrame(np.zeros((len(lSNmR), nC)), index = lSNmR)
            else:
                return pd.DataFrame(data, index = lSNmR)
    else:
        if len(lSNmR) == 0:
            if data is None:
                return pd.DataFrame(np.zeros((nR, len(lSNmC))),
                                    columns = lSNmC)
            else:
                return pd.DataFrame(data, columns = lSNmC)
        else:   # ignore nR
            if data is None:
                return pd.DataFrame(np.zeros((len(lSNmR), len(lSNmC))),
                                    index = lSNmR, columns = lSNmC)
            else:
                return pd.DataFrame(data, index = lSNmR, columns = lSNmC)

###############################################################################
