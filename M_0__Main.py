# -*- coding: utf-8 -*-
###############################################################################
# --- M_0__Main.py ------------------------------------------------------------
###############################################################################
import Core.C_00__GenConstants as GC
import Core.F_00__GenFunctions as GF
import Core.F_01__SpcFunctions as SF
import Core.F_02__PltFunctions as PF
import Core.F_03__OTpFunctions as TF
# import Core.F_04__MainFunctions as MF

from Control.A_00__GenInput import dictInpG
from Core.I_01__InpData import InputData
from Core.O_99__Simulation import Simulation

# ### MAIN ####################################################################
startTime = GF.startSimu()
# -----------------------------------------------------------------------------
print('='*80, '\n', GC.S_DASH*33, 'M_0__Main.py', GC.S_DASH*33, '\n')
inDG = InputData(dictInpG)
inDG.addObjTps(GC.S_D_OBJINP)
print('Added object types.')
# -----------------------------------------------------------------------------
# cInpFrames = InputFrames(inDG)
# print(cInpFrames.lSCpTpL)
# cInpFrames.printDSCpSL()
# cInpFrames.printDSCpTp()
# cInpFrames.printDNCpObj()
# cInpFrames.printDParCnc()
# cInpFrames.printDTpRct()
# cInpFrames.printDClRct()
# cInpFrames.printDRct()
# cInpFrames.printDCpDepOnSMoCnc()
# cInpFrames.printDSMoCncDepOnCp()
# cInpFrames.printDOthInpV()

cSimulation = Simulation(inDG)
# nRep, doPlt = cSimulation.dITp['nReps'], cSimulation.dITp['doPlots']
# dDfrRunV = {}
# for cRep in range(1, nRep + 1):
#     print(GC.S_PLUS*8, 'Starting repetition', cRep, 'of', nRep)
#     cSystem = System(inDG, cInpFrames, cRp=cRep)
#     if cSimulation.dITp['doEvoT']:
#         cSystem.evolveOverTime(inDG, cRp=cRep, doPlots=doPlt)
#     if doPlt:
#         sFR = cSystem.dITp['sF_Obj'] + GC.S_USC + GC.S_REP + str(cRep)
#         cSystem.plotResEvo(cSimulation, cRp=cRep, sFRes=sFR, overWr=False)
#     SF.calcRunMeanM2Dfr(dDfrRunV, dfrResRed, cCt=cRep)
#     dParPlt = cSystem.dITp[GC.S_D_PLT][GC.S_CP_CNC]
#     for cK, cT in dParPlt['dlSY'].items():
#         dPPltF = TF.getDPFPltEvo(inDG.dI, cSimulation.dITp, cK, dMS=cT[2])
#         PF.plotEvo(dParPlt, dDfrRunV[GC.S_MEAN], dPPltF, cInpFrames.dSCpSL,
#                    tDat=cT[:2], overWr=True)
#     cSystem.printNCompObjSys()
#     # cSystem.printAllCompObjSys()
#     cSystem.printSMo()
#     # cSystem.printCncSMo()

#     cSystem.printFinalSimuTime()
#     print(GC.S_PLUS*8, 'Finished repetition', cRep, 'of', nRep)

# -----------------------------------------------------------------------------

print(GC.S_DASH*80)
GF.endSimu(startTime)

###############################################################################
