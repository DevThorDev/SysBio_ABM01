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
dInfSpS = {GC.S_SPS_K_S839: {GC.S_STAT: GC.S_NOT_PYL,
                             GC.S_DO_PYL: [GC.S_Y__ + GC.S_4DASH],
                             GC.S_DO_DPY: [GC.S_A__ + GC.S_4DASH]},
           GC.S_SPS_K_S870: {GC.S_STAT: GC.S_NOT_PYL,
                             GC.S_DO_PYL: [GC.S_K__ + GC.S_2DASH00,
                                           GC.S_K__ + GC.S_2DASH10],
                             GC.S_DO_DPY: [GC.S_B__ + GC.S_4DASH]}}

# --- create input dictionary -------------------------------------------------
dIO = {# --- general
       'strOType': strOType,
       'strNSpec': strNSpec,
       'strCS': strCS,
       'strCL': strCL,
       # --- dictionary of parameters for special sites
       'dInfSpS': dInfSpS}

###############################################################################
