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

# --- path, directory and file names ------------------------------------------
sD_Obj = GC.S_DIR_SYS
sF_Obj = GC.S_RES_SYS
sFRed = GC.S_RED_SYS

# --- create input dictionary -------------------------------------------------
dIO = {# --- general
       'strOType': strOType,
       'strNSpec': strNSpec,
       'strCS': strCS,
       'strCL': strCL,
       # --- path, directory and file names
       'sD_Obj': sD_Obj,
       'sF_Obj': sF_Obj,
       'sFRed': sFRed}

###############################################################################
