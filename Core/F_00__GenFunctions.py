# -*- coding: utf-8 -*-
###############################################################################
# --- F_00__GenFunctions.py ---------------------------------------------------
###############################################################################
import os, copy, time

import numpy as np
from numpy.random import default_rng as RNG
import scipy.stats as st
import pandas as pd

import Core.C_00__GenConstants as GC

# --- Functions (Python core) -------------------------------------------------
def startSimu():
    startTime = time.time()
    print(GC.S_PLUS*20 + ' START', time.ctime(startTime), GC.S_PLUS*20)
    print('Agent-based model of the NRT2.1/NAR2.1/HPCAL1-system')
    return startTime

def startRepLoop():
    print(GC.S_PLUS*20, 'Starting repetition loop...', GC.S_PLUS*20)
    return time.time()

def getTime():
    return time.time()

def seedRNG(cMode):             # legacy function
    if cMode == GC.M_STOCH:
        np.random.seed()
        print('Seeded RNG.')

def makeDirs(pDTarget):
    if not os.path.isdir(pDTarget):
        os.makedirs(pDTarget)

def joinToPath(lD4P=[], sF='Dummy.txt'):
    if len(lD4P) > 0:
        pD = ''
        for cD in lD4P:
            pD = os.path.join(pD, cD)
        makeDirs(pD)
        return os.path.join(pD, sF)
    else:
        return sF

def getPF(lD4P, sF, sFExt=GC.S_EXT_CSV):
    return joinToPath(lD4P, sF + '.' + sFExt)

def pFExists(pF):
    return os.path.isfile(pF)

def getFNmOfP(pF):
    sF = os.path.split(pF)[-1]
    if len(sF.split('.')) < 2:
        print('WARNING: Returning dir name instead of file name.')
    return sF

def changeFExt(pF, newX=GC.S_EXT_CSV):
    lPF = pF.split('.')
    return pF[:-len(lPF[-1])] + newX

def getFNoExt(sF):
    return getFNmOfP(sF).split('.')[0]

def splitStr(s, sSpl=GC.S_USC):
    return s.split(sSpl)

def partStr(s0, sSplO=GC.S_USC, sSplI=GC.S_PLUS):
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

def getLFromLIt(lIt, k=0):
    return [cIt[k] for cIt in lIt]

def addToDictCt(cD, cK, cCt=1):
    if cK in cD:
        cD[cK] += cCt
    else:
        cD[cK] = cCt

def addToDictL(cD, cK, cE, lUnique=False):
    if cK in cD:
        if not lUnique or cE not in cD[cK]:
            cD[cK].append(cE)
    else:
        cD[cK] = [cE]

def addToDictD(cD, cKO, cKI, cEI):
    if cKO in cD:
        cD[cKO][cKI] = cEI
    else:
        cD[cKO] = {cKI: cEI}

def addToDictDL(cD, cKO, cKI, cEI, lUnique=False):
    if cKO in cD:
        if cKI in cD[cKO]:
            if not lUnique or cEI not in cD[cKO][cKI]:
                cD[cKO][cKI].append(cEI)
        else:
            cD[cKO][cKI] = [cEI]
    else:
        cD[cKO] = {cKI: [cEI]}

def appendToDictL(cD, lE):
    assert len(lE) == len(cD)
    for i, cK in enumerate(cD):
        cD[cK].append(lE[i])

def implMinMax(x, lowB=0, upB=1):
    return min(max(x, lowB), upB)

# get a list of weights corresponding to the distance of the values to a centre
def getWeights(cSer, cCent, halfRng=0.5, maxWt=1.):
    if len(cSer) == 0:
        return np.array([])
    halfRng = max(halfRng, abs(cCent - min(cSer)), abs(cCent - max(cSer)))
    return np.array(maxWt*(1 - abs(cCent - cSer)/halfRng))

# Running mean and standard deviation
# For a new value newValue, compute the new count, new mean, new M2
# mean accumulates the mean of the entire dataset
# M2 aggregates the squared distance from the mean
# count aggregates the number of samples seen so far
def updateAggr(existingAggregate, newValue):
    (count, mean, M2) = existingAggregate
    count += 1
    if not np.isnan(newValue):
        delta = newValue - mean
        mean += delta/count
        delta2 = newValue - mean
        M2 += delta*delta2
    return (count, mean, M2)

