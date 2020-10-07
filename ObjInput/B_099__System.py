# -*- coding: utf-8 -*-
###############################################################################
# --- B_099__System.py --------------------------------------------------------
###############################################################################
import Core.C_00__GenConstants as GC

# --- general -----------------------------------------------------------------
strOType = 'System'
strNSpec = 'System'
strCS = 'Sys'
strCL = 'System'

# --- dictionaries containing state and state transition info -----------------
dNStates = {GC.S_ST_A_INT_AT5G49770_NRT2P1: 2,
            GC.S_ST_B_TRANS_AT5G49770_NRT2P1: 1,
            GC.S_ST_C_INT_NAR2P1_NRT2P1: 3,
            GC.S_ST_D_TRANS_NAR2P1_NRT2P1: 1}
dRRC = {'A_B': 0.1,
        'B_C': 0.05,
        'C_D': 0.15,
        'D_A': 0.02}

# --- create input dictionary -------------------------------------------------
dIO = {'strOType': strOType,
       'strNSpec': strNSpec,
       'strCS': strCS,
       'strCL': strCL,
       # --- dictionaries containing state and state transition info
       'dNStates': dNStates,
       'dRRC': dRRC}

###############################################################################
