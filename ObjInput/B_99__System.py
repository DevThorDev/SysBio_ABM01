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

# --- plant cell data ---------------------------------------------------------
VolC = 10000                        # volume (microns^3)
MassC = 2                           # nanograms

# --- data containing components, reactions and conc. change info -------------
# initial number of objects for each possible component
# dNCpObj = {GC.S_CP_L00: 30,
#            GC.S_CP_L01: 30,
#            GC.S_CP_L10: 30,
#            GC.S_CP_L11: 30,
#            GC.S_CP_S__: 50,
#            GC.S_CP_K00: 40,
#            GC.S_CP_K01: 40,
#            GC.S_CP_K10: 40,
#            GC.S_CP_K11: 40,
#            GC.S_CP_LSI01: 70,
#            GC.S_CP_LST00: 70,
#            GC.S_CP_LST10: 70,
#            GC.S_CP_LST11: 70,
#            GC.S_CP_LKI1001: 20,
#            GC.S_CP_LKT0000: 20,
#            GC.S_CP_LKT0001: 20,
#            GC.S_CP_LKT0010: 20,
#            GC.S_CP_LKT0011: 20,
#            GC.S_CP_LKT0100: 20,
#            GC.S_CP_LKT0101: 20,
#            GC.S_CP_LKT0110: 20,
#            GC.S_CP_LKT0111: 100,
#            GC.S_CP_LKT1000: 20,
#            GC.S_CP_LKT1010: 20,
#            GC.S_CP_LKT1011: 20,
#            GC.S_CP_LKT1100: 20,
#            GC.S_CP_LKT1101: 20,
#            GC.S_CP_LKT1110: 20,
#            GC.S_CP_LKT1111: 20}

# basic weights for interaction partner changes
# w_IPC_LS_LK = 1.1
# w_IPC_LK_LS = 1.

# basic weights for complex formation and disintegration
# w_Frm_L_S_LS = 1.
# w_Frm_L_K_LK = 1.
# w_Dis_LS_L_S = 1
# w_Dis_LK_L_K = 1

# basic weights for phosphorylations and dephosphorylations at the four sites
# w_Pyl_S21 = 1.
# w_Pyl_S28 = 1.5
# w_Pyl_S839 = 0.75
# w_Pyl_S870 = 0.9

# w_DPy_S21 = 1.1
# w_DPy_S28 = 0.85
# w_DPy_S839 = 1.15
# w_DPy_S870 = 0.6

# basic weights for changes between component groups
# w_L_L = 1.
# w_K_K = 1.
# w_L_S_LSI = 1.
# w_L_K_LKI = 1.
# w_LSI_L_S = 1.
# w_LST_L_S = 1.
# w_LKI_L_K = 1.
# w_LKT_L_K = 1.
# w_LSI_LST = 0.1
# w_LST_LST = 10.
# w_LST_LKI = 0.1
# w_LKI_LKT = 0.1
# w_LKT_LKT = 10.
# w_LKT_LSI = 0.1

# dictionary of basic reaction rate weights
dRRC = {}
# dRRC = {GC.TS_RCT_L00:(w_Pyl_S28*w_L_L, w_Pyl_S21*w_L_L),
#         GC.TS_RCT_L01:(w_DPy_S28*w_L_L, w_Pyl_S21*w_L_L,
#                        w_Frm_L_S_LS*w_L_S_LSI),
#         GC.TS_RCT_L10:(w_DPy_S21*w_L_L, w_Pyl_S28*w_L_L,
#                        w_Frm_L_K_LK*w_L_K_LKI),
#         GC.TS_RCT_L11:(w_DPy_S21*w_L_L, w_DPy_S28*w_L_L),

#         # GC.TS_RCT_S__:(w_Frm_L_S_LS*w_L_S_LSI),

