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
dInfSpS = {'S839': {'Stat': GC.S_NOT_PYL,
                    'Pyl': [GC.ID_KAS_1],
                    'DePyl': [GC.ID_PAS_1]},
           'S870': {'Stat': GC.S_NOT_PYL,
                    'Pyl': [GC.ID_KAS_2],
                    'DePyl': [GC.ID_PAS_2]}}

# --- create input dictionary -------------------------------------------------
dIO = {# --- general
       'strOType': strOType,
       'strNSpec': strNSpec,
       'strCS': strCS,
       'strCL': strCL,
       # --- dictionary of parameters for special sites
       'dInfSpS': dInfSpS}
###############################################################################
