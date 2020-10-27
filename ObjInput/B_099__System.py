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

# --- data containing state, state transition and conc. change info -----------
# initial number of objects for each possible state
dNStaObj = {GC.S_ST_A_KIN_INT_1001: 300,
            GC.S_ST_B_KIN_TRA_0000: 20,
            GC.S_ST_B_KIN_TRA_0001: 20,
            GC.S_ST_B_KIN_TRA_0010: 20,
            GC.S_ST_B_KIN_TRA_0011: 20,
            GC.S_ST_B_KIN_TRA_0100: 20,
            GC.S_ST_B_KIN_TRA_0101: 20,
            GC.S_ST_B_KIN_TRA_0110: 20,
            GC.S_ST_B_KIN_TRA_0111: 20,
            GC.S_ST_B_KIN_TRA_1000: 20,
            GC.S_ST_B_KIN_TRA_1010: 20,
            GC.S_ST_B_KIN_TRA_1011: 20,
            GC.S_ST_B_KIN_TRA_1100: 20,
            GC.S_ST_B_KIN_TRA_1101: 20,
            GC.S_ST_B_KIN_TRA_1110: 20,
            GC.S_ST_B_KIN_TRA_1111: 20,
            GC.S_ST_C_SPR_INT_0110: 100,
            GC.S_ST_D_SPR_TRA_0000: 20,
            GC.S_ST_D_SPR_TRA_0001: 20,
            GC.S_ST_D_SPR_TRA_0010: 20,
            GC.S_ST_D_SPR_TRA_0011: 20,
            GC.S_ST_D_SPR_TRA_0100: 20,
            GC.S_ST_D_SPR_TRA_0101: 20,
            GC.S_ST_D_SPR_TRA_0111: 20,
            GC.S_ST_D_SPR_TRA_1000: 20,
            GC.S_ST_D_SPR_TRA_1001: 20,
            GC.S_ST_D_SPR_TRA_1010: 20,
            GC.S_ST_D_SPR_TRA_1011: 20,
            GC.S_ST_D_SPR_TRA_1100: 20,
            GC.S_ST_D_SPR_TRA_1101: 20,
            GC.S_ST_D_SPR_TRA_1110: 20,
            GC.S_ST_D_SPR_TRA_1111: 20}

# basic weights for interaction partner changes
wIPC_KAs_SPr = 1.
wIPC_SPr_KAs = 1.1

# basic weights for phosphorylations and dephosphorylations at the four sites
wPyl_S21 = 1.
wPyl_S28 = 1.5
wPyl_S839 = 0.75
wPyl_S870 = 0.9

wDPy_S21 = 1.1
wDPy_S28 = 0.85
wDPy_S839 = 1.15
wDPy_S870 = 0.6

# basic weights for changes between state groups
w_A_B = 0.1
w_B_B = 10.
w_B_C = 0.1
w_C_D = 0.1
w_D_D = 10.
w_D_A = 0.1

