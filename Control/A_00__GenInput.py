# -*- coding: utf-8 -*-
###############################################################################
# --- A_00__GenInput.py -------------------------------------------------------
###############################################################################
import os

import Core.C_00__GenConstants as GC

# --- Input: Debug Info -------------------------------------------------------
levelDebugOut = 2   # level of debug output (0: no debug output)

# --- Input: Flow control -----------------------------------------------------
doEvoT = True
doPlots = True
tStart = 0                  # 0
tMax = 1.                  # 10.
maxTS = 10000000            # 10000000
minDispTS = 0
modDispTS = 10000           # 10000
assert tMax >= tStart and maxTS > 0

# --- Input: General ----------------------------------------------------------
nDigObj = 2         # number of digits reserved for all input objects
cMode = GC.M_STOCH  # GC.M_DETER / GC.M_STOCH
cSep = GC.SEP_STD

# --- Input: Names of paths, directories and files ----------------------------
sPInD = os.path.join('..', '..', '11_SysBio01_ABM01', '20_InputData')
sPRes = os.path.join('..', '..', '11_SysBio01_ABM01', '40_ModelResults')
sPPlt = os.path.join('..', '..', '11_SysBio01_ABM01', '50_ModelPlots')

dSFInD = {GC.S_00: (GC.S_00 + GC.S_USC + 'Strings', 1),
          GC.S_01: (GC.S_01 + GC.S_USC + 'InitialSysComp', 1),
          GC.S_02: (GC.S_02 + GC.S_USC + 'ConcSMo', 0),
          GC.S_03: (GC.S_03 + GC.S_USC + 'WeightsReactionTypes', 1),
          GC.S_04: (GC.S_04 + GC.S_USC + 'WeightsReactions', 1),
          GC.S_05: (GC.S_05 + GC.S_USC + 'CompDependOnSMoConc', 1),
          GC.S_06: (GC.S_06 + GC.S_USC + 'SMoConcDependOnComp', 1),
          GC.S_07: (GC.S_07 + GC.S_USC + 'OtherInputValues', 1)}

dictInpG = {# --- Input: Debug Info
            'lvlDbg': levelDebugOut,
            # --- Input: Flow control
            'doEvoT': doEvoT,
            'doPlots': doPlots,
            'tStart': tStart,
            'tMax': tMax,
            'maxTS': maxTS,
            'minDispTS': minDispTS,
            'modDispTS': modDispTS,
            # --- Input: General
            'nDigObj': nDigObj,
            'Mode': cMode,
            'cSep': cSep,
            # --- Input: Names of paths, directories and files
            'sPInD': sPInD,
            'sPRes': sPRes,
            'sPPlt': sPPlt,
            'dSFInD': dSFInD}

###############################################################################
