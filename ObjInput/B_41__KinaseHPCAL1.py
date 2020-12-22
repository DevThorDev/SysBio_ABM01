# -*- coding: utf-8 -*-
###############################################################################
# --- B_41__KinaseHPCAL1.py ---------------------------------------------------
###############################################################################
import Core.C_00__GenConstants as GC

# --- general -----------------------------------------------------------------
strOType = 'Kinase'
strNSpec = 'Kinase A'
strCS = 'HPCAL1'
strCL = 'HPCAL1'

# --- dictionary of parameters for special sites ------------------------------
dInfSpS = {GC.S_SPS_KASA_S839: {GC.S_STAT: GC.S_NOT_PYL,
                                GC.S_DO_PYL: [GC.ID_KAS_Y],
                                GC.S_DO_DPY: [GC.ID_PAS_1]},
           GC.S_SPS_KASA_S870: {GC.S_STAT: GC.S_NOT_PYL,
                                GC.S_DO_PYL: [GC.ID_KAS_HPCAL1],
                                GC.S_DO_DPY: [GC.ID_PAS_2]}}

# --- create input dictionary -------------------------------------------------
dIO = {# --- general
       'strOType': strOType,
       'strNSpec': strNSpec,
       'strCS': strCS,
       'strCL': strCL,
       # --- dictionary of parameters for special sites
       'dInfSpS': dInfSpS}

###############################################################################