# dictionary of basic reaction rate weights
dRRC = {GC.TS_STCH_A1001: (wDPy_S21*w_A_B, wDPy_S870*w_A_B, wPyl_S839*w_A_B, wPyl_S28*w_A_B),
        GC.TS_STCH_B0000: (wPyl_S870*w_B_B, wPyl_S839*w_B_B, wPyl_S28*w_B_B, wPyl_S21*w_B_B),
        GC.TS_STCH_B0001: (wDPy_S870*w_B_B, wPyl_S839*w_B_B, wPyl_S28*w_B_B, wPyl_S21*w_B_B),
        GC.TS_STCH_B0010: (wDPy_S839*w_B_B, wPyl_S870*w_B_B, wPyl_S28*w_B_B, wPyl_S21*w_B_B),
        GC.TS_STCH_B0011: (wDPy_S839*w_B_B, wDPy_S870*w_B_B, wPyl_S28*w_B_B, wPyl_S21*w_B_B),
        GC.TS_STCH_B0100: (wDPy_S28*w_B_B, wPyl_S870*w_B_B, wPyl_S839*w_B_B, wPyl_S21*w_B_B),
        GC.TS_STCH_B0101: (wDPy_S28*w_B_B, wDPy_S870*w_B_B, wPyl_S839*w_B_B, wPyl_S21*w_B_B),
        GC.TS_STCH_B0110: (wDPy_S28*w_B_B, wDPy_S839*w_B_B, wPyl_S870*w_B_B, wPyl_S21*w_B_B,
                           wIPC_KAs_SPr*w_B_C),
        GC.TS_STCH_B0111: (wDPy_S28*w_B_B, wDPy_S839*w_B_B, wDPy_S870*w_B_B, wPyl_S21*w_B_B),
        GC.TS_STCH_B1000: (wDPy_S21*w_B_B, wPyl_S870*w_B_B, wPyl_S839*w_B_B, wPyl_S28*w_B_B),
        GC.TS_STCH_B1010: (wDPy_S21*w_B_B, wDPy_S839*w_B_B, wPyl_S870*w_B_B, wPyl_S28*w_B_B),
        GC.TS_STCH_B1011: (wDPy_S21*w_B_B, wDPy_S839*w_B_B, wDPy_S870*w_B_B, wPyl_S28*w_B_B),
        GC.TS_STCH_B1100: (wDPy_S21*w_B_B, wDPy_S28*w_B_B, wPyl_S870*w_B_B, wPyl_S839*w_B_B),
        GC.TS_STCH_B1101: (wDPy_S21*w_B_B, wDPy_S28*w_B_B, wDPy_S870*w_B_B, wPyl_S839*w_B_B),
        GC.TS_STCH_B1110: (wDPy_S21*w_B_B, wDPy_S28*w_B_B, wDPy_S839*w_B_B, wPyl_S870*w_B_B),
        GC.TS_STCH_B1111: (wDPy_S21*w_B_B, wDPy_S28*w_B_B, wDPy_S839*w_B_B, wDPy_S870*w_B_B),

        GC.TS_STCH_C0110: (wDPy_S28*w_C_D, wDPy_S839*w_C_D, wPyl_S870*w_C_D, wPyl_S21*w_C_D),
        GC.TS_STCH_D0000: (wPyl_S870*w_D_D, wPyl_S839*w_D_D, wPyl_S28*w_D_D, wPyl_S21*w_D_D),
        GC.TS_STCH_D0001: (wDPy_S870*w_D_D, wPyl_S839*w_D_D, wPyl_S28*w_D_D, wPyl_S21*w_D_D),
        GC.TS_STCH_D0010: (wDPy_S839*w_D_D, wPyl_S870*w_D_D, wPyl_S28*w_D_D, wPyl_S21*w_D_D),
        GC.TS_STCH_D0011: (wDPy_S839*w_D_D, wDPy_S870*w_D_D, wPyl_S28*w_D_D, wPyl_S21*w_D_D),
        GC.TS_STCH_D0100: (wDPy_S28*w_D_D, wPyl_S870*w_D_D, wPyl_S839*w_D_D, wPyl_S21*w_D_D),
        GC.TS_STCH_D0101: (wDPy_S28*w_D_D, wDPy_S870*w_D_D, wPyl_S839*w_D_D, wPyl_S21*w_D_D),
        GC.TS_STCH_D0111: (wDPy_S28*w_D_D, wDPy_S839*w_D_D, wDPy_S870*w_D_D, wPyl_S21*w_D_D),
        GC.TS_STCH_D1000: (wDPy_S21*w_D_D, wPyl_S870*w_D_D, wPyl_S839*w_D_D, wPyl_S28*w_D_D),
        GC.TS_STCH_D1001: (wDPy_S21*w_D_D, wDPy_S870*w_D_D, wPyl_S839*w_D_D, wPyl_S28*w_D_D,
                           wIPC_SPr_KAs*w_D_A),
        GC.TS_STCH_D1010: (wDPy_S21*w_D_D, wDPy_S839*w_D_D, wPyl_S870*w_D_D, wPyl_S28*w_D_D),
        GC.TS_STCH_D1011: (wDPy_S21*w_D_D, wDPy_S839*w_D_D, wDPy_S870*w_D_D, wPyl_S28*w_D_D),
        GC.TS_STCH_D1100: (wDPy_S21*w_D_D, wDPy_S28*w_D_D, wPyl_S870*w_D_D, wPyl_S839*w_D_D),
        GC.TS_STCH_D1101: (wDPy_S21*w_D_D, wDPy_S28*w_D_D, wDPy_S870*w_D_D, wPyl_S839*w_D_D),
        GC.TS_STCH_D1110: (wDPy_S21*w_D_D, wDPy_S28*w_D_D, wDPy_S839*w_D_D, wPyl_S870*w_D_D),
        GC.TS_STCH_D1111: (wDPy_S21*w_D_D, wDPy_S28*w_D_D, wDPy_S839*w_D_D, wDPy_S870*w_D_D)}

# dictionary of initial, min. and max. concentrations of small molecules
dConcSMo = {'Ini': {GC.ID_NO3_1M: {'cTp': 'uniform',
                                   'dPar': {'min': 9., 'max': 11.}},
                    GC.ID_H2PO4_1M: {'cTp': 'uniform',
                                     'dPar': {'min': 1.7, 'max': 2.2}}},
            'Min': {GC.ID_NO3_1M: 1., GC.ID_H2PO4_1M: 0.01},
            'Max': {GC.ID_NO3_1M: 1000., GC.ID_H2PO4_1M: 100.}}

# dictionary containing parameters which determine concentration changes of
# small molecules depending on the distribution of states, and vice versa

# depenency of small molecule concentration changes on state
dPar_N_A1001 = {'absChg': -0.001}
dPar_N_B0000 = {'absChg': -0.0}
dPar_N_B0001 = {'absChg': -0.0}
dPar_N_B0010 = {'absChg': -0.0}
dPar_N_B0011 = {'absChg': -0.0}
dPar_N_B0100 = {'absChg': -0.0}
dPar_N_B0101 = {'absChg': -0.0}
dPar_N_B0110 = {'absChg': -0.0}
dPar_N_B0111 = {'absChg': -0.0}
dPar_N_B1000 = {'absChg': -0.0}
dPar_N_B1010 = {'absChg': -0.0}
dPar_N_B1011 = {'absChg': -0.0}
dPar_N_B1100 = {'absChg': -0.0}
dPar_N_B1101 = {'absChg': -0.0}
dPar_N_B1110 = {'absChg': -0.0}
dPar_N_B1111 = {'absChg': -0.0}

