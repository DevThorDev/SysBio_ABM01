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
        self.dDfrStats = None
        self.hT = self.dITp['tMax']/(2*self.dITp['nTSRed'])
        self.lTRed = [k*self.hT for k in range(1, 2*self.dITp['nTSRed'], 2)]
        self.serRp = GF.iniPdSer(nEl=len(self.lTRed), v=0, sNm=GC.S_NUM_REP,
                                 dTp=int)
        self.sFRes = self.dITp['sFObj']
        # print('Initiated "Simulation" object.')

    def getDDfrRed(self, inpDat):
        dDfrRed = {}
        # dDfrPlt, dDfrI, d4LgSim = {}, {}, {}
        for cRp in range(1, self.dITp['nReps'] + 1):
            cSys, sD = System(inpDat, self.inFr, cRp=cRp), self.dITp['sDObj']
            dDfrRed[cRp] = SF.loadPdDfr(self.dITp, [sD], cSys.sFRed, iCol=0)
            # TEMP - plotting part (BEGIN)
            if dPltG['dCHdGr'] is not None: # collapse if groups were specif.
                dDfrT, d4Lg = collapseColumns(dPltG, cDfr, sLX, lSLY, sOp)
                cDfr = dDfrT[GC.S_CENT]
                d4LgSim.update(d4Lg)
            else:                           # reduce if no groups were specif.
                cDfr = cDfr.loc[:, [GC.S_TIME] + dPltG['lSCpCnc']]
            SF.updateDictDfr(cDfr, self.dDfrStats, serRp=serRp)
            # TEMP - plotting part (END)
        return dDfrRed

    def getProcData4Plt(self, pFDat, saveDDfr=False):
        SF.calcStatsDfr(self.dDfrStats, serRp=self.serRp)
        # if dPltG['dCHdGr'] is not None:     # save data if groups were specified
        if saveDDfr:     # save data if groups were specified
            SF.saveDictDfr(self.dITp, self.dDfrStats, lK=GC.L_S_STATS_OUT,
                           sFEnd=GF.getFNoExt(pFDat))

    def plotSimRes(self, inpDat):
        dDfrRed = {}
        for cRp in range(1, self.dITp['nReps'] + 1):
            cSys, sD = System(inpDat, self.inFr, cRp=cRp), self.dITp['sDObj']
            dDfrRed[cRp] = SF.loadPdDfr(self.dITp, [sD], cSys.sFRed, iCol=0)
        Pltr = PlotterSysSim(inpDat, self.inFr)
        Pltr.plotSimRes(self.dITp, self.dDfrStats, dDfrRed, serRp=self.serRp)

    def calcRepStatistics(self):
        SF.calcStatsDfr(self.dDfrStats, serRp=self.serRp)
        SF.saveSerRep(self.dITp, self.dDfrStats[GC.S_MEAN], self.serRp,
                      lD=[self.dITp['sDObj']])
        for sStat in GC.L_S_STATS_OUT:
            sF = self.sFRes + GC.S_USC + str(sStat) + GC.S_USC + GC.S_NO_GR
            SF.savePdDfr(self.dITp, self.dDfrStats[sStat],
                         lD=[self.dITp['sDObj'], sStat], sF=sF)

    def doReps(self, inpDat):
        stTL, self.dDfrStats = GF.startRepLoop(), {}
        for cRep in range(1, self.nRep + 1):
            print(GC.S_PLUS*8, 'Starting repetition', cRep, 'of', self.nRep)
            cSys = System(inpDat, self.inFr, cRp=cRep)
            if cSys.dITp['doEvoT']:
                cSys.evolveOverTime(inpDat, self.dITp)
            if not cSys.dITp['doEvoT'] and cSys.dITp['doPlots']:
                cSys.plotResEvo(inpDat, self.dITp)
            SF.calcRunStatsDfr(self.dITp, cSys, self.dDfrStats,
                               lTRd=self.lTRed, serRp=self.serRp)
            cSys.printRepDone(cRep, self.nRep, stTL)

    def runSimulation(self, inpDat):
        self.doReps(inpDat)
        if self.dITp['calcStats'] or self.dITp['doPlots']:
            self.calcRepStatistics()
            if self.dITp['doPlots']:
                self.plotSimRes(inpDat)

    def printDfrStats(self, lSStatsOut = GC.L_S_STATS_OUT):
        if self.dITp['printStats']:
            print(GC.S_PLUS*8, 'Simulation results:', GC.S_PLUS*8)
            for sStat in lSStatsOut:
                assert sStat in self.dDfrStats
                print(GC.S_DASH*8, sStat, GC.S_DASH*8)
                print(self.dDfrStats[sStat])
            print(GC.S_PLUS*80)

###############################################################################
