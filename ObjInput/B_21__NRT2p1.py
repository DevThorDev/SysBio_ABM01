# -*- coding: utf-8 -*-
###############################################################################
# --- B_21__NRT2p1.py ---------------------------------------------------------
###############################################################################
import Core.C_00__GenConstants as GC

# --- general -----------------------------------------------------------------
strOType = 'Large protein'
strNSpec = 'Large protein NRT2.1'
strCS = GC.S_L
strCL = GC.ID_LPR_NRT2P1

# --- dictionary of parameters for special sites ------------------------------
dInfSpS = {GC.S_SPS_LPR_L_S21: {GC.S_STAT: GC.S_NOT_PYL,
                                GC.S_DO_PYL: [GC.ID_KAS_K],
                                GC.S_DO_DPY: [GC.ID_PAS_C]},
           GC.S_SPS_LPR_L_S28: {GC.S_STAT: GC.S_NOT_PYL,
                                GC.S_DO_PYL: [GC.ID_KAS_X],
                                GC.S_DO_DPY: [GC.ID_PAS_D]}}

# --- create input dictionary -------------------------------------------------
dIO = {# --- general
       'strOType': strOType,
       'strNSpec': strNSpec,
       'strCS': strCS,
       'strCL': strCL,
       # --- dictionary of parameters for special sites
       'dInfSpS': dInfSpS}

###############################################################################
