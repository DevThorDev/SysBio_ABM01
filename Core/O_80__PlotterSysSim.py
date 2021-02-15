# -*- coding: utf-8 -*-
###############################################################################
# --- O_80__PlotterSysSim.py --------------------------------------------------
###############################################################################
import Core.C_00__GenConstants as GC
import Core.F_00__GenFunctions as GF
import Core.F_01__SpcFunctions as SF
import Core.F_02__PltFunctions as PF

from Core.O_00__Base import Base

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class PlotterSysSim(Base):
    def __init__(self, inpDat, inpFr, pltDatIn, cOp=None, cRp=0, iTp=80):
        super().__init__(inpDat, iTp)
        self.idO = GC.ID_PSS
        self.descO = 'PlotterSysSim'
        self.inFr = inpFr
        self.lSCpSL = list(self.inFr.dSCpSL)
        self.pltDtI = pltDatIn
        self.cOp = cOp
        self.cRp = cRp
        self.sPPlt = self.dITp['sPPlt']
        self.pltSpr = self.dITp[GC.S_PLT_CL_CP_CNC]['plotSpread']
        self.alpSpr = self.dITp[GC.S_PLT_CL_CP_CNC]['alphaSpread']
        self.pltAxXY = self.dITp[GC.S_PLT_CL_CP_CNC]['pltAxXY']
        self.dIPlt = self.dITp[GC.S_PLT_CL_CP_CNC]
        self.dfrCent, self.dfrSpread = None, None
        self.dDfrPlt, self.dSHdCY, self.pltSgl = {}, {}, False
        self.sHdCX, self.lSHdCY = GC.S_TIME, self.pltDtI.lSCpCnc
        # print('Initiated "PlotterSysSim" object.')

    def __str__(self):
        sIn = ('~'*24 + ' ' + self.descO + ' with ID ' + str(self.idO) + ' ' +
               '~'*24 + '\nPerformed operation: ' + str(self.cOp) + '\n' +
               '~'*24 + '\nRepetition: ' + str(self.cRp) + '\n' +
               '~'*24 + '\nPath to plot results directory: ' +
               str(self.sPPlt) + '\n' + '~'*24 + '\nPlot spread: ' +
               str(self.pltSpr) + '\n' + '~'*24 + '\nAlpha confidence: ' +
               str(self.alpSpr) + '\n' + '~'*24 + '\nPlot x-/y-axis: ' +
               str(self.pltAxXY) + '\n' +  '~'*80 + '\n')
        return sIn

    def printInpData(self):
        print('-'*20, 'Plot input data', '-'*20)
        self.pltDtI.printData()

    def printObj(self, sAttr, sTxt=''):
        if getattr(self, sAttr) is None:
            print(sTxt, 'None!')
        else:
            print(sTxt)
            print(getattr(self, sAttr))

    def printDictDfr(self, sAttr, sTxt=''):
        if getattr(self, sAttr) is None:
            print(sTxt, 'None!')
        else:
            for cK, cDfr in getattr(self, sAttr).items():
                print('DataFrame of key "' + str(cK) + '":')
                print(cDfr)

    def printContent(self):
        print('-'*8, 'Content of "PlotterSysSim" object', '-'*8)
        print('ID of object:', self.idO)
        print('Description of object:', self.descO)
        print('List of component strings (short):', self.lSCpSL)
        print('Current operation:', self.cOp)
        print('Current repetition:', self.cRp)
        print('Plot single realisation:', self.pltSgl)
        print('Header of "x" values column:', self.sHdCX)
        self.printObj(sAttr='lSHdCY', sTxt='Headers of "y" values columns:')
        self.printObj(sAttr='dSHdCY', sTxt='Dict. of "y" values column hdrs.:')
        self.printObj(sAttr='dfrCent', sTxt='DataFrame of centres:')
        self.printObj(sAttr='dfrSpread', sTxt='DataFrame of spread:')
        self.printDictDfr(sAttr='dDfrPlt', sTxt='Dict. of DataFrames to plot:')
        print('-'*80)

    def setPropPlotSys(self, PltD, dfrRes, dSHdCY, sD, sOp=None, cRp=0,
                       overWr=True):
        self.dfrCent = dfrRes
        self.dDfrPlt = {GC.S_SGL: self.dfrCent}
        self.dSHdCY = dSHdCY
        self.ovWr=overWr
        self.pPltF = SF.getPPltF(PltD, self.sPPlt, sDSub=sD, sOp=sOp, cRp=cRp)
        if not GF.pFExists(self.pPltF) or self.ovWr:
            PF.plotEvoSglR(self)

    def setPropPlotSim(self, PltD, dDfrStats, dSHdCY, serRp, sD, tMax,
                       sOp=None, cRp=0, overWr=True):
        self.dfrCent = dDfrStats[GC.S_MEAN]
        self.dfrSpread = dDfrStats[self.pltSpr]
        self.dDfrPlt = {GC.S_CENT: self.dfrCent, GC.S_SPREAD: self.dfrSpread}
        self.dSHdCY = dSHdCY
        self.ovWr=overWr
        self.pPltF = SF.getPPltF(PltD, self.sPPlt, sDSub=sD, sOp=sOp, cRp=cRp)
        if not GF.pFExists(self.pPltF) or self.ovWr:
            PF.plotEvoMltR(self, serRp, tMax=tMax)

###############################################################################
