# -*- coding: utf-8 -*-
###############################################################################
# --- F_02__PltFunctions.py ---------------------------------------------------
###############################################################################
import os
import matplotlib.pyplot as plt
import pandas as pd

import Core.C_00__GenConstants as GC
import Core.F_00__GenFunctions as GF

# --- Functions (general) -----------------------------------------------------
def pltXYAxis(cDfr, nmCX = None, nmCY = None, pltAxXY = (True, True)):
    minDfr, maxDfr = 0, 1
    if cDfr.ndim == 1:
        minDfr, maxDfr = min(0, cDfr.min()), cDfr.max()
    elif cDfr.ndim > 1:
        minDfr, maxDfr = min(0, cDfr.stack().min()), cDfr.stack().max()
    if pltAxXY[0]:
        if nmCX is not None:
            minX, maxX = min(0, min(cDfr.loc[:, nmCX])), max(cDfr.loc[:, nmCX])
            plt.plot([minX, maxX], [0, 0], lw = 0.75, color = 'k')
        else:
            plt.plot([0, cDfr.shape[0] - 1], [0, 0], lw = 0.75, color = 'k')
    if pltAxXY[1]:
        if nmCY is not None:
            minY, maxY = min(0, min(cDfr.loc[:, nmCY])), max(cDfr.loc[:, nmCY])
            plt.plot([0, 0], [minY, maxY], lw = 0.75, color = 'k')
        else:
            plt.plot([0, 0], [minDfr, maxDfr], lw = 0.75, color = 'k')

def decorateSavePlot(pF, pdDfr, sTtl = None, xLbl = None, yLbl = None,
                     xLim = None, yLim = None, nmCX = None, nmCY = None,
                     pltAxXY = (False, False)):
    assert len(pltAxXY) >= 2
    if pdDfr.size > 0:
        pltXYAxis(pdDfr, nmCX, nmCY, pltAxXY = pltAxXY)
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

# --- Functions (O_90_State) --------------------------------------------------
def plotDCncEvo(dIPlt, dCncEvo, pFPlt, lIPlt, tpMark = 'x', szMark = 5,
               ewMark = 2, ecMark = (0.95, 0., 0.), fcMark = (0.9, 0.45, 0.),
               styLn = 'solid', wdthLn = 1, colLn = 'b', sTtl = '', xLbl = '',
               yLbl = '', overWr = True):
    if not os.path.isfile(pFPlt) or overWr:
        assert len(lIPlt) >= 2
        cFig = plt.figure()
        pdDfr = pd.DataFrame(dCncEvo)
        cX, cY = pdDfr.iloc[:, lIPlt[0]], pdDfr.iloc[:, lIPlt[1:]]
        plt.plot(cX, cY, marker = dIPlt['tpMark'], ms = dIPlt['szMark'],
                 mew = dIPlt['ewMark'], mec = dIPlt['ecMark'],
                 mfc = dIPlt['fcMark'], ls = dIPlt['styLn'],
                 lw = dIPlt['wdthLn'], color = dIPlt['colLn'])
        decorateSavePlot(pFPlt, cY, dIPlt['title'], dIPlt['xLbl'],
                         dIPlt['yLbl'], pltAxXY = dIPlt['pltAxXY_Conc'])
        plt.close()

# --- Functions (O_99_System) -------------------------------------------------
def preProcMeanSum(pdDfr, sLX, lSLY, k1):
    d4Sel, mdDfr, lSLYMd = {}, pd.DataFrame(), list(GC.DS_ST_4)
    for sCol in lSLY:
        for sSimple in GC.DS_ST_4:
            if len(sCol) >= 2:
                if sCol[0] == sSimple and set(sCol[1:]) <= {'0', '1'}:
                    GF.addToDictL(d4Sel, sSimple, sCol)
                else:
                    if ((sCol[0] not in GC.DS_ST_4) or
                        (not set(sCol[1:]) <= {'0', '1'})):
                        GF.addToDictL(d4Sel, sCol, sCol)
                        lSLYMd.append(sCol)
    mdDfr.loc[:, sLX] = pdDfr.loc[:, sLX]
    for sStS in d4Sel:
        if sStS in GC.DS_ST_4:
            if k1 == GC.S_MEAN:
                mdDfr.loc[:, sStS] = pdDfr.loc[:, d4Sel[sStS]].T.mean()
            elif k1 == GC.S_SUM:
                mdDfr.loc[:, sStS] = pdDfr.loc[:, d4Sel[sStS]].T.sum()
        else:
            mdDfr.loc[:, sStS] = pdDfr[:, sStS]
    return mdDfr, lSLYMd

def plotEvo(dIPlt, dResEvo, pF, tKey, tDat, sLblX = GC.S_TIME, overWr = True):
    if (not os.path.isfile(pF) or overWr) and len(tDat[0]) > 0:
        ((_, k1), (lSLblY, t1)) = (tKey, tDat)
        pdDfr = pd.DataFrame(dResEvo).loc[:, [sLblX] + lSLblY]
        if k1 in [GC.S_MEAN, GC.S_SUM]:
            pdDfr, lSLblY = preProcMeanSum(pdDfr, sLblX, lSLblY, k1)
        cFig = plt.figure()
        for sLblY in lSLblY:
            plt.plot(pdDfr.loc[:, sLblX], pdDfr.loc[:, sLblY],
                     marker = dIPlt['tpMark'], ms = dIPlt['szMark'],
                     mew = dIPlt['ewMark'], mec = dIPlt['ecMark'],
                     mfc = dIPlt['fcMark'], ls = dIPlt['styLn'],
                     lw = dIPlt['wdthLn'], color = dIPlt['colLn'],
                     label = sLblY)
        plt.legend(loc = 'best')
        decorateSavePlot(pF, pdDfr, sTtl = dIPlt['title'],
                         xLbl = dIPlt['xLbl'], yLbl = t1, nmCX = sLblX,
                         pltAxXY = dIPlt['pltAxXY'])
        plt.close()

###############################################################################
