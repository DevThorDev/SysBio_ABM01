# -*- coding: utf-8 -*-
###############################################################################
# --- F_01__SpcFunctions.py ---------------------------------------------------
###############################################################################
import os, copy
from operator import itemgetter
import numpy as np

import Core.C_00__GenConstants as GC
import Core.F_00__GenFunctions as GF

# --- Functions (general) -----------------------------------------------------
def getPF(lD4P, sF, sFExt=GC.S_EXT_CSV):
    return GF.joinToPath(lD4P, sF + '.' + sFExt)

def savePdDfr(dITp, pdDfr, lD, sF, overWr=True, sFExt=GC.S_EXT_CSV):
    sP = getPF([dITp['sPRes']] + lD, sF, sFExt=sFExt)
    if not os.path.isfile(sP) or overWr:
        pdDfr.to_csv(sP, sep=dITp['cSep'])
    return sP

def loadPdDfr(dITp, lD, sF, sFExt=GC.S_EXT_CSV):
    sP = getPF([dITp['sPRes']] + lD, sF, sFExt=sFExt)
    if os.path.isfile(sP):
        return GF.readCSV(sP, sepD=dITp['cSep'])
    return GF.iniPdDfr()

def saveAsPdDfr(dITp, dRes, lD, sF, overWr=True, sFExt=GC.S_EXT_CSV):
    sP = getPF([dITp['sPRes']] + lD, sF, sFExt=sFExt)
    if not os.path.isfile(sP) or overWr:
        GF.iniPdDfr(dRes).to_csv(sP, sep=dITp['cSep'])
    return sP

# --- Functions (O_00__Base) --------------------------------------------------
def getDITp(dIG, iTp, lITpU):
    dITp = {}
    if len(lITpU) > 0:
        dITp = copy.deepcopy(dIG[lITpU[0]])     # content of lITpU[0] input
        for iTpU in lITpU[1:]:
            GF.updateDITpDIPlt(dITp, dIG[iTpU]) # updated with iTpU input
    GF.updateDITpDIPlt(dITp, dIG[iTp])          # updated with iTp input
    return dITp

# --- Functions (O_03__Metabolite) --------------------------------------------
def clampF(x, xSlopeStart=0., xSlopeEnd=1.):
    assert xSlopeEnd >= xSlopeStart
    if x < xSlopeStart:
        x = xSlopeStart
    elif x > xSlopeEnd:
        x = xSlopeEnd
    return x

def smoothStepF(x, lX_LR=[0., 1.], lY_LR=[0., 1.], cOrdSm=0):
    assert (len(lX_LR) == len(lY_LR) and len(lX_LR) == 2)
    ((xL, xR), (yL, yR)) = lX_LR, lY_LR
    lbd = 1.
    if xL != xR:
        # scale, bias and saturate x to the [0, 1] range
        x = clampF((x - xL)/abs(xR - xL))
        lbd = x
        # evaluate polynomial corresponding to current smoothing order cOrdSm
        if cOrdSm == 1:
            lbd = x*x*(-2*x + 3)
        elif cOrdSm == 2:
            lbd = x*x*x*(x*(6*x - 15) + 10)
        elif cOrdSm == 3:
            lbd = x*x*x*x*(x*(x*(-20*x + 70) - 84) + 35)
    return yL + lbd*(yR - yL)

def stepF_1Step(dPar, x, lX_LR, lY_LR, lSStep, cOrdSm=0):
    assert (len(lX_LR) == len(lY_LR) and len(lX_LR) == len(lSStep) and
            len(lX_LR) >= 2)
    if (x < lX_LR[0]):
        return dPar[lSStep[0]]
    elif (x >= lX_LR[0] and x < lX_LR[1]):
        return smoothStepF(x, lX_LR, lY_LR, cOrdSm)
    else:
        return dPar[lSStep[1]]

