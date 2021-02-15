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
calcStats = True
doPlots = True
printStats = False
overWrCSV = True
overWrPDF = True
nReps = 3                   # 3 / 5 / 10
nTSRed = 500                # 500 / 200 / 100
tStart = 0                  # 0
tMax = 10.                  # 10.
maxTS = 10000000            # 10000000
minDispTS = 0               # 0
modDispTS = 10000           # 10000
assert tMax >= tStart and maxTS > 0

# --- list of index strings of plot data used for plots -----------------------
lIPltDat = [GC.S_01, GC.S_02, GC.S_03, GC.S_04, GC.S_05, GC.S_06]

# --- path, directory and file names ------------------------------------------
sDObj = GC.S_DIR_SIM
sFObj = GC.S_RES_SIM
sFNRp = GC.S_NUM_REP

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
       'calcStats': calcStats,
       'doPlots': doPlots,
       'printStats': printStats,
       'overWrCSV': overWrCSV,
       'overWrPDF': overWrPDF,
       'nReps': nReps,
       'nTSRed': nTSRed,
       'tStart': tStart,
       'tMax': tMax,
       'maxTS': maxTS,
       'minDispTS': minDispTS,
       'modDispTS': modDispTS,
       # --- list of index strings of plot data used for plots
       'lIPltDat': lIPltDat,
       # --- path, directory and file names
       'sDObj': sDObj,
       'sFObj': sFObj,
       'sFNRp': sFNRp,
       'sPInD': sPInD,
       'sPRes': sPRes,
       # 'sPPlt': sPPlt,
       'dSFInD': dSFInD}

###############################################################################
