# -*- coding: utf-8 -*-
###############################################################################
# --- C_00__GenConstants.py ---------------------------------------------------
###############################################################################
# --- names of files and dirs -------------------------------------------------
S_D_OBJINP = 'ObjInput'
S_F_OBJINP_PRE = 'B_'

S_EXT_CSV = 'csv'
S_EXT_PY = 'py'
S_EXT_PDF = 'pdf'

# --- constants related to molecule objects -----------------------------------
SPC_LPR_A = 'LPr_A'
SPC_SPR_A = 'SPr_A'
SPC_KAS_A = 'KAs_A'
SPC_KAS_X = 'KAs_X'
SPC_L_SMO = 'lSMo'

ID_LPR_NRT2P1 = 'LPr_NRT2p1'
ID_SPR_NAR2P1 = 'SPr_NAR2p1'
ID_KAS_HPCAL1, ID_KAS_X = 'KAs_HPCAL1', 'KAs_X'
ID_KAS_1, ID_KAS_2, ID_KAS_3 = 'KAs1', 'KAs2', 'KAs3'
ID_PAS_1, ID_PAS_2, ID_PAS_3, ID_PAS_4 = 'PAs1', 'PAs2', 'PAs3', 'PAs4'
ID_NO3_1M = 'NO3_1m'
ID_H2PO4_1M = 'H2PO4_1m'

L_ID_MOL = ['Mol']
L_ID_PRO = ['Pro']
L_ID_LPR = ['LPr', ID_LPR_NRT2P1]
L_ID_SPR = ['SPr', ID_SPR_NAR2P1]
L_ID_ENZ = ['Enz']
L_ID_KAS = ['KAs', ID_KAS_HPCAL1, ID_KAS_X, ID_KAS_1, ID_KAS_2, ID_KAS_3]
L_ID_PAS = ['PAs', ID_PAS_1, ID_PAS_2, ID_PAS_3, ID_PAS_4]
L_ID_MET = ['Met']
L_ID_LMO = ['LMo']
L_ID_SMO = ['SMo', ID_NO3_1M, ID_H2PO4_1M]
L_ID_SMO_USED = [ID_NO3_1M, ID_H2PO4_1M]
L_ID_INT = ['Int']
L_ID_PYL = ['Pyl']
L_ID_DEPYL = ['DePyl']

S_CONC_INI = 'concIni'
S_MD_CONC_CH = 'mdConcCh'
S_PER_CONC_CH = 'perConcCh'
S_AMPL_CONC_CH = 'amplConcCh'
S_THR_LOW_CONC = 'thrLowConc'
S_THR_HIGH_CONC = 'thrHighConc'

S_PROP_DEC_ST_AB = 'propDecStAB'
S_PROP_INC_ST_CD = 'propIncStCD'

S_NO = 'no'
S_CH_SIN = 'sin'

# --- constants related to specific sites -------------------------------------
S_SPS_LPRA_S21 = 'S21'
S_SPS_LPRA_S28 = 'S28'
S_SPS_KASA_S839 = 'S839'
S_SPS_KASA_S870 = 'S870'

DS_SPS_LPR_NRT2P1 = {S_SPS_LPRA_S21: {'iSP': 3, 'iLAse': 2},
                     S_SPS_LPRA_S28: {'iSP': 4, 'iLAse': 3}}
DS_SPS_KAS_HPCAL1 = {S_SPS_KASA_S839: {'iSP': 5, 'iLAse': 0},
                     S_SPS_KASA_S870: {'iSP': 6, 'iLAse': 1}}
DS_SPS = {ID_LPR_NRT2P1: DS_SPS_LPR_NRT2P1,
          ID_KAS_HPCAL1: DS_SPS_KAS_HPCAL1}

# --- constants related to interactions ---------------------------------------
B_DO_PYL = 'Pyl'
B_DO_DEPYL = 'DePyl'
B_IS_PYL = 'P+'
B_NOT_PYL = 'P-'

# --- constants related to short states ---------------------------------------
S_ST_L_SHORT = 'L__'
S_ST_S_SHORT = 'S__'
S_ST_K_SHORT = 'K__'
S_ST_LSI_SHORT = 'LSI'
S_ST_LST_SHORT = 'LST'
S_ST_LKI_SHORT = 'LKI'
S_ST_LKT_SHORT = 'LKT'

