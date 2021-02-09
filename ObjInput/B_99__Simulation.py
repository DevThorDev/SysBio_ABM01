# -*- coding: utf-8 -*-
###############################################################################
# --- B_99__Simulation.py -----------------------------------------------------
###############################################################################
import os

import Core.C_00__GenConstants as GC

# --- general -----------------------------------------------------------------
strOType = 'Simulation'
strNSpec = 'Simulation including all repetitions'
strCS = GC.ID_SIM
strCL = GC.S_CL_SIMULATION

# --- flow control ------------------------------------------------------------
doEvoT = True
doPlots = True
printStats = False
nReps = 3                   # 3 / 5 / 10
nTSRed = 500                # 500 / 200 / 100
tStart = 0                  # 0
tMax = 0.2                  # 10.
maxTS = 10000000            # 10000000
minDispTS = 0               # 0
modDispTS = 10000           # 10000
assert tMax >= tStart and maxTS > 0

# --- path, directory and file names ------------------------------------------
sD_Obj = GC.S_DIR_SIM
sF_Obj = GC.S_RES_SIM
sF_NRp = GC.S_NUM_REP

sPInD = os.path.join('..', '..', '11_SysBio01_ABM01', '20_InputData')
sPRes = os.path.join('..', '..', '11_SysBio01_ABM01', '40_ModelResults')

dSFInD = {GC.S_00: (GC.S_00 + GC.S_USC + 'Strings', 1),
          GC.S_01: (GC.S_01 + GC.S_USC + 'InitialSysComp', 1),
          GC.S_02: (GC.S_02 + GC.S_USC + 'ConcSMo', 0),
          GC.S_03: (GC.S_03 + GC.S_USC + 'WeightsReactionTypes', 1),
          GC.S_04: (GC.S_04 + GC.S_USC + 'WeightsReactions', 2),
          GC.S_05: (GC.S_05 + GC.S_USC + 'CompDependOnSMoConc', 1),
          GC.S_06: (GC.S_06 + GC.S_USC + 'SMoConcDependOnComp', 1),
          GC.S_07: (GC.S_07 + GC.S_USC + 'OtherInputValues', 1)}

# --- create input dictionary -------------------------------------------------
dIO = {# --- general
       'strOType': strOType,
       'strNSpec': strNSpec,
       'strCS': strCS,
       'strCL': strCL,
       # --- flow control
       'doEvoT': doEvoT,
       'doPlots': doPlots,
       'printStats': printStats,
       'nReps': nReps,
       'nTSRed': nTSRed,
       'tStart': tStart,
       'tMax': tMax,
       'maxTS': maxTS,
       'minDispTS': minDispTS,
       'modDispTS': modDispTS,
       # --- path, directory and file names
       'sD_Obj': sD_Obj,
       'sF_Obj': sF_Obj,
       'sF_NRp': sF_NRp,
       'sPInD': sPInD,
       'sPRes': sPRes,
       # 'sPPlt': sPPlt,
       'dSFInD': dSFInD}

###############################################################################
