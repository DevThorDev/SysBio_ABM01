# -*- coding: utf-8 -*-
###############################################################################
# --- O_80__PlotterSysSim.py --------------------------------------------------
###############################################################################
import Core.C_00__GenConstants as GC
import Core.F_00__GenFunctions as GF
import Core.F_01__SpcFunctions as SF
# import Core.F_02__PltFunctions as PF

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
        self.dfrCent, self.dfrSpread  = None, None
        self.dDfrPlt, self.pltSgl = None, False
        self.sHdCX, self.lSHdCY, self.dSHdCY = GC.S_TIME, None, None
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
        self.printDictDfr(sAttr='dDfrPlt', sTxt='Dict. of DataFrames 4 plot:')
        print('-'*80)

    # def procNoGroups(self, serRp):
    #     # no collapsing of columns necessary (no groups)
    #     dfrPlt = self.dfrCent.loc[:, [self.sHdCX] + self.lSHdCY]
    #     self.dDfrPlt = {GC.S_CENT: dfrPlt}
    #     self.dSHdCY = {sHd: [sHd] for sHd in self.lSHdCY}
    #     if not self.pltSgl:
    #         # including spread (from multiple repeats)
    #         for cDfr in dDfrRd:
    #             cDfr = cDfr.loc[:, [GC.S_TIME] + self.lSHdCY]
    #             SF.updateDictDfr(cDfr, self.dDfrPlt, serRp=serRp)
    #         # self.dDfrPlt, _ = SF.procData(dITp, dPltG, pF, self.pltSpr, serRp=serRp)

    def procWGroups(self, serRp):
        # collapsing of columns necessary (component groups)
        dfrPlt = self.dfrCent.loc[:, [self.sHdCX] + self.lSHdCY]
        self.dDfrPlt = {GC.S_CENT: dfrPlt}
        if self.pltSgl:
            # single stochastic realisation
            t = SF.collapseColumns(dPltG, dfrPlt, self.sHdCX, self.lSHdCY, sOp)
            self.dDfrPlt, self.dSHdCY = t
        else:
            # including spread (from multiple repeats)
            for cDfr in dDfrRd:
                dDfrT, d4Lg = SF.collapseColumns(dPltG, cDfr, sLX, lSLY, sOp)
                cDfr = dDfrT[GC.S_CENT]
                d4LgSim.update(d4Lg)
                SF.updateDictDfr(cDfr, self.dDfrPlt, serRp=serRp)

            # self.dDfrPlt, dSHdCY = SF.procData(dITp, dPltG, pF, self.pltSpr, self.sHdCX,
            #                               lSHdCY, sOp=sOp, serRp=serRp)

    def plotSimRes(self, dITp, dDfrSt, dfrRd, serRp=None, overWr=True):
        sDSub, self.dDfrPlt = dITp['sDObj'], {}
        self.lSHdCY = self.pltDtI.lSCpCnc
        self.pPltF = SF.getPPltF(self.pltDtI, self.sPPlt, sDSub, sOp=self.cOp)
        self.dfrCent, self.dfrSpread = dDfrSt[GC.S_MEAN], dDfrSt[self.pltSpr]
        print('-'*8, 'TEMP - dDfrSt:\n')
        for cK, cDfr in dDfrSt.items():
            print('-'*4, cK, '-'*4)
            print(cDfr)
        print('-'*8, 'TEMP - dfrRd:\n')
        print(dfrRd)
        print('-'*8, 'TEMP - serRp:\n')
        print(serRp)
        print('-'*8, 'TEMP - lSHdCY:\n')
        print(self.lSHdCY)
        print('-'*8, 'TEMP - pPltF:\n')
        print(self.pPltF)
        print('-'*8, 'TEMP - sOp:\n')
        print(self.cOp)
        print('-'*8, 'TEMP - END', '-'*8)
        assert False
        if overWr or not GF.pFExists(self.pPltF):
            if self.pltDtI.dCHdGr is None:      # no groups defined
                # self.procNoGroups(dfrRd, serRp)
                dfrPltC = self.dfrCent.loc[:, [self.sHdCX] + self.lSHdCY]
                dfrPltS = self.dfrSpread.loc[:, [self.sHdCX] + self.lSHdCY]
                self.dDfrPlt = {GC.S_CENT: dfrPltC, self.pltSpr: dfrPltS}
                self.dSHdCY = {sHd: [sHd] for sHd in self.lSHdCY}
            else:                               # groups were defined
                # self.procWGroups(dfrRd, serRp)
                dfrPltC = self.dfrCent.loc[:, [self.sHdCX] + self.lSHdCY]
                self.dDfrPlt = {GC.S_CENT: dfrPltC}

    # # def genDDfrPlt(self):
    # #     assert self.pltSpr in self.dDfrPlt
    # #     dDfrPlt = {GC.S_CENT: self.dDfrPlt[GC.S_MEAN],
    # #                GC.S_SPREAD: self.dDfrPlt[self.dIPlt['plotSpread']]}
    # #     return dDfrPlt, d4LgSim
    # #                 return dDfrPlt, dSHdCY


    # def getI4Plot(self, dITp, dPltG, sOp, pF, serRp):
    #     lSHdCY = dPltG['lSCpCnc']
    #     if dPltG['dCHdGr'] is None:
    #         # no collapsing of columns necessary (no groups)
    #         dDfrPlt = {GC.S_CENT: self.dfrCent.loc[:, [self.sHdCX] + lSHdCY]}
    #         dSHdCY = {sHd: [sHd] for sHd in lSHdCY}
    #         if not self.pltSgl:
    #             # including spread (from multiple repeats)
    #             dDfrPlt, _ = SF.procData(dITp, dPltG, pF, self.pltSpr, serRp=serRp)
    #     else:
    #         # collapsing of columns necessary (component groups)
    #         dfrPlt = self.dfrCent.loc[:, [self.sHdCX] + lSHdCY]
    #         dDfrPlt = {GC.S_CENT: dfrPlt}
    #         if self.pltSgl:
    #             # single stochastic realisation
    #             dDfrPlt, dSHdCY = SF.collapseColumns(dPltG, dfrPlt, self.sHdCX,
    #                                                  lSHdCY, sOp=sOp)
    #         else:
    #             # including spread (from multiple repeats)
    #             dDfrPlt, dSHdCY = SF.procData(dITp, dPltG, pF, self.pltSpr,
    #                                           self.sHdCX, lSHdCY, sOp=sOp,
    #                                           serRp=serRp)
    #     return dDfrPlt, dSHdCY

    # def plotEvoGen(self, dPPltF, serRp=None, dITp=None, overWr=True):
    #     for (pF, (sOp, dPltG)) in dPPltF.items():
    #         if overWr or not GF.pFExists(pF):
    #             dDfrPlt, dSHdCY = self.getI4Plot(dITp, dPltG, sOp, pF, serRp)
    #             if self.pltSgl:
    #                 PF.plotEvoSglR(self.dIPlt, dPltG, dDfrPlt[GC.S_CENT], pF,
    #                                self.sHdCX, dSHdCY, sLblY=dPltG['yLbl'])
    #             else:
    #                 PF.plotEvoMltR(dITp, self.dIPlt, dPltG, dDfrPlt, serRp, pF,
    #                                self.sHdCX, dSHdCY, sLblY=dPltG['yLbl'])

    # def plotSysRes(self, dfrR, sDSub='.', overWr=True):
    #     self.dfrCent, self.pltSgl = dfrR, True
    #     if self.dfrCent is not None:
    #         for dPltG in self.dIPlt['dPltG'].values():
    #             dPPltF = SF.getDPFPltEvo(dPltG, self.dITp['sPPlt'], sDSub,
    #                                      cRp=self.cRp)
    #             self.plotEvoGen(dPPltF, overWr=overWr)

###############################################################################
