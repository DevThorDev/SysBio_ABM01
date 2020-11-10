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
tStart = 0
tMax = 5.
maxTS = 10000000
minDispTS = 0
modDispTS = 10000

# --- Input: General ----------------------------------------------------------
nDigObj = 2         # number of digits reserved for all input objects
cMode = GC.M_STOCH  # GC.M_DETER / GC.M_STOCH
cSep = GC.SEP_STD

# --- Input: Names of paths, directories and files ----------------------------
sPInD = os.path.join('..', '..', '11_SysBio01_ABM01', '20_InputData')
sPRes = os.path.join('..', '..', '11_SysBio01_ABM01', '40_ModelResults')
sPPlt = os.path.join('..', '..', '11_SysBio01_ABM01', '50_ModelPlots')

dSFInD = {GC.S_00: (GC.S_00 + GC.S_USC + 'Strings', 1),
          GC.S_01: (GC.S_01 + GC.S_USC + 'InitialSysComponents', 1),
          GC.S_02: (GC.S_02 + GC.S_USC + 'Conc', 0),
          GC.S_03: (GC.S_03 + GC.S_USC + 'Weights4Rct', 1),
          GC.S_04: (GC.S_04 + GC.S_USC + 'Reactions', 1),
          GC.S_05: (GC.S_05 + GC.S_USC + 'CompIncidDependencies', 1),
          GC.S_06: (GC.S_06 + GC.S_USC + 'SMoConcDependencies', 1)}

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