#         GC.TS_RCT_K00:(w_Pyl_S28*w_K_K, w_Pyl_S21*w_K_K),
#         GC.TS_RCT_K01:(w_DPy_S28*w_K_K, w_Pyl_S21*w_K_K,
#                        w_Frm_L_K_LK*w_L_K_LKI),
#         GC.TS_RCT_K10:(w_DPy_S21*w_K_K, w_Pyl_S28*w_K_K),
#         GC.TS_RCT_K11:(w_DPy_S21*w_K_K, w_DPy_S28*w_K_K),
#         GC.TS_RCT_LSI01: (w_DPy_S28*w_LSI_LST, w_Pyl_S21*w_LSI_LST,
#                           w_Dis_LS_L_S*w_LSI_L_S),
#         GC.TS_RCT_LST00: (w_Pyl_S28*w_LST_LST, w_Pyl_S21*w_LST_LST,
#                           w_Dis_LS_L_S*w_LST_L_S),
#         GC.TS_RCT_LST10: (w_DPy_S21*w_LST_LST, w_Pyl_S28*w_LST_LST,
#                           w_Dis_LS_L_S*w_LST_L_S),
#         GC.TS_RCT_LST11: (w_DPy_S21*w_LST_LST, w_DPy_S28*w_LST_LST,
#                           w_Dis_LS_L_S*w_LST_L_S),
#         GC.TS_RCT_LKI1001: (w_DPy_S21*w_LKI_LKT, w_DPy_S870*w_LKI_LKT,
#                             w_Pyl_S839*w_LKI_LKT, w_Pyl_S28*w_LKI_LKT,
#                             w_Dis_LK_L_K*w_LKI_L_K),
#         GC.TS_RCT_LKT0000: (w_Pyl_S870*w_LKT_LKT, w_Pyl_S839*w_LKT_LKT,
#                             w_Pyl_S28*w_LKT_LKT, w_Pyl_S21*w_LKT_LKT,
#                             w_Dis_LK_L_K*w_LKT_L_K),
#         GC.TS_RCT_LKT0001: (w_DPy_S870*w_LKT_LKT, w_Pyl_S839*w_LKT_LKT,
#                             w_Pyl_S28*w_LKT_LKT, w_Pyl_S21*w_LKT_LKT,
#                             w_Dis_LK_L_K*w_LKT_L_K),
#         GC.TS_RCT_LKT0010: (w_DPy_S839*w_LKT_LKT, w_Pyl_S870*w_LKT_LKT,
#                             w_Pyl_S28*w_LKT_LKT, w_Pyl_S21*w_LKT_LKT,
#                             w_Dis_LK_L_K*w_LKT_L_K),
#         GC.TS_RCT_LKT0011: (w_DPy_S839*w_LKT_LKT, w_DPy_S870*w_LKT_LKT,
#                             w_Pyl_S28*w_LKT_LKT, w_Pyl_S21*w_LKT_LKT,
#                             w_Dis_LK_L_K*w_LKT_L_K),
#         GC.TS_RCT_LKT0100: (w_DPy_S28*w_LKT_LKT, w_Pyl_S870*w_LKT_LKT,
#                             w_Pyl_S839*w_LKT_LKT, w_Pyl_S21*w_LKT_LKT,
#                             w_Dis_LK_L_K*w_LKT_L_K),
#         GC.TS_RCT_LKT0101: (w_DPy_S28*w_LKT_LKT, w_DPy_S870*w_LKT_LKT,
#                             w_Pyl_S839*w_LKT_LKT, w_Pyl_S21*w_LKT_LKT,
#                             w_Dis_LK_L_K*w_LKT_L_K),
#         GC.TS_RCT_LKT0110: (w_DPy_S28*w_LKT_LKT, w_DPy_S839*w_LKT_LKT,
#                             w_Pyl_S870*w_LKT_LKT, w_Pyl_S21*w_LKT_LKT,
#                             w_Dis_LK_L_K*w_LKT_L_K, w_IPC_LK_LS*w_LKT_LSI),
#         GC.TS_RCT_LKT0111: (w_DPy_S28*w_LKT_LKT, w_DPy_S839*w_LKT_LKT,
#                             w_DPy_S870*w_LKT_LKT, w_Pyl_S21*w_LKT_LKT,
#                             w_Dis_LK_L_K*w_LKT_L_K),
#         GC.TS_RCT_LKT1000: (w_DPy_S21*w_LKT_LKT, w_Pyl_S870*w_LKT_LKT,
#                             w_Pyl_S839*w_LKT_LKT, w_Pyl_S28*w_LKT_LKT,
#                             w_Dis_LK_L_K*w_LKT_L_K),
#         GC.TS_RCT_LKT1010: (w_DPy_S21*w_LKT_LKT, w_DPy_S839*w_LKT_LKT,
#                             w_Pyl_S870*w_LKT_LKT, w_Pyl_S28*w_LKT_LKT,
#                             w_Dis_LK_L_K*w_LKT_L_K),
#         GC.TS_RCT_LKT1011: (w_DPy_S21*w_LKT_LKT, w_DPy_S839*w_LKT_LKT,
#                             w_DPy_S870*w_LKT_LKT, w_Pyl_S28*w_LKT_LKT,
#                             w_Dis_LK_L_K*w_LKT_L_K),
#         GC.TS_RCT_LKT1100: (w_DPy_S21*w_LKT_LKT, w_DPy_S28*w_LKT_LKT,
#                             w_Pyl_S870*w_LKT_LKT, w_Pyl_S839*w_LKT_LKT,
#                             w_Dis_LK_L_K*w_LKT_L_K),
#         GC.TS_RCT_LKT1101: (w_DPy_S21*w_LKT_LKT, w_DPy_S28*w_LKT_LKT,
#                             w_DPy_S870*w_LKT_LKT, w_Pyl_S839*w_LKT_LKT,
#                             w_Dis_LK_L_K*w_LKT_L_K),
#         GC.TS_RCT_LKT1110: (w_DPy_S21*w_LKT_LKT, w_DPy_S28*w_LKT_LKT,
#                             w_DPy_S839*w_LKT_LKT, w_Pyl_S870*w_LKT_LKT,
#                             w_Dis_LK_L_K*w_LKT_L_K),
#         GC.TS_RCT_LKT1111: (w_DPy_S21*w_LKT_LKT, w_DPy_S28*w_LKT_LKT,
#                             w_DPy_S839*w_LKT_LKT, w_DPy_S870*w_LKT_LKT,
#                             w_Dis_LK_L_K*w_LKT_L_K)}

