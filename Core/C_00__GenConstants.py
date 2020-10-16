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
SPC_KAS_A = 'KAs_A'
SPC_KAS_X = 'KAs_X'
SPC_LPR_A = 'LPr_A'
SPC_SPR_A = 'SPr_A'
SPC_L_SMO = 'lSMo'

ID_KAS_AT5G49770, ID_KAS_X = 'KAs_AT5G49770', 'KAs_X'
ID_KAS_1, ID_KAS_2, ID_KAS_3 = 'KAs1', 'KAs2', 'KAs3'
ID_PAS_1, ID_PAS_2, ID_PAS_3, ID_PAS_4 = 'PAs1', 'PAs2', 'PAs3', 'PAs4'
ID_LPR_NRT2P1 = 'LPr_NRT2p1'
ID_SPR_NAR2P1 = 'SPr_NAR2p1'
ID_NO3_1M = 'NO3_1m'
ID_H2PO4_1M = 'H2PO4_1m'

L_ID_MOL = ['Mol']
L_ID_PRO = ['Pro']
L_ID_ENZ = ['Enz']
L_ID_KAS = ['KAs', ID_KAS_AT5G49770, ID_KAS_X, ID_KAS_1, ID_KAS_2, ID_KAS_3]
L_ID_PAS = ['PAs', ID_PAS_1, ID_PAS_2, ID_PAS_3, ID_PAS_4]
L_ID_LPR = ['LPr', ID_LPR_NRT2P1]
L_ID_SPR = ['SPr', ID_SPR_NAR2P1]
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
S_SPS_KAS1_S839 = 'S839'
S_SPS_KAS1_S870 = 'S870'
S_SPS_LPR1_S21 = 'S21'
S_SPS_LPR1_S28 = 'S28'

# --- constants related to interactions ---------------------------------------
B_DO_PYL = 'Pyl'
B_DO_DEPYL = 'DePyl'
B_IS_PYL = 'P+'
B_NOT_PYL = 'P-'

# --- constants related to states ---------------------------------------------
S_ST_A_SIMPLE = 'A'
S_ST_B_SIMPLE = 'B'
S_ST_C_SIMPLE = 'C'
S_ST_D_SIMPLE = 'D'

S_ST_A_KIN_INT = 'St_A_Int_AT5G49770_NRT2p1'
S_ST_B_KIN_TRA = 'St_B_Trans_AT5G49770_NRT2p1'
S_ST_C_SPR_INT = 'St_C_Int_NAR2p1_NRT2p1'
S_ST_D_SPR_TRA = 'St_D_Trans_NAR2p1_NRT2p1'

DS_ST_4 = {S_ST_A_SIMPLE: S_ST_A_KIN_INT, S_ST_B_SIMPLE: S_ST_B_KIN_TRA,
           S_ST_C_SIMPLE: S_ST_C_SPR_INT, S_ST_D_SIMPLE: S_ST_D_SPR_TRA}

# --- constants related to new states -----------------------------------------
S_ST_A_KIN_INT_1001 = 'A1001'
S_ST_B_KIN_TRA_0000 = 'B0000'
S_ST_B_KIN_TRA_0001 = 'B0001'
S_ST_B_KIN_TRA_0010 = 'B0010'
S_ST_B_KIN_TRA_0011 = 'B0011'
S_ST_B_KIN_TRA_0100 = 'B0100'
S_ST_B_KIN_TRA_0101 = 'B0101'
S_ST_B_KIN_TRA_0110 = 'B0110'
S_ST_B_KIN_TRA_0111 = 'B0111'
S_ST_B_KIN_TRA_1000 = 'B1000'
S_ST_B_KIN_TRA_1010 = 'B1010'
S_ST_B_KIN_TRA_1011 = 'B1011'
S_ST_B_KIN_TRA_1100 = 'B1100'
S_ST_B_KIN_TRA_1101 = 'B1101'
S_ST_B_KIN_TRA_1110 = 'B1110'
S_ST_B_KIN_TRA_1111 = 'B1111'
S_ST_C_SPR_INT_0110 = 'C0110'
S_ST_D_SPR_TRA_0000 = 'D0000'
S_ST_D_SPR_TRA_0001 = 'D0001'
S_ST_D_SPR_TRA_0010 = 'D0010'
S_ST_D_SPR_TRA_0011 = 'D0011'
S_ST_D_SPR_TRA_0100 = 'D0100'
S_ST_D_SPR_TRA_0101 = 'D0101'
S_ST_D_SPR_TRA_0111 = 'D0111'
S_ST_D_SPR_TRA_1000 = 'D1000'
S_ST_D_SPR_TRA_1001 = 'D1001'
S_ST_D_SPR_TRA_1010 = 'D1010'
S_ST_D_SPR_TRA_1011 = 'D1011'
S_ST_D_SPR_TRA_1100 = 'D1100'
S_ST_D_SPR_TRA_1101 = 'D1101'
S_ST_D_SPR_TRA_1110 = 'D1110'
S_ST_D_SPR_TRA_1111 = 'D1111'

