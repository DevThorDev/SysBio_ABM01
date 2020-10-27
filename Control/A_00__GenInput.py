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
tMax = 100.
maxTS = 10000000
minDispTS = 0
modDispTS = 10000

# --- Input: General ----------------------------------------------------------
nDigObj = 2         # number of digits reserved for all input objects
cMode = GC.M_STOCH  # GC.M_DETER / GC.M_STOCH
cSep = GC.SEP_STD

# --- Input: Names of paths, directories and files ----------------------------
sPRes = os.path.join('..', '..', '11_SysBio01_ABM01', '40_ModelResults')
sPPlt = os.path.join('..', '..', '11_SysBio01_ABM01', '50_ModelPlots')

# --- Input: Constants --------------------------------------------------------
dS_St = GC.DS_ST
dS_StCh = GC.DS_STCH

# --- create input dictionary -------------------------------------------------
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
            'sPRes': sPRes,
            'sPPlt': sPPlt,
            # --- Input: Constants
            'dS_St': dS_St,
            'dS_StCh': dS_StCh}

###############################################################################
