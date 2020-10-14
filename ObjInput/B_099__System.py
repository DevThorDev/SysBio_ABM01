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
# initial number of objects for each possible state
dNStaObj = {GC.S_ST_A_KIN_INT_1001: 630,
            GC.S_ST_B_KIN_TRA_0000: 10,
            GC.S_ST_B_KIN_TRA_0001: 20,
            GC.S_ST_B_KIN_TRA_0010: 30,
            GC.S_ST_B_KIN_TRA_0011: 40,
            GC.S_ST_B_KIN_TRA_0100: 50,
            GC.S_ST_B_KIN_TRA_0101: 60,
            GC.S_ST_B_KIN_TRA_0110: 70,
            GC.S_ST_B_KIN_TRA_0111: 80,
            GC.S_ST_B_KIN_TRA_1000: 90,
            GC.S_ST_B_KIN_TRA_1010: 95,
            GC.S_ST_B_KIN_TRA_1011: 85,
            GC.S_ST_B_KIN_TRA_1100: 75,
            GC.S_ST_B_KIN_TRA_1101: 65,
            GC.S_ST_B_KIN_TRA_1110: 55,
            GC.S_ST_B_KIN_TRA_1111: 45,
            GC.S_ST_C_SPR_INT_0110: 100,
            GC.S_ST_D_SPR_TRA_0000: 15,
            GC.S_ST_D_SPR_TRA_0001: 25,
            GC.S_ST_D_SPR_TRA_0010: 35,
            GC.S_ST_D_SPR_TRA_0011: 45,
            GC.S_ST_D_SPR_TRA_0100: 55,
            GC.S_ST_D_SPR_TRA_0101: 65,
            GC.S_ST_D_SPR_TRA_0111: 75,
            GC.S_ST_D_SPR_TRA_1000: 85,
            GC.S_ST_D_SPR_TRA_1001: 95,
            GC.S_ST_D_SPR_TRA_1010: 80,
            GC.S_ST_D_SPR_TRA_1011: 70,
            GC.S_ST_D_SPR_TRA_1100: 60,
            GC.S_ST_D_SPR_TRA_1101: 50,
            GC.S_ST_D_SPR_TRA_1110: 40,
            GC.S_ST_D_SPR_TRA_1111: 30}

# basic weights for interaction partner changes
wIPC_KAs_SPr = 5.
wIPC_SPr_KAs = 4.

# basic weights for phosphorylations and dephosphorylations at the four sites
wPyl_S21 = 1.
wPyl_S28 = 1.5
wPyl_S839 = 0.75
wPyl_S870 = 0.9

wDPy_S21 = 1.1
wDPy_S28 = 0.85
wDPy_S839 = 1.15
wDPy_S870 = 0.6

# dictionary of basic reaction rate weights
dRRC = {GC.TS_STCH_A1001: (wDPy_S21, wDPy_S870, wPyl_S839, wPyl_S28),
        GC.TS_STCH_B0000: (wPyl_S870, wPyl_S839, wPyl_S28, wPyl_S21),
        GC.TS_STCH_B0001: (wDPy_S870, wPyl_S839, wPyl_S28, wPyl_S21),
        GC.TS_STCH_B0010: (wDPy_S839, wPyl_S870, wPyl_S28, wPyl_S21),
        GC.TS_STCH_B0011: (wDPy_S839, wDPy_S870, wPyl_S28, wPyl_S21),
        GC.TS_STCH_B0100: (wDPy_S28, wPyl_S870, wPyl_S839, wPyl_S21),
        GC.TS_STCH_B0101: (wDPy_S28, wDPy_S870, wPyl_S839, wPyl_S21),
        GC.TS_STCH_B0110: (wDPy_S28, wDPy_S839, wPyl_S870, wPyl_S21,
                           wIPC_KAs_SPr),
        GC.TS_STCH_B0111: (wDPy_S28, wDPy_S839, wDPy_S870, wPyl_S21),
        GC.TS_STCH_B1000: (wDPy_S21, wPyl_S870, wPyl_S839, wPyl_S28),
        GC.TS_STCH_B1010: (wDPy_S21, wDPy_S839, wPyl_S870, wPyl_S28),
        GC.TS_STCH_B1011: (wDPy_S21, wDPy_S839, wDPy_S870, wPyl_S28),
        GC.TS_STCH_B1100: (wDPy_S21, wDPy_S28, wPyl_S870, wPyl_S839),
        GC.TS_STCH_B1101: (wDPy_S21, wDPy_S28, wDPy_S870, wPyl_S839),
        GC.TS_STCH_B1110: (wDPy_S21, wDPy_S28, wDPy_S839, wPyl_S870),
        GC.TS_STCH_B1111: (wDPy_S21, wDPy_S28, wDPy_S839, wDPy_S870),
        
        GC.TS_STCH_C0110: (wDPy_S28, wDPy_S839, wPyl_S870, wPyl_S21),
        GC.TS_STCH_D0000: (wPyl_S870, wPyl_S839, wPyl_S28, wPyl_S21),
        GC.TS_STCH_D0001: (wDPy_S870, wPyl_S839, wPyl_S28, wPyl_S21),
        GC.TS_STCH_D0010: (wDPy_S839, wPyl_S870, wPyl_S28, wPyl_S21),
        GC.TS_STCH_D0011: (wDPy_S839, wDPy_S870, wPyl_S28, wPyl_S21),
        GC.TS_STCH_D0100: (wDPy_S28, wPyl_S870, wPyl_S839, wPyl_S21),
        GC.TS_STCH_D0101: (wDPy_S28, wDPy_S870, wPyl_S839, wPyl_S21),
        GC.TS_STCH_D0111: (wDPy_S28, wDPy_S839, wDPy_S870, wPyl_S21),
        GC.TS_STCH_D1000: (wDPy_S21, wPyl_S870, wPyl_S839, wPyl_S28),
        GC.TS_STCH_D1001: (wDPy_S21, wDPy_S870, wPyl_S839, wPyl_S28,
                           wIPC_SPr_KAs),
        GC.TS_STCH_D1010: (wDPy_S21, wDPy_S839, wPyl_S870, wPyl_S28),
        GC.TS_STCH_D1011: (wDPy_S21, wDPy_S839, wDPy_S870, wPyl_S28),
        GC.TS_STCH_D1100: (wDPy_S21, wDPy_S28, wPyl_S870, wPyl_S839),
        GC.TS_STCH_D1101: (wDPy_S21, wDPy_S28, wDPy_S870, wPyl_S839),
        GC.TS_STCH_D1110: (wDPy_S21, wDPy_S28, wDPy_S839, wPyl_S870),
        GC.TS_STCH_D1111: (wDPy_S21, wDPy_S28, wDPy_S839, wDPy_S870)}