DS_ST = {S_ST_A_KIN_INT: [S_ST_A_KIN_INT_1001],
         S_ST_B_KIN_TRA: [S_ST_B_KIN_TRA_0000, S_ST_B_KIN_TRA_0001,
                          S_ST_B_KIN_TRA_0010, S_ST_B_KIN_TRA_0011,
                          S_ST_B_KIN_TRA_0100, S_ST_B_KIN_TRA_0101,
                          S_ST_B_KIN_TRA_0110, S_ST_B_KIN_TRA_0111,
                          S_ST_B_KIN_TRA_1000, S_ST_B_KIN_TRA_1010,
                          S_ST_B_KIN_TRA_1011, S_ST_B_KIN_TRA_1100,
                          S_ST_B_KIN_TRA_1101, S_ST_B_KIN_TRA_1110,
                          S_ST_B_KIN_TRA_1111],
         S_ST_C_SPR_INT: [S_ST_C_SPR_INT_0110],
         S_ST_D_SPR_TRA: [S_ST_D_SPR_TRA_0000, S_ST_D_SPR_TRA_0001,
                          S_ST_D_SPR_TRA_0010, S_ST_D_SPR_TRA_0011,
                          S_ST_D_SPR_TRA_0100, S_ST_D_SPR_TRA_0101,
                          S_ST_D_SPR_TRA_0111, S_ST_D_SPR_TRA_1000,
                          S_ST_D_SPR_TRA_1001, S_ST_D_SPR_TRA_1010,
                          S_ST_D_SPR_TRA_1011, S_ST_D_SPR_TRA_1100,
                          S_ST_D_SPR_TRA_1101, S_ST_D_SPR_TRA_1110,
                          S_ST_D_SPR_TRA_1111]}

TS_STCH_A1001 = ('A1001_B0001', 'A1001_B1000', 'A1001_B1011', 'A1001_B1101')
TS_STCH_B0000 = ('B0000_B0001', 'B0000_B0010', 'B0000_B0100', 'B0000_B1000')
TS_STCH_B0001 = ('B0001_B0000', 'B0001_B0011', 'B0001_B0101', 'B0001_A1001')
TS_STCH_B0010 = ('B0010_B0000', 'B0010_B0011', 'B0010_B0110', 'B0010_B1010')
TS_STCH_B0011 = ('B0011_B0001', 'B0011_B0010', 'B0011_B0111', 'B0011_B1011')
TS_STCH_B0100 = ('B0100_B0000', 'B0100_B0101', 'B0100_B0110', 'B0100_B1100')
TS_STCH_B0101 = ('B0101_B0001', 'B0101_B0100', 'B0101_B0111', 'B0101_B1101')
TS_STCH_B0110 = ('B0110_B0010', 'B0110_B0100', 'B0110_B0111', 'B0110_B1110',
                 'B0110_C0110')
TS_STCH_B0111 = ('B0111_B0011', 'B0111_B0101', 'B0111_B0110', 'B0111_B1111')
TS_STCH_B1000 = ('B1000_B0000', 'B1000_A1001', 'B1000_B1010', 'B1000_B1100')
TS_STCH_B1010 = ('B1010_B0010', 'B1010_B1000', 'B1010_B1011', 'B1010_B1110')
TS_STCH_B1011 = ('B1011_B0011', 'B1011_A1001', 'B1011_B1010', 'B1011_B1111')
TS_STCH_B1100 = ('B1100_B0100', 'B1100_B1000', 'B1100_B1101', 'B1100_B1110')
TS_STCH_B1101 = ('B1101_B0101', 'B1101_A1001', 'B1101_B1100', 'B1101_B1111')
TS_STCH_B1110 = ('B1110_B0110', 'B1110_B1010', 'B1110_B1100', 'B1110_B1111')
TS_STCH_B1111 = ('B1111_B0111', 'B1111_B1011', 'B1111_B1101', 'B1111_B1110')

