# -*- coding: utf-8 -*-
###############################################################################
# --- T_01__Gillespie_A.py ----------------------------------------------------
###############################################################################
import math, random

# Input dictionary ------------------------------------------------------------
dInp = {'N': 350,       # total population (int)
        'T': 100.0,     # maximum elapsed time (float)
        't': 0.0,       # start time (float)
        'V': 100.0,     # spatial parameter (float)
        'alpha': 10.0,  # rate of infection after contact (float)
        'beta': 10.0,   # rate of cure (float)
        'nI': 1,        # initial infected population (int)
        # path, directory and file names
        'sF_DataSIR': 'DataSIR.txt',
        'mdApp': 'w+'}

# Functions -------------------------------------------------------------------
def iniSimu(dI):
    dO = {}
    nS, nR = dI['N'] - dI['nI'], 0
    dO['lT_SIR'] = [(dI['t'], nS, dI['nI'], nR)]    # ini. results
    return dO

def Gillespie_A(dI, dO):
    t, nS, nI, nR =  dO['lT_SIR'][0]
    while t < dI['T']:
        if nI <= 0:
            break
        w1 = dI['alpha']*nS*nI/dI['V']
        w2 = dI['beta']*nI
        W = w1 + w2
        # generate exponentially distributed random variable dt
        # using inverse transform sampling
        dt = -math.log(1 - random.uniform(0.0, 1.0))/W
        t = t + dt
        if random.uniform(0.0, 1.0) < w1/W:
            nS = nS - 1
            nI = nI + 1
        else:
            nI = nI - 1
            nR = nR + 1
        dO['lT_SIR'].append((t, nS, nI, nR))

def writeResults(dI, dO):
    with open(dI['sF_DataSIR'], dI['mdApp']) as fp:
        fp.write('\n'.join('%f %i %i %i' % x for x in dO['lT_SIR']))

# Main ------------------------------------------------------------------------
dOut = iniSimu(dInp)
Gillespie_A(dInp, dOut)
writeResults(dInp, dOut)
print('*'*24, 'DONE', '*'*24)

# -----------------------------------------------------------------------------