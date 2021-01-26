# -*- coding: utf-8 -*-
###############################################################################
# --- O_99__Simulation.py -----------------------------------------------------
###############################################################################
# import pprint

import Core.C_00__GenConstants as GC
import Core.F_01__SpcFunctions as SF
import Core.F_02__PltFunctions as PF
import Core.F_03__OTpFunctions as TF

from Core.I_02__InpFrames import InputFrames
from Core.O_00__Base import Base
from Core.O_95__System import System

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class Simulation(Base):
    def __init__(self, inpDat, iTp=99):
        super().__init__(inpDat, iTp)
        self.idO = GC.ID_SIM
        self.descO = 'Simulation'
        self.inFr = InputFrames(self.dITp)
        self.sFRes = self.dITp['sFRes']
        self.dParPlt = self.dITp[GC.S_D_PLT][GC.S_CP_CNC]
        # print('Initiated "Simulation" object.')

    def runSimulation(self, inpDat):
        nRep, doPlt, dDfrRunV = self.dITp['nReps'], self.dITp['doPlots'], {}
        for cRep in range(1, nRep + 1):
            print(GC.S_PLUS*8, 'Starting repetition', cRep, 'of', nRep)
            cSys = System(inpDat, self.inFr, cRp=cRep)
            if self.dITp['doEvoT']:
                cSys.evolveOverTime(inpDat, self.dITp, cRp=cRep, doPlots=doPlt)
            if not self.dITp['doEvoT'] and doPlt:
                cSys.plotResEvo(self.dITp, cRp=cRep, overWr=True)
            TF.calcRunMeanM2Dfr(self.dITp, cSys, dDfrRunV, cCt=cRep)
            cSys.printFinalSimuTime()
            print(GC.S_PLUS*8, 'Finished repetition', cRep, 'of', nRep)
        self.plotResEvo(dDfrRunV)
        self.calcRepStatistics(dDfrRunV, nRp=nRep)

    def plotResEvo(self, dDfrRV):
        for cK, cT in self.dParPlt['dlSY'].items():
            dPPltF = TF.getDPFPltEvo(self.dITp, tKey=cK, dMS=cT[2])
            PF.plotEvo(self.dParPlt, dDfrRV[GC.S_MEAN], dPPltF,
                       self.inFr.dSCpSL, tDat=cT[:2], overWr=True)

    def calcRepStatistics(self, dDfrRV, nRp=0):
        SF.calcMeanVarSDDfr(dDfrRV, nRp=nRp)
        self.dDfrStats = dDfrRV
        for sStat, dfrStat in self.dDfrStats.items():
            TF.savePdDfr(self.dITp, dfrStat, [self.dITp['sD_Obj']],
                         self.sFRes + GC.S_USC + str(sStat), overWr=True)

    def printDfrStats(self, lSStatsOut = GC.L_S_STATS_OUT):
        print(GC.S_PLUS*8, 'Simulation results:', GC.S_PLUS*8)
        for sStat in lSStatsOut:
            assert sStat in self.dDfrStats
            print(GC.S_DASH*8, sStat, GC.S_DASH*8)
            print(self.dDfrStats[sStat])
        print(GC.S_PLUS*80)

###############################################################################