def updateMeanM2(cMean, cM2, newValue, cCnt):
    if np.isfinite(cMean):
        delta = newValue - cMean
        cMean += delta/cCnt
        delta2 = newValue - cMean
        if np.isfinite(cM2):
            cM2 += delta*delta2
    else:
        cMean, cM2 = newValue, 0
    return cMean, cM2

# Retrieve the mean, variance and sample variance from an aggregate
def finalRunMeanSD(existingAggregate):
    (count, mean, M2) = existingAggregate
    if (not (np.isfinite(count) and np.isfinite(mean))) or (count < 2):
        return (mean, np.nan, np.nan)
    else:
        (mean, variance, sampleVariance) = (mean, M2/count, M2/(count - 1))
        return (mean, variance, sampleVariance)

# clip a value so that it is between xMin and xMax
def clipVal(x, xMin=None, xMax=None):
    if xMin is not None:
        if xMax is not None:
            return min(max(x, xMin), xMax)
        else:
            return max(x, xMin)
    else:
        if xMax is not None:
            return min(x, xMax)
        else:
            return x

# calculate the confidence interval of the mean using the SEM
def getCI(cData=None, nRp=1, cMn=0., cSEM=1., cAlph=0.95, mnV=None, mxV=None):
    cAlph = clipVal(cAlph, xMin=0, xMax=1)
    if cData is None:
        if cSEM <= 0:
            tCI = (np.nan, np.nan)
        else:
            tCI = st.t.interval(alpha=cAlph, df=nRp-1, loc=cMn, scale=cSEM)
    else:
        tCI = st.t.interval(alpha=cAlph, df=len(cData)-1, loc=np.mean(cData),
                            scale=st.sem(cData))
    if np.isfinite(tCI[0]):
        if np.isfinite(tCI[1]):
            return tuple(clipVal(cBd, xMin=mnV, xMax=mxV) for cBd in tCI)
        else:
            return (clipVal(tCI[0], xMin=mnV), tCI[1])
    else:
        if np.isfinite(tCI[1]):
            return (tCI[0], clipVal(tCI[1], xMax=mxV))
        else:
            return tCI

# calculate the confidence interval of the mean using the SEM (for an array)
def getArrCI(serC, serS, serRp, cAlph=0.95, mnV=None, mxV=None):
    assert serC.ndim == 1 and serS.ndim == 1 and serRp.ndim == 1
    assert serC.size == serS.size and serC.size == serRp.size
    arrLB, arrUB = np.zeros(serC.size), np.zeros(serC.size)
    for i, x in enumerate(serC):
        arrLB[i], arrUB[i] = getCI(nRp=serRp.at[i], cMn=x, cSEM=serS.at[i],
                                   cAlph=cAlph, mnV=mnV, mxV=mxV)
    return (arrLB, arrUB)

# calculate a point of a general sigmoidal function
def calcPSigmoidal(x, dPar):
    B, C, D = dPar[GC.S_PAR_B], dPar[GC.S_PAR_C], dPar[GC.S_PAR_D]
    fCh = (B*(B + C)/C*(1/(B + C*np.exp(-D*x)) - 1/(B + C)))
    prMin, prMax = dPar[GC.S_PAR_PMIN], dPar[GC.S_PAR_PMAX]
    return prMin + (prMax - prMin)*fCh

