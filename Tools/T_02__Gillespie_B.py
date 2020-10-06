# -*- coding: utf-8 -*-
###############################################################################
# --- T_01__Gillespie_B.py ----------------------------------------------------
###############################################################################
import os
import pandas as pd
from operator import itemgetter
from numpy.random import default_rng as RNG

# Constants -------------------------------------------------------------------
S_TIME = 'Time'
R_04 = 4

# Input dictionary ------------------------------------------------------------
dInp = {'dNSpec':{'E': 100,         # names & numbers of chemical species
                  'S': 500,
                  'ES': 10,
                  'P': 0},
        'RRC_EpS_ES': 0.0001,       # reaction rate constant E + S --> ES
        'RRC_ES_EpS': 2.5,          # reaction rate constant ES --> E + S
        'RRC_ES_EpP': 0.5,          # reaction rate constant ES --> E + P
        'Tmax': 100.0,              # maximum elapsed time (float)
        'tStart': 0.0,              # start time (float)
        # path, directory and file names, and file extensions
        'pF_DataCR': 'Gillespie_B',
        'sF_DataCR': 'DataCR',
        'sFExtCSV': 'csv',
        'sepCSV': ';',
        'mdApp': 'w',
        # other constants
        'sTime': S_TIME,
        'nDgRnd': R_04}

# Functions (initialisation) --------------------------------------------------
def iniSimu(dI):
    dO = {}
    dO['lRRC'] = [dI['RRC_EpS_ES'], dI['RRC_ES_EpS'], dI['RRC_ES_EpP']]
    dO['dRes'] = {dI['sTime']: [dI['tStart']]}              # times
    for s, k in dI['dNSpec'].items():
        dO['dRes'][s] = [k]                                 # species numbers
    return dO

# Functions (Gillespie core) --------------------------------------------------
def sortLReactHazardsAsc(dO, h):
    nRs = len(dO['lRRC'])
    hTupS = sorted(((h[k], k) for k in range(nRs)), key = itemgetter(0))
    (dO['lhS'], dO['liS']) = ([hTupS[k][0] for k in range(nRs)],
                              [hTupS[k][1] for k in range(nRs)])
    # the combined reaction hazard hSum = sum(lhS)
    dO['hSum'] = sum(dO['lhS'])

def reCalcReactHazardsCR(dI, dO, cTS):
    dO['dN'] = {s: dO['dRes'][s][cTS] for s in dI['dNSpec']}
    h = [0.0]*len(dO['lRRC'])
    # recalculate h, which contains the h_i (i = 1, 2, 3)
    h[0] = dO['lRRC'][0]*dO['dN']['E']*dO['dN']['S']
    h[1] = dO['lRRC'][1]*dO['dN']['ES']
    h[2] = dO['lRRC'][2]*dO['dN']['ES']
    # sort h in ascending order for numerical stability
    sortLReactHazardsAsc(dO, h)

def eventReactionsMM(dO):
    # draw the index of the reaction that happens
    uRN = RNG().random()
    # get the reaction index
    rIdx = -1
    if uRN < dO['lhS'][0]/dO['hSum']:
        rIdx = dO['liS'][0]
    elif (uRN >= dO['lhS'][0]/dO['hSum'] and
          uRN < sum(dO['lhS'][:2])/dO['hSum']):
        rIdx = dO['liS'][1]
    else:
        rIdx = dO['liS'][2]
    # update the state dO['dN']
    if rIdx == 0:       # (E + S --> ES)
        dO['dN']['E'] -= 1
        dO['dN']['S'] -= 1
        dO['dN']['ES'] += 1
    elif rIdx == 1:     # (ES --> E + S)
        dO['dN']['E'] += 1
        dO['dN']['S'] += 1
        dO['dN']['ES'] -= 1
    elif rIdx == 2:     # (ES --> E + P)
        dO['dN']['E'] += 1
        dO['dN']['ES'] -= 1
        dO['dN']['P'] += 1 
    else:
        print('No reaction occurred!?') # so something went wrong...

def nextEvent(dI, dO, cTS):
    tToNxt = 0
    if dO['hSum'] > 0:    # otherwise the while-loop ends, see the other case
        # draw the time to the next event from exponential(lambd = 1./hSum)
        tToNxt = RNG().exponential(1./dO['hSum'])
        # adapt the event reactions to considered system
        eventReactionsMM(dO)
    else:
        # if no reaction is possible, then hSum becomes 0, therefore stop
        print('The combined reaction hazard is 0 - no reaction possible')
        tToNxt = dI['Tmax'] - dO['dRes'][dI['sTime']][cTS]
    return tToNxt

def updateDictOut(dI, dO, t):
    dO['dRes'][dI['sTime']].append(t)
    for s in dO['dN']:
        dO['dRes'][s].append(dO['dN'][s])
        
def Gillespie_B(dI):
    print('Starting new stochastic simulation (Gillespie_B algorithm)!')
    cTSt, t, dO = 0, dI['tStart'], iniSimu(dI)
    while t < dI['Tmax']:
        # adapt the re-calc reaction rate hazards function to current system
        reCalcReactHazardsCR(dI, dO, cTSt)
        # do next event and update time with tToNext
        t += nextEvent(dI, dO, cTSt)
        # update the data storage matrix
        if t < dI['Tmax']:
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
    fRes.write(dI['sTime'])
    for s in dI['dNSpec']:
        fRes.write(dI['sepCSV'] + s)
    fRes.write('\n')
    for k, cT in enumerate(dO['dRes'][dI['sTime']]):
        fRes.write(str(round(cT, dI['nDgRnd'])))
        for s in dO['dRes']:
            fRes.write(dI['sepCSV'] + str(dO['dRes'][s][k]))
        fRes.write('\n')
    fRes.close()

def saveDataFrame(dI, dO, overWrite = True):
    pF = joinToPath(dI['pF_DataCR'], dI['sF_DataCR'] + '.' + dI['sFExtCSV'])
    if not os.path.isfile(pF) or overWrite:
        pd.DataFrame(dO['dRes']).to_csv(pF, sep = dI['sepCSV'])
    return pF

# MAIN ========================================================================
dOut = Gillespie_B(dInp)
# saveDataDict(dInp, dOut)
pFDfr = saveDataFrame(dInp, dOut)
print('Saved result DataFrame to', pFDfr)
print('*'*24, 'DONE', '*'*24)

# -----------------------------------------------------------------------------