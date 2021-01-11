# -*- coding: utf-8 -*-
###############################################################################
# --- B_21__NRT2p1.py ---------------------------------------------------------
###############################################################################
import Core.C_00__GenConstants as GC

# --- general -----------------------------------------------------------------
strOType = 'Large protein'
strNSpec = 'Large protein NRT2.1'
strCS = GC.S_L
strCL = GC.S_CL_LPR_NRT2P1

# --- dictionary of parameters for special sites ------------------------------
dInfSpS = {GC.S_SPS_L_S21: {GC.S_STAT: GC.S_NOT_PYL,
                            GC.S_DO_PYL: [GC.S_K__ + GC.S_2DASH01],
                            GC.S_DO_DPY: [GC.S_C__ + GC.S_4DASH]},
           GC.S_SPS_L_S28: {GC.S_STAT: GC.S_NOT_PYL,
                            GC.S_DO_PYL: [GC.S_X__ + GC.S_4DASH],
                            GC.S_DO_DPY: [GC.S_D__ + GC.S_4DASH]}}

# --- create input dictionary -------------------------------------------------
dIO = {# --- general
       'strOType': strOType,
       'strNSpec': strNSpec,
       'strCS': strCS,
       'strCL': strCL,
       # --- dictionary of parameters for special sites
       'dInfSpS': dInfSpS}

###############################################################################
