# -*- coding: utf-8 -*-
###############################################################################
# --- M_0__Main.py ------------------------------------------------------------
###############################################################################
import Core.F_00__GenFunctions as GF
import Core.F_04__MainFunctions as MF

from Control.A_00__GenInput import dictInpG
from Core.C_00__GenConstants import NMD_OBJINP
from Core.I_01__InpData import InputData

# from Core.O_02__Protein import Kinase, Phosphatase, LargeProtein, SmallProtein
# from Core.O_03__Metabolite import LargeMolecule, SmallMolecule
# from Core.O_80__Interaction import (Interaction, Phosphorylation,
#                                     Dephosphorylation)

# ### MAIN ####################################################################
startTime = GF.startSimu()
# -----------------------------------------------------------------------------
print('='*80, '\n', '-'*33, 'M_0__Main.py', '-'*33, '\n', '-'*80)
inDG = InputData(dictInpG)
inDG.addObjTps(NMD_OBJINP)
print('Added object types.')
# -----------------------------------------------------------------------------
cSystem = MF.iniSystem(inDG)
cSystem.printSystem()

# -----------------------------------------------------------------------------
MF.initialState(inDG)

# -----------------------------------------------------------------------------

print('-'*80)
GF.endSimu(startTime)

###############################################################################