dPar_N_C0110 = {'absChg': 0.001}
dPar_N_D0000 = {'absChg': 0.0}
dPar_N_D0001 = {'absChg': 0.0}
dPar_N_D0010 = {'absChg': 0.0}
dPar_N_D0011 = {'absChg': 0.0}
dPar_N_D0100 = {'absChg': 0.0}
dPar_N_D0101 = {'absChg': 0.0}
dPar_N_D0111 = {'absChg': 0.0}
dPar_N_D1000 = {'absChg': 0.0}
dPar_N_D1001 = {'absChg': 0.0}
dPar_N_D1010 = {'absChg': 0.0}
dPar_N_D1011 = {'absChg': 0.0}
dPar_N_D1100 = {'absChg': 0.0}
dPar_N_D1101 = {'absChg': 0.0}
dPar_N_D1110 = {'absChg': 0.0}
dPar_N_D1111 = {'absChg': 0.0}

dPar_P_A1001 = {'absChg': 0}
dPar_P_B0000 = {'absChg': 0}
dPar_P_B0001 = {'absChg': 0}
dPar_P_B0010 = {'absChg': 0}
dPar_P_B0011 = {'absChg': 0}
dPar_P_B0100 = {'absChg': 0}
dPar_P_B0101 = {'absChg': 0}
dPar_P_B0110 = {'absChg': 0}
dPar_P_B0111 = {'absChg': 0}
dPar_P_B1000 = {'absChg': 0}
dPar_P_B1010 = {'absChg': 0}
dPar_P_B1011 = {'absChg': 0}
dPar_P_B1100 = {'absChg': 0}
dPar_P_B1101 = {'absChg': 0}
dPar_P_B1110 = {'absChg': 0}
dPar_P_B1111 = {'absChg': 0}

dPar_P_C0110 = {'absChg': 0}
dPar_P_D0000 = {'absChg': 0}
dPar_P_D0001 = {'absChg': 0}
dPar_P_D0010 = {'absChg': 0}
dPar_P_D0011 = {'absChg': 0}
dPar_P_D0100 = {'absChg': 0}
dPar_P_D0101 = {'absChg': 0}
dPar_P_D0111 = {'absChg': 0}
dPar_P_D1000 = {'absChg': 0}
dPar_P_D1001 = {'absChg': 0}
dPar_P_D1010 = {'absChg': 0}
dPar_P_D1011 = {'absChg': 0}
dPar_P_D1100 = {'absChg': 0}
dPar_P_D1101 = {'absChg': 0}
dPar_P_D1110 = {'absChg': 0}
dPar_P_D1111 = {'absChg': 0}

# parameters of sigmoidal function for interaction partner changes
dPar_B0110_C0110 = {'prMin': 1, 'prMax': 0, 'B': 8., 'C': 0.2, 'D': 0.02}
dPar_D1001_A1001 = {'prMin': 0, 'prMax': 1, 'B': 12., 'C': 2.75, 'D': 0.01}

# parameters of sigmoidal function for (de)phosphorylations at the four sites
dPar_Pyl_S21 = {'prMin': 0, 'prMax': 1, 'B': 10., 'C': 1., 'D': 0.025}
dPar_Pyl_S28 = {'prMin': 1, 'prMax': 0, 'B': 5., 'C': 1.5, 'D': 0.02}
dPar_Pyl_S839 = {'prMin': 1, 'prMax': 0, 'B': 3., 'C': 2.5, 'D': 0.03}
dPar_Pyl_S870 = {'prMin': 0, 'prMax': 1, 'B': 20., 'C': 0.5, 'D': 0.015}

dPar_DPy_S21 = {'prMin': 1, 'prMax': 0, 'B': 1., 'C': 20., 'D': 0.035}
dPar_DPy_S28 = {'prMin': 0, 'prMax': 1, 'B': 12., 'C': 2.75, 'D': 0.01}
dPar_DPy_S839 = {'prMin': 0, 'prMax': 1, 'B': 25., 'C': 5., 'D': 0.03}
dPar_DPy_S870 = {'prMin': 1, 'prMax': 0, 'B': 8., 'C': 0.2, 'D': 0.02}

# dummy parameters of sigmoidal function for H2PO4- dependency
dPar_Dummy = {'prMin': 0, 'prMax': 0, 'B': 0., 'C': 1., 'D': 0.}

