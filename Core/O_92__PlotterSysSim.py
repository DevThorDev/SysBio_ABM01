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
        self.dfrRes, self.dDfrRes, self.pltSgl = None, None, False
        self.dIPlt = self.dITp[GC.S_CP_CNC]
        self.sHdCX = GC.S_TIME
        # print('Initiated "PlotterSysSim" object.')

    def getI4Plot(self, dITp, dPltG, sOp, pF, serRp):
        lSHdCY, pltSpr = dPltG['lSCpCnc'], self.dIPlt['plotSpread']
        if dPltG['dCHdGr'] is None:
            # no collapsing of columns necessary (no groups)
            dDfrPlt = {GC.S_CENT: self.dfrRes.loc[:, [self.sHdCX] + lSHdCY]}
            dSHdCY = {sHd: [sHd] for sHd in lSHdCY}
            if not self.pltSgl:
                # including spread (from multiple repeats)
                dDfrPlt, _ = SF.procData(dITp, dPltG, pF, pltSpr, serRp=serRp)
        else:
            # collapsing of columns necessary (component groups)
            dfrPlt = self.dfrRes.loc[:, [self.sHdCX] + lSHdCY]
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

    def plotResEvoSgl(self, dfrR, sDSub='.', overWr=True):
        self.dfrRes, self.dDfrRes, self.pltSgl = dfrR, {GC.S_SGL: dfrR}, True
        if self.dfrRes is not None:
            for dPltG in self.dIPlt['dPltG'].values():
                dPPltF = SF.getDPFPltEvo(dPltG, self.dITp['sPPlt'], sDSub,
                                         cRp=self.cRep)
                self.plotEvoGen(dPPltF, overWr=overWr)

    def plotResEvoAvg(self, dITp, dDfrRV, serRp, overWr=True):
        self.dfrRes, self.dDfrRes = dDfrRV[GC.S_MEAN], dDfrRV
        self.pltSgl, sDSub = False, dITp['sD_Obj']
        if self.dfrRes is not None and self.dDfrRes is not None:
            for dPltG in self.dIPlt['dPltG'].values():
                dPPltF = SF.getDPFPltEvo(dPltG, self.dITp['sPPlt'], sDSub)
                self.plotEvoGen(dPPltF, serRp=serRp, dITp=dITp, overWr=overWr)

###############################################################################
