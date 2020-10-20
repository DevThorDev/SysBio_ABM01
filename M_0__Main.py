# -*- coding: utf-8 -*-
###############################################################################
# --- M_0__Main.py ------------------------------------------------------------
###############################################################################
import Core.F_00__GenFunctions as GF
# import Core.F_04__MainFunctions as MF

from Control.A_00__GenInput import dictInpG
from Core.C_00__GenConstants import S_D_OBJINP
from Core.I_01__InpData import InputData
from Core.O_99__System import System

# ### MAIN ####################################################################
startTime = GF.startSimu()
# -----------------------------------------------------------------------------
print('='*80, '\n', '-'*33, 'M_0__Main.py', '-'*33, '\n', '-'*80)
inDG = InputData(dictInpG)
inDG.addObjTps(S_D_OBJINP)
print('Added object types.')
# -----------------------------------------------------------------------------
cSystem = System(inDG)
if cSystem.dIG['doEvoT']:
    cSystem.evolveOverTime(doPlots = cSystem.dIG['doPlots'])
if cSystem.dIG['doPlots']:
    cSystem.plotResEvo(sFRes = cSystem.dITp['sF_SysEvo'], overWr = False)
    # cSystem.plotResEvo(sFRes = 'SysEvo__T100__Sc050__0p1_50', overWr = False)
cSystem.printNStateObjSys()
# cSystem.printAllStateObjSys()

# -----------------------------------------------------------------------------

print('-'*80)
GF.endSimu(startTime)

###############################################################################
