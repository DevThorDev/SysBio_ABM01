# -*- coding: utf-8 -*-
###############################################################################
# --- T_01__Gillespie_C.py ----------------------------------------------------
###############################################################################
import os
import pandas as pd
from operator import itemgetter
from numpy.random import default_rng as RNG

# Constants -------------------------------------------------------------------
S_TIME = 'Time'
R_04 = 4

# Input dictionary ------------------------------------------------------------
dInp = {# flow control
        'Tmax': 500.0,              # maximum elapsed time (float)
        'tStart': 0.0,              # start time (float)
        # species and reactions dictionaries
        'dNSpec':{'E': 100,         # names & numbers of chemical species
                  'S': 500,
                  'ES': 10,
                  'P': 0},
        'dRRC': {'EpS_to_ES': 0.0001,   # reaction rate constant E + S --> ES
                 'ES_to_EpS': 2.5,      # reaction rate constant ES --> E + S
                 'ES_to_EpP': 1.5},     # reaction rate constant ES --> E + P
        # path, directory and file names, and file extensions
        'pF_DataCR': 'Gillespie_C',
        'sF_DataCR': 'DataCR',
        'sFExtCSV': 'csv',
        'sepCSV': ';',
        'mdApp': 'w',
        # other constants
        'sTime': S_TIME,
        'nDgRnd': R_04}

# Functions (initialisation) --------------------------------------------------
def iniDictOut(dI, t = 0.):
    dO = {'dN': {}, 'dH': {}, 'h': 0., 'dRes': {S_TIME: [t]}}
    for s, k in dI['dNSpec'].items():
        dO['dRes'][s] = [k]
        dO['dN'][s] = k
    return dO

# Functions (Gillespie core) --------------------------------------------------
def reCalcReactHazardsCR(dI, dO):
    dRRC, dH = dI['dRRC'], dO['dH']
    # recalculate dH, which contains the h_i (i = 1,... len(dH))
    dH['EpS_to_ES'] = dRRC['EpS_to_ES']*dO['dN']['E']*dO['dN']['S']
    dH['ES_to_EpS'] = dRRC['ES_to_EpS']*dO['dN']['ES']
    dH['ES_to_EpP'] = dRRC['ES_to_EpP']*dO['dN']['ES']
    # h, the sum of the h_i, is the overall reaction hazard
    dO['h'] = sum(dH.values())
    # sort dH in ascending order for numerical stability
    dO['dH'] = {cK: cV/dO['h'] for cK, cV in
                sorted(dH.items(), key = itemgetter(1))}

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
    # update the numbers in dO['dN']
    if sRct == 'EpS_to_ES':     # (E + S --> ES)
        dO['dN']['E'] -= 1
        dO['dN']['S'] -= 1
        dO['dN']['ES'] += 1
    elif sRct == 'ES_to_EpS':   # (ES --> E + S)
        dO['dN']['E'] += 1
        dO['dN']['S'] += 1
        dO['dN']['ES'] -= 1
    elif sRct == 'ES_to_EpP':   # (ES --> E + P)
        dO['dN']['E'] += 1
        dO['dN']['ES'] -= 1
        dO['dN']['P'] += 1 
    else:
        print('No reaction occurred!?') # so something went wrong...
        assert False

def nextEvent(dI, dO, T, cTS):
    tToNxt = 0
    if dO['h'] > 0:    # otherwise the while-loop ends, see the other case
        # draw the time to the next event from exponential(lambd = 1./h)
        tToNxt = RNG().exponential(1./dO['h'])
        # adapt the event reactions to considered system
        eventReactionSys(dO)
    else:
        # if no reaction is possible, then h becomes 0, therefore stop
        print('The combined reaction hazard is 0 - no reaction possible')
        tToNxt = T - dO['dRes'][S_TIME][cTS]
    return tToNxt

def updateDictOut(dI, dO, t):
    dO['dRes'][S_TIME].append(t)
    for s in dO['dN']:
        dO['dRes'][s].append(dO['dN'][s])
     
def Gillespie_C(dI):
    print('Starting new stochastic simulation (Gillespie_C algorithm)!')
    t, T, cTSt = dI['tStart'], dI['Tmax'], 0
    dO = iniDictOut(dI, t)
    while t < T:
        # adapt the re-calc reaction rate hazards function to current system
        reCalcReactHazardsCR(dI, dO)
        # do next event and update time with tToNext
        t += nextEvent(dI, dO, T, cTSt)
        # update the data storage matrix
        if t < T:
            updateDictOut(dI, dO, t)
        cTSt += 1
    return dO

# Functions (output) ----------------------------------------------------------
def createDir(pF):
    if not os.path.isdir(pF):
        os.mkdir(pF)

def joinToPath(pF = '', sF = 'Dummy.txt'):
    if len(pF) > 0:
        createDir(pF)
        return os.path.join(pF, sF)
    else:
        return sF

def saveDataDict(dI, dO):
    pF = joinToPath(dI['pF_DataCR'], dI['sF_DataCR'] + '.' + dI['sFExtCSV'])
    fRes = open(pF, dI['mdApp'])
    fRes.write(S_TIME)
    for s in dI['dNSpec']:
        fRes.write(dI['sepCSV'] + s)
    fRes.write('\n')
    for k, cT in enumerate(dO['dRes'][S_TIME]):
        fRes.write(str(round(cT, dI['nDgRnd'])))
        for s in dO['dRes']:
            fRes.write(dI['sepCSV'] + str(dO['dRes'][s][k]))
        fRes.write('\n')
    fRes.close()

def saveResDataFrame(dI, dO, overWrite = True):
    pF = joinToPath(dI['pF_DataCR'], dI['sF_DataCR'] + '.' + dI['sFExtCSV'])
    if not os.path.isfile(pF) or overWrite:
        pd.DataFrame(dO['dRes']).to_csv(pF, sep = dI['sepCSV'])
    return pF

# MAIN ========================================================================
dOut = Gillespie_C(dInp)
pFDfr = saveResDataFrame(dInp, dOut)
print('Saved result DataFrame to', pFDfr)
print('*'*24, 'DONE', '*'*24)

# -----------------------------------------------------------------------------