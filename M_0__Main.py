# -*- coding: utf-8 -*-
###############################################################################
# --- M_0__Main.py ------------------------------------------------------------
###############################################################################
import Core.F_00__GenFunctions as GF
import Core.F_01__SpcFunctions as SF
# import Core.F_04__MainFunctions as MF

from Control.A_00__GenInput import dictInpG
from Core.C_00__GenConstants import S_D_OBJINP, S_DASH, S_PLUS
from Core.I_01__InpData import InputData
from Core.I_02__InpFrames import InputFrames
from Core.O_99__System import System

# ### MAIN ####################################################################
startTime = GF.startSimu()
# -----------------------------------------------------------------------------
print('='*80, '\n', S_DASH*33, 'M_0__Main.py', S_DASH*33, '\n', S_DASH*80)
inDG = InputData(dictInpG)
inDG.addObjTps(S_D_OBJINP)
print('Added object types.')
# -----------------------------------------------------------------------------
cInpFrames = InputFrames(inDG)
# print(cInpFrames.lSCpTpL)
# cInpFrames.printDSCpSL()
# cInpFrames.printDSCpTp()
# cInpFrames.printDNCpObj()
cInpFrames.printDParCnc()
# cInpFrames.printDTpRct()
# cInpFrames.printDClRct()
# cInpFrames.printDRct()
# cInpFrames.printDCpDepOnSMoCnc()
# cInpFrames.printDSMoCncDepOnCp()
# cInpFrames.printDOthInpV()

for cRep in range(1, inDG.dI['nReps'] + 1):
    print(S_PLUS*8, 'Starting repetition', cRep, 'of', inDG.dI['nReps'])
    cSystem = System(inDG, cInpFrames)
    if cSystem.dIG['doEvoT']:
        cSystem.evolveOverTime(inDG, doPlots = cSystem.dIG['doPlots'])
    if cSystem.dIG['doPlots']:
        cSystem.plotResEvo(sFRes = cSystem.dITp['sF_SysEvo'], overWr = False)
    dResRed = SF.reduceData(inDG.dI, cSystem.dResEvo)
    cSystem.printNCompObjSys()
    # cSystem.printAllCompObjSys()
    cSystem.printSMo()
    # cSystem.printCncSMo()

    cSystem.printFinalSimuTime()
    print(S_PLUS*8, 'Finished repetition', cRep, 'of', inDG.dI['nReps'])

# -----------------------------------------------------------------------------

print(S_DASH*80)
GF.endSimu(startTime)

###############################################################################
