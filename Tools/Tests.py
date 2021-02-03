# -*- coding: utf-8 -*-
###############################################################################
# --- Tests.py ----------------------------------------------------------------
###############################################################################
import os
import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt
import pandas as pd

# Constants -------------------------------------------------------------------
S_EXT_CSV = 'csv'
S_EXT_PDF = 'pdf'

SEP_STD = ';'

S_USC = '_'

S_PLT_GRP_A = 'A__9_Main_Groups'
S_PLT_GRP_B = 'B__Complexes'
S_PLT_GRP_C = 'C__I_vs_J_vs_T'
S_PLT_GRP_D = 'D__LS-_vs_LK-'

S_TIME = 'Time'

S_SGL = 'Single'
S_MEAN = 'Mean'
S_STDDEV = 'StdDev'
S_SEM = 'SEM'
S_CENT = 'Central'
S_SPREAD = 'Spread'

nRep = 5
tMax = 10.

s_FMn = 'SimRes_Mean_02_SelCp_SumGrp'
s_FStdDev = 'SimRes_StdDev_02_SelCp_SumGrp'
s_FSEM = 'SimRes_SEM_02_SelCp_SumGrp'

s_A_FMn = s_FMn + S_USC + S_PLT_GRP_A
s_A_FStdDev = s_FStdDev + S_USC + S_PLT_GRP_A
s_A_FSEM = s_FSEM + S_USC + S_PLT_GRP_A

s_B_FMn = s_FMn + S_USC + S_PLT_GRP_B
s_B_FStdDev = s_FStdDev + S_USC + S_PLT_GRP_B
s_B_FSEM = s_FSEM + S_USC + S_PLT_GRP_B

s_C_FMn = s_FMn + S_USC + S_PLT_GRP_C
s_C_FStdDev = s_FStdDev + S_USC + S_PLT_GRP_C
s_C_FSEM = s_FSEM + S_USC + S_PLT_GRP_C

s_D_FMn = s_FMn + S_USC + S_PLT_GRP_D
s_D_FStdDev = s_FStdDev + S_USC + S_PLT_GRP_D
s_D_FSEM = s_FSEM + S_USC + S_PLT_GRP_D

dSF = {S_PLT_GRP_A: {S_MEAN: s_A_FMn, S_STDDEV: s_A_FStdDev, S_SEM: s_A_FSEM},
       S_PLT_GRP_B: {S_MEAN: s_B_FMn, S_STDDEV: s_B_FStdDev, S_SEM: s_B_FSEM},
       S_PLT_GRP_C: {S_MEAN: s_C_FMn, S_STDDEV: s_C_FStdDev, S_SEM: s_C_FSEM},
       S_PLT_GRP_D: {S_MEAN: s_D_FMn, S_STDDEV: s_D_FStdDev, S_SEM: s_D_FSEM}}

# --- file names, paths and directories ---------------------------------------
sPBase = os.path.join('..', '..', '..', '11_SysBio01_ABM01')
sPResData = os.path.join(sPBase, '40_ModelResults', '99_Sim')
sDResDataMn, sDResDataStdDev, sDResDataSEM = S_MEAN, S_STDDEV, S_SEM

# --- plot parameters: component numbers and molecule conc. plot --------------
plotGroup = S_PLT_GRP_D                 # S_PLT_GRP_A / S_PLT_GRP_B
                                        # S_PLT_GRP_C / S_PLT_GRP_D
plotSpread = S_STDDEV                      # S_SGL / S_STDDEV / S_SEM
alphaSpread = 0.95                      # 0.9 / 0.95 / 0.99

sFPlt = 'Test1' + S_USC + plotGroup + S_USC + plotSpread + '.' + S_EXT_PDF
sPPlt = os.path.join(sPBase, '50_ModelPlots')

sPlt_SSC = '01_SelCpConc'               # name of sel. comps and conc. plot
sPlt_SCp = '02_SelCp'                   # name of sel. comps plot
sPlt_SCn = '03_SelConc'                 # name of sel. conc. plot