def drawFromDist(sDist, dPar, nVal=None):
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
    sLHS, sRHS, lSKeys, sRctCl = lSLHS[0], lSRHS[0], GC.L_S_SPS, ''
    # check if it is a valid reaction string
    assert (len(sLHS) == GC.LEN_S_CP and len(sLHS) == len(sRHS) and
            len(sLHS[GC.I_S_CP_SEP1:]) >= len(lSKeys))
    # find the appropriate key and value, and add the pair to the dict.
    sRctAI1 = (sLHS[:GC.I_S_CP_SEP1].strip(GC.S_DASH) + GC.S_USC +
               sRHS[:GC.I_S_CP_SEP1].strip(GC.S_DASH))
    for k, chLHS in enumerate(sLHS[GC.I_S_CP_SEP1:]):
        chRHS = sRHS[k + GC.I_S_CP_SEP1]
        assert chLHS in GC.SET_0_1_DASH and chRHS in GC.SET_0_1_DASH
        if chLHS in GC.SET_0_1 and chRHS in GC.SET_0_1:
            if chLHS != chRHS:
                if chLHS == GC.S_0 and chRHS == GC.S_1: # phosphorylation
                    sRctCl = GC.S_DO_PYL + GC.S_USC + lSKeys[k]
                else:                                   # dephosphorylation
                    sRctCl = GC.S_DO_DPY + GC.S_USC + lSKeys[k]
                break       # only one (de)phosphorylation per event
    return GC.S_RCT_11, sRctCl, [sRctAI1]

def sRct21(lSLHS, lSRHS):
    ((sLHS1, sLHS2), sRHS) = (lSLHS, lSRHS[0])
    sRctCl, sRctAI1, s01LHS, s01RHS = GC.S_DO_FRM + GC.S_USC, '', '', ''
    # check if it is a valid reaction string
    assert (len(sLHS1) == GC.LEN_S_CP and len(sLHS1) == len(sLHS2) and
            len(sLHS1) == len(sRHS))
    assert (sLHS1[0] in GC.L_S_LSK and sLHS2[0] in GC.L_S_LSK and
            sRHS[0] in GC.L_S_LSK and sRHS[1] in GC.L_S_LSK)
    assert sRHS[0] == sLHS1[0] and sRHS[1] == sLHS2[0]
    assert sRHS[2] in GC.L_S_IJT
    # find the appropriate key
    if sRHS[:3] == GC.S_LSI:
        sRctCl += GC.S_FRM_L_S_LSI
    elif sRHS[:3] == GC.S_LSJ:
        sRctCl += GC.S_FRM_L_S_LSJ
    elif sRHS[:3] == GC.S_LST:
        sRctCl += GC.S_FRM_L_S_LST
    elif sRHS[:3] == GC.S_LKI:
        sRctCl += GC.S_FRM_L_K_LKI
    elif sRHS[:3] == GC.S_LKJ:
        sRctCl += GC.S_FRM_L_K_LKJ
    elif sRHS[:3] == GC.S_LKT:
        sRctCl += GC.S_FRM_L_K_LKT
    # find and check the appropriate value
    for k, chRHS in enumerate(sRHS[GC.I_S_CP_SEP1:]):
        chLHS1, chLHS2 = sLHS1[k + GC.I_S_CP_SEP1], sLHS2[k + GC.I_S_CP_SEP1]
        assert (chLHS1 in GC.SET_0_1_DASH and chLHS2 in GC.SET_0_1_DASH and
                chRHS in GC.SET_0_1_DASH)
        if chLHS1 in GC.SET_0_1 and chLHS2 not in GC.SET_0_1:
            s01LHS += chLHS1
        elif chLHS2 in GC.SET_0_1 and chLHS1 not in GC.SET_0_1:
            s01LHS += chLHS2
        elif chLHS1 in GC.SET_0_1 and chLHS2 in GC.SET_0_1:
            print('ERROR: Position', k + GC.I_S_CP_SEP1, ': LHS string 1 is',
                  chLHS1, 'while LHS string 2 is', chLHS2)
        if chRHS in GC.SET_0_1:
            s01RHS += chRHS
    # if OK, add the pair to the dict.
    if len(sRctCl) > len(GC.S_DO_FRM + GC.S_USC) and s01LHS == s01RHS:
        sRctAI1 = s01LHS
    else:
        print('ERROR: Reaction class is', sRctCl, 'while LHS 01-string is',
              s01LHS, 'but RHS 01-string is', s01RHS)
    return GC.S_RCT_21, sRctCl, [sRctAI1]

