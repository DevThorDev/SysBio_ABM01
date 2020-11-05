# -*- coding: utf-8 -*-
###############################################################################
# --- F_01__SpcFunctions.py ---------------------------------------------------
###############################################################################
import pandas as pd

import Core.C_00__GenConstants as GC
import Core.F_00__GenFunctions as GF

# --- Functions (O_90__Component) ---------------------------------------------
def setPylDPy(dIdx, sComp, lKAs, lPAs, dSitesPyl = GC.DS_SITES_PYL):
    assert len(sComp) == 3 + 4
    assert set(sComp[3:]) <= GC.SET_01_USC
    assert dIdx['iSP'] >= 3 and dIdx['iSP'] < len(sComp)
    sPylDePyl, cAse = dSitesPyl[sComp[dIdx['iSP']]], None
    if sPylDePyl == GC.S_DO_PYL:
        cAse = lKAs[dIdx['iLAse']]
    elif sPylDePyl == GC.S_DO_DEPYL:
        cAse = lPAs[dIdx['iLAse']]
    return sPylDePyl, cAse

# --- Functions (O_99__System) ------------------------------------------------
def prepDict4Sel(d4Sel, d4Leg, lSLY, dCp, dSCp):
    for sCol in lSLY:
        for sSimple, lSimple in dCp.items():
            if len(sCol) >= 2:
                if sCol[0] in lSimple and set(sCol[1:]) <= GC.SET_01_USC:
                    GF.addToDictL(d4Sel, sSimple, sCol, lUnique = True)
                    GF.addToDictL(d4Leg, sSimple, GC.S_COM_BL.join(lSimple),
                                  lUnique = True)
                else:
                    if ((sCol[0] not in dSCp) or
                        (not (set(sCol[1:]) <= GC.SET_01_USC))):
                        if sCol not in d4Sel:
                            GF.addToDictL(d4Sel, sCol, sCol, lUnique = True)
                            GF.addToDictL(d4Leg, sCol, sCol, lUnique = True)

def preProcMeanSum(pdDfr, sLX, lSLY, tKDCp, dSCp):
    d4Sel, d4Leg, mdDfr = {}, {}, pd.DataFrame()
    sOp, dCp = tKDCp
    prepDict4Sel(d4Sel, d4Leg, lSLY, dCp, dSCp = dSCp)
    mdDfr.loc[:, sLX] = pdDfr.loc[:, sLX]
    for sK in d4Sel:
        if sK in dSCp:
            if sOp == GC.S_MEAN:
                mdDfr.loc[:, sK] = pdDfr.loc[:, d4Sel[sK]].T.mean()
            elif sOp == GC.S_SUM:
                mdDfr.loc[:, sK] = pdDfr.loc[:, d4Sel[sK]].T.sum()
        else:
            mdDfr.loc[:, sK] = pdDfr.loc[:, sK]
    return mdDfr, d4Leg

###############################################################################