# dictionary of initial, min. and max. concentrations of small molecules
dConcSMo = {}
# dConcSMo = {'Ini': {GC.ID_NO3_1M: {'cTp': 'uniform',
#                                    'dPar': {'min': 9., 'max': 11.}},
#                     GC.ID_H2PO4_1M: {'cTp': 'uniform',
#                                      'dPar': {'min': 1.7, 'max': 2.2}}},
#             'Min': {GC.ID_NO3_1M: 1., GC.ID_H2PO4_1M: 0.01},
#             'Max': {GC.ID_NO3_1M: 1000., GC.ID_H2PO4_1M: 100.}}

# dictionary containing parameters which determine concentration changes of
# small molecules depending on the distribution of components, and vice versa

# dependency of small molecule concentration changes on component
# dPar_N_L00 = {'absChg': 0.0}
# dPar_N_L01 = {'absChg': 0.0}
# dPar_N_L10 = {'absChg': 0.0}
# dPar_N_L11 = {'absChg': 0.0}

# dPar_N_S = {'absChg': 0.0}

# dPar_N_K00 = {'absChg': 0.0}
# dPar_N_K01 = {'absChg': 0.0}
# dPar_N_K10 = {'absChg': 0.0}
# dPar_N_K11 = {'absChg': 0.0}

# dPar_N_LSI01 = {'absChg': 0.001}
# dPar_N_LST00 = {'absChg': 0.0}
# dPar_N_LST10 = {'absChg': 0.0}
# dPar_N_LST11 = {'absChg': 0.0}

# dPar_N_LKI1001 = {'absChg': -0.001}
# dPar_N_LKT0000 = {'absChg': -0.0}
# dPar_N_LKT0001 = {'absChg': -0.0}
# dPar_N_LKT0010 = {'absChg': -0.0}
# dPar_N_LKT0011 = {'absChg': -0.0}
# dPar_N_LKT0100 = {'absChg': -0.0}
# dPar_N_LKT0101 = {'absChg': -0.0}
# dPar_N_LKT0110 = {'absChg': -0.0}
# dPar_N_LKT0111 = {'absChg': -0.0}
# dPar_N_LKT1000 = {'absChg': -0.0}
# dPar_N_LKT1010 = {'absChg': -0.0}
# dPar_N_LKT1011 = {'absChg': -0.0}
# dPar_N_LKT1100 = {'absChg': -0.0}
# dPar_N_LKT1101 = {'absChg': -0.0}
# dPar_N_LKT1110 = {'absChg': -0.0}
# dPar_N_LKT1111 = {'absChg': -0.0}

# dPar_P_L00 = {'absChg': 0.0}
# dPar_P_L01 = {'absChg': 0.0}
# dPar_P_L10 = {'absChg': 0.0}
# dPar_P_L11 = {'absChg': 0.0}

# dPar_P_S = {'absChg': 0.0}

# dPar_P_K00 = {'absChg': 0.0}
# dPar_P_K01 = {'absChg': 0.0}
# dPar_P_K10 = {'absChg': 0.0}
# dPar_P_K11 = {'absChg': 0.0}

# dPar_P_LSI01 = {'absChg': 0.001}
# dPar_P_LST00 = {'absChg': 0.0}
# dPar_P_LST10 = {'absChg': 0.0}
# dPar_P_LST11 = {'absChg': 0.0}