def sRct12(lSLHS, lSRHS):
    (sLHS, (sRHS1, sRHS2)) = (lSLHS[0], lSRHS)
    sRctCl, sRctAI1, s01LHS, s01RHS = GC.S_DO_DIS + GC.S_USC, '', '', ''
    # check if it is a valid reaction string
    assert (len(sLHS) == GC.LEN_S_CP and len(sLHS) == len(sRHS1) and
            len(sLHS) == len(sRHS2))
    assert (sLHS[0] in GC.L_S_LSK and sLHS[1] in GC.L_S_LSK
            and sRHS1[0] in GC.L_S_LSK and sRHS2[0] in GC.L_S_LSK)
    assert sLHS[0] == sRHS1[0] and sLHS[1] == sRHS2[0]
    assert sLHS[2] in GC.L_S_IJT
    # find the appropriate key
    if sLHS[:3] == GC.S_LSI:
        sRctCl += GC.S_DIS_LSI_L_S
    elif sLHS[:3] == GC.S_LSJ:
        sRctCl += GC.S_DIS_LSJ_L_S
    elif sLHS[:3] == GC.S_LST:
        sRctCl += GC.S_DIS_LST_L_S
    elif sLHS[:3] == GC.S_LKI:
        sRctCl += GC.S_DIS_LKI_L_K
    elif sLHS[:3] == GC.S_LKJ:
        sRctCl += GC.S_DIS_LKJ_L_K
    elif sLHS[:3] == GC.S_LKT:
        sRctCl += GC.S_DIS_LKT_L_K
    # find and check the appropriate value
    for k, chLHS in enumerate(sLHS[GC.I_S_CP_SEP1:]):
        chRHS1, chRHS2 = sRHS1[k + GC.I_S_CP_SEP1], sRHS2[k + GC.I_S_CP_SEP1]
        assert (chLHS in GC.SET_0_1_DASH and chRHS1 in GC.SET_0_1_DASH and
                chRHS2 in GC.SET_0_1_DASH)
        if chRHS1 in GC.SET_0_1 and chRHS2 not in GC.SET_0_1:
            s01RHS += chRHS1
        elif chRHS2 in GC.SET_0_1 and chRHS1 not in GC.SET_0_1:
            s01RHS += chRHS2
        elif chRHS1 in GC.SET_0_1 and chRHS2 in GC.SET_0_1:
            print('ERROR: Position', k + GC.I_S_CP_SEP1, ': RHS string 1 is',
                  chRHS1, 'while RHS string 2 is', chRHS2)
        if chLHS in GC.SET_0_1:
            s01LHS += chLHS
    # if OK, add the pair to the dict.
    if len(sRctCl) > len(GC.S_DO_DIS + GC.S_USC) and s01LHS == s01RHS:
        sRctAI1 = s01LHS
    else:
        print('ERROR: Reaction class is', sRctCl, 'while LHS 01-string is',
              s01LHS, 'but RHS 01-string is', s01RHS)
    return GC.S_RCT_12, sRctCl, [sRctAI1]

