# -*- coding: utf-8 -*-
###############################################################################
# --- O_99__Simulation.py -----------------------------------------------------
###############################################################################
import Core.C_00__GenConstants as GC
import Core.F_00__GenFunctions as GF
import Core.F_01__SpcFunctions as SF

from Core.I_02__InpFrames import InputFrames
from Core.O_00__Base import Base
from Core.O_80__PlotterSysSim import PlotterSysSim
from Core.O_90__PlotterData import PlotterData
from Core.O_95__System import System

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class Simulation(Base):
    def __init__(self, inpDat, iTp=99):
        super().__init__(inpDat, iTp)
        self.idO = GC.ID_SIM
        self.descO = 'Simulation'
        self.inFr = InputFrames(self.dITp)
        self.nRp = self.dITp['nReps']
        self.dDfrStats, self.dDfrRed = {}, {}
        self.hT = self.dITp['tMax']/(2*self.dITp['nTSRed'])
        self.lTRed = [k*self.hT for k in range(1, 2*self.dITp['nTSRed'], 2)]
        self.serRp = GF.iniPdSer(nEl=len(self.lTRed), v=0, sNm=GC.S_NUM_REP,
                                 tpDt=int)
        self.sFRes = self.dITp['sFObj']
        # print('Initiated "Simulation" object.')

    def doReps(self, inpDat):
        stTL = GF.startRepLoop()
        for cRp in range(1, self.nRp + 1):
            print(GC.S_PLUS*8, 'Starting repetition', cRp, 'of', self.nRp)
            cSys = System(inpDat, self.inFr, cRp=cRp)
            if cSys.dITp['doEvoT']:
                cSys.evolveOverTime(inpDat, self.dITp, cRp=cRp)
            else:
                lD, sFR = [cSys.dITp['sDObj']], cSys.sFRes
                cSys.dfrResEvo = SF.loadPdDfr(self.dITp, lD=lD, sF=sFR, iCol=0)
            if not cSys.dITp['doEvoT'] and cSys.dITp['doPlots']:
                cSys.plotSysResults(inpDat, self.dITp, cRp=cRp)
            SF.calcDfrRunStats(self.dITp, cSys, self.dDfrStats, self.dDfrRed,
                               hT=self.hT, lTRd=self.lTRed, serRp=self.serRp,
                               cRp=cRp)
            cSys.printRepDone(cRp, self.nRp, stTL)

    def calcRepStatistics(self, inpDat):
        # re-calc mean and M2 of self.dDfrStats if any dictionary is empty
        if len(self.dDfrStats) == 0 or len(self.dDfrRed) == 0:
            for cRp in range(1, self.nRp + 1):
                cSys = System(inpDat, self.inFr, cRp=cRp)
                SF.calcDfrRunStats(self.dITp, cSys, self.dDfrStats,
                                   self.dDfrRed, hT=self.hT, lTRd=self.lTRed,
                                   serRp=self.serRp, cRp=cRp)
        # calc final statistics and store them in self.dDfrStats
        SF.calcDfrFinStats(self.dDfrStats, serRp=self.serRp)
        SF.saveSerRep(self.dITp, self.dDfrStats[GC.S_MEAN], self.serRp,
                      lD=[self.dITp['sDObj']])
        # save the final statistics (for all components, without grouping)
        SF.saveDictDfr(self.dITp, self.dDfrStats, lK=GC.L_S_STATS_OUT,
                       sFEnd=GC.S_NO_GR, overWr=self.dITp['overWrCSV'])

    def getDfrStatsAndLeg(self, inpDat, PltD, dDfrStats, dSHdCY, sOp=None):
        for cRp in range(1, self.nRp + 1):
            Pltr = PlotterSysSim(inpDat, self.inFr, PltD, cOp=sOp, cRp=cRp)
            if sOp is None: # no groups - PltD.lSOp = [None]
                lSXY = [Pltr.sHdCX] + Pltr.lSHdCY
                dfrRed = self.dDfrRed[cRp].loc[:, lSXY]
                dSY = {sHd: [sHd] for sHd in Pltr.lSHdCY}
            else:           # groups - PltD.lSOp = [S_MEAN_GR, S_SUM_GR]
                t = SF.collapseColumns(PltD, self.dDfrRed[cRp], Pltr.sHdCX,
                                       Pltr.lSHdCY, sOp)
                dfrRed, dSY = t
            SF.updateDictDfr(dfrRed, dDfrStats, serRp=self.serRp)
            dSHdCY.update(dSY)
        SF.calcDfrFinStats(dDfrStats, serRp=self.serRp)

    def prepAndPlotData(self, inpDat, PltD):
        for sOp in PltD.lSOp:
            dDfrStats, dSHdCY, sDObj = {}, {}, self.dITp['sDObj']
            self.getDfrStatsAndLeg(inpDat, PltD, dDfrStats, dSHdCY, sOp=sOp)
            Pltr = PlotterSysSim(inpDat, self.inFr, PltD, cOp=sOp)
            Pltr.setPropPlotSim(PltD, dDfrStats, dSHdCY, self.serRp,
                                sD=sDObj, tMax=self.dITp['tMax'], sOp=sOp,
                                overWr=self.dITp['overWrPDF'])
            SF.saveDictDfr(self.dITp, dDfrStats, lK=GC.L_S_STATS_OUT,
                           sFEnd=GF.getFNoExt(Pltr.pPltF),
                           overWr=self.dITp['overWrCSV'])

    def plotSimResults(self, inpDat):
        for sI in self.dITp['lIPltDat']:
            PltD = PlotterData(inpDat, iTp=int(sI)+self.dIG['o_B_PltDt'])
            self.prepAndPlotData(inpDat, PltD)

    def runSimulation(self, inpDat):
        self.doReps(inpDat)
        if self.dITp['calcStats'] or self.dITp['doPlots']:
            self.calcRepStatistics(inpDat)
            if self.dITp['doPlots']:
                self.plotSimResults(inpDat)

    def printDfrStats(self, lSStatsOut=GC.L_S_STATS_OUT):
        if self.dITp['printStats']:
            print(GC.S_PLUS*8, 'Simulation results:', GC.S_PLUS*8)
            for sStat in lSStatsOut:
                assert sStat in self.dDfrStats
                print(GC.S_DASH*8, sStat, GC.S_DASH*8)
                print(self.dDfrStats[sStat])
            print(GC.S_PLUS*80)

###############################################################################
