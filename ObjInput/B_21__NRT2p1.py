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
dInfSpS = {'S21': {'Stat': GC.S_NOT_PYL,
                   'Pyl': [GC.ID_KAS_3],
                   'DPy': [GC.ID_PAS_3]},
           'S28': {'Stat': GC.S_NOT_PYL,
                   'Pyl': [GC.ID_KAS_X],
                   'DPy': [GC.ID_PAS_4]}}

# --- create input dictionary -------------------------------------------------
dIO = {# --- general
       'strOType': strOType,
       'strNSpec': strNSpec,
       'strCS': strCS,
       'strCL': strCL,
       # --- dictionary of parameters for special sites
       'dInfSpS': dInfSpS}

###############################################################################