title_CpCnc = None                      # title of plot
xLbl_CpCnc = S_TIME                     # x-label of plot
yLbl_CpCnc = 'Mol. conc. / Comp. incid.'    # y x-label of plot
tpMark_CpCnc = None                     # marker type of plot
szMark_CpCnc = 1                        # marker size of plot
ewMark_CpCnc = 1                        # marker edge width of plot
ecMark_CpCnc = (1., 0., 0.)             # marker edge colour of plot
fcMark_CpCnc = (1., 0.5, 0.)            # marker face colour of plot
styLn_CpCnc = 'solid'                   # line style of plot
wdthLn_CpCnc = 1                        # line width of plot
colLn_CpCnc = (0.9, 0.3, 0.8)           # line colour of plot
pltAxXY_CpCnc = (True, True)            # plot x- and/or y-axis
alpCol = 0.3
lColA = [(0., 0., 0.9), (0.9, 0.1, 0.), (0.8, 0.8, 0.05),
         (0.4, 0.2, 0.9), (0.9, 0., 0.8), (0.8, 0.3, 0.8),
         (0.2, 0.9, 0.4), (0.3, 1., 0.8), (0., 0.9, 0.8)]
lColB = [(0.2, 0., 0.8), (0.9, 0., 0.), (0.8, 0.0, 0.7),
         (0., 0.8, 0.), (0.3, 0.5, 0.), (0.8, 0.6, 0.)]
lColC = [(0., 0., 0.8), (0.9, 0., 0.), (0.8, 0.4, 0.)]
lColD = [(0., 0., 0.8), (0.9, 0., 0.), (0.8, 0.4, 0.)]
dColLn = {S_PLT_GRP_A: lColA, S_PLT_GRP_B: lColB, S_PLT_GRP_C: lColC,
          S_PLT_GRP_D: lColD}
# dColLn = {'A__9_Main_Groups': lColA,
#           'B__Complexes': lColB,
#           'C__I_vs_J_vs_T': lColC,
#           'D__LS-_vs_LK-': lColD}

# --- type dictionary ---------------------------------------------------------
dIType = {'nRep': nRep,
          'tMax': tMax,
          'dSF': dSF,
          'sPResData': sPResData,
          'sDResDataMn': sDResDataMn,
          'sDResDataStdDev': sDResDataStdDev,
          'sDResDataSEM': sDResDataSEM}

# --- plot dictionary ---------------------------------------------------------
dIPlot = {'plotGroup': plotGroup,
          'plotSpread': plotSpread,
          'alphaSpread': alphaSpread,
          'sFPlt': sFPlt,
          'sPPlt': sPPlt,
          'sPlt_SSC': sPlt_SSC,
          'sPlt_SCp': sPlt_SCp,
          'sPlt_SCn': sPlt_SCn,
          'title': title_CpCnc,
          'xLbl': xLbl_CpCnc,
          'yLbl': yLbl_CpCnc,
          'styLn': styLn_CpCnc,
          'wdthLn': wdthLn_CpCnc,
          'colLn': colLn_CpCnc,
          'pltAxXY': pltAxXY_CpCnc,
          'alpCol': alpCol,
          'dColLn': dColLn}

# Functions -------------------------------------------------------------------
def makeDirs(pDTarget):
    if not os.path.isdir(pDTarget):
        os.makedirs(pDTarget)

def joinToPath(lD4P=[], sF='Dummy.txt'):
    if len(lD4P) > 0:
        pD = ''
        for cD in lD4P:
            pD = os.path.join(pD, cD)
        makeDirs(pD)
        return os.path.join(pD, sF)
    else:
        return sF

def getPF(lD4P, sF, sFExt=S_EXT_CSV):
    return joinToPath(lD4P, sF + '.' + sFExt)

def readCSV(pF, sepD=SEP_STD, iCol=None, dDtype=None):
    return pd.read_csv(pF, sep=sepD, index_col=iCol, dtype=dDtype)

def iniPdDfr(data=None, lSNmC=[], lSNmR=[], shape=(0, 0)):
    assert len(shape) == 2
    nR, nC = shape
    if len(lSNmC) == 0:
        if len(lSNmR) == 0:
            if data is None:
                return pd.DataFrame(np.zeros(shape))
            else:
                return pd.DataFrame(data)
        else:
            if data is None:
                return pd.DataFrame(np.zeros((len(lSNmR), nC)), index=lSNmR)
            else:
                return pd.DataFrame(data, index=lSNmR)
    else:
        if len(lSNmR) == 0:
            if data is None:
                return pd.DataFrame(np.zeros((nR, len(lSNmC))),
                                    columns=lSNmC)
            else:
                return pd.DataFrame(data, columns=lSNmC)
        else:   # ignore nR
            if data is None:
                return pd.DataFrame(np.zeros((len(lSNmR), len(lSNmC))),
                                    index=lSNmR, columns=lSNmC)
            else:
                return pd.DataFrame(data, index=lSNmR, columns=lSNmC)