S_ST_L_LONG = 'St_L_NRT2p1'
S_ST_S_LONG = 'St_S_NAR2p1'
S_ST_K_LONG = 'St_K_HPCAL1'
S_ST_LSI_LONG = 'St_NRT2p1_NAR2p1_Int'
S_ST_LST_LONG = 'St_NRT2p1_NAR2p1_Trans'
S_ST_LKI_LONG = 'St_NRT2p1_HPCAL1_Int'
S_ST_LKT_LONG = 'St_NRT2p1_HPCAL1_Trans'

DS_ST_7 = {S_ST_L_SHORT: S_ST_L_LONG, S_ST_S_SHORT: S_ST_S_LONG,
           S_ST_K_SHORT: S_ST_K_LONG, S_ST_LSI_SHORT: S_ST_LSI_LONG,
           S_ST_LST_SHORT: S_ST_LST_LONG, S_ST_LKI_SHORT: S_ST_LKI_LONG,
           S_ST_LKT_SHORT: S_ST_LKT_LONG}

# --- constants related to extended states -----------------------------------
S_ST_L_00 = 'X00__'
S_ST_L_01 = 'X01__'
S_ST_L_10 = 'X10__'
S_ST_L_11 = 'X11__'
S_ST_S_ = 'Y____'
S_ST_K_00 = 'Z00__'
S_ST_K_01 = 'Z01__'
S_ST_K_10 = 'Z10__'
S_ST_K_11 = 'Z11__'
S_ST_LSI_01 = 'C01__'
S_ST_LST_00 = 'D00__'
S_ST_LST_10 = 'D10__'
S_ST_LST_11 = 'D11__'
S_ST_LKI_1001 = 'A1001'
S_ST_LKT_0000 = 'B0000'
S_ST_LKT_0001 = 'B0001'
S_ST_LKT_0010 = 'B0010'
S_ST_LKT_0011 = 'B0011'
S_ST_LKT_0100 = 'B0100'
S_ST_LKT_0101 = 'B0101'
S_ST_LKT_0110 = 'B0110'
S_ST_LKT_0111 = 'B0111'
S_ST_LKT_1000 = 'B1000'
S_ST_LKT_1010 = 'B1010'
S_ST_LKT_1011 = 'B1011'
S_ST_LKT_1100 = 'B1100'
S_ST_LKT_1101 = 'B1101'
S_ST_LKT_1110 = 'B1110'
S_ST_LKT_1111 = 'B1111'

DS_ST = {S_ST_L_LONG: [S_ST_L_00, S_ST_L_01, S_ST_L_10, S_ST_L_11],
         S_ST_S_LONG: [S_ST_S_],
         S_ST_K_LONG: [S_ST_K_00, S_ST_K_01, S_ST_K_10, S_ST_K_11],
         S_ST_LSI_LONG: [S_ST_LSI_01],
         S_ST_LST_LONG: [S_ST_LST_00,  S_ST_LST_10, S_ST_LST_11],
         S_ST_LKI_LONG: [S_ST_LKI_1001],
         S_ST_LKT_LONG: [S_ST_LKT_0000, S_ST_LKT_0001, S_ST_LKT_0010,
                         S_ST_LKT_0011, S_ST_LKT_0100, S_ST_LKT_0101,
                         S_ST_LKT_0110, S_ST_LKT_0111, S_ST_LKT_1000,
                         S_ST_LKT_1010, S_ST_LKT_1011, S_ST_LKT_1100,
                         S_ST_LKT_1101, S_ST_LKT_1110, S_ST_LKT_1111]}


TS_STCH_X00 = ('X00_X01', 'X00_X10')
TS_STCH_X01 = ('X01_X00', 'X01_X11', 'X01+Y_C01')
TS_STCH_X10 = ('X10_X00', 'X10_X11', 'X10+Z01_A1001')
TS_STCH_X11 = ('X11_X01', 'X11_X10')

TS_STCH_Y = ('X01+Y_C01')

TS_STCH_Z00 = ('Z00_Z01', 'Z00_Z10')
TS_STCH_Z01 = ('Z01_Z00', 'Z01_Z11', 'X10+Z01_A1001')
TS_STCH_Z10 = ('Z10_Z00', 'Z10_Z11')
TS_STCH_Z11 = ('Z11_Z01', 'Z11_Z10')

