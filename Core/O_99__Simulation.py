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

    # def getDDfrRed(self, inpDat):
    #     dDfrRed = {}
    #     # dDfrPlt, dDfrI, d4LgSim = {}, {}, {}
    #     for cRp in range(1, self.nRp + 1):
    #         cSys, sD = System(inpDat, self.inFr, cRp=cRp), self.dITp['sDObj']
    #         dDfrRed[cRp] = SF.loadPdDfr(self.dITp, [sD], cSys.sFRed, iCol=0)
    #         # TEMP - plotting part (BEGIN)
    #         if dPltG['dCHdGr'] is not None: # collapse if groups were specif.
    #             dDfrT, d4Lg = collapseColumns(dPltG, cDfr, sLX, lSLY, sOp)
    #             cDfr = dDfrT[GC.S_CENT]
    #             d4LgSim.update(d4Lg)
    #         else:                           # reduce if no groups were specif.
    #             cDfr = cDfr.loc[:, [GC.S_TIME] + dPltG['lSCpCnc']]
    #         SF.updateDictDfr(cDfr, self.dDfrStats, serRp=serRp)
    #         # TEMP - plotting part (END)
    #     return dDfrRed

    def doReps(self, inpDat):
        stTL = GF.startRepLoop()
        for cRp in range(1, self.nRp + 1):
            print(GC.S_PLUS*8, 'Starting repetition', cRp, 'of', self.nRp)
            cSys = System(inpDat, self.inFr, cRp=cRp)
            if cSys.dITp['doEvoT']:
                cSys.evolveOverTime(inpDat, self.dITp)
            else:
                lD, sFR = [cSys.dITp['sDObj']], cSys.sFRes
                cSys.dfrResEvo = SF.loadPdDfr(self.dITp, lD=lD, sF=sFR, iCol=0)
            if not cSys.dITp['doEvoT'] and cSys.dITp['doPlots']:
                cSys.plotResEvo(inpDat, self.dITp)
            SF.calcDfrRunStats(self.dITp, cSys, self.dDfrStats, self.dDfrRed,
                               lTRd=self.lTRed, serRp=self.serRp, cRp=cRp)
            cSys.printRepDone(cRp, self.nRp, stTL)

    def saveDictDfrStatsNoGrp(self):
        for sStat in GC.L_S_STATS_OUT:
            sF = self.sFRes + GC.S_USC + str(sStat) + GC.S_USC + GC.S_NO_GR
            SF.savePdDfr(self.dITp, self.dDfrStats[sStat],
                         lD=[self.dITp['sDObj'], sStat], sF=sF,
                         overWr=self.dITp['overWrCSV'])

    def calcRepStatistics(self, inpDat):
        # re-calc mean and M2 of self.dDfrStats if any dictionary is None
        if self.dDfrStats is None or self.dDfrRed is None:
            for cRp in range(1, self.nRp + 1):
                cSys = System(inpDat, self.inFr, cRp=cRp)
                SF.calcDfrRunStats(self.dITp, cSys, self.dDfrStats,
                                   self.dDfrRed, lTRd=self.lTRed,
                                   serRp=self.serRp, cRp=cRp)
        # calc final statistics and store them in self.dDfrStats
        SF.calcDfrFinStats(self.dDfrStats, serRp=self.serRp)
        SF.saveSerRep(self.dITp, self.dDfrStats[GC.S_MEAN], self.serRp,
                      lD=[self.dITp['sDObj']])
        # save the final statistics (for all components, without grouping)
        self.saveDictDfrStatsNoGrp()

    def calcGroupStats(self, inpDat, PltD, dDfrStats, dSHdCY, sOp):
        for cRp in range(1, self.nRp + 1):
            Pltr = PlotterSysSim(inpDat, self.inFr, PltD, sOp, cRp=cRp)
            t = SF.collapseColumns(PltD, self.dDfrRed[cRp], Pltr.sHdCX,
                                   Pltr.lSHdCY, sOp)
            dfrRed, dSY = t
            SF.updateDictDfr(dfrRed, dDfrStats, serRp=self.serRp)
            dSHdCY.update(dSY)
        SF.calcDfrFinStats(dDfrStats, serRp=self.serRp)

    def plotGroups(self, inpDat, PltD):
        for sOp in PltD.lSOp:
            dDfrStats, dSHdCY, sDObj = {}, {}, self.dITp['sDObj']
            self.calcGroupStats(inpDat, PltD, dDfrStats, dSHdCY, sOp)
            Pltr = PlotterSysSim(inpDat, self.inFr, PltD, sOp)
            Pltr.setPropAndPlot(PltD, dDfrStats, dSHdCY, self.serRp,
                                sDSim=sDObj, tMax=self.dITp['tMax'], sOp=sOp)
            SF.saveDictDfr(self.dITp, Pltr.dDfrPlt, lK=GC.L_S_STATS_OUT,
                           sFEnd=GF.getFNoExt(Pltr.pPltF))

    def plotSimRes(self, inpDat):
        for sI in self.dITp['lIPltDat']:
            PltD = PlotterData(inpDat, iTp=int(sI)+self.dIG['o_B_PltDt'])
            if PltD.lSOp is not None and PltD.dCHdGr is not None:   # groups
                self.plotGroups(inpDat, PltD)

    def runSimulation(self, inpDat):
        self.doReps(inpDat)
        if self.dITp['calcStats'] or self.dITp['doPlots']:
            self.calcRepStatistics(inpDat)
            if self.dITp['doPlots']:
                self.plotSimRes(inpDat)

    def printDfrStats(self, lSStatsOut=GC.L_S_STATS_OUT):
        if self.dITp['printStats']:
            print(GC.S_PLUS*8, 'Simulation results:', GC.S_PLUS*8)
            for sStat in lSStatsOut:
                assert sStat in self.dDfrStats
                print(GC.S_DASH*8, sStat, GC.S_DASH*8)
                print(self.dDfrStats[sStat])
            print(GC.S_PLUS*80)

###############################################################################