def clipVal(x, xMin=None, xMax=None):
    if xMin is not None:
        if xMax is not None:
            return min(max(x, xMin), xMax)
        else:
            return max(x, xMin)
    else:
        if xMax is not None:
            return min(x, xMax)
        else:
            return x

def getCI(cData=None, cDF=1, cMn=0., cSEM=1., cAlpha=0.95, mnV=None, mxV=None):
    cAlpha = clipVal(cAlpha, xMin=0, xMax=1)
    if cData is None:
        cCI = st.t.interval(alpha=cAlpha, df=cDF, loc=cMn, scale=cSEM)
    else:
        cCI = st.t.interval(alpha=cAlpha, df=len(cData)-1,
                           loc=np.mean(cData), scale=st.sem(cData))
    return tuple(clipVal(cBd, xMin=mnV, xMax=mxV) for cBd in cCI)

def getArrCI(cDF=1, arrC=np.zeros((1, 1)), arrS=np.ones((1, 1)), cAlpha=0.95,
             mnV=None, mxV=None):
    assert arrC.ndim == 1 and arrS.ndim == 1
    assert arrC.shape[0] == arrS.shape[0]
    arrLB, arrUB = np.zeros(arrC.shape[0]), np.zeros(arrC.shape[0])
    for i, x in enumerate(arrC):
        arrLB[i], arrUB[i] = getCI(cDF=cDF, cMn=x, cSEM=arrS[i], cAlpha=cAlpha,
                                   mnV=mnV, mxV=mxV)
    return (arrLB, arrUB)

def pltXYAxisS(maxX, maxY, pltAxXY=(True, True), cLwd=0.75, cCol='k'):
    if pltAxXY[0] and maxX is not None:
        plt.plot([0, maxX], [0, 0], lw=cLwd, color=cCol)
    if pltAxXY[1] and maxY is not None:
        plt.plot([0, 0], [0, maxY], lw=cLwd, color=cCol)

def pltXYAxis(cDfr, nmCX=None, nmCY=None, pltAxXY=(True, True)):
    minDfr, maxDfr = 0, 1
    if cDfr.ndim == 1:
        minDfr, maxDfr = min(0, cDfr.min()), cDfr.max()
    elif cDfr.ndim > 1:
        minDfr, maxDfr = min(0, cDfr.stack().min()), cDfr.stack().max()
    if pltAxXY[0]:
        if nmCX is not None:
            minX, maxX = min(0, min(cDfr.loc[:, nmCX])), max(cDfr.loc[:, nmCX])
            plt.plot([minX, maxX], [0, 0], lw=0.75, color='k')
        else:
            plt.plot([0, cDfr.shape[0] - 1], [0, 0], lw=0.75, color='k')
    if pltAxXY[1]:
        if nmCY is not None:
            minY, maxY = min(0, min(cDfr.loc[:, nmCY])), max(cDfr.loc[:, nmCY])
            plt.plot([0, 0], [minY, maxY], lw=0.75, color='k')
        else:
            plt.plot([0, 0], [minDfr, maxDfr], lw=0.75, color='k')

def decorateSavePlotS(pF, maxX=None, maxY=None, sTtl=None, xLbl=None,
                      yLbl=None, xLim=None, yLim=None, pltAxXY=(False, False)):
    assert len(pltAxXY) >= 2
    pltXYAxisS(maxX=maxX, maxY=maxY, pltAxXY=pltAxXY)
    if sTtl is not None:
        plt.title(sTtl)
    if xLbl is not None:
        plt.xlabel(xLbl)
    if yLbl is not None:
        plt.ylabel(yLbl)
    if xLim is not None:
        assert len(xLim) == 2
        plt.xlim(xLim)
    if yLim is not None:
        assert len(yLim) == 2
        plt.ylim(yLim)
    plt.savefig(pF)

def checkConsistency2Dfr(dDfr, lK):
    assert len(lK) == 2
    for cK in lK:
        assert cK in dDfr
    dfr1, dfr2 = dDfr[lK[0]], dDfr[lK[1]]
    assert list(dfr1.index) == list(dfr2.index)
    assert list(dfr1.columns) == list(dfr2.columns)

