# -*- coding: utf-8 -*-
###############################################################################
# --- F_00__GenFunctions.py ---------------------------------------------------
###############################################################################
import os, copy, time

import numpy as np
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

def joinToPath(pF = '', nmF = 'Dummy.txt'):
    if len(pF) > 0:
        createDir(pF)
        return os.path.join(pF, nmF)
    else:
        return nmF

def lItToUniqueList(lIt):
    if len(lIt) > 0:
        seAll = set(lIt[0])
        for cIt in lIt[1:]:
            seAll = seAll.union(set(cIt))
        return list(seAll)
    return []

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