def stepF_2Step(dPar, x, lX_LR1, lX_LR2, lY_LR1, lY_LR2, lSStep, cOrdSm=0):
    assert (len(lX_LR1) == len(lY_LR1) and len(lX_LR2) == len(lY_LR2) and
            len(lX_LR1) >= 2 and len(lX_LR2) >= 2 and len(lSStep) >= 3)
    if (x < lX_LR1[0]):
        return dPar[lSStep[0]]
    elif (x >= lX_LR1[0] and x < lX_LR1[1]):
        return smoothStepF(x, lX_LR1, lY_LR1, cOrdSm)
    elif (x >= lX_LR1[1] and x < lX_LR2[0]):
        return dPar[lSStep[1]]
    elif (x >= lX_LR2[0] and x < lX_LR2[1]):
        return smoothStepF(x, lX_LR2, lY_LR2, cOrdSm)
    else:
        return dPar[lSStep[2]]

def doStepChange(x, dPar):
    sStepT1, sStepT2 = GC.S_STEP_T1, GC.S_STEP_T2
    sStepV01, sStepV12, sStepV_T = GC.S_STEP_V01, GC.S_STEP_V12, GC.S_STEP_V_T
    sDltSm1, sDltSm2, sSmOrd = GC.S_DLT_SM_1, GC.S_DLT_SM_2, GC.S_SM_ORD
    if (sStepT1 in dPar and sStepV01 in dPar and sStepV_T in dPar):
        yL_T1, yR_T1, smOrd = dPar[sStepV01], dPar[sStepV_T], -1
        xL_T1, xR_T1 = dPar[sStepT1], dPar[sStepT1]
        if sSmOrd in dPar:
            smOrd = dPar[sSmOrd]
        if (sDltSm1 in dPar and smOrd >= 0):
            assert dPar[sDltSm1] >= 0
            xL_T1 = dPar[sStepT1] - dPar[sDltSm1]
            xR_T1 = dPar[sStepT1] + dPar[sDltSm1]
        if (sStepT2 in dPar and sStepV12 in dPar):
            assert dPar[sStepT1] <= dPar[sStepT2]
            yR_T1, yR_T2 = dPar[sStepV12], dPar[sStepV_T]
            yL_T2, xL_T2, xR_T2 = yR_T1, dPar[sStepT2], dPar[sStepT2]
            if (sDltSm2 in dPar and smOrd >= 0):
                assert dPar[sDltSm2] >= 0
                xL_T2 = dPar[sStepT2] - dPar[sDltSm2]
                xR_T2 = dPar[sStepT2] + dPar[sDltSm2]
            if (xL_T2 < xR_T1):
                xL_T2 = 0.5*(xR_T1 + xL_T2)
                xR_T1 = xL_T2
            return stepF_2Step(dPar, x, [xL_T1, xR_T1], [xL_T2, xR_T2],
                               [yL_T1, yR_T1], [yL_T2, yR_T2],
                               [sStepV01, sStepV12, sStepV_T], cOrdSm=smOrd)
        else:
            return stepF_1Step(dPar, x, [xL_T1, xR_T1], [yL_T1, yR_T1],
                               [sStepV01, sStepV_T], cOrdSm=smOrd)
    else:
        return 0.0

def doSinChange(x, dPar):
    if (GC.S_PERIOD_CHG in dPar and GC.S_AMPL_CHG in dPar):
        cPeriod, cAmplit = dPar[GC.S_PERIOD_CHG], dPar[GC.S_AMPL_CHG]
        return cAmplit*np.sin(x*2*np.pi/cPeriod)
    else:
        return 0.0

def doMixedQChange(x, dPar):
    cChg, qMix = 0.0, dPar[GC.S_QMIX]
    if (GC.S_QMIX in dPar and GC.S_STEP_T1 in dPar and
        GC.S_STEP_V01 in dPar and GC.S_STEP_V_T in dPar):
        cChg += (1 - qMix)*doStepChange(x, dPar)
        if (GC.S_PERIOD_CHG in dPar and GC.S_AMPL_CHG in dPar):
            cChg += qMix*doSinChange(x, dPar)
    else:
        if (GC.S_PERIOD_CHG in dPar and GC.S_AMPL_CHG in dPar):
            cChg += qMix*doSinChange(x, dPar)
    return cChg

