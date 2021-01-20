# -*- coding: utf-8 -*-
###############################################################################
# --- B_99__Simulation.py -----------------------------------------------------
###############################################################################
import Core.C_00__GenConstants as GC

# --- general -----------------------------------------------------------------
strOType = 'Simulation'
strNSpec = 'Simulation including all repetitions'
strCS = GC.ID_SIM
strCL = GC.S_CL_SIMULATION

# --- path, directory and file names ------------------------------------------
sD_Sim = '99_Sim'
sF_Sim = 'SimSysEvo'

# --- create input dictionary -------------------------------------------------
dIO = {# --- general
       'strOType': strOType,
       'strNSpec': strNSpec,
       'strCS': strCS,
       'strCL': strCL,
       # --- path, directory and file names
       'sD_Sim': sD_Sim,
       'sF_Sim': sF_Sim}

###############################################################################