# dPar_P_LKI1001 = {'absChg': -0.001}
# dPar_P_LKT0000 = {'absChg': -0.0}
# dPar_P_LKT0001 = {'absChg': -0.0}
# dPar_P_LKT0010 = {'absChg': -0.0}
# dPar_P_LKT0011 = {'absChg': -0.0}
# dPar_P_LKT0100 = {'absChg': -0.0}
# dPar_P_LKT0101 = {'absChg': -0.0}
# dPar_P_LKT0110 = {'absChg': -0.0}
# dPar_P_LKT0111 = {'absChg': -0.0}
# dPar_P_LKT1000 = {'absChg': -0.0}
# dPar_P_LKT1010 = {'absChg': -0.0}
# dPar_P_LKT1011 = {'absChg': -0.0}
# dPar_P_LKT1100 = {'absChg': -0.0}
# dPar_P_LKT1101 = {'absChg': -0.0}
# dPar_P_LKT1110 = {'absChg': -0.0}
# dPar_P_LKT1111 = {'absChg': -0.0}

# parameters of sigmoidal function for interaction partner changes
# dPar_LST1001_LKI1001 = {'prMin': 0, 'prMax': 1, 'B': 12., 'C': 2.75, 'D': 0.01}
# dPar_LKT0110_LSI0110 = {'prMin': 1, 'prMax': 0, 'B': 8., 'C': 0.2, 'D': 0.02}

# parameters of sigmoidal function for (de)phosphorylations at the four sites
# dPar_Pyl_S21 = {'prMin': 0, 'prMax': 1, 'B': 10., 'C': 1., 'D': 0.025}
# dPar_Pyl_S28 = {'prMin': 1, 'prMax': 0, 'B': 5., 'C': 1.5, 'D': 0.02}
# dPar_Pyl_S839 = {'prMin': 1, 'prMax': 0, 'B': 3., 'C': 2.5, 'D': 0.03}
# dPar_Pyl_S870 = {'prMin': 0, 'prMax': 1, 'B': 20., 'C': 0.5, 'D': 0.015}

# dPar_DPy_S21 = {'prMin': 1, 'prMax': 0, 'B': 1., 'C': 20., 'D': 0.035}
# dPar_DPy_S28 = {'prMin': 0, 'prMax': 1, 'B': 12., 'C': 2.75, 'D': 0.01}
# dPar_DPy_S839 = {'prMin': 0, 'prMax': 1, 'B': 25., 'C': 5., 'D': 0.03}
# dPar_DPy_S870 = {'prMin': 1, 'prMax': 0, 'B': 8., 'C': 0.2, 'D': 0.02}

# dummy parameters of sigmoidal function for H2PO4- dependency
# dPar_Dummy = {'prMin': 0, 'prMax': 0, 'B': 0., 'C': 1., 'D': 0.}

# tuples of dictionaries containing parameters of sigmoidal function
# tDPar_LSI01_N = (dPar_DPy_S28, dPar_Pyl_S21)
# tDPar_LST00_N = (dPar_Pyl_S28, dPar_Pyl_S21)
# tDPar_LST10_N = (dPar_DPy_S21, dPar_Pyl_S28)
# tDPar_LST1001_N = (dPar_DPy_S21, dPar_DPy_S870, dPar_Pyl_S839, dPar_Pyl_S28,
#                    dPar_LST1001_LKI1001)
# tDPar_LST1010_N = (dPar_DPy_S21, dPar_DPy_S839, dPar_Pyl_S870, dPar_Pyl_S28)
# tDPar_LST1011_N = (dPar_DPy_S21, dPar_DPy_S839, dPar_DPy_S870, dPar_Pyl_S28)
# tDPar_LST1100_N = (dPar_DPy_S21, dPar_DPy_S28, dPar_Pyl_S870, dPar_Pyl_S839)
# tDPar_LST1101_N = (dPar_DPy_S21, dPar_DPy_S28, dPar_DPy_S870, dPar_Pyl_S839)
# tDPar_LST1110_N = (dPar_DPy_S21, dPar_DPy_S28, dPar_DPy_S839, dPar_Pyl_S870)
# tDPar_LST1111_N = (dPar_DPy_S21, dPar_DPy_S28, dPar_DPy_S839, dPar_Pyl_S870)

