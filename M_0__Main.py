# -*- coding: utf-8 -*-
###############################################################################
# --- M_0__Main.py ------------------------------------------------------------
###############################################################################
from numpy.random import default_rng as RNG

import Core.C_00__GenConstants as GC
import Core.F_00__GenFunctions as GF
import Core.F_04__MainFunctions as MF

from Control.A_00__GenInput import dictInpG
from Core.C_00__GenConstants import NMD_OBJINP
from Core.I_01__InpData import InputData

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
numStates = 2
dVStoch = {GC.ID_NO3_1M: {GC.S_CONC_INI: RNG().uniform(4.6, 5.8, numStates),
                          GC.S_PER_CONC_CH: RNG().uniform(10, 200, numStates)},
           GC.ID_H2PO4_1M: {GC.S_CONC_INI: RNG().uniform(1.7, 2.2, numStates)}}

MF.evolveOverTime(inDG, numSta = numStates, ddVOvwr = dVStoch)
    
# -----------------------------------------------------------------------------

print('-'*80)
GF.endSimu(startTime)

###############################################################################