TS_STCH_A1001 = ('A1001_B0001', 'A1001_B1000', 'A1001_B1011', 'A1001_B1101')
TS_STCH_B0000 = ('B0000_B0001', 'B0000_B0010', 'B0000_B0100', 'B0000_B1000')
TS_STCH_B0001 = ('B0001_B0000', 'B0001_B0011', 'B0001_B0101', 'B0001_A1001')
TS_STCH_B0010 = ('B0010_B0000', 'B0010_B0011', 'B0010_B0110', 'B0010_B1010')
TS_STCH_B0011 = ('B0011_B0001', 'B0011_B0010', 'B0011_B0111', 'B0011_B1011')
TS_STCH_B0100 = ('B0100_B0000', 'B0100_B0101', 'B0100_B0110', 'B0100_B1100')
TS_STCH_B0101 = ('B0101_B0001', 'B0101_B0100', 'B0101_B0111', 'B0101_B1101')
TS_STCH_B0110 = ('B0110_B0010', 'B0110_B0100', 'B0110_B0111', 'B0110_B1110',
                 'B0110_C01+Z10')
TS_STCH_B0111 = ('B0111_B0011', 'B0111_B0101', 'B0111_B0110', 'B0111_B1111')
TS_STCH_B1000 = ('B1000_B0000', 'B1000_A1001', 'B1000_B1010', 'B1000_B1100')
TS_STCH_B1010 = ('B1010_B0010', 'B1010_B1000', 'B1010_B1011', 'B1010_B1110')
TS_STCH_B1011 = ('B1011_B0011', 'B1011_A1001', 'B1011_B1010', 'B1011_B1111')
TS_STCH_B1100 = ('B1100_B0100', 'B1100_B1000', 'B1100_B1101', 'B1100_B1110')
TS_STCH_B1101 = ('B1101_B0101', 'B1101_A1001', 'B1101_B1100', 'B1101_B1111')
TS_STCH_B1110 = ('B1110_B0110', 'B1110_B1010', 'B1110_B1100', 'B1110_B1111')
TS_STCH_B1111 = ('B1111_B0111', 'B1111_B1011', 'B1111_B1101', 'B1111_B1110')

TS_STCH_C01 = ('C01_D00', 'C01_D11')
TS_STCH_D00 = ('D00_C01', 'D00_D10')
TS_STCH_D10 = ('D10_D00', 'D10_D11')
TS_STCH_D11 = ('D11_C01', 'D11_D10')

DS_STCH = {S_ST_LKI_1001: TS_STCH_A1001,
           S_ST_LKT_0000: TS_STCH_B0000,
           S_ST_LKT_0001: TS_STCH_B0001,
           S_ST_LKT_0010: TS_STCH_B0010,
           S_ST_LKT_0011: TS_STCH_B0011,
           S_ST_LKT_0100: TS_STCH_B0100,
           S_ST_LKT_0101: TS_STCH_B0101,
           S_ST_LKT_0110: TS_STCH_B0110,
           S_ST_LKT_0111: TS_STCH_B0111,
           S_ST_LKT_1000: TS_STCH_B1000,
           S_ST_LKT_1010: TS_STCH_B1010,
           S_ST_LKT_1011: TS_STCH_B1011,
           S_ST_LKT_1100: TS_STCH_B1100,
           S_ST_LKT_1101: TS_STCH_B1101,
           S_ST_LKT_1110: TS_STCH_B1110,
           S_ST_LKT_1111: TS_STCH_B1111,

           S_ST_LSI_01: TS_STCH_C01,
           S_ST_LST_00: TS_STCH_D00,
           S_ST_LST_10: TS_STCH_D10,
           S_ST_LST_11: TS_STCH_D11}

SET_01 = {'0', '1'}
SET_01_ = {'0', '1', '_'}

# --- constants related to phosphorylations and dephosphorylations of sites ---
DS_SITES_PYL = {'0': B_DO_DEPYL, '1': B_DO_PYL}

# --- constants related to model output ---------------------------------------
S_TS = 'TimeStep'
S_TIME = 'Time'
S_STATE = 'State'
S_CONC_NO3_1M = 'Conc_NO3-'
S_CONC_H2PO4_1M = 'Conc_H2PO4-'
S_MEAN = 'Mean'
S_SUM = 'Sum'

# --- constants related to plots ----------------------------------------------
S_D_PLT = 'dPlt'
S_STA_CNC = 'A_StaConc'

# --- other constants ---------------------------------------------------------
M_DETER = 'Deterministic'
M_STOCH = 'Stochastic'
SEP_STD = ';'
S_USC = '_'
S_COM_BL = ', '
R04 = 4

###############################################################################
