# -*- coding: utf-8 -*-
###############################################################################
# --- F_02__PltFunctions.py ---------------------------------------------------
###############################################################################
import matplotlib.pyplot as plt

import Core.C_00__GenConstants as GC
import Core.F_00__GenFunctions as GF
import Core.F_01__SpcFunctions as SF

# --- Functions (general) -----------------------------------------------------
def pltXYAxisS(maxX, maxY, pltAxXY=(True, True), cLwd=0.75, cClr='k'):
    assert len(pltAxXY) >= 2
    if pltAxXY[0] and maxX is not None:
        plt.plot([0, maxX], [0, 0], lw=cLwd, color=cClr)
    if pltAxXY[1] and maxY is not None:
        plt.plot([0, 0], [0, maxY], lw=cLwd, color=cClr)

def pltXYAxisD(cDfr, nmCX=None, nmCY=None, pltAxXY=(True, True), cLwd=0.75,
               cClr='k'):
    minDfrY, maxDfrY, cDfrY = 0, 1, cDfr
    if nmCX is not None:
        cDfrY = cDfr.drop(nmCX, axis=1)
    if cDfr.ndim == 1:
        minDfrY, maxDfrY = min(0, cDfrY.min()), cDfrY.max()
    elif cDfr.ndim > 1:
        minDfrY, maxDfrY = min(0, cDfrY.stack().min()), cDfrY.stack().max()
    assert len(pltAxXY) >= 2
    if pltAxXY[0]:
        if nmCX is not None:
            minX, maxX = min(0, min(cDfr.loc[:, nmCX])), max(cDfr.loc[:, nmCX])
            plt.plot([minX, maxX], [0, 0], lw=cLwd, color=cClr)
        else:
            plt.plot([0, cDfr.shape[0] - 1], [0, 0], lw=cLwd, color=cClr)
    if pltAxXY[1]:
        if nmCY is not None:
            minY, maxY = min(0, min(cDfr.loc[:, nmCY])), max(cDfr.loc[:, nmCY])
            plt.plot([0, 0], [minY, maxY], lw=cLwd, color=cClr)
        else:
            plt.plot([0, 0], [minDfrY, maxDfrY], lw=cLwd, color=cClr)

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

def decorateSavePlotD(pF, pdDfr, sTtl=None, xLbl=None, yLbl=None, xLim=None,
                      yLim=None, nmCX=None, nmCY=None, pltAxXY=(False, False)):
    if pdDfr.size > 0:
        pltXYAxisD(pdDfr, nmCX, nmCY, pltAxXY=pltAxXY)
    decorateSaveIt(pF, sTtl=sTtl, xLbl=xLbl, yLbl=yLbl, xLim=xLim, yLim=yLim)

# --- Functions (O_95__System / O_99__Simulation) -----------------------------
def plotCentres(cPltr, cDfr, sHdCY, lSY):
    serX, serY = cDfr.loc[:, cPltr.sHdCX], cDfr.loc[:, sHdCY]
    serX, serY = GF.arrFinVal(serX, serY), GF.arrFinVal(serY, serY)
    cClr, dIPlt, pltDt = cPltr.pltDtI.dCol[sHdCY], cPltr.dIPlt, cPltr.pltDtI
    plt.plot(serX, serY, marker=dIPlt['tpMark'], ms=dIPlt['szMark'],
             mew=dIPlt['ewMark'], mec=dIPlt['ecMark'], mfc=dIPlt['fcMark'],
             ls=pltDt.styLnCt, lw=pltDt.wdthLnCt, color=cClr,
             label=lSY[0])

def plotEvoSglR(cPltr):
    SF.checkConsistencyDictDfrPlt(cPltr.dDfrPlt, lK=[GC.S_SGL])
    assert cPltr.sHdCX in cPltr.dfrCent.columns
    cFig = plt.figure()
    for sHdCY, lSY in cPltr.dSHdCY.items():
        plotCentres(cPltr, cPltr.dfrCent, sHdCY, lSY)
    plt.legend(loc='best')
    dfrRed = cPltr.dfrCent.loc[:, [cPltr.sHdCX] + list(cPltr.dSHdCY)]
    decorateSavePlotD(cPltr.pPltF, dfrRed, sTtl=cPltr.dIPlt['title'],
                      xLbl=cPltr.dIPlt['xLbl'], yLbl=cPltr.pltDtI.yLbl,
                      nmCX=cPltr.sHdCX, pltAxXY=cPltr.dIPlt['pltAxXY'])
    plt.close()

# --- Functions (O_99__Simulation) --------------------------------------------
def plotCIs(cPltr, dfrC, dfrS, serRp, sHdCY, mxY=0):
    serC, serS = dfrC.loc[:, sHdCY], dfrS.loc[:, sHdCY]
    tArrB = GF.getArrCI(serC=serC, serS=serS, serRp=serRp, cAlph=cPltr.alpSpr,
                        mnV=0)
    # filter out CIs of range 0 and non-finite values
    arrBRng = GF.getBoolAND3C(tArrB[0] != tArrB[1], GF.boolFinVal(tArrB[0]),
                              GF.boolFinVal(tArrB[1]))
    arrYMn, arrYMx = tArrB[0][arrBRng], tArrB[1][arrBRng]
    cClr = cPltr.pltDtI.dCol[sHdCY] + (cPltr.pltDtI.alpCol,)
    plt.vlines(dfrS.loc[:, cPltr.sHdCX][arrBRng], arrYMn, arrYMx,
               ls=cPltr.pltDtI.styLnCI, lw=cPltr.pltDtI.wdthLnCI, color=cClr)
    return max([mxY] + list(serC) + list(tArrB[1]))

def plotEvoMltR(cPltr, serRp, tMax):
    SF.checkConsistencyDictDfrPlt(cPltr.dDfrPlt, lK=[GC.S_CENT, GC.S_SPREAD])
    dfrCen, dfrSpr, maxY = cPltr.dfrCent, cPltr.dfrSpread, 0
    assert (cPltr.sHdCX in dfrCen.columns and cPltr.sHdCX in dfrSpr.columns)
    cFig = plt.figure()
    for sHdCY, lSY in cPltr.dSHdCY.items():
        maxY = plotCIs(cPltr, dfrCen, dfrSpr, serRp, sHdCY, mxY=maxY)
        plotCentres(cPltr, dfrCen, sHdCY, lSY)
    plt.legend(loc='best')
    decorateSavePlotS(cPltr.pPltF, maxX=tMax, maxY=maxY,
                      sTtl=cPltr.dIPlt['title'], xLbl=cPltr.dIPlt['xLbl'],
                      yLbl=cPltr.pltDtI.yLbl, pltAxXY=cPltr.dIPlt['pltAxXY'])
    plt.close()

###############################################################################
