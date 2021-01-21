# -*- coding: utf-8 -*-
###############################################################################
# --- F_01__SpcFunctions.py ---------------------------------------------------
###############################################################################
import numpy as np

import Core.C_00__GenConstants as GC
import Core.F_00__GenFunctions as GF

# --- Functions (M_0__Main) ---------------------------------------------------
def calcRunMeanM2Dfr(dDfrI, cDfr, cCt=0, lSCDisr=[GC.S_TIME]):
    lSCCalc = [sC for sC in cDfr.columns if sC not in lSCDisr]
    # initialise if full results DataFrame is still empty
    if len(dDfrI) == 0:
        for sK in [GC.S_MEAN, GC.S_M2]:
            dDfrI[sK] = GF.iniPdDfr(lSNmC=lSCCalc, lSNmR=cDfr.index)
            # try:
            #     dDfrI[sK] = GF.iniPdDfr(lSNmC=lSCCalc, lSNmR=cDfr.index)
            # except:
            #     print('sK =', sK)
            #     print('lSCCalc =', lSCCalc)
            #     print('cDfr.index =', list(cDfr.index))
            #     assert False
    # update the current value aggregate, and re-assign values to DataFrames
    for sR in cDfr.index:
        for sC in lSCCalc:
            cMn, cM2 = dDfrI[GC.S_MEAN].at[sR, sC], dDfrI[GC.S_M2].at[sR, sC]
            # if sR in list(cDfr.index)[:2] and sC in lSCCalc[:3]:
            #     print('(', sR, ',', sC, ') - cMn/M2 (before):', cMn, cM2)
            cMn, cM2 = GF.updateMeanM2(cMn, cM2, cCt, cDfr.at[sR, sC])
            # if sR in list(cDfr.index)[:2] and sC in lSCCalc[:3]:
            #     print('(', sR, ',', sC, ') - cMn/M2 (after):', cMn, cM2)
            dDfrI[GC.S_MEAN].at[sR, sC], dDfrI[GC.S_M2].at[sR, sC] = cMn, cM2

def calcMeanVarSDDfr(dDfrI, nRp=0):
    lSR, lSC = dDfrI[GC.S_MEAN].index, dDfrI[GC.S_MEAN].columns
    for sK in [GC.S_VARIANCE, GC.S_STDDEV, GC.S_SEM]:
        dDfrI[sK] = GF.iniPdDfr(lSNmC=lSC, lSNmR=lSR)
    for sR in lSR:
        for sC in lSC:
            cAg = (nRp, dDfrI[GC.S_MEAN].at[sR, sC], dDfrI[GC.S_M2].at[sR, sC])
            cMn, cVar, cVarS = GF.finalRunMeanSD(cAg)
            cStdDevS, cSEM = np.sqrt(cVarS), 0
            if nRp > 0:
                cSEM = cStdDevS/np.sqrt(nRp)
            dDfrI[GC.S_MEAN].at[sR, sC] = cMn
            dDfrI[GC.S_VARIANCE].at[sR, sC] = cVarS
            dDfrI[GC.S_STDDEV].at[sR, sC] = cStdDevS
            dDfrI[GC.S_SEM].at[sR, sC] = cSEM