# tuples of dictionaries containing parameters of sigmoidal function
tDPar_A1001_N = (dPar_DPy_S21, dPar_DPy_S870, dPar_Pyl_S839, dPar_Pyl_S28)
tDPar_B0000_N = (dPar_Pyl_S870, dPar_Pyl_S839, dPar_Pyl_S28, dPar_Pyl_S21)
tDPar_B0001_N = (dPar_DPy_S870, dPar_Pyl_S839, dPar_Pyl_S28, dPar_Pyl_S21)
tDPar_B0010_N = (dPar_DPy_S839, dPar_Pyl_S870, dPar_Pyl_S28, dPar_Pyl_S21)
tDPar_B0011_N = (dPar_DPy_S839, dPar_DPy_S870, dPar_Pyl_S28, dPar_Pyl_S21)
tDPar_B0100_N = (dPar_DPy_S28, dPar_Pyl_S870, dPar_Pyl_S839, dPar_Pyl_S21)
tDPar_B0101_N = (dPar_DPy_S28, dPar_DPy_S870, dPar_Pyl_S839, dPar_Pyl_S21)
tDPar_B0110_N = (dPar_DPy_S28, dPar_DPy_S839, dPar_Pyl_S870, dPar_Pyl_S21,
                 dPar_B0110_C0110)
tDPar_B0111_N = (dPar_DPy_S28, dPar_DPy_S839, dPar_DPy_S870, dPar_Pyl_S21)
tDPar_B1000_N = (dPar_DPy_S21, dPar_Pyl_S870, dPar_Pyl_S839, dPar_Pyl_S28)
tDPar_B1010_N = (dPar_DPy_S21, dPar_DPy_S839, dPar_Pyl_S870, dPar_Pyl_S28)
tDPar_B1011_N = (dPar_DPy_S21, dPar_DPy_S839, dPar_DPy_S870, dPar_Pyl_S28)
tDPar_B1100_N = (dPar_DPy_S21, dPar_DPy_S28, dPar_Pyl_S870, dPar_Pyl_S839)
tDPar_B1101_N = (dPar_DPy_S21, dPar_DPy_S28, dPar_DPy_S870, dPar_Pyl_S839)
tDPar_B1110_N = (dPar_DPy_S21, dPar_DPy_S28, dPar_DPy_S839, dPar_Pyl_S870)
tDPar_B1111_N = (dPar_DPy_S21, dPar_DPy_S28, dPar_DPy_S839, dPar_DPy_S870)

tDPar_C0110_N = (dPar_DPy_S28, dPar_DPy_S839, dPar_Pyl_S870, dPar_Pyl_S21)
tDPar_D0000_N = (dPar_Pyl_S870, dPar_Pyl_S839, dPar_Pyl_S28, dPar_Pyl_S21)
tDPar_D0001_N = (dPar_DPy_S870, dPar_Pyl_S839, dPar_Pyl_S28, dPar_Pyl_S21)
tDPar_D0010_N = (dPar_DPy_S839, dPar_Pyl_S870, dPar_Pyl_S28, dPar_Pyl_S21)
tDPar_D0011_N = (dPar_DPy_S839, dPar_DPy_S870, dPar_Pyl_S28, dPar_Pyl_S21)
tDPar_D0100_N = (dPar_DPy_S28, dPar_Pyl_S870, dPar_Pyl_S839, dPar_Pyl_S21)
tDPar_D0101_N = (dPar_DPy_S28, dPar_DPy_S870, dPar_Pyl_S839, dPar_Pyl_S21)
tDPar_D0111_N = (dPar_DPy_S28, dPar_DPy_S839, dPar_DPy_S870, dPar_Pyl_S21)
tDPar_D1000_N = (dPar_DPy_S21, dPar_Pyl_S870, dPar_Pyl_S839, dPar_Pyl_S28)
tDPar_D1001_N = (dPar_DPy_S21, dPar_DPy_S870, dPar_Pyl_S839, dPar_Pyl_S28,
                 dPar_D1001_A1001)
tDPar_D1010_N = (dPar_DPy_S21, dPar_DPy_S839, dPar_Pyl_S870, dPar_Pyl_S28)
tDPar_D1011_N = (dPar_DPy_S21, dPar_DPy_S839, dPar_DPy_S870, dPar_Pyl_S28)
tDPar_D1100_N = (dPar_DPy_S21, dPar_DPy_S28, dPar_Pyl_S870, dPar_Pyl_S839)
tDPar_D1101_N = (dPar_DPy_S21, dPar_DPy_S28, dPar_DPy_S870, dPar_Pyl_S839)
tDPar_D1110_N = (dPar_DPy_S21, dPar_DPy_S28, dPar_DPy_S839, dPar_Pyl_S870)
tDPar_D1111_N = (dPar_DPy_S21, dPar_DPy_S28, dPar_DPy_S839, dPar_Pyl_S870)