# tDPar_LKI1001_N = (dPar_DPy_S21, dPar_DPy_S870, dPar_Pyl_S839, dPar_Pyl_S28)
# tDPar_LKT0000_N = (dPar_Pyl_S870, dPar_Pyl_S839, dPar_Pyl_S28, dPar_Pyl_S21)
# tDPar_LKT0001_N = (dPar_DPy_S870, dPar_Pyl_S839, dPar_Pyl_S28, dPar_Pyl_S21)
# tDPar_LKT0010_N = (dPar_DPy_S839, dPar_Pyl_S870, dPar_Pyl_S28, dPar_Pyl_S21)
# tDPar_LKT0011_N = (dPar_DPy_S839, dPar_DPy_S870, dPar_Pyl_S28, dPar_Pyl_S21)
# tDPar_LKT0100_N = (dPar_DPy_S28, dPar_Pyl_S870, dPar_Pyl_S839, dPar_Pyl_S21)
# tDPar_LKT0101_N = (dPar_DPy_S28, dPar_DPy_S870, dPar_Pyl_S839, dPar_Pyl_S21)
# tDPar_LKT0110_N = (dPar_DPy_S28, dPar_DPy_S839, dPar_Pyl_S870, dPar_Pyl_S21,
#                    dPar_LKT0110_LSI0110)
# tDPar_LKT0111_N = (dPar_DPy_S28, dPar_DPy_S839, dPar_DPy_S870, dPar_Pyl_S21)
# tDPar_LKT1000_N = (dPar_DPy_S21, dPar_Pyl_S870, dPar_Pyl_S839, dPar_Pyl_S28)
# tDPar_LKT1010_N = (dPar_DPy_S21, dPar_DPy_S839, dPar_Pyl_S870, dPar_Pyl_S28)
# tDPar_LKT1011_N = (dPar_DPy_S21, dPar_DPy_S839, dPar_DPy_S870, dPar_Pyl_S28)
# tDPar_LKT1100_N = (dPar_DPy_S21, dPar_DPy_S28, dPar_Pyl_S870, dPar_Pyl_S839)
# tDPar_LKT1101_N = (dPar_DPy_S21, dPar_DPy_S28, dPar_DPy_S870, dPar_Pyl_S839)
# tDPar_LKT1110_N = (dPar_DPy_S21, dPar_DPy_S28, dPar_DPy_S839, dPar_Pyl_S870)
# tDPar_LKT1111_N = (dPar_DPy_S21, dPar_DPy_S28, dPar_DPy_S839, dPar_DPy_S870)

# tDPar_LSI0110_P = (dPar_Dummy, dPar_Dummy, dPar_Dummy, dPar_Dummy)
# tDPar_LST0000_P = (dPar_Dummy, dPar_Dummy, dPar_Dummy, dPar_Dummy)
# tDPar_LST0001_P = (dPar_Dummy, dPar_Dummy, dPar_Dummy, dPar_Dummy)
# tDPar_LST0010_P = (dPar_Dummy, dPar_Dummy, dPar_Dummy, dPar_Dummy)
# tDPar_LST0011_P = (dPar_Dummy, dPar_Dummy, dPar_Dummy, dPar_Dummy)
# tDPar_LST0100_P = (dPar_Dummy, dPar_Dummy, dPar_Dummy, dPar_Dummy)
# tDPar_LST0101_P = (dPar_Dummy, dPar_Dummy, dPar_Dummy, dPar_Dummy)
# tDPar_LST0111_P = (dPar_Dummy, dPar_Dummy, dPar_Dummy, dPar_Dummy)
# tDPar_LST1000_P = (dPar_Dummy, dPar_Dummy, dPar_Dummy, dPar_Dummy)
# tDPar_LST1001_P = (dPar_Dummy, dPar_Dummy, dPar_Dummy, dPar_Dummy, dPar_Dummy)
# tDPar_LST1010_P = (dPar_Dummy, dPar_Dummy, dPar_Dummy, dPar_Dummy)
# tDPar_LST1011_P = (dPar_Dummy, dPar_Dummy, dPar_Dummy, dPar_Dummy)
# tDPar_LST1100_P = (dPar_Dummy, dPar_Dummy, dPar_Dummy, dPar_Dummy)
# tDPar_LST1101_P = (dPar_Dummy, dPar_Dummy, dPar_Dummy, dPar_Dummy)
# tDPar_LST1110_P = (dPar_Dummy, dPar_Dummy, dPar_Dummy, dPar_Dummy)
# tDPar_LST1111_P = (dPar_Dummy, dPar_Dummy, dPar_Dummy, dPar_Dummy)

