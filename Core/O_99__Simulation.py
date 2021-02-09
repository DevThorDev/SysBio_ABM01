# -*- coding: utf-8 -*-
###############################################################################
# --- O_99__Simulation.py -----------------------------------------------------
###############################################################################
import Core.C_00__GenConstants as GC
import Core.F_00__GenFunctions as GF
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
        self.hT = self.dITp['tMax']/(2*self.dITp['nTSRed'])
        self.lTRed = [k*self.hT for k in range(1, 2*self.dITp['nTSRed'], 2)]
        self.serRp = GF.iniPdSer(nEl=len(self.lTRed), v=0, sNm=GC.S_NUM_REP,
                                 dTp=int)
        self.sFRes = self.dITp['sF_Obj']
        # print('Initiated "Simulation" object.')

    def plotResEvo(self, inpDat):
        Pltr = PlotterSysSim(inpDat, self.inFr)
        Pltr.plotResEvoAvg(self.dITp, self.dDfrStats, serRp=self.serRp)

    def calcRepStatistics(self):
        SF.calcStatsDfr(self.dDfrStats, serRp=self.serRp)
        SF.saveSerRep(self.dITp, self.dDfrStats[GC.S_MEAN], self.serRp,
                      lD=[self.dITp['sD_Obj']])
        for sStat in GC.L_S_STATS_OUT:
            sF = self.sFRes + GC.S_USC + str(sStat) + GC.S_USC + GC.S_NO_GR
            SF.savePdDfr(self.dITp, self.dDfrStats[sStat],
                         lD=[self.dITp['sD_Obj'], sStat], sF=sF)

    def runSimulation(self, inpDat):
        stTL = GF.startRepLoop()
        doPlt, self.dDfrStats = self.dITp['doPlots'], {}
        for cRep in range(1, self.nRep + 1):
            print(GC.S_PLUS*8, 'Starting repetition', cRep, 'of', self.nRep)
            cSys = System(inpDat, self.inFr, cRp=cRep)
            if self.dITp['doEvoT']:
                cSys.evolveOverTime(inpDat, self.dITp, doPlots=doPlt)
            if not self.dITp['doEvoT'] and doPlt:
                cSys.plotResEvo(inpDat, self.dITp)
            SF.calcRunMeanM2Dfr(self.dITp, cSys, self.dDfrStats,
                                lTRd=self.lTRed, serRp=self.serRp)
            cSys.printRepDone(cRep, self.nRep, stTL)
        self.calcRepStatistics()
        self.plotResEvo(inpDat)

    def printDfrStats(self, lSStatsOut = GC.L_S_STATS_OUT):
        if self.dITp['printStats']:
            print(GC.S_PLUS*8, 'Simulation results:', GC.S_PLUS*8)
            for sStat in lSStatsOut:
                assert sStat in self.dDfrStats
                print(GC.S_DASH*8, sStat, GC.S_DASH*8)
                print(self.dDfrStats[sStat])
            print(GC.S_PLUS*80)

###############################################################################