# --- Functions (O_80__Interaction) -------------------------------------------
def doSiteChange(cO, sSpS, lSCpAs, doPyl=True):
    opDone = False
    assert sSpS in cO.dSpS
    cSpS = cO.dSpS[sSpS]
    if doPyl and cSpS.sSPTM == GC.S_NOT_PYL:
        for sCpAs in lSCpAs:
            if sCpAs in cSpS.lPyl:
                cSpS.sSPTM = GC.S_IS_PYL
                opDone = True
                break
    elif not doPyl and cSpS.sSPTM == GC.S_IS_PYL:
        for sCpAs in lSCpAs:
            if sCpAs in cSpS.lDPy:
                cSpS.sSPTM = GC.S_NOT_PYL
                opDone = True
                break
    return opDone

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

def createLSCp(inpDt, lOAll, sPylDPy=GC.S_DO_PYL):
    lSCp = []
    for cO in lOAll:
        for cSpS in cO.dITp['dInfSpS']:
            for sCp in cO.dITp['dInfSpS'][cSpS][sPylDPy]:
                if sCp not in lSCp:
                    lSCp.append(sCp)
    return sorted(lSCp)

# --- Functions (O_95__System) ------------------------------------------------
def createDCnc(inpFr):
    dCncIni = {}
    for sSMo, dIni in inpFr.dParCnc.items():
        cTp, dPar = dIni[GC.S_INI_CNC_DISTR]
        dCncIni[sSMo] = GF.drawFromDist(cTp, dPar)
    return dCncIni

def iniDictOut(inpFr, dCnc, t=0., tDlt=0.):
    dO = {'dN': {}, 'dH': {}, 'h': 0., 'tDlt': tDlt, 'dCncIni': {},
          'dCncChgInt': {}, 'dRes': {GC.S_TIME: [t]}}
    for s, cCnc in dCnc.items():
        dO['dRes'][s] = [cCnc]
        dO['dCncIni'][s] = cCnc
        dO['dCncChgInt'][s] = 0.
    for s, k in inpFr.dNCpObj.items():
        dO['dRes'][s] = [k]
        dO['dN'][s] = k
    return dO

def changeCncSMo(inpFr, dO, dCncSMo, t, cID=None):
    for sSMo in dCncSMo:
        assert sSMo in inpFr.dParCnc
        cD, cncChgSMo, cncChgExt = inpFr.dParCnc[sSMo], 0., 0.
        cncMn, cncMx = cD[GC.S_CNC_MIN], cD[GC.S_CNC_MAX]
        for s, nO in dO['dN'].items():
            ss = s.replace(GC.S_DASH, '')
            assert ss in inpFr.dSMoCncDepOnCp[sSMo]
            cncChgSMo += inpFr.dSMoCncDepOnCp[sSMo][ss]*nO
        # component-distribution-dependent (internal) conc. change
        nCpO = sum(dO['dN'].values())
        cncChgInt = cncChgSMo*dO['tDlt']/nCpO*inpFr.dOthInpV['cncChgScale']
        dO['dCncChgInt'][sSMo] += cncChgInt
        # externally forced conc. change
        cTp, dPar = cD[GC.S_CNC_CHG_MODE]
        if cTp == GC.S_CH_STEP:
            cncChgExt = doStepChange(t, dPar)
        elif cTp == GC.S_CH_SIN:
            cncChgExt = doSinChange(t, dPar)
        elif cTp == GC.S_CH_MXDQ:
            cncChgExt = doMixedQChange(t, dPar)
        dCncSMo[sSMo] = dO['dCncIni'][sSMo]
        dCncSMo[sSMo] += dO['dCncChgInt'][sSMo] + cncChgExt
        dCncSMo[sSMo] = GF.implMinMax(dCncSMo[sSMo], cncMn, cncMx)

def incorpEnzyme(dICp, dO, lSPyl, lSDPy, sRct, sRctCl, sSpS):
    x, sPylDPy = 0., GC.S_DO_PYL
    if sRctCl in lSPyl:
        sPylDPy = GC.S_DO_PYL
    elif sRctCl in lSDPy:
        sPylDPy = GC.S_DO_DPY
    for sCpAse in dICp[sPylDPy][sSpS]:
        x += dO['dN'][sCpAse]
    dO['dH'][sRct] *= x

