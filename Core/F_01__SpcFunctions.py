# -*- coding: utf-8 -*-
###############################################################################
# --- F_01__SpcFunctions.py ---------------------------------------------------
###############################################################################
import os

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
    # update the current value aggregate, and re-assign values to DataFrames
    for sR in cDfr.index:
        for sC in lSCCalc:
            cMn, cM2 = dDfrI[GC.S_MEAN].at[sR, sC], dDfrI[GC.S_M2].at[sR, sC]
            cMn, cM2 = GF.updateMeanM2(cMn, cM2, cCt, cDfr.at[sR, sC])
            dDfrI[GC.S_MEAN].at[sR, sC], dDfrI[GC.S_M2].at[sR, sC] = cMn, cM2
    for sK in [GC.S_MEAN, GC.S_M2]:
        if GC.S_TIME not in dDfrI[sK].columns:
            dDfrI[sK] = GF.iniPdDfr(cDfr[GC.S_TIME]).join(dDfrI[sK])

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

def reduceData(dIG, dITp, dfrResFull, sCT=GC.S_TIME, cRep=0):
    sP = os.path.join(dIG['sPRes'], dITp['sD_Obj'])
    if cRep > 0:
        sP = os.path.join(sP, GC.S_REP + str(cRep))
    halfStep = dIG['tMax']/(2*dIG['nTSAllRep'])
    lTRed = [k*halfStep for k in range(1, 2*dIG['nTSAllRep'], 2)]
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
    dfrRed = GF.iniPdDfr(dL)
    sF = 'dfrRed' + GC.S_USC + GC.S_REP + str(cRep) + '.csv'
    dfrRed.to_csv(dIG['sPRes'] + '/' + sF, sep=dIG['cSep'])
    return dfrRed

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
def prepDict4Sel(d4Sel, d4Leg, lSLY, dCp):
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
    prepDict4Sel(d4Sel, d4Leg, lSLY, dCp)
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
