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
def loadPdDfr(dITp, lD=[], sF=None, sP=None, iCol=None, sFExt=GC.S_EXT_CSV):
    if sP is None:
        sP = GF.getPF([dITp['sPRes']] + lD, sF, sFExt=sFExt)
    if os.path.isfile(sP):
        return GF.readCSV(sP, sepD=dITp['cSep'], iCol=iCol)
    return GF.iniPdDfr()

def savePdDfr(dITp, pdDfr, lD, sF, overWr=True, sFExt=GC.S_EXT_CSV):
    sP = GF.getPF([dITp['sPRes']] + lD, sF, sFExt=sFExt)
    if not os.path.isfile(sP) or overWr:
        pdDfr.to_csv(sP, sep=dITp['cSep'])
    return sP

def saveAsPdDfr(dITp, dRes, lD, sF, overWr=True, sFExt=GC.S_EXT_CSV):
    sP = GF.getPF([dITp['sPRes']] + lD, sF, sFExt=sFExt)
    if not os.path.isfile(sP) or overWr:
        GF.iniPdDfr(dRes).to_csv(sP, sep=dITp['cSep'])
    return sP

def saveSerRep(dITp, cDfr, serRp, lD, sFA='', sFExt=GC.S_EXT_CSV):
    sP = GF.getPF([dITp['sPRes']] + lD, sF=dITp['sFNRp'] + sFA, sFExt=sFExt)
    if not os.path.isfile(sP) or dITp['overWrCSV']:
        lSer = [cDfr.loc[:, GC.S_TIME].round(GC.R08), serRp]
        GF.saveConcatDfr(lSer, pF=sP, sepD=dITp['cSep'])

def saveDictDfr(dITp, dDfr, lK=None, sFEnd = '', overWr=True,
                sFExt=GC.S_EXT_CSV):
    for cK, cDfr in dDfr.items():
        if lK is None or cK in lK:
            sF = GC.S_USC.join([dITp['sFObj'], str(cK), sFEnd])
            savePdDfr(dITp, cDfr, lD=[dITp['sDObj'], str(cK)], sF=sF,
                      overWr=overWr, sFExt=sFExt)

# --- Functions (O_00__Base) --------------------------------------------------
def getDITp(dIG, iTp, lITpU):
    dITp = {}
    if len(lITpU) > 0:
        dITp = copy.deepcopy(dIG[lITpU[0]])     # content of lITpU[0] input
        for iTpU in lITpU[1:]:
            GF.updateDITp(dITp, dIG[iTpU])      # updated with iTpU input
    GF.updateDITp(dITp, dIG[iTp])               # updated with iTp input
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

# --- Functions (O_70__Interaction) -------------------------------------------
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

# --- Functions (O_75__Component) ---------------------------------------------
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

# --- Functions (O_95__System / O_99__Simulation) -----------------------------
def prepDictIsCpStr(d4Sel, d4Leg, lCp, sLg, sHdC):
    for sCp in lCp:
        if sHdC.startswith(sCp):
            GF.addToDictL(d4Sel, sLg, sHdC, lUnique=True)
            if d4Leg is not None:
                GF.addToDictL(d4Leg, sLg, GC.S_COM_BL.join(lCp), lUnique=True)
            break

def prepDictNoCpStr(d4Sel, d4Leg, sHdC):
    if sHdC not in d4Sel:
        GF.addToDictL(d4Sel, sHdC, sHdC, lUnique=True)
        if d4Leg is not None:
            GF.addToDictL(d4Leg, sHdC, sHdC, lUnique=True)

def prepDict4Sel(pltDt, d4Sel, lSLY=[]):
    d4Leg = {}
    for sLg, lCp in pltDt.dCHdGr.items():
        for sHdC in lSLY:
            if (len(sHdC) == GC.LEN_S_CP and
                set(sHdC[GC.I_S_CP_SEP1:]) <= GC.SET_0_1_DASH):
                # this column header is a component string
                prepDictIsCpStr(d4Sel, d4Leg, lCp, sLg, sHdC)
            else:
                # this column header is NOT a component string
                prepDictNoCpStr(d4Sel, d4Leg, sHdC)
    # reorder d4Leg to match the order specified in dCHdGr
    return {sLg: d4Leg[sLg] for sLg in pltDt.dCHdGr}