def updateDictH(dICp, inpFr, dO, dCncSMo):
    sSMoN, p = GC.ID_NO3_1M, GC.P_DUMMY
    lSPyl, lSDPy = inpFr.dClRct[GC.S_DO_PYL], inpFr.dClRct[GC.S_DO_DPY]
    # update the reaction rate constants according to the current [NO3-]
    for sRct, wtRct in inpFr.dRct.items():
        # NO3- dependency of incidences of each component
        sRctType, sRctClass, _ = inpFr.dTpRct[sRct]
        assert (len(GF.splitStr(sRctClass)) >= 2 and sRctClass in
                inpFr.dCpDepOnSMoCnc[sSMoN])
        b = sRctClass in lSPyl + lSDPy
        sSpS = GF.splitStr(sRctClass)[1]
        dParPSig = inpFr.dCpDepOnSMoCnc[sSMoN][sRctClass]
        p = GF.calcPSigmoidal(dCncSMo[sSMoN], dParPSig)
        # recalculate dH, which contains the h_i (i = 1,... len(dH))
        dO['dH'][sRct] = wtRct*p
        for sCpLHS in GF.partStr(sRct)[0]:
            dO['dH'][sRct] *= dO['dN'][sCpLHS]
        if b:   # check if reaction is (de)phosphorylation
            incorpEnzyme(dICp, dO, lSPyl, lSDPy, sRct, sRctClass, sSpS)
        if (sRctType in GC.L_S_RCT_2ORD or b):
            dO['dH'][sRct] /= inpFr.dOthInpV['VolC']
    # (?) update the reaction rate constants according to the current [H2PO4-]

def reCalcReactHazards(dICp, inpFr, dO, dCncSMo):
    updateDictH(dICp, inpFr, dO, dCncSMo)
    # h, the sum of the h_i, is the overall reaction hazard
    dO['h'] = sum(dO['dH'].values())
    # sort dH in ascending order for numerical stability
    dO['dH'] = {cK: cV/dO['h'] for cK, cV in
                sorted(dO['dH'].items(), key=itemgetter(1))}

def eventReactionSys(dO):
    # get the string consisting of the LHS and RHS of the reaction
    sRct = GF.getSRct(dO['dH'])
    # update the numbers of component objects in dO['dN']
    llSCmp = GF.partStr(sRct)
    assert len(llSCmp) >= 2
    for k, lSCmp in enumerate(llSCmp):
        for sCmp in lSCmp:
            assert sCmp in dO['dN']
            if k == 0:              # left-hand side of the reaction equation
                dO['dN'][sCmp] -= 1
            elif k == 1:            # right-hand side of the reaction equation
                dO['dN'][sCmp] += 1

def nextEvent(dO, T, cTS):
    if dO['h'] > 0:    # otherwise the while-loop ends, see the other case
        # draw the time to the next event from exponential(lambd = 1./h)
        dO['tDlt'] = GF.drawFromDist('exponential', dPar={'h': dO['h']})
        # adapt the event reactions to considered system
        eventReactionSys(dO)
    else:
        # if no reaction is possible, then h becomes 0, therefore stop
        print('The combined reaction hazard is 0 - no reaction possible')
        dO['tDlt'] = T - dO['dRes'][GC.S_TIME][cTS]
    return dO['tDlt']

def updateDictOut(dO, dCnc, t):
    dO['dRes'][GC.S_TIME].append(t)
    for s, cCnc in dCnc.items():
        dO['dRes'][s].append(cCnc)
    for s, nO in dO['dN'].items():
        dO['dRes'][s].append(nO)

