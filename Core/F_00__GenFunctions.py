# -*- coding: utf-8 -*-
###############################################################################
# --- F_00__GenFunctions.py ---------------------------------------------------
###############################################################################
import time

import numpy as np

import Core.C_00__GenConstants as GC

# --- Functions ---------------------------------------------------------------
def startSimu():
    startTime = time.time()
    print('+'*50 + ' START', time.ctime(startTime), '+'*30)
    print('Systems Biology Framework')
    return startTime

def seedRNG(cMode):             # legacy function
    if cMode == GC.M_STOCH:
        np.random.seed()
        print('Seeded RNG.')

def lItToUniqueList(lIt):
    if len(lIt) > 0:
        seAll = set(lIt[0])
        for cIt in lIt[1:]:
            seAll = seAll.union(set(cIt))
        return list(seAll)
    return []

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

###############################################################################
