# -*- coding: utf-8 -*-
###############################################################################
# --- O_92__PlotterSysSim.py --------------------------------------------------
###############################################################################
import Core.C_00__GenConstants as GC
import Core.F_00__GenFunctions as GF
import Core.F_01__SpcFunctions as SF
import Core.F_02__PltFunctions as PF

from Core.O_00__Base import Base

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class PlotterSysSim(Base):
    def __init__(self, inpDat, inpFr, cRp=0, iTp=92):
        super().__init__(inpDat, iTp)
        self.idO = GC.ID_PSS
        self.descO = 'PlotterSysSim'
        self.inFr = inpFr
        self.lSCpSL = list(self.inFr.dSCpSL)
        self.cRep = cRp
        self.dDfrCent, self.dDDfrPlt, self.pltSgl = None, None, False
        self.dIPlt = self.dITp[GC.S_CP_CNC]
        self.sHdCX, self.lSHdCY, self.dSHdCY = GC.S_TIME, None, None
        # print('Initiated "PlotterSysSim" object.')

    def procNoGroups(self, dPltG, dDfrRd, serRp, pF, sOp):
        # no collapsing of columns necessary (no groups)
        pltSpr = self.dIPlt['plotSpread']
        dfrPlt = self.dDfrCent[pF].loc[:, [self.sHdCX] + self.lSHdCY]
        self.dDDfrPlt[pF] = {GC.S_CENT: dfrPlt}
        self.dSHdCY = {sHd: [sHd] for sHd in self.lSHdCY}
        if not self.pltSgl:
            # including spread (from multiple repeats)
            for cDfr in dDfrRd:
                cDfr = cDfr.loc[:, [GC.S_TIME] + self.lSHdCY]
                SF.updateDictDfr(cDfr, self.dDDfrPlt[pF], serRp=serRp)
            # self.dDDfrPlt[pF], _ = SF.procData(dITp, dPltG, pF, pltSpr, serRp=serRp)

    def procWGroups(self, dPltG, dDfrRd, serRp, pF, sOp):
        pltSpr = self.dIPlt['plotSpread']
        # collapsing of columns necessary (component groups)
        dfrPlt = self.dDfrCent[pF].loc[:, [self.sHdCX] + self.lSHdCY]
        self.dDDfrPlt[pF] = {GC.S_CENT: dfrPlt}
        if self.pltSgl:
            # single stochastic realisation
            t = SF.collapseColumns(dPltG, dfrPlt, self.sHdCX, self.lSHdCY, sOp)
            self.dDDfrPlt[pF], self.dSHdCY = t
        else:
            # including spread (from multiple repeats)
            for cDfr in dDfrRd:
                dDfrT, d4Lg = SF.collapseColumns(dPltG, cDfr, sLX, lSLY, sOp)
                cDfr = dDfrT[GC.S_CENT]
                d4LgSim.update(d4Lg)
                SF.updateDictDfr(cDfr, self.dDDfrPlt[pF], serRp=serRp)

            # self.dDDfrPlt[pF], dSHdCY = SF.procData(dITp, dPltG, pF, pltSpr, self.sHdCX,
            #                               lSHdCY, sOp=sOp, serRp=serRp)

    def plotSimRes(self, dITp, dDfrStSim, dDfrRd, serRp=None, overWr=True):
        # self.pltSgl, sDSub = False, dITp['sDObj']
        for dPltG in self.dIPlt['dPltG'].values():
            self.dDDfrPlt, self.lSHdCY = {}, dPltG['lSCpCnc']
            dPPltF = SF.getDPFPltEvo(dPltG, self.dITp['sPPlt'], dITp['sDObj'])
            for (pF, (sOp, _)) in dPPltF.items():
                if overWr or not GF.pFExists(pF):
                    self.dSHdCY = {}
                    if dPltG['dCHdGr'] is None:
                        self.procNoGroups(dPltG, dDfrRd, serRp, pF, sOp=sOp)
                    else:
                        self.procWGroups(dPltG, dDfrRd, serRp, pF, sOp=sOp)

    # def genDDfrPlt(self):
    #     assert pltSpr in self.dDDfrPlt[pF]
    #     dDfrPlt = {GC.S_CENT: self.dDDfrPlt[pF][GC.S_MEAN],
    #                GC.S_SPREAD: self.dDDfrPlt[pF][self.dIPlt['plotSpread']]}
    #     return dDfrPlt, d4LgSim
    #                 return dDfrPlt, dSHdCY


    def getI4Plot(self, dITp, dPltG, sOp, pF, serRp):
        lSHdCY, pltSpr = dPltG['lSCpCnc'], self.dIPlt['plotSpread']
        if dPltG['dCHdGr'] is None:
            # no collapsing of columns necessary (no groups)
            dDfrPlt = {GC.S_CENT: self.dfrCent.loc[:, [self.sHdCX] + lSHdCY]}
            dSHdCY = {sHd: [sHd] for sHd in lSHdCY}
            if not self.pltSgl:
                # including spread (from multiple repeats)
                dDfrPlt, _ = SF.procData(dITp, dPltG, pF, pltSpr, serRp=serRp)
        else:
            # collapsing of columns necessary (component groups)
            dfrPlt = self.dfrCent.loc[:, [self.sHdCX] + lSHdCY]
            dDfrPlt = {GC.S_CENT: dfrPlt}
            if self.pltSgl:
                # single stochastic realisation
                dDfrPlt, dSHdCY = SF.collapseColumns(dPltG, dfrPlt, self.sHdCX,
                                                     lSHdCY, sOp=sOp)
            else:
                # including spread (from multiple repeats)
                dDfrPlt, dSHdCY = SF.procData(dITp, dPltG, pF, pltSpr,
                                              self.sHdCX, lSHdCY, sOp=sOp,
                                              serRp=serRp)
        return dDfrPlt, dSHdCY

    def plotEvoGen(self, dPPltF, serRp=None, dITp=None, overWr=True):
        for (pF, (sOp, dPltG)) in dPPltF.items():
            if overWr or not GF.pFExists(pF):
                dDfrPlt, dSHdCY = self.getI4Plot(dITp, dPltG, sOp, pF, serRp)
                if self.pltSgl:
                    PF.plotEvoSglR(self.dIPlt, dPltG, dDfrPlt[GC.S_CENT], pF,
                                   self.sHdCX, dSHdCY, sLblY=dPltG['yLbl'])
                else:
                    PF.plotEvoMltR(dITp, self.dIPlt, dPltG, dDfrPlt, serRp, pF,
                                   self.sHdCX, dSHdCY, sLblY=dPltG['yLbl'])

    def plotSysRes(self, dfrR, sDSub='.', overWr=True):
        self.dfrCent, self.pltSgl = dfrR, True
        if self.dfrCent is not None:
            for dPltG in self.dIPlt['dPltG'].values():
                dPPltF = SF.getDPFPltEvo(dPltG, self.dITp['sPPlt'], sDSub,
                                         cRp=self.cRep)
                self.plotEvoGen(dPPltF, overWr=overWr)

###############################################################################
