# -*- coding: utf-8 -*-
###############################################################################
# --- A_00__GenInput.py -------------------------------------------------------
###############################################################################
import Core.C_00__GenConstants as GC

# --- Input: Debug Info -------------------------------------------------------
levelDebugOut = 2   # level of debug output (0: no debug output)

# --- Input: Initial state ----------------------------------------------------
sStIni = GC.S_ST_D_TRANS_NAR2P1_NRT2P1    # initial state ID string
                                        # GC.S_ST_A_INT_AT5G49770_NRT2P1
                                        # GC.S_ST_B_TRANS_AT5G49770_NRT2P1
                                        # GC.S_ST_C_INT_NAR2P1_NRT2P1
                                        # GC.S_ST_D_TRANS_NAR2P1_NRT2P1

# --- Input: General ----------------------------------------------------------
nDigObj = 3         # number of digits reserved for all input objects
cMode = GC.M_DETER  # GC.M_DETER / GC.M_STOCH

# --- Input: Names and directories --------------------------------------------
nDPlots = 'Plots'                   # name of directory for plots

# --- create input dictionary -------------------------------------------------
dictInpG = {# --- Input: Debug Info
            'lvlDbg': levelDebugOut,
            # --- Input: Initial state
            'sStIni': sStIni,
            # --- Input: General
            'nDigObj': nDigObj,
            'Mode': cMode,
            # --- Input: Names and directories
            'nDPlots': nDPlots}

###############################################################################