tDPar_A1001_P = (dPar_Dummy, dPar_Dummy, dPar_Dummy, dPar_Dummy)
tDPar_B0000_P = (dPar_Dummy, dPar_Dummy, dPar_Dummy, dPar_Dummy)
tDPar_B0001_P = (dPar_Dummy, dPar_Dummy, dPar_Dummy, dPar_Dummy)
tDPar_B0010_P = (dPar_Dummy, dPar_Dummy, dPar_Dummy, dPar_Dummy)
tDPar_B0011_P = (dPar_Dummy, dPar_Dummy, dPar_Dummy, dPar_Dummy)
tDPar_B0100_P = (dPar_Dummy, dPar_Dummy, dPar_Dummy, dPar_Dummy)
tDPar_B0101_P = (dPar_Dummy, dPar_Dummy, dPar_Dummy, dPar_Dummy)
tDPar_B0110_P = (dPar_Dummy, dPar_Dummy, dPar_Dummy, dPar_Dummy, dPar_Dummy)
tDPar_B0111_P = (dPar_Dummy, dPar_Dummy, dPar_Dummy, dPar_Dummy)
tDPar_B1000_P = (dPar_Dummy, dPar_Dummy, dPar_Dummy, dPar_Dummy)
tDPar_B1010_P = (dPar_Dummy, dPar_Dummy, dPar_Dummy, dPar_Dummy)
tDPar_B1011_P = (dPar_Dummy, dPar_Dummy, dPar_Dummy, dPar_Dummy)
tDPar_B1100_P = (dPar_Dummy, dPar_Dummy, dPar_Dummy, dPar_Dummy)
tDPar_B1101_P = (dPar_Dummy, dPar_Dummy, dPar_Dummy, dPar_Dummy)
tDPar_B1110_P = (dPar_Dummy, dPar_Dummy, dPar_Dummy, dPar_Dummy)
tDPar_B1111_P = (dPar_Dummy, dPar_Dummy, dPar_Dummy, dPar_Dummy)

tDPar_C0110_P = (dPar_Dummy, dPar_Dummy, dPar_Dummy, dPar_Dummy)
tDPar_D0000_P = (dPar_Dummy, dPar_Dummy, dPar_Dummy, dPar_Dummy)
tDPar_D0001_P = (dPar_Dummy, dPar_Dummy, dPar_Dummy, dPar_Dummy)
tDPar_D0010_P = (dPar_Dummy, dPar_Dummy, dPar_Dummy, dPar_Dummy)
tDPar_D0011_P = (dPar_Dummy, dPar_Dummy, dPar_Dummy, dPar_Dummy)
tDPar_D0100_P = (dPar_Dummy, dPar_Dummy, dPar_Dummy, dPar_Dummy)
tDPar_D0101_P = (dPar_Dummy, dPar_Dummy, dPar_Dummy, dPar_Dummy)
tDPar_D0111_P = (dPar_Dummy, dPar_Dummy, dPar_Dummy, dPar_Dummy)
tDPar_D1000_P = (dPar_Dummy, dPar_Dummy, dPar_Dummy, dPar_Dummy)
tDPar_D1001_P = (dPar_Dummy, dPar_Dummy, dPar_Dummy, dPar_Dummy, dPar_Dummy)
tDPar_D1010_P = (dPar_Dummy, dPar_Dummy, dPar_Dummy, dPar_Dummy)
tDPar_D1011_P = (dPar_Dummy, dPar_Dummy, dPar_Dummy, dPar_Dummy)
tDPar_D1100_P = (dPar_Dummy, dPar_Dummy, dPar_Dummy, dPar_Dummy)
tDPar_D1101_P = (dPar_Dummy, dPar_Dummy, dPar_Dummy, dPar_Dummy)
tDPar_D1110_P = (dPar_Dummy, dPar_Dummy, dPar_Dummy, dPar_Dummy)
tDPar_D1111_P = (dPar_Dummy, dPar_Dummy, dPar_Dummy, dPar_Dummy)

