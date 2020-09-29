# -*- coding: utf-8 -*-
###############################################################################
# --- F_03__OTpFunctions.py ---------------------------------------------------
###############################################################################
import copy
import numpy as np

import Core.C_00__GenConstants as GC

# --- Functions (general) -----------------------------------------------------

# --- Functions (O_00__Base) --------------------------------------------------
def getDITp(dIG, iTp0, iTp):
    dITp = copy.deepcopy(dIG[iTp0])    # content of iTp = 0 input
    dITp.update(dIG[iTp])              # updated with iTp = iTp input
    return dITp

# --- Functions (O_03__Metabolite) --------------------------------------------
def doSinChange(x, cPer, cAmpl):
    return cAmpl*np.sin(x*2*np.pi/cPer)

# --- Functions (O_80__Interaction) -------------------------------------------
def doSiteChange(cO, sSpS, sAse, doDePyl = False):
    opDone = False
    assert sSpS in cO.dITp['dInfSpS']
    dSpS = cO.dITp['dInfSpS'][sSpS]
    if not doDePyl and dSpS['Stat'] == GC.B_NOT_PYL and sAse in dSpS['Pyl']:
        dSpS['Stat'] = GC.B_IS_PYL
        opDone = True
    elif doDePyl and dSpS['Stat'] == GC.B_IS_PYL and sAse in dSpS['DePyl']:
        dSpS['Stat'] = GC.B_NOT_PYL
        opDone = True
    if opDone:
        cO.dSpS[sSpS].sSPTM = dSpS['Stat']
    return opDone

# --- Functions (O_90_State) --------------------------------------------------
def complLSpec(inpDt, lOAll, sTp = 'KAs', sD = 'Pyl'):
    lID = []
    for cO in lOAll:
        for cSpS in cO.dITp['dInfSpS']:
            for idTp in cO.dITp['dInfSpS'][cSpS][sD]:
                if idTp not in lID:
                    lID.append(idTp)
    return sorted(lID)

# --- Functions (O_99__System) ------------------------------------------------
def printSysComp(sCmp = 'Base', lOCmp = []):
    print('-'*8, sCmp, '-'*8)
    for cO in lOCmp:
        s = cO.descO + ' ' + cO.dITp['strCS'] + ' with ID ' + str(cO.idO)
        if cO.nSpS > 0:
            s += ' and special sites '
            s += str(cO.extractLSpecSitesS())
        if len(cO.sSpS) > 0:
            s += ' for special site ' + cO.sSpS
        print(s)

###############################################################################