def collapseColumns(pltDt, pdDfr, sLX, lSLY, sOp):
    d4Sel, mdDfr = {}, GF.iniPdDfr()
    d4Leg = prepDict4Sel(pltDt, d4Sel, lSLY=lSLY)
    mdDfr.loc[:, sLX] = pdDfr.loc[:, sLX]
    for sK in d4Sel:
        if sOp == GC.S_MEAN_GR:
            mdDfr.loc[:, sK] = pdDfr.loc[:, d4Sel[sK]].T.mean()
        elif sOp == GC.S_SUM_GR:
            mdDfr.loc[:, sK] = pdDfr.loc[:, d4Sel[sK]].T.sum(min_count=1)
        else:
            mdDfr.loc[:, sK] = pdDfr.loc[:, sK]
    # return {GC.S_CENT: mdDfr}, d4Leg
    return mdDfr, d4Leg

def getPPltF(pltDt, sPPlt, sDSub, sOp=None, cRp=0):
    sPSub, sFPlt = sDSub, pltDt.sPltTp
    if sOp is not None:
        sFPlt += GC.S_USC + sOp
    if pltDt.sPltNm is not None:
        sFPlt += GC.S_USC + pltDt.sPltNm
    if cRp > 0:
        sFPlt += GC.S_USC*2 + GC.S_REP + str(cRp)
        sPSub = os.path.join(sPSub, GC.S_REP + str(cRp))
    return GF.getPF([sPPlt, sPSub], sFPlt, sFExt=GC.S_EXT_PDF)

# --- Functions (O_99__Simulation) --------------------------------------------
def getDfrRdWt(lDfr, hT, lTRd, lSC=[], sCTime=GC.S_TIME):
    dRd, dCAv = {sCTime: lTRd}, {sC: [] for sC in lSC}
    for sC in lSC:
        for i, cDfr in enumerate(lDfr):
            arrWts = GF.getWeights(cDfr[sCTime], cCent=lTRd[i], halfRng=2*hT)
            if len(arrWts) > 0:
                dCAv[sC].append(np.average(cDfr[sC], weights=arrWts))
            else:
                dCAv[sC].append(np.nan)
    dRd.update(dCAv)
    return(GF.iniPdDfr(dRd))

def getDfrRdNoWt(lDfr, lTRd, lSC=[], sCTime=GC.S_TIME):
    dRd = {sCTime: lTRd}
    dRd.update({sC: [np.mean(cDfr[sC]) for cDfr in lDfr] for sC in lSC})
    return(GF.iniPdDfr(dRd))

def collapseTimes(dITp, cSys, hT, lTRd, sCTime=GC.S_TIME):
    assert len(lTRd) >= 2
    lD, dfrRE = [cSys.dITp['sDObj']], cSys.dfrResEvo
    serT, pFRed = dfrRE[sCTime], GF.getPF([dITp['sPRes']] + lD, cSys.sFRed)
    if not os.path.isfile(pFRed) or dITp['overWrCSV']:
        assert sCTime in dfrRE.columns
        lDfr = [dfrRE[(serT >= lTRd[k - 1]) & (serT < lTRd[k + 1])]
                for k in range(1, len(lTRd) - 1)]
        lDfr = ([dfrRE[serT < lTRd[1]]] + lDfr + [dfrRE[serT >= lTRd[-2]]])
        lDfr = [cDfr.reset_index(drop=True) for cDfr in lDfr]
        # list of column header strings where averages should be calculated
        lSCAv = [sC for sC in dfrRE.columns if sC != sCTime]
        if dITp['useWtMeans']:
            dfrRd = getDfrRdWt(lDfr, hT, lTRd, lSC=lSCAv, sCTime=sCTime)
        else:
            dfrRd = getDfrRdNoWt(lDfr, lTRd, lSC=lSCAv, sCTime=sCTime)
        savePdDfr(dITp, dfrRd, lD, cSys.sFRed, overWr=dITp['overWrCSV'])
    else:
        dfrRd = loadPdDfr(dITp, lD, cSys.sFRed, iCol=0)
    return dfrRd

def getCtVal(serRp, xTest, iR=0, modRp=False):
    cCt, isValid = serRp.at[iR], True
    if modRp:
        cCt, isValid = GF.checkValid(serRp, iR, xTest)
    return cCt, isValid