# GC.ID_NO3_1M, GC.ID_H2PO4_1M: max. changes per unit time
dConcChg = {GC.ID_NO3_1M: {GC.S_ST_A_KIN_INT_1001: dPar_N_A1001,
                           GC.S_ST_B_KIN_TRA_0000: dPar_N_B0000,
                           GC.S_ST_B_KIN_TRA_0001: dPar_N_B0001,
                           GC.S_ST_B_KIN_TRA_0010: dPar_N_B0010,
                           GC.S_ST_B_KIN_TRA_0011: dPar_N_B0011,
                           GC.S_ST_B_KIN_TRA_0100: dPar_N_B0100,
                           GC.S_ST_B_KIN_TRA_0101: dPar_N_B0101,
                           GC.S_ST_B_KIN_TRA_0110: dPar_N_B0110,
                           GC.S_ST_B_KIN_TRA_0111: dPar_N_B0111,
                           GC.S_ST_B_KIN_TRA_1000: dPar_N_B1000,
                           GC.S_ST_B_KIN_TRA_1010: dPar_N_B1010,
                           GC.S_ST_B_KIN_TRA_1011: dPar_N_B1011,
                           GC.S_ST_B_KIN_TRA_1100: dPar_N_B1100,
                           GC.S_ST_B_KIN_TRA_1101: dPar_N_B1101,
                           GC.S_ST_B_KIN_TRA_1110: dPar_N_B1110,
                           GC.S_ST_B_KIN_TRA_1111: dPar_N_B1111,

                           GC.S_ST_C_SPR_INT_0110: dPar_N_C0110,
                           GC.S_ST_D_SPR_TRA_0000: dPar_N_D0000,
                           GC.S_ST_D_SPR_TRA_0001: dPar_N_D0001,
                           GC.S_ST_D_SPR_TRA_0010: dPar_N_D0010,
                           GC.S_ST_D_SPR_TRA_0011: dPar_N_D0011,
                           GC.S_ST_D_SPR_TRA_0100: dPar_N_D0100,
                           GC.S_ST_D_SPR_TRA_0101: dPar_N_D0101,
                           GC.S_ST_D_SPR_TRA_0111: dPar_N_D0111,
                           GC.S_ST_D_SPR_TRA_1000: dPar_N_D1000,
                           GC.S_ST_D_SPR_TRA_1001: dPar_N_D1001,
                           GC.S_ST_D_SPR_TRA_1010: dPar_N_D1010,
                           GC.S_ST_D_SPR_TRA_1011: dPar_N_D1011,
                           GC.S_ST_D_SPR_TRA_1100: dPar_N_D1100,
                           GC.S_ST_D_SPR_TRA_1101: dPar_N_D1101,
                           GC.S_ST_D_SPR_TRA_1110: dPar_N_D1110,
                           GC.S_ST_D_SPR_TRA_1111: dPar_N_D1111},

            GC.ID_H2PO4_1M: {GC.S_ST_A_KIN_INT_1001: dPar_P_A1001,
                             GC.S_ST_B_KIN_TRA_0000: dPar_P_B0000,
                             GC.S_ST_B_KIN_TRA_0001: dPar_P_B0001,
                             GC.S_ST_B_KIN_TRA_0010: dPar_P_B0010,
                             GC.S_ST_B_KIN_TRA_0011: dPar_P_B0011,
                             GC.S_ST_B_KIN_TRA_0100: dPar_P_B0100,
                             GC.S_ST_B_KIN_TRA_0101: dPar_P_B0101,
                             GC.S_ST_B_KIN_TRA_0110: dPar_P_B0110,
                             GC.S_ST_B_KIN_TRA_0111: dPar_P_B0111,
                             GC.S_ST_B_KIN_TRA_1000: dPar_P_B1000,
                             GC.S_ST_B_KIN_TRA_1010: dPar_P_B1010,
                             GC.S_ST_B_KIN_TRA_1011: dPar_P_B1011,
                             GC.S_ST_B_KIN_TRA_1100: dPar_P_B1100,
                             GC.S_ST_B_KIN_TRA_1101: dPar_P_B1101,
                             GC.S_ST_B_KIN_TRA_1110: dPar_P_B1110,
                             GC.S_ST_B_KIN_TRA_1111: dPar_P_B1111,

                             GC.S_ST_C_SPR_INT_0110: dPar_P_C0110,
                             GC.S_ST_D_SPR_TRA_0000: dPar_P_D0000,
                             GC.S_ST_D_SPR_TRA_0001: dPar_P_D0001,
                             GC.S_ST_D_SPR_TRA_0010: dPar_P_D0010,
                             GC.S_ST_D_SPR_TRA_0011: dPar_P_D0011,
                             GC.S_ST_D_SPR_TRA_0100: dPar_P_D0100,
                             GC.S_ST_D_SPR_TRA_0101: dPar_P_D0101,
                             GC.S_ST_D_SPR_TRA_0111: dPar_P_D0111,
                             GC.S_ST_D_SPR_TRA_1000: dPar_P_D1000,
                             GC.S_ST_D_SPR_TRA_1001: dPar_P_D1001,
                             GC.S_ST_D_SPR_TRA_1010: dPar_P_D1010,
                             GC.S_ST_D_SPR_TRA_1011: dPar_P_D1011,
                             GC.S_ST_D_SPR_TRA_1100: dPar_P_D1100,
                             GC.S_ST_D_SPR_TRA_1101: dPar_P_D1101,
                             GC.S_ST_D_SPR_TRA_1110: dPar_P_D1110,
                             GC.S_ST_D_SPR_TRA_1111: dPar_P_D1111},

            GC.TS_STCH_A1001: {GC.ID_NO3_1M: tDPar_A1001_N,
                               GC.ID_H2PO4_1M: tDPar_A1001_P},
            GC.TS_STCH_B0000: {GC.ID_NO3_1M: tDPar_B0000_N,
                               GC.ID_H2PO4_1M: tDPar_B0000_P},
            GC.TS_STCH_B0001: {GC.ID_NO3_1M: tDPar_B0001_N,
                               GC.ID_H2PO4_1M: tDPar_B0001_P},
            GC.TS_STCH_B0010: {GC.ID_NO3_1M: tDPar_B0010_N,
                               GC.ID_H2PO4_1M: tDPar_B0010_P},
            GC.TS_STCH_B0011: {GC.ID_NO3_1M: tDPar_B0011_N,
                               GC.ID_H2PO4_1M: tDPar_B0011_P},
            GC.TS_STCH_B0100: {GC.ID_NO3_1M: tDPar_B0100_N,
                               GC.ID_H2PO4_1M: tDPar_B0100_P},
            GC.TS_STCH_B0101: {GC.ID_NO3_1M: tDPar_B0101_N,
                               GC.ID_H2PO4_1M: tDPar_B0101_P},
            GC.TS_STCH_B0110: {GC.ID_NO3_1M: tDPar_B0110_N,
                               GC.ID_H2PO4_1M: tDPar_B0110_P},
            GC.TS_STCH_B0111: {GC.ID_NO3_1M: tDPar_B0111_N,
                               GC.ID_H2PO4_1M: tDPar_B0111_P},
            GC.TS_STCH_B1000: {GC.ID_NO3_1M: tDPar_B1000_N,
                               GC.ID_H2PO4_1M: tDPar_B1000_P},
            GC.TS_STCH_B1010: {GC.ID_NO3_1M: tDPar_B1010_N,
                               GC.ID_H2PO4_1M: tDPar_B1010_P},
            GC.TS_STCH_B1011: {GC.ID_NO3_1M: tDPar_B1011_N,
                               GC.ID_H2PO4_1M: tDPar_B1011_P},
            GC.TS_STCH_B1100: {GC.ID_NO3_1M: tDPar_B1100_N,
                               GC.ID_H2PO4_1M: tDPar_B1100_P},
            GC.TS_STCH_B1101: {GC.ID_NO3_1M: tDPar_B1101_N,
                               GC.ID_H2PO4_1M: tDPar_B1101_P},
            GC.TS_STCH_B1110: {GC.ID_NO3_1M: tDPar_B1110_N,
                               GC.ID_H2PO4_1M: tDPar_B1110_P},
            GC.TS_STCH_B1111: {GC.ID_NO3_1M: tDPar_B1111_N,
                               GC.ID_H2PO4_1M: tDPar_B1111_P},

            GC.TS_STCH_C0110: {GC.ID_NO3_1M: tDPar_C0110_N,
                               GC.ID_H2PO4_1M: tDPar_C0110_P},
            GC.TS_STCH_D0000: {GC.ID_NO3_1M: tDPar_D0000_N,
                               GC.ID_H2PO4_1M: tDPar_D0000_P},
            GC.TS_STCH_D0001: {GC.ID_NO3_1M: tDPar_D0001_N,
                               GC.ID_H2PO4_1M: tDPar_D0001_P},
            GC.TS_STCH_D0010: {GC.ID_NO3_1M: tDPar_D0010_N,
                               GC.ID_H2PO4_1M: tDPar_D0010_P},
            GC.TS_STCH_D0011: {GC.ID_NO3_1M: tDPar_D0011_N,
                               GC.ID_H2PO4_1M: tDPar_D0011_P},
            GC.TS_STCH_D0100: {GC.ID_NO3_1M: tDPar_D0100_N,
                               GC.ID_H2PO4_1M: tDPar_D0100_P},
            GC.TS_STCH_D0101: {GC.ID_NO3_1M: tDPar_D0101_N,
                               GC.ID_H2PO4_1M: tDPar_D0101_P},
            GC.TS_STCH_D0111: {GC.ID_NO3_1M: tDPar_D0111_N,
                               GC.ID_H2PO4_1M: tDPar_D0111_P},
            GC.TS_STCH_D1000: {GC.ID_NO3_1M: tDPar_D1000_N,
                               GC.ID_H2PO4_1M: tDPar_D1000_P},
            GC.TS_STCH_D1001: {GC.ID_NO3_1M: tDPar_D1001_N,
                               GC.ID_H2PO4_1M: tDPar_D1001_P},
            GC.TS_STCH_D1010: {GC.ID_NO3_1M: tDPar_D1010_N,
                               GC.ID_H2PO4_1M: tDPar_D1010_P},
            GC.TS_STCH_D1011: {GC.ID_NO3_1M: tDPar_D1011_N,
                               GC.ID_H2PO4_1M: tDPar_D1011_P},
            GC.TS_STCH_D1100: {GC.ID_NO3_1M: tDPar_D1100_N,
                               GC.ID_H2PO4_1M: tDPar_D1100_P},
            GC.TS_STCH_D1101: {GC.ID_NO3_1M: tDPar_D1101_N,
                               GC.ID_H2PO4_1M: tDPar_D1101_P},
            GC.TS_STCH_D1110: {GC.ID_NO3_1M: tDPar_D1110_N,
                               GC.ID_H2PO4_1M: tDPar_D1110_P},
            GC.TS_STCH_D1111: {GC.ID_NO3_1M: tDPar_D1111_N,
                               GC.ID_H2PO4_1M: tDPar_D1111_P}}