# tDPar_LKI1001_P = (dPar_Dummy, dPar_Dummy, dPar_Dummy, dPar_Dummy)
# tDPar_LKT0000_P = (dPar_Dummy, dPar_Dummy, dPar_Dummy, dPar_Dummy)
# tDPar_LKT0001_P = (dPar_Dummy, dPar_Dummy, dPar_Dummy, dPar_Dummy)
# tDPar_LKT0010_P = (dPar_Dummy, dPar_Dummy, dPar_Dummy, dPar_Dummy)
# tDPar_LKT0011_P = (dPar_Dummy, dPar_Dummy, dPar_Dummy, dPar_Dummy)
# tDPar_LKT0100_P = (dPar_Dummy, dPar_Dummy, dPar_Dummy, dPar_Dummy)
# tDPar_LKT0101_P = (dPar_Dummy, dPar_Dummy, dPar_Dummy, dPar_Dummy)
# tDPar_LKT0110_P = (dPar_Dummy, dPar_Dummy, dPar_Dummy, dPar_Dummy, dPar_Dummy)
# tDPar_LKT0111_P = (dPar_Dummy, dPar_Dummy, dPar_Dummy, dPar_Dummy)
# tDPar_LKT1000_P = (dPar_Dummy, dPar_Dummy, dPar_Dummy, dPar_Dummy)
# tDPar_LKT1010_P = (dPar_Dummy, dPar_Dummy, dPar_Dummy, dPar_Dummy)
# tDPar_LKT1011_P = (dPar_Dummy, dPar_Dummy, dPar_Dummy, dPar_Dummy)
# tDPar_LKT1100_P = (dPar_Dummy, dPar_Dummy, dPar_Dummy, dPar_Dummy)
# tDPar_LKT1101_P = (dPar_Dummy, dPar_Dummy, dPar_Dummy, dPar_Dummy)
# tDPar_LKT1110_P = (dPar_Dummy, dPar_Dummy, dPar_Dummy, dPar_Dummy)
# tDPar_LKT1111_P = (dPar_Dummy, dPar_Dummy, dPar_Dummy, dPar_Dummy)

# GC.ID_NO3_1M, GC.ID_H2PO4_1M: max. changes per unit time
dConcChg = {}
# dConcChg = {GC.ID_NO3_1M: {GC.TS_RCT_LKI1001: dPar_N_LKI1001,
#                            GC.TS_RCT_LKT0000: dPar_N_LKT0000,
#                            GC.TS_RCT_LKT0001: dPar_N_LKT0001,
#                            GC.TS_RCT_LKT0010: dPar_N_LKT0010,
#                            GC.TS_RCT_LKT0011: dPar_N_LKT0011,
#                            GC.TS_RCT_LKT0100: dPar_N_LKT0100,
#                            GC.TS_RCT_LKT0101: dPar_N_LKT0101,
#                            GC.TS_RCT_LKT0110: dPar_N_LKT0110,
#                            GC.TS_RCT_LKT0111: dPar_N_LKT0111,
#                            GC.TS_RCT_LKT1000: dPar_N_LKT1000,
#                            GC.TS_RCT_LKT1010: dPar_N_LKT1010,
#                            GC.TS_RCT_LKT1011: dPar_N_LKT1011,
#                            GC.TS_RCT_LKT1100: dPar_N_LKT1100,
#                            GC.TS_RCT_LKT1101: dPar_N_LKT1101,
#                            GC.TS_RCT_LKT1110: dPar_N_LKT1110,
#                            GC.TS_RCT_LKT1111: dPar_N_LKT1111},

#             GC.ID_H2PO4_1M: {GC.TS_RCT_LKI1001: dPar_P_LKI1001,
#                              GC.TS_RCT_LKT0000: dPar_P_LKT0000,
#                              GC.TS_RCT_LKT0001: dPar_P_LKT0001,
#                              GC.TS_RCT_LKT0010: dPar_P_LKT0010,
#                              GC.TS_RCT_LKT0011: dPar_P_LKT0011,
#                              GC.TS_RCT_LKT0100: dPar_P_LKT0100,
#                              GC.TS_RCT_LKT0101: dPar_P_LKT0101,
#                              GC.TS_RCT_LKT0110: dPar_P_LKT0110,
#                              GC.TS_RCT_LKT0111: dPar_P_LKT0111,
#                              GC.TS_RCT_LKT1000: dPar_P_LKT1000,
#                              GC.TS_RCT_LKT1010: dPar_P_LKT1010,
#                              GC.TS_RCT_LKT1011: dPar_P_LKT1011,
#                              GC.TS_RCT_LKT1100: dPar_P_LKT1100,
#                              GC.TS_RCT_LKT1101: dPar_P_LKT1101,
#                              GC.TS_RCT_LKT1110: dPar_P_LKT1110,
#                              GC.TS_RCT_LKT1111: dPar_P_LKT1111},

