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
        # print('Initiated "PlotterSysSim" object.')

    def getI4Plot(self, dITp, dPltG, sOp, pF, sHdCX=GC.S_TIME):
        lSHdCY, pltSpr = dPltG['lSCpCnc'], self.dIPlt['plotSpread']
        if dPltG['dCHdGr'] is None:
            # no collapsing of columns necessary (no groups)
            dDfrPlt = {GC.S_CENT: self.dfrRes.loc[:, [sHdCX] + lSHdCY]}
            dSHdCY = {sHd: [sHd] for sHd in lSHdCY}
            if not self.pltSgl:
                # including spread (from multiple repeats)
                dDfrPlt, _ = SF.preProcData(dITp, dPltG, pF, pltSpr)
        else:
            # collapsing of columns necessary (component groups)
            dfrPlt = self.dfrRes.loc[:, [sHdCX] + lSHdCY]
            dDfrPlt = {GC.S_CENT: dfrPlt}
            if self.pltSgl:
                # single stochastic realisation
                dDfrPlt, dSHdCY = SF.collapseColumns(dPltG, dfrPlt, sHdCX,
                                                     lSHdCY, sOp=sOp)
            else:
                # including spread (from multiple repeats)
                dDfrPlt, dSHdCY = SF.preProcData(dITp, dPltG, pF, pltSpr,
                                                 sHdCX, lSHdCY, sOp=sOp)
        return dDfrPlt, dSHdCY

    def plotEvoGen(self, dPPF, serCt=None, dITp=None, overWr=True,
                   sHdCX=GC.S_TIME):
        for (pF, (sOp, dPltG)) in dPPF.items():
            if overWr or not GF.pFExists(pF):
                dDfrPlt, dSHdCY = self.getI4Plot(dITp, dPltG, sOp, pF, sHdCX)
                if self.pltSgl:
                    PF.plotEvoSglR(self.dIPlt, dPltG, dDfrPlt[GC.S_CENT], pF,
                                   sHdCX, dSHdCY, sLblY=dPltG['yLbl'])
                else:
                    PF.plotEvoMultR(dITp, self.dIPlt, dPltG, dDfrPlt, serCt,
                                    pF, sHdCX, dSHdCY, sLblY=dPltG['yLbl'])

    def plotResEvoSgl(self, dfrR, sDSub='.', overWr=True):
        self.dfrRes, self.dDfrRes, self.pltSgl = dfrR, {GC.S_SGL: dfrR}, True
        if self.dfrRes is not None:
            for dPltG in self.dIPlt['dPltG'].values():
                dPPltF = SF.getDPFPltEvo(dPltG, self.dITp['sPPlt'], sDSub,
                                         cRp=self.cRep)
                self.plotEvoGen(dPPltF, overWr=overWr)

    def plotResEvoAvg(self, dITp, dDfrRV, serCt, overWr=True):
        self.dfrRes, self.dDfrRes = dDfrRV[GC.S_MEAN], dDfrRV
        self.pltSgl, sDSub = False, dITp['sD_Obj']
        if self.dfrRes is not None and self.dDfrRes is not None:
            for dPltG in self.dIPlt['dPltG'].values():
                dPPltF = SF.getDPFPltEvo(dPltG, self.dITp['sPPlt'], sDSub)
                self.plotEvoGen(dPPltF, serCt=serCt, dITp=dITp, overWr=overWr)

###############################################################################