# dictionary of initial, min. and max. concentrations of small molecules
dConcSMo = {'Ini': {GC.ID_NO3_1M: {'cTp': 'uniform',
                                   'dPar': {'min': 250., 'max': 350.}},
                    GC.ID_H2PO4_1M: {'cTp': 'uniform',
                                     'dPar': {'min': 1.7, 'max': 2.2}}},
            'Min': {GC.ID_NO3_1M: 1., GC.ID_H2PO4_1M: 0.01},
            'Max': {GC.ID_NO3_1M: 1000., GC.ID_H2PO4_1M: 100.}}

# dictionary containing parameters which determine concentration changes of
# small molecules depending on the distribution of states, and vice versa

# depenency of small molecule concentration changes on state
dPar_N_A1001 = {'absChg': -20.}
dPar_N_B0000 = {'absChg': -0.5}
dPar_N_B0001 = {'absChg': -0.3}
dPar_N_B0010 = {'absChg': -0.4}
dPar_N_B0011 = {'absChg': -0.6}
dPar_N_B0100 = {'absChg': -0.55}
dPar_N_B0101 = {'absChg': -0.45}
dPar_N_B0110 = {'absChg': -0.35}
dPar_N_B0111 = {'absChg': -0.65}
dPar_N_B1000 = {'absChg': -0.75}
dPar_N_B1010 = {'absChg': -0.8}
dPar_N_B1011 = {'absChg': -0.7}
dPar_N_B1100 = {'absChg': -0.125}
dPar_N_B1101 = {'absChg': -0.375}
dPar_N_B1110 = {'absChg': -0.9}
dPar_N_B1111 = {'absChg': -0.95}

dPar_N_C0110 = {'absChg': 10.}
dPar_N_D0000 = {'absChg': 0.5}
dPar_N_D0001 = {'absChg': 0.3}
dPar_N_D0010 = {'absChg': 0.4}
dPar_N_D0011 = {'absChg': 0.6}
dPar_N_D0100 = {'absChg': 0.55}
dPar_N_D0101 = {'absChg': 0.45}
dPar_N_D0111 = {'absChg': 0.65}
dPar_N_D1000 = {'absChg': 0.75}
dPar_N_D1001 = {'absChg': 0.35}
dPar_N_D1010 = {'absChg': 0.8}
dPar_N_D1011 = {'absChg': 0.7}
dPar_N_D1100 = {'absChg': 0.125}
dPar_N_D1101 = {'absChg': 0.375}
dPar_N_D1110 = {'absChg': 0.9}
dPar_N_D1111 = {'absChg': 0.95}

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
       'dConcSMo': dConcSMo,
       'dConcChg': dConcChg,
       'concChgScale': concChgScale,
       # --- path, directory and file names
       'sD_Sys': sD_Sys,
       'sF_SysEvo': sF_SysEvo}

###############################################################################