def sRct22(lSLHS, lSRHS):
    ((sLHS1, sLHS2), (sRHS1, sRHS2)) = (lSLHS, lSRHS)
    sRctCl, sRctAI1, s01LHS, s01RHS = GC.S_DO_IPC + GC.S_USC, '', '', ''
    # check if it is a valid reaction string
    assert (len(sLHS1) == GC.LEN_S_CP and len(sLHS1) == len(sLHS2) and
            len(sLHS1) == len(sRHS1) and len(sLHS1) == len(sRHS2))
    assert (sLHS1[0] in GC.L_S_LSK and sLHS1[1] in GC.L_S_LSK and
            sLHS2[0] in GC.L_S_LSK and sRHS1[0] in GC.L_S_LSK and
            sRHS1[1] in GC.L_S_LSK and sRHS2[0] in GC.L_S_LSK)
    assert (sLHS1[0] == sRHS1[0] and sLHS1[1] == sRHS2[0] and
            sLHS2[0] == sRHS1[1])
    assert sLHS1[2] in GC.L_S_IJT and sRHS1[2] in GC.L_S_IJT
    # find the appropriate key
    if sLHS1[:3] == GC.S_LSI and sRHS1[:3] == GC.S_LKT:
        sRctCl += GC.S_IPC_LSI_LKT
    elif sLHS1[:3] == GC.S_LSJ and sRHS1[:3] == GC.S_LKT:
        sRctCl += GC.S_IPC_LSJ_LKT
    elif sLHS1[:3] == GC.S_LST and sRHS1[:3] == GC.S_LKI:
        sRctCl += GC.S_IPC_LST_LKI
    elif sLHS1[:3] == GC.S_LST and sRHS1[:3] == GC.S_LKJ:
        sRctCl += GC.S_IPC_LST_LKJ
    elif sLHS1[:3] == GC.S_LKI and sRHS1[:3] == GC.S_LST:
        sRctCl += GC.S_IPC_LKI_LST
    elif sLHS1[:3] == GC.S_LKJ and sRHS1[:3] == GC.S_LST:
        sRctCl += GC.S_IPC_LKJ_LST
    elif sLHS1[:3] == GC.S_LKT and sRHS1[:3] == GC.S_LSI:
        sRctCl += GC.S_IPC_LKT_LSI
    elif sLHS1[:3] == GC.S_LKT and sRHS1[:3] == GC.S_LSJ:
        sRctCl += GC.S_IPC_LKT_LSJ
    # find and check the appropriate value
    for k, _ in enumerate(sLHS1[GC.I_S_CP_SEP1:]):
        chLHS1, chLHS2 = sLHS1[k + GC.I_S_CP_SEP1], sLHS2[k + GC.I_S_CP_SEP1]
        chRHS1, chRHS2 = sRHS1[k + GC.I_S_CP_SEP1], sRHS2[k + GC.I_S_CP_SEP1]
        assert (chLHS1 in GC.SET_0_1_DASH and chLHS2 in GC.SET_0_1_DASH and
                chRHS1 in GC.SET_0_1_DASH and chRHS2 in GC.SET_0_1_DASH)
        if chLHS1 in GC.SET_0_1 and chLHS2 not in GC.SET_0_1:
            s01LHS += chLHS1
        elif chLHS2 in GC.SET_0_1 and chLHS1 not in GC.SET_0_1:
            s01LHS += chLHS2
        elif chLHS1 in GC.SET_0_1 and chLHS2 in GC.SET_0_1:
            print('ERROR: Position', k + GC.I_S_CP_SEP1, ': LHS string 1 is',
                  chLHS1, 'while LHS string 2 is', chLHS2)
        if chRHS1 in GC.SET_0_1 and chRHS2 not in GC.SET_0_1:
            s01RHS += chRHS1
        elif chRHS2 in GC.SET_0_1 and chRHS1 not in GC.SET_0_1:
            s01RHS += chRHS2
        elif chRHS1 in GC.SET_0_1 and chRHS2 in GC.SET_0_1:
            print('ERROR: Position', k + GC.I_S_CP_SEP1, ': RHS string 1 is',
                  chRHS1, 'while RHS string 2 is', chRHS2)
    # if OK, add the pair to the dict.
    if len(sRctCl) > len(GC.S_DO_IPC + GC.S_USC) and s01LHS == s01RHS:
        sRctAI1 = s01LHS
    else:
        print('ERROR: Reaction class is', sRctCl, 'while LHS 01-string is',
              s01LHS, 'but RHS 01-string is', s01RHS)
    return GC.S_RCT_22, sRctCl, [sRctAI1]

