# -*- coding: utf-8 -*-
###############################################################################
# --- A_00__GenInput.py -------------------------------------------------------
###############################################################################
import Core.C_00__GenConstants as GC

# --- Input: Debug Info -------------------------------------------------------
levelDebugOut = 2   # level of debug output (0: no debug output)

# --- Input: General ----------------------------------------------------------
nDigObj = 3         # number of digits reserved for all input objects
cMode = GC.M_DETER  # GC.M_DETER / GC.M_STOCH

# --- Input: Names and directories --------------------------------------------
nDPlots = 'Plots'                   # name of directory for plots

# --- create input dictionary -------------------------------------------------
dictInpG = {# --- Input: Debug Info
            'lvlDbg': levelDebugOut,
            # --- Input: General
            'nDigObj': nDigObj,
            'Mode': cMode,
            # --- Input: Names and directories
            'nDPlots': nDPlots}

###############################################################################