def evolveGillespie(dITp, dICp, inpFr, dCncSMo):
    # initialisation
    t, T, tDelta, cTSt = dITp['tStart'], dITp['tMax'], 0, 0
    dO = iniDictOut(inpFr, dCncSMo, t, tDelta)
    reCalcReactHazards(dICp, inpFr, dO, dCncSMo)
    while t < T and cTSt < dITp['maxTS']:
        cTSt += 1
        if cTSt >= dITp['minDispTS'] and cTSt%dITp['modDispTS'] == 0:
            print('Reached time step', cTSt, 'at time', round(t, GC.R04))
        # do next event and update time with tToNext
        t += nextEvent(dO, T, cTSt)
        # change the concentrations of the small molecules
        changeCncSMo(inpFr, dO, dCncSMo, t)
        # adapt the re-calc reaction hazards function to current system
        reCalcReactHazards(dICp, inpFr, dO, dCncSMo)
        # update the data storage matrix
        updateDictOut(dO, dCncSMo, t)
    return dO['dRes'], dO['dN']

def getPFResEvo(dITp, sPRs, sFRs):
    sD = dITp['sD_Obj']
    pFRes = getPF([sPRs, sD], sFRs, sFExt=GC.S_EXT_CSV)
    if os.path.isfile(pFRes):
        return GF.readCSV(pFRes, iCol=0)
    return None

def getDPFPltEvo(dITp, sPPlt=None, tKey=GC.S_USC, cRp=0, dMS=None):
    dP, sD = {}, dITp['sD_Obj']
    if sPPlt is None:
        sPPlt = dITp['sPPlt']
    if cRp > 0:
        sD = os.path.join(sD, GC.S_REP + str(cRp))
    if dMS is None:
        sF = GC.S_USC.join([str(cEl) for cEl in tKey if cEl is not None])
        if cRp > 0:
            sF += GC.S_USC*2 + GC.S_REP + str(cRp)
        pF = getPF([sPPlt, sD], sF, sFExt=GC.S_EXT_PDF)
        dP[pF] = dMS
    else:
        for sMS, dCp in dMS.items():
            sF = str(tKey[0]) + GC.S_USC + sMS
            if tKey[1] is not None:
                sF +=  GC.S_USC + str(tKey[1])
            if cRp > 0:
                sF += GC.S_USC*2 + GC.S_REP + str(cRp)
            pF = getPF([sPPlt, sD], sF, sFExt=GC.S_EXT_PDF)
            dP[pF] = (sMS, dCp)
    return dP

# --- Functions (O_95__System / O_99__Simulation) -----------------------------
def getDfr4Plot(dIPlt, dRes):
    dfrRes, dfrSpr, pltSpr, isSgl = None, None, GC.S_SGL, False
    if 'plotSpread' in dIPlt:
        pltSpr = dIPlt['plotSpread']
    if GC.S_SGL in dRes:
        dfrRes = dRes[GC.S_SGL]
        isSgl = True
    elif GC.S_MEAN in dRes:
        dfrRes = dRes[GC.S_MEAN]
        if GC.S_STDDEV in dRes and pltSpr == GC.S_STDDEV:
            dfrSpr = dRes[GC.S_STDDEV]
        elif GC.S_SEM in dRes and pltSpr == GC.S_SEM:
            dfrSpr = dRes[GC.S_SEM]
    return dfrRes, dfrSpr, isSgl

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

def preProcMS_Sgl(pdDfr, sLX, lSLY, tKDCp, lSCp):
    d4Sel, d4Leg, mdDfr = {}, {}, GF.iniPdDfr()
    sOp, dCp = tKDCp
    prepDict4Sel(d4Sel, d4Leg, lSLY, dCp)
    mdDfr.loc[:, sLX] = pdDfr.loc[:, sLX]
    for sK in d4Sel:
        if sK in lSCp:
            if sOp == GC.S_MEAN:
                mdDfr.loc[:, sK] = pdDfr.loc[:, d4Sel[sK]].T.mean()
            elif sOp == GC.S_SUM:
                mdDfr.loc[:, sK] = pdDfr.loc[:, d4Sel[sK]].T.sum()
        else:
            mdDfr.loc[:, sK] = pdDfr.loc[:, sK]
    return {GC.S_CENT: mdDfr}, d4Leg

# --- Functions (O_99__Simulation) --------------------------------------------
def calcStatsDfr(dDfrI, nRp=0):
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

