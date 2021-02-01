# -*- coding: utf-8 -*-
###############################################################################
# --- Tests.py ----------------------------------------------------------------
###############################################################################
import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt
import pandas as pd

# Constants -------------------------------------------------------------------
S_TIME = 'Time'
S_SGL = 'Single'
S_STDDEV = 'StdDev'
S_SEM = 'SEM'
S_CENT = 'Central'
S_SPREAD = 'Spread'
nRep = 5

plotSpread = S_STDDEV                # S_SGL / S_STDDEV / S_SEM
alphaSpread = 0.95                      # 0.9 / 0.95 / 0.99

sPlt_SSC = '01_SelCpConc'               # name of sel. comps and conc. plot
sPlt_SCp = '02_SelCp'                   # name of sel. comps plot
sPlt_SCn = '03_SelConc'                 # name of sel. conc. plot

title_CpCnc = None                      # title of plot
xLbl_CpCnc = S_TIME                  # x-label of plot
tpMark_CpCnc = None                     # marker type of plot
szMark_CpCnc = 1                        # marker size of plot
ewMark_CpCnc = 1                        # marker edge width of plot
ecMark_CpCnc = (1., 0., 0.)             # marker edge colour of plot
fcMark_CpCnc = (1., 0.5, 0.)            # marker face colour of plot
styLn_CpCnc = 'solid'                   # line style of plot
wdthLn_CpCnc = 1                        # line width of plot
colLn_CpCnc = None                      # line colour of plot
pltAxXY_CpCnc = (True, True)            # plot x- and/or y-axis

dIPlot = {'plotSpread': plotSpread,
          'alphaSpread': alphaSpread,
          'title': title_CpCnc,
          'xLbl': xLbl_CpCnc,
          'tpMark': tpMark_CpCnc,
          'szMark': szMark_CpCnc,
          'ewMark': ewMark_CpCnc,
          'ecMark': ecMark_CpCnc,
          'fcMark': fcMark_CpCnc,
          'styLn': styLn_CpCnc,
          'wdthLn': wdthLn_CpCnc,
          'colLn': colLn_CpCnc,
          'pltAxXY': pltAxXY_CpCnc}

# Functions -------------------------------------------------------------------
def getCI(cData=None, cDF=1, cMn=0., cSEM=1., cAlpha=0.95):
    cAlpha = min(max(0, cAlpha), 1)
    if cData is None:
        return st.t.interval(alpha=cAlpha, df=cDF, loc=cMn, scale=cSEM)
    else:
        return st.t.interval(alpha=cAlpha, df=len(cData)-1, loc=np.mean(cData),
                             scale=st.sem(cData)) 

def getArrCI(cDF=1, arrC=np.zeros((1, 1)), arrS=np.ones((1, 1)), cAlpha=0.95):
    assert arrC.ndim == 1 and arrS.ndim == 1
    assert arrC.shape[0] == arrS.shape[0]
    arrLB, arrUB = np.zeros(arrC.shape[0]), np.zeros(arrC.shape[0])
    for i, x in enumerate(arrC):
        arrLB[i], arrUB[i] = getCI(cDF=cDF, cMn=x, cSEM=arrS[i], cAlpha=cAlpha)
    return (arrLB, arrUB)

def plotEvoSpread(dIPlt, dDfrRes, nRp):
    cFig = plt.figure()
    assert S_CENT in dDfrRes and S_SPREAD in dDfrRes
    dfrCent, dfrSpread = dDfrRes[S_CENT], dDfrRes[S_SPREAD]
    assert list(dfrCent.index) == list(dfrSpread.index)
    assert list(dfrCent.columns) == list(dfrSpread.columns)
    if nRp > 1:
        for sC in dfrCent.columns:
            tArrB = getArrCI(cDF=nRp-1, arrC=dfrCent.loc[:, sC],
                             arrS=dfrSpread.loc[:, sC],
                             cAlpha=dIPlt['alphaSpread'])
            plt.plot(dfrR.loc[:, sHdCX], dfrR.loc[:, sHdCY],
                      marker=dIPlt['tpMark'], ms=dIPlt['szMark'],
                      mew=dIPlt['ewMark'], mec=dIPlt['ecMark'], mfc=dIPlt['fcMark'],
                      ls=dIPlt['styLn'], lw=dIPlt['wdthLn'], color=dIPlt['colLn'],
                      label=lSY[0])
    plt.legend(loc='best')
    decorateSavePlot(pF, dfrR, sTtl=dIPlt['title'], xLbl=dIPlt['xLbl'],
                      yLbl=sLblY, nmCX=sHdCX, pltAxXY=dIPlt['pltAxXY'])
    plt.close()

# Main ------------------------------------------------------------------------
#define sample data
lData = [12, 12, 13, 13, 15, 16, 17, 22, 23, 25, 26, 27, 28, 28, 29]
cDF = len(lData) - 1
cMean = sum(lData)/len(lData)
cSEM = st.sem(lData)
print('SEM:', cSEM)
print('95% confidence interval (direct calc.):\t', getCI(cData=lData))
print('95% confidence interval (indirect calc.):\t', getCI(cDF=cDF, cMn=cMean,
                                                           cSEM=cSEM))
arrCent, arrSpread = 10*np.random.randn(nRep), abs(np.random.randn(nRep))
print('arrCent:\n', arrCent)
print('arrSpread:\n', arrSpread)
arrCI = getArrCI(cDF=nRep - 1, arrC=arrCent, arrS=arrSpread)
print('Array CI:' + '\n' + str(arrCI[0]) + '\n' + str(arrCI[1]))
print('Single CIs:')
for i in range(nRep):
    print(str(i) + ':\t', getCI(cDF=nRep - 1, cMn=arrCent[i], cSEM=arrSpread[i]))
    
print('*'*24, 'DONE', '*'*24)

###############################################################################
