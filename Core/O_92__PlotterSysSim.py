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

    def getDDfrPlot(self, dITp, tDat, tKDCp, pF, sHdCX=GC.S_TIME):
        lSHdCY, _ = tDat
        dfrPlt = self.dfrRes.loc[:, [sHdCX] + lSHdCY]
        dDfrPlt = {GC.S_CENT: dfrPlt}
        if tKDCp is None:
            dSHdCY = {sHd: [sHd] for sHd in lSHdCY}
        elif tKDCp is not None and self.pltSgl:
            # single stochastic realisation
            dDfrPlt, dSHdCY = SF.collapseColumns(dfrPlt, sHdCX, lSHdCY, tKDCp,
                                                 lSCp=self.lSCpSL)
        else:
            # including spread (from multiple repeats)
            dDfrPlt, dSHdCY = SF.preProcFull(dITp, self.dIPlt, sHdCX, lSHdCY,
                                             tKDCp, pF, lSCp=self.lSCpSL)
        return dDfrPlt, dSHdCY

    def plotEvoGen(self, dPF, tDat, dITp=None, overWr=True, sHdCX=GC.S_TIME):
        if self.dfrRes is not None:
            for pF, tKDCp in dPF.items():
                if (GF.pFExists(pF) or overWr) and len(tDat[0]) > 0:
                    dDfrPlt, dSHdCY = self.getDDfrPlot(dITp, tDat, tKDCp, pF,
                                                       sHdCX=sHdCX)
                    PF.plotEvoCent(self.dIPlt, dDfrPlt[GC.S_CENT], pF, sHdCX,
                                   dSHdCY, sLblY=tDat[1])

    def plotResEvoSgl(self, dfrR, sDSub='.', overWr=True):
        self.dfrRes, self.dDfrRes, self.pltSgl = dfrR, {GC.S_SGL: dfrR}, True
        if self.dfrRes is not None:
            for cK, cT in self.dIPlt['dlSY'].items():
                assert len(cK) == 2 and len(cT) == 3
                dPPltF = SF.getDPFPltEvo(sPPlt=self.dITp['sPPlt'], sDSub=sDSub,
                                         tKey=cK, cRp=self.cRep, dMS=cT[2])
                self.plotEvoGen(dPPltF, tDat=cT[:2], overWr=overWr)

    def plotResEvoAvg(self, dITp, dDfrRV, overWr=True):
        self.dfrRes, self.dDfrRes = dDfrRV[GC.S_MEAN], dDfrRV
        self.pltSgl, sDSub = False, dITp['sD_Obj']
        if self.dDfrRes is not None:
            for cK, cT in self.dIPlt['dlSY'].items():
                dPPltF = SF.getDPFPltEvo(sPPlt=self.dITp['sPPlt'], sDSub=sDSub,
                                         tKey=cK, dMS=cT[2])
                self.plotEvoGen(dPPltF, tDat=cT[:2], dITp=dITp, overWr=overWr)

###############################################################################