def reduceData(dITp, cSys, cRp=0, sCTime=GC.S_TIME):
    halfStep = dITp['tMax']/(2*dITp['nTSAllRep'])
    lTRed = [k*halfStep for k in range(1, 2*dITp['nTSAllRep'], 2)]
    assert sCTime in cSys.dfrResEvo.columns
    lDfr = [cSys.dfrResEvo[(cSys.dfrResEvo[sCTime] >= lTRed[k - 1]) &
                           (cSys.dfrResEvo[sCTime] < lTRed[k + 1])]
            for k in range(1, len(lTRed) - 1)]
    lDfr = ([cSys.dfrResEvo[cSys.dfrResEvo[sCTime] < lTRed[1]]] + lDfr +
            [cSys.dfrResEvo[cSys.dfrResEvo[sCTime] >= lTRed[-2]]])
    lDfr = [cDfr.reset_index(drop=True) for cDfr in lDfr]
    lSCAv = [sC for sC in cSys.dfrResEvo.columns if sC != sCTime]
    dL = {sCTime: lTRed}
    dL.update({sC: [np.mean(cDfr[sC]) for cDfr in lDfr] for sC in lSCAv})
    dfrRed = GF.iniPdDfr(dL)
    savePdDfr(dITp, dfrRed, [cSys.dITp['sD_Obj']], cSys.sFRed, overWr=True)
    return dfrRed

def updateDictDfr(cDfr, dDfrI, cCt=0, lSCDisr=[GC.S_TIME]):
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
    # add the time column
    for sK in [GC.S_MEAN, GC.S_M2]:
        if GC.S_TIME not in dDfrI[sK].columns:
            dDfrI[sK] = GF.iniPdDfr(cDfr[GC.S_TIME]).join(dDfrI[sK])

def calcRunMeanM2Dfr(dITp, cSys, dDfrI, cCt=0, lSCDisr=[GC.S_TIME]):
    # reduce the data to the given number of lines
    dfrRed = reduceData(dITp, cSys, cRp=cCt)
    # update the DataFrames dictionary
    updateDictDfr(dfrRed, dDfrI, cCt=cCt, lSCDisr=lSCDisr)

def getSumRedDfr(dITp):
    dDfrI, nRp = {}, dITp['nReps']
    for cRp in range(1, nRp + 1):
        sF = GC.S_RED_SYS + GC.S_USC + GC.S_REP + str(cRp)
        cDfr = loadPdDfr(dITp, [GC.S_DIR_SYS], sF)
        updateDictDfr(cDfr, dDfrI, cCt=cRp)
    calcStatsDfr(dDfrI, nRp=nRp)

def preProcMS_Sprd(pdDfr, sLX, lSLY, tKDCp, lSCp):
    d4Sel, d4Leg, mdDfr, sumDfr = {}, {}, GF.iniPdDfr(), GF.iniPdDfr()
    sOp, dCp = tKDCp
    prepDict4Sel(d4Sel, d4Leg, lSLY, dCp)
    mdDfr.loc[:, sLX] = pdDfr.loc[:, sLX]
    sumDfr.loc[:, sLX] = pdDfr.loc[:, sLX]
    for sK in d4Sel:
        if sK in lSCp:
            sumDfr.loc[:, sK] = pdDfr.loc[:, d4Sel[sK]].T.sum()
            if sOp == GC.S_MEAN:
                mdDfr.loc[:, sK] = pdDfr.loc[:, d4Sel[sK]].T.mean()
            elif sOp == GC.S_SUM:
                mdDfr.loc[:, sK] = sumDfr.loc[:, sK]
        else:
            mdDfr.loc[:, sK] = pdDfr.loc[:, sK]
            sumDfr.loc[:, sK] = pdDfr.loc[:, sK]
    print('TEMP - mdDfr:\n', mdDfr)
    print('TEMP - sumDfr:\n', sumDfr)
    assert False
    return {GC.S_CENT: mdDfr, GC.S_SPREAD: sumDfr}, d4Leg

###############################################################################
