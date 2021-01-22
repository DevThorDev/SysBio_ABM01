# -*- coding: utf-8 -*-
###############################################################################
# --- O_99__Simulation.py -----------------------------------------------------
###############################################################################
# import pprint

import Core.C_00__GenConstants as GC
# import Core.F_00__GenFunctions as GF
# import Core.F_02__PltFunctions as PF
# import Core.F_03__OTpFunctions as TF

from Core.O_00__Base import Base

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class Simulation(Base):
    def __init__(self, inpDat, iTp = 99):
        super().__init__(inpDat, iTp)
        self.idO = GC.ID_SIM
        self.descO = 'Simulation'
        # print('Initiated "Simulation" object.')

    def printSimuData(self):
        print(GC.S_STAR*8, 'Simulation data:',
              GC.S_STAR*8)
        print(GC.S_STAR*80)

###############################################################################
