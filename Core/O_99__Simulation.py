# -*- coding: utf-8 -*-
###############################################################################
# --- O_99__Simulation.py -----------------------------------------------------
###############################################################################
import Core.C_00__GenConstants as GC
import Core.F_01__SpcFunctions as SF

from Core.I_02__InpFrames import InputFrames
from Core.O_00__Base import Base
from Core.O_92__PlotterSysSim import PlotterSysSim
from Core.O_95__System import System

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class Simulation(Base):
    def __init__(self, inpDat, iTp=99):
        super().__init__(inpDat, iTp)
        self.idO = GC.ID_SIM
        self.descO = 'Simulation'
        self.inFr = InputFrames(self.dITp)
        self.nRep = self.dITp['nReps']
        self.sFRes = self.dITp['sF_Obj']
        # self.dParPlt = self.dITp[GC.S_D_PLT][GC.S_CP_CNC]
        # print('Initiated "Simulation" object.')

    def plotResEvo(self, inpDat, dDfrRV):
        Pltr = PlotterSysSim(inpDat, self.inFr)
        Pltr.plotResEvoAvg(self.dITp, dDfrRV)

    def calcRepStatistics(self, dDfrRV):
        SF.calcStatsDfr(dDfrRV, nRp=self.nRep)
        self.dDfrStats = dDfrRV
        for sStat, dfrStat in self.dDfrStats.items():
            SF.savePdDfr(self.dITp, dfrStat, [self.dITp['sD_Obj']],
                         self.sFRes + GC.S_USC + str(sStat), overWr=True)

    def runSimulation(self, inpDat):
        doPlt, dDfrRunV = self.dITp['doPlots'], {}
        for cRep in range(1, self.nRep + 1):
            print(GC.S_PLUS*8, 'Starting repetition', cRep, 'of', self.nRep)
            cSys = System(inpDat, self.inFr, cRp=cRep)
            if self.dITp['doEvoT']:
                cSys.evolveOverTime(inpDat, self.dITp, doPlots=doPlt)
            if not self.dITp['doEvoT'] and doPlt:
                cSys.plotResEvo(inpDat, self.dITp, overWr=True)
            SF.calcRunMeanM2Dfr(self.dITp, cSys, dDfrRunV, cCt=cSys.cRep)
            cSys.printFinalSimuTime()
            print(GC.S_PLUS*8, 'Finished repetition', cRep, 'of', self.nRep)
        self.calcRepStatistics(dDfrRunV)
        self.plotResEvo(inpDat, dDfrRunV)

    def printDfrStats(self, lSStatsOut = GC.L_S_STATS_OUT):
        print(GC.S_PLUS*8, 'Simulation results:', GC.S_PLUS*8)
        for sStat in lSStatsOut:
            assert sStat in self.dDfrStats
            print(GC.S_DASH*8, sStat, GC.S_DASH*8)
            print(self.dDfrStats[sStat])
        print(GC.S_PLUS*80)

###############################################################################
