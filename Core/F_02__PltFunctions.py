# -*- coding: utf-8 -*-
###############################################################################
# --- F_02__PltFunctions.py ---------------------------------------------------
###############################################################################
import matplotlib.pyplot as plt

import Core.C_00__GenConstants as GC
import Core.F_00__GenFunctions as GF
import Core.F_01__SpcFunctions as SF

# --- Functions (general) -----------------------------------------------------
def pltXYAxisS(maxX, maxY, pltAxXY=(True, True), cLwd=0.75, cCol='k'):
    assert len(pltAxXY) >= 2
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
    assert len(pltAxXY) >= 2
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

def decorateSaveIt(pF, sTtl=None, xLbl=None, yLbl=None, xLim=None, yLim=None):
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

def decorateSavePlotS(pF, maxX=None, maxY=None, sTtl=None, xLbl=None,
                      yLbl=None, xLim=None, yLim=None, pltAxXY=(False, False)):
    pltXYAxisS(maxX=maxX, maxY=maxY, pltAxXY=pltAxXY)
    decorateSaveIt(pF, sTtl=sTtl, xLbl=xLbl, yLbl=yLbl, xLim=xLim, yLim=yLim)

def decorateSavePlot(pF, pdDfr, sTtl=None, xLbl=None, yLbl=None, xLim=None,
                     yLim=None, nmCX=None, nmCY=None, pltAxXY=(False, False)):
    if pdDfr.size > 0:
        pltXYAxis(pdDfr, nmCX, nmCY, pltAxXY=pltAxXY)
    decorateSaveIt(pF, sTtl=sTtl, xLbl=xLbl, yLbl=yLbl, xLim=xLim, yLim=yLim)

# --- Functions (O_95__System / O_99__Simulation) -----------------------------
def plotCentres(dIPlt, dPltG, cDfr, sHdCX, sHdCY, lSY):
    serX, serY = cDfr.loc[:, sHdCX], cDfr.loc[:, sHdCY]
    serX, serY = GF.arrFinVal(serX, serY), GF.arrFinVal(serY, serY)
    cCol = dPltG['dCol'][sHdCY]
    plt.plot(serX, serY, marker=dIPlt['tpMark'], ms=dIPlt['szMark'],
             mew=dIPlt['ewMark'], mec=dIPlt['ecMark'], mfc=dIPlt['fcMark'],
             ls=dPltG['styLnCt'], lw=dPltG['wdthLnCt'], color=cCol,
             label=lSY[0])

def plotEvoSglR(dIPlt, dPltG, dfrR, pF, sHdCX, dSHdCY, sLblY):
    cFig = plt.figure()
    for sHdCY, lSY in dSHdCY.items():
        plotCentres(dIPlt, dPltG, dfrR, sHdCX, sHdCY, lSY)
    plt.legend(loc='best')
    decorateSavePlot(pF, dfrR, sTtl=dIPlt['title'], xLbl=dIPlt['xLbl'],
                     yLbl=sLblY, nmCX=sHdCX, pltAxXY=dIPlt['pltAxXY'])
    plt.close()

# --- Functions (O_99__Simulation) --------------------------------------------
def plotCIs(dIPlt, dPltG, dfrC, dfrS, serRp, sHdCX, sHdCY, mxY=0):
    serC, serS = dfrC.loc[:, sHdCY], dfrS.loc[:, sHdCY]
    tArrB = GF.getArrCI(serC=serC, serS=serS, serRp=serRp,
                        cAlph=dIPlt['alphaSpread'], mnV=0)
    # filter out CIs of range 0 and non-finite values
    arrBRng = GF.getBoolAND3C(tArrB[0] != tArrB[1], GF.boolFinVal(tArrB[0]),
                              GF.boolFinVal(tArrB[1]))
    arrYMn, arrYMx = tArrB[0][arrBRng], tArrB[1][arrBRng]
    cCol = dPltG['dCol'][sHdCY] + (dPltG['alpCol'],)
    plt.vlines(dfrS.loc[:, sHdCX][arrBRng], arrYMn, arrYMx,
               ls=dPltG['styLnCI'], lw=dPltG['wdthLnCI'], color=cCol)
    return max([mxY] + list(serC) + list(tArrB[1]))

def plotEvoMltR(dITp, dIPlt, dPltG, dDfrR, serRp, pF, sHdCX, dSHdCY, sLblY):
    SF.checkConsistency2Dfr(dDfrR, lK=[GC.S_CENT, GC.S_SPREAD])
    dfrCen, dfrSpr, maxY = dDfrR[GC.S_CENT], dDfrR[GC.S_SPREAD], 0
    assert sHdCX in dfrCen.columns and sHdCX in dfrSpr.columns
    cFig = plt.figure()
    for sHdCY, lSY in dSHdCY.items():
        maxY = plotCIs(dIPlt, dPltG, dfrCen, dfrSpr, serRp=serRp, sHdCX=sHdCX,
                       sHdCY=sHdCY, mxY=maxY)
        plotCentres(dIPlt, dPltG, dfrCen, sHdCX, sHdCY, lSY)
    plt.legend(loc='best')
    decorateSavePlotS(pF, maxX=dITp['tMax'], maxY=maxY, sTtl=dIPlt['title'],
                      xLbl=dIPlt['xLbl'], yLbl=sLblY, pltAxXY=dIPlt['pltAxXY'])
    plt.close()

###############################################################################