def updateElements(cDfr, dDfrSt, sR, lSC=[], cCt=0):
    for sC in lSC:
        cMn, cM2 = dDfrSt[GC.S_MEAN].at[sR, sC], dDfrSt[GC.S_M2].at[sR, sC]
        cMn, cM2 = GF.updateMeanM2(cMn, cM2, cDfr.at[sR, sC], cCt)
        dDfrSt[GC.S_MEAN].at[sR, sC], dDfrSt[GC.S_M2].at[sR, sC] = cMn, cM2

def addFirstColToDfrs(dDfr, serC1, lK=None, sKC1=GC.S_TIME):
    for cK, cDfr in dDfr.items():
        if lK is None or cK in lK:
            if sKC1 not in cDfr.columns:
                dDfr[cK] = GF.iniPdDfr(serC1).join(cDfr)

def updateDictDfr(cDfr, dDfrSt, serRp, modRp=False, lSCDisr=[GC.S_TIME]):
    lSCCalc = [sC for sC in cDfr.columns if sC not in lSCDisr]
    # initialise if full results DataFrame is still empty
    if dDfrSt is None or len(dDfrSt) == 0:
        for sK in GC.L_S_STATS_ALL:
            dDfrSt[sK] = GF.iniPdDfr(lSNmC=lSCCalc, lSNmR=cDfr.index, v=np.nan)
    # update the current value aggregate, and re-assign values to DataFrames
    if len(lSCCalc) > 0:
        for sR in cDfr.index:
            cCt, isVal = getCtVal(serRp, cDfr.at[sR, lSCCalc[0]], sR, modRp)
            if isVal:
                updateElements(cDfr, dDfrSt, sR, lSC=lSCCalc, cCt=cCt)
    # add the time column
    addFirstColToDfrs(dDfrSt, serC1=cDfr[GC.S_TIME])

def calcDfrRunStats(dITp, cSys, dDfrSt, dDfrRd, hT, lTRd, serRp, cRp=0):
    # reduce the data to the given number of lines
    dfrRd = collapseTimes(dITp, cSys, hT=hT, lTRd=lTRd)
    dDfrRd[cRp] = dfrRd
    # update the DataFrames dictionary
    updateDictDfr(dfrRd, dDfrSt, serRp=serRp, modRp=True)

def calcStatsSingleSet(dDfrSt, sR, sC, cCt=0):
    cMn, cM2 = dDfrSt[GC.S_MEAN].at[sR, sC], dDfrSt[GC.S_M2].at[sR, sC]
    cMn, cVar, cVarS = GF.finalRunMeanSD((cCt, cMn, cM2))
    cStdDevS, cSEM = np.nan, np.nan
    if np.isfinite(cVarS) and cVarS >= 0:
        cStdDevS = np.sqrt(cVarS)
    if np.isfinite(cStdDevS) and cCt > 0:
        cSEM = cStdDevS/np.sqrt(cCt)
    for i, sK in enumerate([GC.S_MEAN] + GC.L_S_STATS_DER):
        dDfrSt[sK].at[sR, sC] = [cMn, cVarS, cStdDevS, cSEM][i]

def calcDfrFinStats(dDfrSt, serRp, lSCDisr=[GC.S_TIME]):
    lSR = dDfrSt[GC.S_MEAN].index
    lSC = [sC for sC in dDfrSt[GC.S_MEAN].columns if sC not in lSCDisr]
    for sK in GC.L_S_STATS_DER:
        dDfrSt[sK] = GF.iniPdDfr(lSNmC=lSC, lSNmR=lSR, v=np.nan)
    for sR in lSR:
        for sC in lSC:
            calcStatsSingleSet(dDfrSt, sR, sC, cCt=serRp.at[sR])
    addFirstColToDfrs(dDfrSt, serC1=dDfrSt[GC.S_MEAN][GC.S_TIME],
                      lK=GC.L_S_STATS_DER)

def checkConsistencyDictDfrPlt(dDfr, lK):
    assert len(lK) in [1, 2]
    for cK in lK:
        assert cK in dDfr
    if len(lK) == 2:
        dfr1, dfr2 = dDfr[lK[0]], dDfr[lK[1]]
        assert list(dfr1.index) == list(dfr2.index)
        assert list(dfr1.columns) == list(dfr2.columns)

###############################################################################
