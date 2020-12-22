# -*- coding: utf-8 -*-
###############################################################################
# --- B_21__NRT2p1.py ---------------------------------------------------------
###############################################################################
import Core.C_00__GenConstants as GC

# --- general -----------------------------------------------------------------
strOType = 'Large protein'
strNSpec = 'NRT2.1'
strCS = 'NRT2.1'
strCL = 'NRT2p1'

# --- dictionary of parameters for special sites ------------------------------
dInfSpS = {GC.S_SPS_LPRA_S21: {GC.S_STAT: GC.S_NOT_PYL,
                               GC.S_DO_PYL: [GC.ID_KAS_HPCAL1],
                               GC.S_DO_DPY: [GC.ID_PAS_3]},
           GC.S_SPS_LPRA_S28: {GC.S_STAT: GC.S_NOT_PYL,
                               GC.S_DO_PYL: [GC.ID_KAS_X],
                               GC.S_DO_DPY: [GC.ID_PAS_4]}}

# --- create input dictionary -------------------------------------------------
dIO = {# --- general
       'strOType': strOType,
       'strNSpec': strNSpec,
       'strCS': strCS,
       'strCL': strCL,
       # --- dictionary of parameters for special sites
       'dInfSpS': dInfSpS}

###############################################################################