def plotEvoSpread(dITp, dIPlt, dDfrRes, lSY, nRp):
    cFig = plt.figure()
    dfrCent, dfrSpread = dDfrRes[S_CENT], dDfrRes[S_SPREAD]
    assert S_TIME in dfrCent.columns and S_TIME in dfrSpread.columns
    serX, maxY = dfrSpread.loc[:, S_TIME], dfrCent.loc[:, lSY].stack().max()
    for i, sC in enumerate(lSY):
        tArrB = getArrCI(cDF=nRp-1, arrC=dfrCent.loc[:, sC],
                         arrS=dfrSpread.loc[:, sC],
                         cAlpha=dIPlt['alphaSpread'], mnV=0)
        maxY = max([maxY] + list(tArrB[1]))
        cCol = dIPlt['dColLn'][dIPlt['plotGroup']][i] + (dIPlt['alpCol'],)
        plt.vlines(serX, tArrB[0], tArrB[1], ls=dIPlt['styLn'],
                   lw=dIPlt['wdthLn'], color=cCol, label=sC)
    plt.legend(loc='best')
    pPltF = getPF([dIPlt['sPPlt']], dIPlt['sFPlt'], sFExt=S_EXT_PDF)
    decorateSavePlotS(pPltF, maxX=dITp['tMax'], maxY=maxY, sTtl=dIPlt['title'],
                      xLbl=dIPlt['xLbl'], yLbl=dIPlt['yLbl'],
                      pltAxXY=dIPlt['pltAxXY'])
    plt.close()

# Main ------------------------------------------------------------------------
# define sample data
# lData = [12, 12, 13, 13, 15, 16, 17, 22, 23, 25, 26, 27, 28, 28, 29]
# cDF = len(lData) - 1
# cMean = sum(lData)/len(lData)
# cSEM = st.sem(lData)
# print('SEM:', cSEM)
# print('95% confidence interval (direct calc.):\t', getCI(cData=lData))
# print('95% confidence interval (indirect calc.):\t', getCI(cDF=cDF, cMn=cMean,
#                                                            cSEM=cSEM))
# arrCent, arrSpread = 10*np.random.randn(nRep), abs(np.random.randn(nRep))
# print('arrCent:\n', arrCent)
# print('arrSpread:\n', arrSpread)
# arrCI = getArrCI(cDF=nRep - 1, arrC=arrCent, arrS=arrSpread)
# print('Array CI:' + '\n' + str(arrCI[0]) + '\n' + str(arrCI[1]))
# lSC = [S_TIME] + list('ABCD')
# print(pd.DataFrame(np.vstack((np.array(arrCI[0]), np.array(arrCI[1]))),
#                    columns=lSC))
# print(pd.DataFrame(np.vstack((np.array(arrCI[0]), np.array(arrCI[1]))).T,
#                    columns=lSC[:2]))
# print('Single CIs:')
# for i in range(nRep):
#     print(str(i) + ':\t', getCI(cDF=nRep - 1, cMn=arrCent[i],
#                                 cSEM=arrSpread[i]))

pFMn = getPF([dIType['sPResData'], dIType['sDResDataMn']],
             dIType['dSF'][dIPlot['plotGroup']][S_MEAN])
pFStdDev = getPF([dIType['sPResData'], dIType['sDResDataStdDev']],
             dIType['dSF'][dIPlot['plotGroup']][S_STDDEV])
pFSEM = getPF([dIType['sPResData'], dIType['sDResDataSEM']],
             dIType['dSF'][dIPlot['plotGroup']][S_SEM])

pFCent, pFSpread = pFMn, pFMn
if dIPlot['plotSpread'] == S_STDDEV:
    pFSpread = pFStdDev
elif dIPlot['plotSpread'] == S_SEM:
    pFSpread = pFSEM

dDfrResult = {S_CENT: readCSV(pFCent, iCol=0),
              S_SPREAD: readCSV(pFSpread, iCol=0)}
checkConsistency2Dfr(dDfrResult, lK=[S_CENT, S_SPREAD])
lSCY = [sC for sC in dDfrResult[S_CENT].columns if sC not in [S_TIME]]
if nRep > 1:
    plotEvoSpread(dIType, dIPlot, dDfrResult, lSY=lSCY, nRp=nRep)

print('*'*24, 'DONE', '*'*24)

###############################################################################
