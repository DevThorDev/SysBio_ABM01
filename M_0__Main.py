# -*- coding: utf-8 -*-
###############################################################################
# --- M_0__Main.py ------------------------------------------------------------
###############################################################################
import Core.C_00__GenConstants as GC
import Core.F_00__GenFunctions as GF

from Control.A_00__GenInput import dictInpG
from Core.I_01__InpData import InputData
from Core.O_99__Simulation import Simulation
# TEMP (BEGIN)
from Core.O_80__PlotterSysSim import PlotterSysSim
from Core.O_90__PlotterData import PlotterData
# TEMP (END)

# ### MAIN ####################################################################
startTime = GF.startSimu()
# -----------------------------------------------------------------------------
print('='*80 + '\n' + GC.S_DASH*33, 'M_0__Main.py', GC.S_DASH*33 + '\n')
inDG = InputData(dictInpG)
inDG.addObjTps(GC.S_D_OBJINP)
print('Added object types.')
# -----------------------------------------------------------------------------
cSimulation = Simulation(inDG)
# cSimulation.runSimulation(inDG)
# cSimulation.printDfrStats()
# TEMP (BEGIN)
# for cITp in list(range(81, 87)):
#     # print('*'*8, 'Plotter data (type =', str(cITp) + ')', '*'*8)
#     cPltD = PlotterData(inDG, iTp=cITp)
#     # cPltD.printData()
#     cPltrSysSim = PlotterSysSim(inDG, cSimulation.inFr, cPltD, cOp=GC.S_SUM_GR,
#                                 cRp=2)
#     print(cPltrSysSim)
#     cPltrSysSim.printContent()
#     print('Plot name:', cPltrSysSim.pltDtI.sPltNm)
cSimulation.runSimulation(inDG)

# TEMP (END)
# -----------------------------------------------------------------------------
GF.endSimu(startTime)

###############################################################################
