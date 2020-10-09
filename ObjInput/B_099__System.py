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

# --- data containing state, state transition and conc. change info -----------
dNStaObj = {GC.S_ST_A_INT_AT5G49770_NRT2P1: 5,
            GC.S_ST_B_TRANS_AT5G49770_NRT2P1: 8,
            GC.S_ST_C_INT_NAR2P1_NRT2P1: 4,
            GC.S_ST_D_TRANS_NAR2P1_NRT2P1: 7}

dRRC = {'A_B': 0.1,
        'B_C': 0.05,
        'C_D': 0.15,
        'D_A': 0.02}

dConcIni = {GC.ID_NO3_1M: {'cTp': 'uniform',
                           'dPar': {'min': 4.6, 'max': 5.8}},
            GC.ID_H2PO4_1M: {'cTp': 'uniform',
                             'dPar': {'min': 1.7, 'max': 2.2}}}

dConcChg = {GC.ID_NO3_1M: {GC.S_ST_A_INT_AT5G49770_NRT2P1: -1.5,
                           GC.S_ST_B_TRANS_AT5G49770_NRT2P1: -0.1,
                           GC.S_ST_C_INT_NAR2P1_NRT2P1: 1.2,
                           GC.S_ST_D_TRANS_NAR2P1_NRT2P1: 0.05},
            GC.ID_H2PO4_1M: {GC.S_ST_A_INT_AT5G49770_NRT2P1: 0,
                             GC.S_ST_B_TRANS_AT5G49770_NRT2P1: 0,
                             GC.S_ST_C_INT_NAR2P1_NRT2P1: 0,
                             GC.S_ST_D_TRANS_NAR2P1_NRT2P1: 0}}

concChgScale = 0.005        # scale of concentration change def. in dConcChg

# --- path, directory and file names ------------------------------------------
sD_Sys = '99_Sys'
sF_SysEvo = 'SysEvo'

# --- create input dictionary -------------------------------------------------
dIO = {'strOType': strOType,
       'strNSpec': strNSpec,
       'strCS': strCS,
       'strCL': strCL,
       # --- data containing state, state transition and conc. change info
       'dNStaObj': dNStaObj,
       'dRRC': dRRC,
       'dConcIni': dConcIni,
       'dConcChg': dConcChg,
       'concChgScale': concChgScale,
       # --- path, directory and file names
       'sD_Sys': sD_Sys,
       'sF_SysEvo': sF_SysEvo}

###############################################################################