TS_STCH_C0110 = ('C0110_D0010', 'C0110_D0100', 'C0110_D0111', 'C0110_D1110')
TS_STCH_D0000 = ('D0000_D0001', 'D0000_D0010', 'D0000_D0100', 'D0000_D1000')
TS_STCH_D0001 = ('D0001_D0000', 'D0001_D0011', 'D0001_D0101', 'D0001_D1001')
TS_STCH_D0010 = ('D0010_D0000', 'D0010_D0011', 'D0010_C0110', 'D0010_D1010')
TS_STCH_D0011 = ('D0011_D0001', 'D0011_D0010', 'D0011_D0111', 'D0011_D1011')
TS_STCH_D0100 = ('D0100_D0000', 'D0100_D0101', 'D0100_C0110', 'D0100_D1100')
TS_STCH_D0101 = ('D0101_D0001', 'D0101_D0100', 'D0101_D0111', 'D0101_D1101')
TS_STCH_D0111 = ('D0111_D0011', 'D0111_D0101', 'D0111_C0110', 'D0111_D1111')
TS_STCH_D1000 = ('D1000_D0000', 'D1000_D1001', 'D1000_D1010', 'D1000_D1100')
TS_STCH_D1001 = ('D1001_D0001', 'D1001_D1000', 'D1001_D1011', 'D1001_D1101',
                 'D1001_A1001')
TS_STCH_D1010 = ('D1010_D0010', 'D1010_D1000', 'D1010_D1011', 'D1010_D1110')
TS_STCH_D1011 = ('D1011_D0011', 'D1011_D1001', 'D1011_D1010', 'D1011_D1111')
TS_STCH_D1100 = ('D1100_D0100', 'D1100_D1000', 'D1100_D1101', 'D1100_D1110')
TS_STCH_D1101 = ('D1101_D0101', 'D1101_D1001', 'D1101_D1100', 'D1101_D1111')
TS_STCH_D1110 = ('D1110_C0110', 'D1110_D1010', 'D1110_D1100', 'D1110_D1111')
TS_STCH_D1111 = ('D1111_D0111', 'D1111_D1011', 'D1111_D1101', 'D1111_D1110')

DS_STCH = {S_ST_A_KIN_INT_1001: TS_STCH_A1001,
           S_ST_B_KIN_TRA_0000: TS_STCH_B0000,
           S_ST_B_KIN_TRA_0001: TS_STCH_B0001,
           S_ST_B_KIN_TRA_0010: TS_STCH_B0010,
           S_ST_B_KIN_TRA_0011: TS_STCH_B0011,
           S_ST_B_KIN_TRA_0100: TS_STCH_B0100,
           S_ST_B_KIN_TRA_0101: TS_STCH_B0101,
           S_ST_B_KIN_TRA_0110: TS_STCH_B0110,
           S_ST_B_KIN_TRA_0111: TS_STCH_B0111,
           S_ST_B_KIN_TRA_1000: TS_STCH_B1000,
           S_ST_B_KIN_TRA_1010: TS_STCH_B1010,
           S_ST_B_KIN_TRA_1011: TS_STCH_B1011,
           S_ST_B_KIN_TRA_1100: TS_STCH_B1100,
           S_ST_B_KIN_TRA_1101: TS_STCH_B1101,
           S_ST_B_KIN_TRA_1110: TS_STCH_B1110,
           S_ST_B_KIN_TRA_1111: TS_STCH_B1111,
           
           S_ST_C_SPR_INT_0110: TS_STCH_C0110,
           S_ST_D_SPR_TRA_0000: TS_STCH_D0000,
           S_ST_D_SPR_TRA_0001: TS_STCH_D0001,
           S_ST_D_SPR_TRA_0010: TS_STCH_D0010,
           S_ST_D_SPR_TRA_0011: TS_STCH_D0011,
           S_ST_D_SPR_TRA_0100: TS_STCH_D0100,
           S_ST_D_SPR_TRA_0101: TS_STCH_D0101,
           S_ST_D_SPR_TRA_0111: TS_STCH_D0111,
           S_ST_D_SPR_TRA_1000: TS_STCH_D1000,
           S_ST_D_SPR_TRA_1001: TS_STCH_D1001,
           S_ST_D_SPR_TRA_1010: TS_STCH_D1010,
           S_ST_D_SPR_TRA_1011: TS_STCH_D1011,
           S_ST_D_SPR_TRA_1100: TS_STCH_D1100,
           S_ST_D_SPR_TRA_1101: TS_STCH_D1101,
           S_ST_D_SPR_TRA_1110: TS_STCH_D1110,
           S_ST_D_SPR_TRA_1111: TS_STCH_D1111}

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
S_SPL = '_'
R04 = 4

###############################################################################
