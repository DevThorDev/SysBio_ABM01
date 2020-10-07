# -*- coding: utf-8 -*-
###############################################################################
# --- A_00__GenInput.py -------------------------------------------------------
###############################################################################
import os

import Core.C_00__GenConstants as GC

# --- Input: Debug Info -------------------------------------------------------
levelDebugOut = 2   # level of debug output (0: no debug output)

# # --- Input: Initial state ----------------------------------------------------
# sStIni = GC.S_ST_D_TRANS_NAR2P1_NRT2P1    # initial state ID string
#                                         # GC.S_ST_A_INT_AT5G49770_NRT2P1
#                                         # GC.S_ST_B_TRANS_AT5G49770_NRT2P1
#                                         # GC.S_ST_C_INT_NAR2P1_NRT2P1
#                                         # GC.S_ST_D_TRANS_NAR2P1_NRT2P1

# --- Input: Flow control -----------------------------------------------------
maxTS = 100                             # for the time step mode
tStart = 0                              # for the max time mode
tMax = 100.0                            # for the max time mode

# --- Input: General ----------------------------------------------------------
nDigObj = 3         # number of digits reserved for all input objects
cMode = GC.M_DETER  # GC.M_DETER / GC.M_STOCH
cSep = GC.SEP_STD

# --- Input: Names of paths, directories and files ----------------------------
sPRes = os.path.join('..', '..', '11_SysBio01_ABM01', '40_ModelResults')
sPPlt = os.path.join('..', '..', '11_SysBio01_ABM01', '50_ModelPlots')

# --- create input dictionary -------------------------------------------------
dictInpG = {# --- Input: Debug Info
            'lvlDbg': levelDebugOut,
            # --- Input: Flow control
            'maxTS': maxTS,
            'tStart': tStart,
            'tMax': tMax,
            # --- Input: General
            'nDigObj': nDigObj,
            'Mode': cMode,
            'cSep': cSep,
            # --- Input: Names of paths, directories and files
            'sPRes': sPRes,
            'sPPlt': sPPlt}

###############################################################################