def analyseSRct(sRct):
    lSSplRct = partStr(sRct)
    assert len(lSSplRct) == 2       # required for a valid reaction: LHS, RHS
    # 1st-order reactions with single product (Rct11) [potentially KAs/PAs]
    if len(lSSplRct[0]) == 1 and len(lSSplRct[1]) == 1:
        return sRct11(lSSplRct[0], lSSplRct[1])
    # 2nd-order reactions with single product (Rct21)
    elif len(lSSplRct[0]) == 2 and len(lSSplRct[1]) == 1:
        return sRct21(lSSplRct[0], lSSplRct[1])
    # 1st-order reactions with two products (Rct12)
    elif len(lSSplRct[0]) == 1 and len(lSSplRct[1]) == 2:
        return sRct12(lSSplRct[0], lSSplRct[1])
    # 2nd-order reactions with two products (Rct22)
    elif len(lSSplRct[0]) == 2 and len(lSSplRct[1]) == 2:
        return sRct22(lSSplRct[0], lSSplRct[1])
    else:
        print('Reaction type with more than two reactants or products not',
              'implemented. Number of reactants is', len(lSSplRct[0]),
              'while number of products is', len(lSSplRct[1]), '.')

def calcRctWeight(cDfr, tSRctI):
    sRctTp, sRctCl, lSRctAI = tSRctI
    wRct = 1.
    # get weight for reaction class
    if sRctCl in cDfr.index and GC.S_VAL in cDfr.columns:
        wRct = cDfr.at[sRctCl, GC.S_VAL]
    else:
        print('ERROR: Position (' + sRctCl + ', ' + GC.S_VAL + ') does not',
              'exist in DataFrame!\nIndex =', cDfr.index, '\Columns =',
              cDfr.columns)
    # get weight for group change if reaction type == GC.S_RCT_11
    if sRctTp == GC.S_RCT_11:
        assert len(lSRctAI) >= 1
        if lSRctAI[0] in cDfr.index and GC.S_VAL in cDfr.columns:
            wRct *= cDfr.at[lSRctAI[0], GC.S_VAL]
        else:
            print('ERROR: Position (' + lSRctAI[0] + ', ' + GC.S_VAL +
                  ') does not exist in DataFrame!\nIndex =', cDfr.index,
                  '\Columns =', cDfr.columns)
    return wRct

# function updating the dITp with that of a higher-priority class
def updateDITp(dITpC, dITpU):
    dITpC.update(dITpU)

# special function for updating both the general dITp and a sub-dITp ("dIPlt")
def updateDITpDIPlt(dITpC, dITpU, lKSpc=[]):
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

def printElapsedTimeSim(stT, cT, sPre=GC.S_TIME):
    # calculate and display elapsed time
    elT = round(cT - stT, GC.R04)
    print(sPre, 'elapsed:', elT, 'seconds, this is', round(elT/60, GC.R04),
          'minutes\nor', round(elT/3600, GC.R04), 'hours or',
          round(elT/(3600*24), GC.R04), 'days.')

def showElapsedTime(startTime):
    print(GC.S_DASH*80)
    printElapsedTimeSim(startTime, time.time(), GC.S_TIME)
    print(GC.S_PLUS*3 + ' Current time:', time.ctime(time.time()), GC.S_PLUS*3)
    print(GC.S_DASH*80)

def endSimu(startTime):
    print(GC.S_DASH*80)
    printElapsedTimeSim(startTime, time.time(), 'Total real time')
    print(GC.S_STAR*20 + ' DONE', time.ctime(time.time()), GC.S_STAR*20)

# --- Functions (NumPy) -------------------------------------------------------
def iniNpArr0(tShape=(0, 0)):
    return np.zeros(tShape)

def iniNpArr1(tShape=(0, 0)):
    return np.ones(tShape)

def iniNpArrV(tShape=(0, 0), v=0, tpDt=float):
    return np.full(tShape, v, dtype=tpDt)

def boolFinVal(cArr):
    return np.isfinite(cArr)

def arrFinVal(cArrRet, cArrTest):
    assert len(cArrRet) == len(cArrTest)
    return cArrRet[np.isfinite(cArrTest)]

def getBoolAND2C(cnd1, cnd2):
    return np.logical_and(cnd1, cnd2)

def getBoolAND3C(cnd1, cnd2, cnd3):
    return np.logical_and(cnd1, cnd2, cnd3)

# --- Functions (Pandas) ------------------------------------------------------
def readCSV(pF, sepD=GC.SEP_STD, iCol=None, dDtype=None):
    return pd.read_csv(pF, sep=sepD, index_col=iCol, dtype=dDtype)

