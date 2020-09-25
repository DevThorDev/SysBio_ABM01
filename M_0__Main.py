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
# cSystem = MF.iniSystem(inDG)
# cSystem.printSystem()

# -----------------------------------------------------------------------------
# cState, cSystem = MF.initialState(inDG)
# # cSystem.printSystemDetails()
# print('~'*30, 'INITIAL STATE', '~'*30)
# cState.printStateDetails()
# print('~'*30, 'STATE A', '~'*30)
# cState.to_St_A_Int_AT5G49770_NRT2p1(inDG)
# cState.printStateDetails()
# print('~'*30, 'STATE B', '~'*30)
# cState.to_St_B_Trans_AT5G49770_NRT2p1(inDG)
# cState.printStateDetails()
# print('~'*30, 'STATE C', '~'*30)
# cState.to_St_C_Int_NAR2p1_NRT2p1(inDG)
# cState.printStateDetails()
# print('~'*30, 'STATE D', '~'*30)
# cState.to_St_D_Trans_NAR2p1_NRT2p1(inDG)
# cState.printStateDetails()

# -----------------------------------------------------------------------------
cState, cSystem = MF.initialState(inDG)
for curTS in range(1, inDG.dI['maxTS'] + 1):
    cState.changeConcSMo(curTS)
    print('--- Current time step:', curTS)
    cState.printDCnc()
    
# -----------------------------------------------------------------------------

print('-'*80)
GF.endSimu(startTime)

###############################################################################