concChgScale = 1.    # scale of concentration change def. in dConcChg

# --- graphics parameters: state numbers and molecule conc. plot --------------
sPlt_SSC = '01_SelStatesConc'           # name of all states and conc. plot
sPlt_SSt = '02_SelStates'               # name of sel. states and conc. plot
sPlt_SCn = '03_SelConc'                 # name of sel. states and conc. plot

title_StCnc = None                      # title of plot
xLbl_StCnc = GC.S_TIME                  # x-label of plot
yLbl_StCnc = 'State incidence and molecule concentration (mM)'
yLbl_St = 'State incidence'
yLbl_Cnc = 'Molecule concentration (mM)'
yLbl_Cnc_N = '$[NO_3^-]$ (mM)'          # y-label of NO3- concentration plot
yLbl_Cnc_P = '$[H_2PO_4^-]$ (mM)'       # y-label of H2PO4- concentration plot
tpMark_StCnc = None                     # marker type of plot
szMark_StCnc = 1                        # marker size of plot
ewMark_StCnc = 1                        # marker edge width of plot
ecMark_StCnc = (1., 0., 0.)             # marker edge colour of plot
fcMark_StCnc = (1., 0.5, 0.)            # marker face colour of plot
styLn_StCnc = 'solid'                   # line style of plot
wdthLn_StCnc = 1                        # line width of plot
colLn_StCnc = None                      # line colour of plot
pltAxXY_StCnc = (True, True)            # plot x- and/or y-axis

