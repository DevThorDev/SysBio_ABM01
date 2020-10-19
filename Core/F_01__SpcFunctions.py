# -*- coding: utf-8 -*-
###############################################################################
# --- F_01__SpcFunctions.py ---------------------------------------------------
###############################################################################
import pandas as pd

import Core.C_00__GenConstants as GC
import Core.F_00__GenFunctions as GF

# --- Functions (O_99__System) ------------------------------------------------
def prepDict4Sel(d4Sel, d4Leg, lSLY, dSt):
    for sCol in lSLY:
        for sSimple, lSimple in dSt.items():
            if len(sCol) >= 2:
                if sCol[0] in lSimple and set(sCol[1:]) <= {'0', '1'}:
                    GF.addToDictL(d4Sel, sSimple, sCol, lUnique = True)
                    GF.addToDictL(d4Leg, sSimple, GC.S_COM_BL.join(lSimple),
                                  lUnique = True)
                else:
                    if ((sCol[0] not in GC.DS_ST_4) or
                        (not (set(sCol[1:]) <= {'0', '1'}))):
                        if sCol not in d4Sel:
                            GF.addToDictL(d4Sel, sCol, sCol, lUnique = True)
                            GF.addToDictL(d4Leg, sCol, sCol, lUnique = True)

def preProcMeanSum(pdDfr, sLX, lSLY, tKDSt):
    d4Sel, d4Leg, mdDfr = {}, {}, pd.DataFrame()
    sOp, dSt = tKDSt
    prepDict4Sel(d4Sel, d4Leg, lSLY, dSt)
    mdDfr.loc[:, sLX] = pdDfr.loc[:, sLX]
    for sK in d4Sel:
        if sK in GC.DS_ST_4:
            if sOp == GC.S_MEAN:
                mdDfr.loc[:, sK] = pdDfr.loc[:, d4Sel[sK]].T.mean()
            elif sOp == GC.S_SUM:
                mdDfr.loc[:, sK] = pdDfr.loc[:, d4Sel[sK]].T.sum()
        else:
            mdDfr.loc[:, sK] = pdDfr.loc[:, sK]
    # print('TEMP  d4Leg =\n', d4Leg)
    return mdDfr, d4Leg

###############################################################################