#             GC.TS_RCT_LKI1001: {GC.ID_NO3_1M: tDPar_LKI1001_N,
#                                 GC.ID_H2PO4_1M: tDPar_LKI1001_P},
#             GC.TS_RCT_LKT0000: {GC.ID_NO3_1M: tDPar_LKT0000_N,
#                                 GC.ID_H2PO4_1M: tDPar_LKT0000_P},
#             GC.TS_RCT_LKT0001: {GC.ID_NO3_1M: tDPar_LKT0001_N,
#                                 GC.ID_H2PO4_1M: tDPar_LKT0001_P},
#             GC.TS_RCT_LKT0010: {GC.ID_NO3_1M: tDPar_LKT0010_N,
#                                 GC.ID_H2PO4_1M: tDPar_LKT0010_P},
#             GC.TS_RCT_LKT0011: {GC.ID_NO3_1M: tDPar_LKT0011_N,
#                                 GC.ID_H2PO4_1M: tDPar_LKT0011_P},
#             GC.TS_RCT_LKT0100: {GC.ID_NO3_1M: tDPar_LKT0100_N,
#                                 GC.ID_H2PO4_1M: tDPar_LKT0100_P},
#             GC.TS_RCT_LKT0101: {GC.ID_NO3_1M: tDPar_LKT0101_N,
#                                 GC.ID_H2PO4_1M: tDPar_LKT0101_P},
#             GC.TS_RCT_LKT0110: {GC.ID_NO3_1M: tDPar_LKT0110_N,
#                                 GC.ID_H2PO4_1M: tDPar_LKT0110_P},
#             GC.TS_RCT_LKT0111: {GC.ID_NO3_1M: tDPar_LKT0111_N,
#                                 GC.ID_H2PO4_1M: tDPar_LKT0111_P},
#             GC.TS_RCT_LKT1000: {GC.ID_NO3_1M: tDPar_LKT1000_N,
#                                 GC.ID_H2PO4_1M: tDPar_LKT1000_P},
#             GC.TS_RCT_LKT1010: {GC.ID_NO3_1M: tDPar_LKT1010_N,
#                                 GC.ID_H2PO4_1M: tDPar_LKT1010_P},
#             GC.TS_RCT_LKT1011: {GC.ID_NO3_1M: tDPar_LKT1011_N,
#                                 GC.ID_H2PO4_1M: tDPar_LKT1011_P},
#             GC.TS_RCT_LKT1100: {GC.ID_NO3_1M: tDPar_LKT1100_N,
#                                 GC.ID_H2PO4_1M: tDPar_LKT1100_P},
#             GC.TS_RCT_LKT1101: {GC.ID_NO3_1M: tDPar_LKT1101_N,
#                                 GC.ID_H2PO4_1M: tDPar_LKT1101_P},
#             GC.TS_RCT_LKT1110: {GC.ID_NO3_1M: tDPar_LKT1110_N,
#                                 GC.ID_H2PO4_1M: tDPar_LKT1110_P},
#             GC.TS_RCT_LKT1111: {GC.ID_NO3_1M: tDPar_LKT1111_N,
#                                 GC.ID_H2PO4_1M: tDPar_LKT1111_P}}

concChgScale = 1.    # scale of concentration change def. in dConcChg

# --- graphics parameters: component numbers and molecule conc. plot ----------
sPlt_SSC = '01_SelCpConc'               # name of sel. comps and conc. plot
sPlt_SCp = '02_SelCp'                   # name of sel. comps plot
sPlt_SCn = '03_SelConc'                 # name of sel. conc. plot

title_CpCnc = None                      # title of plot
xLbl_CpCnc = GC.S_TIME                  # x-label of plot
yLbl_CpCnc = 'Component incidence and molecule concentration (mM)'
yLbl_Cp = 'Component incidence'
yLbl_Cnc = 'Molecule concentration (mM)'
yLbl_Cnc_N = '$[NO_3^-]$ (mM)'          # y-label of NO3- concentration plot
yLbl_Cnc_P = '$[H_2PO_4^-]$ (mM)'       # y-label of H2PO4- concentration plot
tpMark_CpCnc = None                     # marker type of plot
szMark_CpCnc = 1                        # marker size of plot
ewMark_CpCnc = 1                        # marker edge width of plot
ecMark_CpCnc = (1., 0., 0.)             # marker edge colour of plot
fcMark_CpCnc = (1., 0.5, 0.)            # marker face colour of plot
styLn_CpCnc = 'solid'                   # line style of plot
wdthLn_CpCnc = 1                        # line width of plot
colLn_CpCnc = None                      # line colour of plot
pltAxXY_CpCnc = (True, True)            # plot x- and/or y-axis

# dict. of concentration or component strings to be plotted, incl. y-label
# key: (start string of plot, number of plot)
# value: (list of components to be plotted, y-label of plot, dictionary of ops)
d_Int_vs_Tra = {cK: {GC.S_CP_LSI_SHORT: [GC.S_CP_LSI_SHORT, GC.S_CP_LKI_SHORT],
                     GC.S_CP_LST_SHORT: [GC.S_CP_LST_SHORT, GC.S_CP_LKT_SHORT]}
                for cK in [GC.S_MEAN, GC.S_SUM]}