# dict. of concentration or state strings to be plotted, incl. y-label
# key: (start string of plot, number of plot)
# value: (list of states to be plotted, y-label of plot, dictionary of ops)
dAC = {cK: {GC.S_ST_A_SIMPLE: [GC.S_ST_A_SIMPLE, GC.S_ST_B_SIMPLE],
            GC.S_ST_C_SIMPLE: [GC.S_ST_C_SIMPLE, GC.S_ST_D_SIMPLE]}
       for cK in [GC.S_MEAN, GC.S_SUM]}
dAB = {cK: {GC.S_ST_A_SIMPLE: [GC.S_ST_A_SIMPLE, GC.S_ST_C_SIMPLE],
            GC.S_ST_B_SIMPLE: [GC.S_ST_B_SIMPLE, GC.S_ST_D_SIMPLE]}
       for cK in [GC.S_MEAN, GC.S_SUM]}
dABCD = {cK: {GC.S_ST_A_SIMPLE: [GC.S_ST_A_SIMPLE],
              GC.S_ST_B_SIMPLE: [GC.S_ST_B_SIMPLE],
              GC.S_ST_C_SIMPLE: [GC.S_ST_C_SIMPLE],
              GC.S_ST_D_SIMPLE: [GC.S_ST_D_SIMPLE]}
         for cK in [GC.S_MEAN, GC.S_SUM]}
dlSY = {(sPlt_SSC, 'AC'): (list(GC.DS_STCH) + [GC.ID_NO3_1M], yLbl_StCnc, dAC),
        (sPlt_SSC, 'AB'): (list(GC.DS_STCH) + [GC.ID_NO3_1M], yLbl_StCnc, dAB),
        (sPlt_SSC, 'ABCD'): (list(GC.DS_STCH) + [GC.ID_NO3_1M], yLbl_StCnc,
                             dABCD),
        (sPlt_SSC, 'Sel4'): ([GC.S_ST_A_KIN_INT_1001, GC.S_ST_B_KIN_TRA_0110,
                              GC.S_ST_C_SPR_INT_0110, GC.S_ST_D_SPR_TRA_1001,
                              GC.ID_NO3_1M], yLbl_StCnc, None),
        (sPlt_SSt, 1): (list(GC.DS_STCH)[:8], yLbl_St, None),
        (sPlt_SSt, 2): (list(GC.DS_STCH)[8:16], yLbl_St, None),
        (sPlt_SSt, 3): (list(GC.DS_STCH)[16:24], yLbl_St, None),
        (sPlt_SSt, 4): (list(GC.DS_STCH)[24:], yLbl_St, None),
        (sPlt_SSt, None): (list(GC.DS_STCH), yLbl_St, dABCD),
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
       # --- data containing state, state transition and conc. change info
       'dNStaObj': dNStaObj,
       'nStaObj': sum(dNStaObj.values()),
       'dRRC': dRRC,
       'dConcSMo': dConcSMo,
       'dConcChg': dConcChg,
       'concChgScale': concChgScale,
       # --- path, directory and file names
       'sD_Sys': sD_Sys,
       'sF_SysEvo': sF_SysEvo,
       # --- graphics parameters: state numbers and molecule conc. plot
       GC.S_D_PLT: {GC.S_STA_CNC: {'sPlt_SSC': sPlt_SSC,
                                   'sPlt_SSt': sPlt_SSt,
                                   'sPlt_SCn': sPlt_SCn,
                                   'title': title_StCnc,
                                   'xLbl': xLbl_StCnc,
                                   'yLbl_StCnc': yLbl_StCnc,
                                   'yLbl_St': yLbl_St,
                                   'yLbl_Cnc': yLbl_Cnc,
                                   'yLbl_Cnc_N': yLbl_Cnc_N,
                                   'yLbl_Cnc_P': yLbl_Cnc_P,
                                   'tpMark': tpMark_StCnc,
                                   'szMark': szMark_StCnc,
                                   'ewMark': ewMark_StCnc,
                                   'ecMark': ecMark_StCnc,
                                   'fcMark': fcMark_StCnc,
                                   'styLn': styLn_StCnc,
                                   'wdthLn': wdthLn_StCnc,
                                   'colLn': colLn_StCnc,
                                   'pltAxXY': pltAxXY_StCnc,
                                   'dlSY': dlSY}}}

###############################################################################
