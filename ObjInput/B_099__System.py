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
dNStaObj = {GC.S_ST_A_INT_AT5G49770_NRT2P1: 330,
            GC.S_ST_B_TRANS_AT5G49770_NRT2P1: 30,
            GC.S_ST_C_INT_NAR2P1_NRT2P1: 100,
            GC.S_ST_D_TRANS_NAR2P1_NRT2P1: 40}

dRRC = {GC.S_STCH_A_B: 0.2,
        GC.S_STCH_B_C: 0.02,
        GC.S_STCH_C_D: 0.1,
        GC.S_STCH_D_A: 0.05}

dConcIni = {GC.ID_NO3_1M: {'cTp': 'uniform',
                           'dPar': {'min': 250., 'max': 350.}},
            GC.ID_H2PO4_1M: {'cTp': 'uniform',
                             'dPar': {'min': 1.7, 'max': 2.2}}}

dParP__A_B__N = {'prMin': 0, 'prMax': 1, 'B': 5., 'C': 1.5, 'D': 0.02}
dParP__A_B__P = {'prMin': 0, 'prMax': 0., 'B': 0., 'C': 1., 'D': 0.}

dParP__B_C__N = {'prMin': 0, 'prMax': 1, 'B': 8., 'C': 0.2, 'D': 0.02}
dParP__B_C__P = {'prMin': 0, 'prMax': 0., 'B': 0., 'C': 1., 'D': 0.}

dParP__C_D__N = {'prMin': 0, 'prMax': 1, 'B': 4., 'C': 12., 'D': 0.03}
dParP__C_D__P = {'prMin': 0, 'prMax': 0., 'B': 0., 'C': 1., 'D': 0.}

dParP__D_A__N = {'prMin': 0, 'prMax': 1, 'B': 12., 'C': 2.75, 'D': 0.01}
dParP__D_A__P = {'prMin': 0, 'prMax': 0., 'B': 0., 'C': 1., 'D': 0.}

# GC.ID_NO3_1M, GC.ID_H2PO4_1M: max. changes per unit time
dConcChg = {GC.ID_NO3_1M: {GC.S_ST_A_INT_AT5G49770_NRT2P1: -20.,
                           GC.S_ST_B_TRANS_AT5G49770_NRT2P1: -0.5,
                           GC.S_ST_C_INT_NAR2P1_NRT2P1: 10.,
                           GC.S_ST_D_TRANS_NAR2P1_NRT2P1: 2.},
            GC.ID_H2PO4_1M: {GC.S_ST_A_INT_AT5G49770_NRT2P1: 0,
                             GC.S_ST_B_TRANS_AT5G49770_NRT2P1: 0,
                             GC.S_ST_C_INT_NAR2P1_NRT2P1: 0,
                             GC.S_ST_D_TRANS_NAR2P1_NRT2P1: 0},
            GC.S_STCH_A_B: {GC.ID_NO3_1M: dParP__A_B__N,
                            GC.ID_H2PO4_1M: dParP__A_B__P},
            GC.S_STCH_B_C: {GC.ID_NO3_1M: dParP__B_C__N,
                            GC.ID_H2PO4_1M: dParP__B_C__P},
            GC.S_STCH_C_D: {GC.ID_NO3_1M: dParP__C_D__N,
                            GC.ID_H2PO4_1M: dParP__C_D__P},
            GC.S_STCH_D_A: {GC.ID_NO3_1M: dParP__D_A__N,
                            GC.ID_H2PO4_1M: dParP__D_A__P}}

concChgScale = 10.    # scale of concentration change def. in dConcChg

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
       'nStaObj': sum(dNStaObj.values()),
       'dRRC': dRRC,
       'dConcIni': dConcIni,
       'dConcChg': dConcChg,
       'concChgScale': concChgScale,
       # --- path, directory and file names
       'sD_Sys': sD_Sys,
       'sF_SysEvo': sF_SysEvo}

###############################################################################