def saveAsCSV(pdDfr, pF, sepD=GC.SEP_STD, sFExt=GC.S_EXT_CSV):
    pdDfr.to_csv(pF + '.' + sFExt, sep=sepD)

def saveConcatDfr(lSerDfr, pF, sepD=GC.SEP_STD):
    pd.concat(lSerDfr, axis=1).to_csv(pF, sep=sepD)

def iniPdSer(data=None, lSI=None, nEl=0, v=0, sNm=None, tpDt=float):
    if lSI is None:
        if data is None:
            if sNm is None:
                return pd.Series(iniNpArrV((nEl,), v, tpDt=tpDt), dtype=tpDt)
            else:
                return pd.Series(iniNpArrV((nEl,), v, tpDt=tpDt), name=sNm,
                                 dtype=tpDt)
        else:
            if sNm is None:
                return pd.Series(data, dtype=tpDt)
            else:
                return pd.Series(data, name=sNm, dtype=tpDt)
    else:
        if data is None:
            if sNm is None:
                return pd.Series(iniNpArrV((len(lSI),), v, tpDt=tpDt),
                                 index=lSI, dtype=tpDt)
            else:
                return pd.Series(iniNpArrV((len(lSI),), v, tpDt=tpDt),
                                 index=lSI, name=sNm, dtype=tpDt)
        else:
            if sNm is None:
                return pd.Series(data, index=lSI, dtype=tpDt)
            else:
                return pd.Series(data, index=lSI, name=sNm, dtype=tpDt)

def iniPdDfr(data=None, lSNmC=[], lSNmR=[], shape=(0, 0), v=0, tpDt=float):
    assert len(shape) == 2
    nR, nC = shape
    if len(lSNmC) == 0:
        if len(lSNmR) == 0:
            if data is None:
                return pd.DataFrame(iniNpArrV(shape, v, tpDt=tpDt), dtype=tpDt)
            else:
                return pd.DataFrame(data, dtype=tpDt)
        else:
            if data is None:
                return pd.DataFrame(iniNpArrV((len(lSNmR), nC), v, tpDt=tpDt),
                                    index=lSNmR, dtype=tpDt)
            else:
                return pd.DataFrame(data, index=lSNmR, dtype=tpDt)
    else:
        if len(lSNmR) == 0:
            if data is None:
                return pd.DataFrame(iniNpArrV((nR, len(lSNmC)), v, tpDt=tpDt),
                                    columns=lSNmC, dtype=tpDt)
            else:
                return pd.DataFrame(data, columns=lSNmC, dtype=tpDt)
        else:   # ignore nR
            if data is None:
                arrDat = iniNpArrV((len(lSNmR), len(lSNmC)), v, tpDt=tpDt)
                return pd.DataFrame(arrDat, index=lSNmR, columns=lSNmC,
                                    dtype=tpDt)
            else:
                return pd.DataFrame(data, index=lSNmR, columns=lSNmC,
                                    dtype=tpDt)

def getElOfSerIfValid(pdSer, cI, xAlt=0):
    xRet = xAlt
    if cI in pdSer.index:
        if np.isfinite(pdSer.at[cI]):
            xRet = pdSer.at[cI]
    return xRet

def getElOfDfrIfValid(pdDfr, sR, sC, xAlt=0):
    xRet = xAlt
    if sR in pdDfr.index and sC in pdDfr.columns:
        if np.isfinite(pdDfr.at[sR, sC]):
            xRet = pdDfr.at[sR, sC]
    return xRet

def checkValid(pdSer, cI, x=0, xAlt=0):
    xRet, isValid = xAlt, False
    if np.isfinite(x):
        isValid = True
        if cI in pdSer.index:
            pdSer.at[cI] += 1
            xRet = pdSer.at[cI]
    return xRet, isValid

def printDictDfr(dDfr, lK=None):
    print(GC.S_USC*8, 'Dictionary of DataFrames', GC.S_USC*8, '\n')
    for cK, cDfr in dDfr.items():
        if lK is None or cK in lK:
            print(str(cK) + ':')
            print(cDfr, '\n')

###############################################################################
