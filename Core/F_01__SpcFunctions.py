# -*- coding: utf-8 -*-
###############################################################################
# --- F_01__SpcFunctions.py ---------------------------------------------------
###############################################################################
import numpy as np

import Core.C_00__GenConstants as GC
import Core.F_00__GenFunctions as GF

# --- Functions (M_0__Main) ---------------------------------------------------
def reduceData(dIG, dfrRes, cRep = 0, dfrFin = None):
    if dfrFin is None:
        dfrFin = GF.iniPdDfr(lSNmC = list(dfrRes.columns))
    # dfrRed = GF.iniPdDfr(lSNmC = [GC.S_REP] + list(dfrRes.columns))
    halfStep = dIG['tMax']/(2*dIG['nTSAllRep'])
    lTRed = [k*halfStep for k in range(1, 2*dIG['nTSAllRep'], 2)]
    # print('TEMP - lTRed:', lTRed, '--> has', len(lTRed), 'length.')
    # print('TEMP - times from Dfr:', [round(t, 5) for t in dfrRes[GC.S_TIME]],
    #       '--> has', len(list(dfrRes[GC.S_TIME])), 'length.')
    assert GC.S_TIME in dfrRes.columns
    lDfr = [dfrRes[(dfrRes[GC.S_TIME] >= lTRed[k - 1]) &
                   (dfrRes[GC.S_TIME] < lTRed[k + 1])]
            for k in range(1, len(lTRed) - 1)]
    lDfr = ([dfrRes[dfrRes[GC.S_TIME] < lTRed[1]]] + lDfr +
            [dfrRes[dfrRes[GC.S_TIME] >= lTRed[-2]]])
    lDfr = [cDfr.reset_index(drop = True) for cDfr in lDfr]
    # llDatRed = [[cRep]*dIG['nTSAllRep'], lTRed]
    # assert len(llDatRed) == le n(dfrRed.columns)
    lSCMn = [sC for sC in dfrFin.columns if sC != GC.S_TIME]
    dL = {GC.S_REP: [cRep]*dIG['nTSAllRep'], GC.S_TIME: lTRed}
    dL.update({sC: [np.mean(cDfr[sC]) for cDfr in lDfr] for sC in lSCMn})
    dfrRed = GF.iniPdDfr(dL)
    # dfrFin.append({sC: llDatRed[k] for k, sC in enumerate(dfrRed.columns)},
    #               ignore_index = True)
    print('TEMP (BEGIN):')
    print('dfrRed:')
    print(dfrRed)
    dfrRed.to_csv(dIG['sPRes'] + '/dfrRed_' + GC.S_REP + str(cRep) + '.csv',
                  sep = dIG['cSep'])
    # print('List of DataFrames (times only):')
    # d = {}
    # for cDfr in lDfr:
    #     print(len(list(cDfr[GC.S_TIME])), '\tel. list:',
    #           [round(x, 5) for x in cDfr[GC.S_TIME]])
    #     GF.addToDictCt(d, len(list(cDfr[GC.S_TIME])))
    # print('Number of list lengths:')
    # for lL, nOcc in sorted(d.items()):
    #     print(str(lL) + ':\t', nOcc)
    # # print(GC.S_DASH*80)
    # # i, j, ct = 0, 0, 0
    # # for k in dfrRes.index:
    # #     while i == lDfr[j].shape[0]:
    # #         i = 0
    # #         j += 1
    # #     s = str(ct) + '\t' + str(k) + '\t' + str(j) + '\t' + str(i) + '\t' + str(round(dfrRes.loc[k, GC.S_TIME], 5))
    # #     if j < len(lDfr):
    # #         s += '\t' + str(round(lDfr[j].loc[i, GC.S_TIME], 5)) + '\t' + str(j)
    # #         ct += 1
    # #     else:
    # #         s += 'ERROR: j = ' + str(j) + ' but number of Dfr is ' + str(len(lDfr)) + '.'
    # #         break
    # #     print(s)
    # #     i += 1
    # print(GC.S_DASH*80)
    # print('Number of rows in original Dfr:', dfrRes.shape[0])
    # print('Total number of rows in Dfrs from list:',
    #       sum([cDfr.shape[0] for cDfr in lDfr]))
    # # print('Counter:', ct)
    print('TEMP (END).')

def calcDfrAv(dIG, )

# --- Functions (O_90__Component) ---------------------------------------------
def setPylDPy(sCp, iSpS):
    assert len(sCp) == GC.LEN_S_CP
    sCpP2 = sCp[GC.I_S_CP_SEP1:]
    assert set(sCpP2) <= GC.SET_0_1_DASH
    sPD = GC.S_DASH
    if sCpP2[iSpS] == GC.S_1:
        sPD = GC.S_DO_PYL
    elif sCpP2[iSpS] == GC.S_0:
        sPD = GC.S_DO_DPY
    return sPD

# --- Functions (O_95__System) ------------------------------------------------
def prepDict4Sel(d4Sel, d4Leg, lSLY, dCp, dSCp):
    for sHdC in lSLY:
        for sLg, lCp in dCp.items():
            if (len(sHdC) == GC.LEN_S_CP and
                set(sHdC[GC.I_S_CP_SEP1:]) <= GC.SET_0_1_DASH):
                # this column header IS a component string
                for sCp in lCp:
                    if sHdC.startswith(sCp):
                        GF.addToDictL(d4Sel, sLg, sHdC, lUnique = True)
                        GF.addToDictL(d4Leg, sLg, GC.S_COM_BL.join(lCp),
                                      lUnique = True)
                        break
            else:
                # this column header IS NOT a component string
                if sHdC not in d4Sel:
                    GF.addToDictL(d4Sel, sHdC, sHdC, lUnique = True)
                    GF.addToDictL(d4Leg, sHdC, sHdC, lUnique = True)

def preProcMeanSum(pdDfr, sLX, lSLY, tKDCp, dSCp):
    d4Sel, d4Leg, mdDfr = {}, {}, GF.iniPdDfr()
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