def reduceData(dIG, dfrResFull, sCT=GC.S_TIME, cRep=0):
    # dfrRed = GF.iniPdDfr(lSNmC = [GC.S_REP] + list(dfrResFull.columns))
    halfStep = dIG['tMax']/(2*dIG['nTSAllRep'])
    lTRed = [k*halfStep for k in range(1, 2*dIG['nTSAllRep'], 2)]
    # print('TEMP - lTRed:', lTRed, '--> has', len(lTRed), 'length.')
    # print('TEMP - times from Dfr:', [round(t, 5) for t in dfrResFull[sCT]],
    #       '--> has', len(list(dfrResFull[sCT])), 'length.')
    assert sCT in dfrResFull.columns
    lDfr = [dfrResFull[(dfrResFull[sCT] >= lTRed[k - 1]) &
                       (dfrResFull[sCT] < lTRed[k + 1])]
            for k in range(1, len(lTRed) - 1)]
    lDfr = ([dfrResFull[dfrResFull[sCT] < lTRed[1]]] + lDfr +
            [dfrResFull[dfrResFull[sCT] >= lTRed[-2]]])
    lDfr = [cDfr.reset_index(drop=True) for cDfr in lDfr]
    lSCAv = [sC for sC in dfrResFull.columns if sC != sCT]
    dL = {sCT: lTRed}
    dL.update({sC: [np.mean(cDfr[sC]) for cDfr in lDfr] for sC in lSCAv})
    # if cRep == 1:
    #     print('TEMP (BEGIN):')
    #     print('Time F (last 100):', [round(v, 8) for v in list(dfrResFull[sCT])[-100:]])
    #     print()
    #     for k, cDfr in enumerate(lDfr):
    #         # print('Shape:', cDfr.shape)
    #         print('Time\t', k, ':\t', '|\t', lTRed[k])
    #         lV = [round(v, 8) for v in cDfr[sCT]]
    #         print('Times\t', k, ':\t', '|\t', lV)
    #         lV = [round(v, 8) for v in cDfr[lSCAv[0]]]
    #         print('NO3_1m\t', k, ':\t', np.mean(cDfr[lSCAv[0]]), '|\t', lV)
    #     print('TEMP (END).')
    dfrRed = GF.iniPdDfr(dL)
    # dfrResFull.append({sC: llDatRed[k] for k, sC in enumerate(dfrRed.columns)},
    #               ignore_index = True)
    print('TEMP (BEGIN):')
    # print('dfrRed:')
    # print(dfrRed)
    sF = 'dfrRed' + GC.S_USC + GC.S_REP + str(cRep) + '.csv'
    dfrRed.to_csv(dIG['sPRes'] + '/' + sF, sep=dIG['cSep'])
    # print('List of DataFrames (times only):')
    # d = {}
    # for cDfr in lDfr:
    #     print(len(list(cDfr[sCT])), '\tel. list:',
    #           [round(x, 5) for x in cDfr[sCT]])
    #     GF.addToDictCt(d, len(list(cDfr[sCT])))
    # print('Number of list lengths:')
    # for lL, nOcc in sorted(d.items()):
    #     print(str(lL) + ':\t', nOcc)
    # # print(GC.S_DASH*80)
    # # i, j, ct = 0, 0, 0
    # # for k in dfrResFull.index:
    # #     while i == lDfr[j].shape[0]:
    # #         i = 0
    # #         j += 1
    # #     s = str(ct) + '\t' + str(k) + '\t' + str(j) + '\t' + str(i) + '\t' + str(round(dfrResFull.loc[k, sCT], 5))
    # #     if j < len(lDfr):
    # #         s += '\t' + str(round(lDfr[j].loc[i, sCT], 5)) + '\t' + str(j)
    # #         ct += 1
    # #     else:
    # #         s += 'ERROR: j = ' + str(j) + ' but number of Dfr is ' + str(len(lDfr)) + '.'
    # #         break
    # #     print(s)
    # #     i += 1
    # print(GC.S_DASH*80)
    # print('Number of rows in original Dfr:', dfrResFull.shape[0])
    # print('Total number of rows in Dfrs from list:',
    #       sum([cDfr.shape[0] for cDfr in lDfr]))
    # # print('Counter:', ct)
    print('TEMP (END).')
    return dfrRed

# def calcDfrAv(dIG, )

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
                        GF.addToDictL(d4Sel, sLg, sHdC, lUnique=True)
                        GF.addToDictL(d4Leg, sLg, GC.S_COM_BL.join(lCp),
                                      lUnique=True)
                        break
            else:
                # this column header IS NOT a component string
                if sHdC not in d4Sel:
                    GF.addToDictL(d4Sel, sHdC, sHdC, lUnique=True)
                    GF.addToDictL(d4Leg, sHdC, sHdC, lUnique=True)


def preProcMeanSum(pdDfr, sLX, lSLY, tKDCp, dSCp):
    d4Sel, d4Leg, mdDfr = {}, {}, GF.iniPdDfr()
    sOp, dCp = tKDCp
    prepDict4Sel(d4Sel, d4Leg, lSLY, dCp, dSCp=dSCp)
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
