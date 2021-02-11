# -*- coding: utf-8 -*-
###############################################################################
# --- A_00__GenInput.py -------------------------------------------------------
###############################################################################
import Core.C_00__GenConstants as GC
# --- Input: Debug Info -------------------------------------------------------
levelDebugOut = 2   # level of debug output (0: no debug output)

# --- Input: General ----------------------------------------------------------
o_B_PltDt = 80      # offset yy for index in "B_yy_PlotterData" input files
nDigObj = 2         # number of digits reserved for all input objects
cMode = GC.M_STOCH  # GC.M_DETER / GC.M_STOCH

# --- Create general input dictionary -----------------------------------------
dictInpG = {# --- Input: Debug Info
            'lvlDbg': levelDebugOut,
            # --- Input: General
            'o_B_PltDt': o_B_PltDt,
            'nDigObj': nDigObj,
            'Mode': cMode}

###############################################################################
