# -*- coding: utf-8 -*-
###############################################################################
# --- B_95__System.py ---------------------------------------------------------
###############################################################################
import Core.C_00__GenConstants as GC

# --- general -----------------------------------------------------------------
strOType = 'System'
strNSpec = 'System with all components and small molecules'
strCS = GC.ID_SYS
strCL = GC.S_CL_SYSTEM

# --- flow control ------------------------------------------------------------
doEvoT = False
doPlots = False

# --- path, directory and file names ------------------------------------------
sDObj = GC.S_DIR_SYS
sFObj = GC.S_RES_SYS
sFRed = GC.S_RED_SYS

# --- create input dictionary -------------------------------------------------
dIO = {# --- general
       'strOType': strOType,
       'strNSpec': strNSpec,
       'strCS': strCS,
       'strCL': strCL,
       # --- flow control
       'doEvoT': doEvoT,
       'doPlots': doPlots,
       # --- path, directory and file names
       'sDObj': sDObj,
       'sFObj': sFObj,
       'sFRed': sFRed}

###############################################################################
