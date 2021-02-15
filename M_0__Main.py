# -*- coding: utf-8 -*-
###############################################################################
# --- M_0__Main.py ------------------------------------------------------------
###############################################################################
import Core.C_00__GenConstants as GC
import Core.F_00__GenFunctions as GF

from Control.A_00__GenInput import dictInpG
from Core.I_01__InpData import InputData
from Core.O_99__Simulation import Simulation

# ### MAIN ####################################################################
startTime = GF.startSimu()
# -----------------------------------------------------------------------------
print('='*80 + '\n' + GC.S_DASH*33, 'M_0__Main.py', GC.S_DASH*33 + '\n')
inDG = InputData(dictInpG)
inDG.addObjTps(GC.S_D_OBJINP)
print('Added object types.')
# -----------------------------------------------------------------------------
cSimulation = Simulation(inDG)
cSimulation.runSimulation(inDG)
cSimulation.printDfrStats()
# -----------------------------------------------------------------------------
GF.endSimu(startTime)

###############################################################################
