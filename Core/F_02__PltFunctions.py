# -*- coding: utf-8 -*-
###############################################################################
# --- F_02__PltFunctions.py ---------------------------------------------------
###############################################################################
import os
import matplotlib.pyplot as plt

# --- Functions (general) -----------------------------------------------------
def pltXYAxis(cDfr, nmCX = None, nmCY = None, pltAxXY = (True, True)):
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
def plotDfrEvo(dIPlt, pdDfr, pFPlt, lIPlt, tpMark = 'x', szMark = 5,
               ewMark = 2, ecMark = (0.95, 0., 0.), fcMark = (0.9, 0.45, 0.),
               styLn = 'solid', wdthLn = 1, colLn = 'b', sTtl = '', xLbl = '',
               yLbl = ''):
    if not os.path.isfile(pFPlt):
        assert len(lIPlt) >= 2
        cFig = plt.figure()
        cX, cY = pdDfr.iloc[:, lIPlt[0]], pdDfr.iloc[:, lIPlt[1:]]
        plt.plot(cX, cY, marker = dIPlt['tpMark'], ms = dIPlt['szMark'],
                 mew = dIPlt['ewMark'], mec = dIPlt['ecMark'],
                 mfc = dIPlt['fcMark'], ls = dIPlt['styLn'],
                 lw = dIPlt['wdthLn'], color = dIPlt['colLn'])
        decorateSavePlot(pFPlt, cY, dIPlt['title'], dIPlt['xLbl'],
                         dIPlt['yLbl'], pltAxXY = (False, True))
        plt.close()

###############################################################################