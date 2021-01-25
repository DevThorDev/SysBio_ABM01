# -*- coding: utf-8 -*-
###############################################################################
# --- O_99__Simulation.py -----------------------------------------------------
###############################################################################
# import pprint

import Core.C_00__GenConstants as GC
import Core.F_00__GenFunctions as GF
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
        self.inpFrames = InputFrames(self.dITp)
        # print('Initiated "Simulation" object.')

    def runSimulation(self, inpDat):
        nRep, doPlt, dDfrRunV = self.dITp['nReps'], self.dITp['doPlots'], {}
        for cRep in range(1, nRep + 1):
            print(GC.S_PLUS*8, 'Starting repetition', cRep, 'of', nRep)
            cSys = System(inpDat, self.inpFrames, cRp=cRep)
            if self.dITp['doEvoT']:
                cSys.evolveOverTime(inpDat, cRp=cRep, doPlots=doPlt)
            if doPlt:
                cSys.plotResEvo(sPRes=self.dITp['sPRes'], cRp=cRep,
                                overWr=False)
            TF.calcRunMeanM2Dfr(self.dITp, cSys, dDfrRunV, cCt=cRep)
            self.plotResEvo(cSys, dDfrRunV)
            cSys.printNCompObjSys()
            # cSys.printAllCompObjSys()
            cSys.printSMo()
            # cSys.printCncSMo()
            cSys.printFinalSimuTime()
            print(GC.S_PLUS*8, 'Finished repetition', cRep, 'of', nRep)
        self.calcRepStatistics(dDfrRunV, nRp=nRep)

    def plotResEvo(self, cSys, dDfrRV):
        for cK, cT in cSys.dParPlt['dlSY'].items():
            dPPltF = TF.getDPFPltEvo(self.dITp, tKey=cK, dMS=cT[2])
            PF.plotEvo(cSys.dParPlt, dDfrRV[GC.S_MEAN], dPPltF,
                       self.inpFrames.dSCpSL, tDat=cT[:2], overWr=True)

    def calcRepStatistics(self, dDfrRV, nRp=0, sFExt=GC.S_EXT_CSV):
        sPRs, sDSim = self.dITp['sPRes'], self.dITp['sD_Obj']
        SF.calcMeanVarSDDfr(dDfrRV, nRp=nRp)
        for s, d in dDfrRV.items():
            sF = self.dITp['sFRes'] + GC.S_USC + str(s) + '.' + sFExt
            d.to_csv(GF.joinToPath([sPRs, sDSim], sF), sep=self.dITp['cSep'])

    def printSimuData(self):
        print(GC.S_STAR*8, 'Simulation data:',
              GC.S_STAR*8)
        print(GC.S_STAR*80)

###############################################################################
