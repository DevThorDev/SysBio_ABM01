# -*- coding: utf-8 -*-
###############################################################################
# --- M_0__Main.py ------------------------------------------------------------
###############################################################################
import Core.F_00__GenFunctions as GF
# import Core.F_04__MainFunctions as MF

from Control.A_00__GenInput import dictInpG
from Core.C_00__GenConstants import S_D_OBJINP, S_DASH
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
# print(cInpFrames.dSCpSL)
# print(cInpFrames.dSCpTpS)
# print(cInpFrames.lSCpTpL)
# print(cInpFrames.dSCpTpL)
print(cInpFrames.dNCpObj)
# print(cInpFrames.dParCnc)
# cInpFrames.printDTpRct()
# cInpFrames.printDClRct()
# cInpFrames.printDRct()
# print(cInpFrames.dChgCncDep)
# print(cInpFrames.dCncChgSMo)
# for cKO in cInpFrames.dCncChgSMo:
#     print(list(cInpFrames.dCncChgSMo[cKO]))
# print(cInpFrames.dOthInpV)

cSystem = System(inDG, cInpFrames)
cSystem.printDICp()
if cSystem.dIG['doEvoT']:
    cSystem.evolveOverTime(inDG, doPlots = cSystem.dIG['doPlots'])
if cSystem.dIG['doPlots']:
    cSystem.plotResEvo(sFRes = cSystem.dITp['sF_SysEvo'], overWr = False)
cSystem.printNCompObjSys()
# cSystem.printAllCompObjSys()
cSystem.printSMo()
# cSystem.printCncSMo()

cSystem.printFinalSimuTime()

# -----------------------------------------------------------------------------

print(S_DASH*80)
GF.endSimu(startTime)

###############################################################################