d_S_vs_K = {cK: {GC.S_CP_LSI_SHORT: [GC.S_CP_LSI_SHORT, GC.S_CP_LST_SHORT],
            GC.S_CP_LKI_SHORT: [GC.S_CP_LKI_SHORT, GC.S_CP_LKT_SHORT]}
            for cK in [GC.S_MEAN, GC.S_SUM]}
d_4_Int_Tra = {cK: {GC.S_CP_LSI_SHORT: [GC.S_CP_LSI_SHORT],
                    GC.S_CP_LST_SHORT: [GC.S_CP_LST_SHORT],
                GC.S_CP_LKI_SHORT: [GC.S_CP_LKI_SHORT],
                GC.S_CP_LKT_SHORT: [GC.S_CP_LKT_SHORT]}
               for cK in [GC.S_MEAN, GC.S_SUM]}
dlSY = {(sPlt_SSC, 'Int_vs_Tra'): (list(GC.DS_RCT) + [GC.ID_NO3_1M],
                                   yLbl_CpCnc, d_Int_vs_Tra),
        (sPlt_SSC, 'S_vs_K'): (list(GC.DS_RCT) + [GC.ID_NO3_1M], yLbl_CpCnc,
                               d_S_vs_K),
        (sPlt_SSC, '4_Int_Tra'): (list(GC.DS_RCT) + [GC.ID_NO3_1M], yLbl_CpCnc,
                                  d_4_Int_Tra),
        # (sPlt_SSC, 'SelSpec4'): ([GC.TS_RCT_LSI01, GC.TS_RCT_LST10,
        #                           GC.TS_RCT_LKI1001, GC.TS_RCT_LKT0110,
        #                           GC.ID_NO3_1M], yLbl_CpCnc, None),
        (sPlt_SCp, 1): (list(GC.DS_RCT)[:8], yLbl_Cp, None),
        (sPlt_SCp, 2): (list(GC.DS_RCT)[8:16], yLbl_Cp, None),
        (sPlt_SCp, 3): (list(GC.DS_RCT)[16:24], yLbl_Cp, None),
        (sPlt_SCp, 4): (list(GC.DS_RCT)[24:], yLbl_Cp, None),
        (sPlt_SCp, None): (list(GC.DS_RCT), yLbl_Cp, d_4_Int_Tra),
        (sPlt_SCn, None): ([GC.ID_NO3_1M, GC.ID_H2PO4_1M], yLbl_Cnc, None)}

# --- path, directory and file names ------------------------------------------
sD_Sys = '99_Sys'
sF_SysEvo = 'SysEvo'

# --- create input dictionary -------------------------------------------------
dIO = {# --- general
       'strOType': strOType,
       'strNSpec': strNSpec,
       'strCS': strCS,
       'strCL': strCL,
       # --- plant cell data
       'VolC': VolC,
       'MassC': MassC,
       # --- data containing components, reactions and conc. change info
       # 'dNCpObj': dNCpObj,
       # 'nCpObj': sum(dNCpObj.values()),
       'dRRC': dRRC,
       'dConcSMo': dConcSMo,
       'dConcChg': dConcChg,
       'concChgScale': concChgScale,
       # --- path, directory and file names
       'sD_Sys': sD_Sys,
       'sF_SysEvo': sF_SysEvo,
       # --- graphics parameters: component numbers and molecule conc. plot
       GC.S_D_PLT: {GC.S_CP_CNC: {'sPlt_SSC': sPlt_SSC,
                                  'sPlt_SCp': sPlt_SCp,
                                  'sPlt_SCn': sPlt_SCn,
                                  'title': title_CpCnc,
                                  'xLbl': xLbl_CpCnc,
                                  'yLbl_CpCnc': yLbl_CpCnc,
                                  'yLbl_Cp': yLbl_Cp,
                                  'yLbl_Cnc': yLbl_Cnc,
                                  'yLbl_Cnc_N': yLbl_Cnc_N,
                                  'yLbl_Cnc_P': yLbl_Cnc_P,
                                  'tpMark': tpMark_CpCnc,
                                  'szMark': szMark_CpCnc,
                                  'ewMark': ewMark_CpCnc,
                                  'ecMark': ecMark_CpCnc,
                                  'fcMark': fcMark_CpCnc,
                                  'styLn': styLn_CpCnc,
                                  'wdthLn': wdthLn_CpCnc,
                                  'colLn': colLn_CpCnc,
                                  'pltAxXY': pltAxXY_CpCnc,
                                  'dlSY': dlSY}}}

###############################################################################
