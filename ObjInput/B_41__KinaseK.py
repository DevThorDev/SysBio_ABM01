# -*- coding: utf-8 -*-
###############################################################################
# --- B_41__KinaseK.py --------------------------------------------------------
###############################################################################
import Core.C_00__GenConstants as GC

# --- general -----------------------------------------------------------------
strOType = 'Kinase'
strNSpec = 'Kinase K (HPCAL1)'
strCS = GC.S_K
strCL = GC.S_CL_KAS_K

# --- dictionary of parameters for special sites ------------------------------
dInfSpS = {GC.S_SPS_KAS_K_S839: {GC.S_STAT: GC.S_NOT_PYL,
                                 GC.S_DO_PYL: [GC.ID_KAS_Y],
                                 GC.S_DO_DPY: [GC.ID_PAS_A]},
           GC.S_SPS_KAS_K_S870: {GC.S_STAT: GC.S_NOT_PYL,
                                 GC.S_DO_PYL: [GC.ID_KAS_K],
                                 GC.S_DO_DPY: [GC.ID_PAS_B]}}

# --- create input dictionary -------------------------------------------------
dIO = {# --- general
       'strOType': strOType,
       'strNSpec': strNSpec,
       'strCS': strCS,
       'strCL': strCL,
       # --- dictionary of parameters for special sites
       'dInfSpS': dInfSpS}

###############################################################################
