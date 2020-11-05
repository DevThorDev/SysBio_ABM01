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

# --- constants related to input data -----------------------------------------
S_00 = '00'
S_01 = '01'
S_02 = '02'
S_03 = '03'
S_04 = '04'
S_05 = '05'
S_06 = '06'

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

S_PROP_INC_CP_LS = 'propIncCpLS'
S_PROP_DEC_CP_LK = 'propDecCpLK'

S_NO = 'no'
S_CH_SIN = 'sin'

# --- constants related to specific sites -------------------------------------
S_SPS_LPRA_S21 = 'S21'
S_SPS_LPRA_S28 = 'S28'
S_SPS_KASA_S839 = 'S839'
S_SPS_KASA_S870 = 'S870'
L_S_SPS = [S_SPS_LPRA_S21, S_SPS_LPRA_S28, S_SPS_KASA_S839, S_SPS_KASA_S870]

DS_SPS_LPR_NRT2P1 = {S_SPS_LPRA_S21: {'iSP': 3, 'iLAse': 2},
                     S_SPS_LPRA_S28: {'iSP': 4, 'iLAse': 3}}
DS_SPS_KAS_HPCAL1 = {S_SPS_KASA_S839: {'iSP': 5, 'iLAse': 0},
                     S_SPS_KASA_S870: {'iSP': 6, 'iLAse': 1}}
DS_SPS = {ID_LPR_NRT2P1: DS_SPS_LPR_NRT2P1,
          ID_KAS_HPCAL1: DS_SPS_KAS_HPCAL1}

# --- constants related to interactions ---------------------------------------
S_L = 'L'
S_S = 'S'
S_K = 'K'
S_I = 'INTER'
S_T = 'TRANS'
L_S_LSK = [S_L, S_S, S_K]
L_S_IT = [S_I, S_T]

S_DO_PYL = 'Pyl'
S_DO_DEPYL = 'DePyl'
L_DO_PYL_DEPYL = [S_DO_PYL, S_DO_DEPYL]

S_IS_PYL = 'P+'
S_NOT_PYL = 'P-'
L_PYL_OR_NOT = [S_IS_PYL, S_NOT_PYL]

S_FRM_L_S_LSI = 'LpS_LSI'
S_FRM_L_S_LST = 'LpS_LST'
S_FRM_L_K_LKI = 'LpK_LKI'
S_FRM_L_K_LKT = 'LpK_LKT'
L_S_FRM = [S_FRM_L_S_LSI, S_FRM_L_S_LST, S_FRM_L_K_LKI, S_FRM_L_K_LKT]

S_DIS_LSI_L_S = 'LSI_LpS'
S_DIS_LST_L_S = 'LST_LpS'
S_DIS_LKI_L_K = 'LKI_LpK'
S_DIS_LKT_L_K = 'LKT_LpK'
L_S_DIS = [S_DIS_LSI_L_S, S_DIS_LST_L_S, S_DIS_LKI_L_K, S_DIS_LKT_L_K]

S_LST_LKI = 'LST_LKI'
S_LKT_LSI = 'LKT_LSI'
L_S_IPC = [S_LST_LKI, S_LKT_LSI]

# --- constants related to input frames ---------------------------------------
S_COMPDESC = 'ComponentDescription'
S_COMPVAR = 'ComponentVariable'
S_COMPSTR = 'ComponentString'
S_NUM = 'Number'
S_ID_SMO = 'ID_SmallMolecule'
S_INI_CNC_DISTR = 'IniConcDistributionType'
S_STR_PAR_1 = 'StrPar1'
S_STR_PAR_2 = 'StrPar2'
S_VAL_PAR_1 = 'ValPar1'
S_VAL_PAR_2 = 'ValPar2'
S_CNC_MIN = 'ConcMin'
S_CNC_MAX = 'ConcMax'
S_VAL = 'Value'
S_VAL_ABS_CH = 'ValueAbsoluteChange'
S_PAR_DESC = 'ParameterDescription'
S_PAR_VAR = 'ParameterVariable'
S_PAR_PMIN = 'ProbMin'
S_PAR_PMAX = 'ProbMax'
S_PAR_B = 'B'
S_PAR_C = 'C'
S_PAR_D = 'D'
S_RCTDESC = 'ReactionDescription'
S_RCTVAR = 'ReactionVariable'
S_RCTSTR = 'ReactionString'
S_WT = 'Weight'

# --- constants related to components (short and long form) -------------------
S_SHORT = 'SHORT'
S_LONG = 'LONG'

# --- constants related to reactions ------------------------------------------
S_RCT_11 = '11'
S_RCT_12 = '12'
S_RCT_21 = '21'
S_RCT_22 = '22'
LEN_S_RCT = 7
I_S_RCT_ST_01 = 3

# S_CP_L_SHORT = 'L--'
# S_CP_S_SHORT = 'S--'
# S_CP_K_SHORT = 'K--'
# S_CP_LSI_SHORT = 'LSI'
# S_CP_LST_SHORT = 'LST'
# S_CP_LKI_SHORT = 'LKI'
# S_CP_LKT_SHORT = 'LKT'

# S_CP_L_LONG = 'Cp_L_NRT2p1'
# S_CP_S_LONG = 'Cp_S_NAR2p1'
# S_CP_K_LONG = 'Cp_K_HPCAL1'
# S_CP_LSI_LONG = 'Cp_NRT2p1_NAR2p1_Inter'
# S_CP_LST_LONG = 'Cp_NRT2p1_NAR2p1_Trans'
# S_CP_LKI_LONG = 'Cp_NRT2p1_HPCAL1_Inter'
# S_CP_LKT_LONG = 'Cp_NRT2p1_HPCAL1_Trans'

# DS_CP_7 = {S_CP_L_SHORT: S_CP_L_LONG, S_CP_S_SHORT: S_CP_S_LONG,
#            S_CP_K_SHORT: S_CP_K_LONG, S_CP_LSI_SHORT: S_CP_LSI_LONG,
#            S_CP_LST_SHORT: S_CP_LST_LONG, S_CP_LKI_SHORT: S_CP_LKI_LONG,
#            S_CP_LKT_SHORT: S_CP_LKT_LONG}

# --- constants related to components (extended form) -------------------------
# S_CP_L00 = 'L--00--'
# S_CP_L01 = 'L--01--'
# S_CP_L10 = 'L--10--'
# S_CP_L11 = 'L--11--'
# S_CP_S__ = 'S------'
# S_CP_K00 = 'K----00'
# S_CP_K01 = 'K----01'
# S_CP_K10 = 'K----10'
# S_CP_K11 = 'K----11'
# S_CP_LSI01 = 'LSI01--'
# S_CP_LST00 = 'LST00--'
# S_CP_LST10 = 'LST10--'
# S_CP_LST11 = 'LST11--'
# S_CP_LKI1001 = 'LKI1001'
# S_CP_LKT0000 = 'LKT0000'
# S_CP_LKT0001 = 'LKT0001'
# S_CP_LKT0010 = 'LKT0010'
# S_CP_LKT0011 = 'LKT0011'
# S_CP_LKT0100 = 'LKT0100'
# S_CP_LKT0101 = 'LKT0101'
# S_CP_LKT0110 = 'LKT0110'
# S_CP_LKT0111 = 'LKT0111'
# S_CP_LKT1000 = 'LKT1000'
# S_CP_LKT1010 = 'LKT1010'
# S_CP_LKT1011 = 'LKT1011'
# S_CP_LKT1100 = 'LKT1100'
# S_CP_LKT1101 = 'LKT1101'
# S_CP_LKT1110 = 'LKT1110'
# S_CP_LKT1111 = 'LKT1111'

# DS_CP = {S_CP_L_LONG: [S_CP_L00, S_CP_L01, S_CP_L10, S_CP_L11],
#          S_CP_S_LONG: [S_CP_S__],
#          S_CP_K_LONG: [S_CP_K00, S_CP_K01, S_CP_K10, S_CP_K11],
#          S_CP_LSI_LONG: [S_CP_LSI01],
#          S_CP_LST_LONG: [S_CP_LST00,  S_CP_LST10, S_CP_LST11],
#          S_CP_LKI_LONG: [S_CP_LKI1001],
#          S_CP_LKT_LONG: [S_CP_LKT0000, S_CP_LKT0001, S_CP_LKT0010,
#                          S_CP_LKT0011, S_CP_LKT0100, S_CP_LKT0101,
#                          S_CP_LKT0110, S_CP_LKT0111, S_CP_LKT1000,
#                          S_CP_LKT1010, S_CP_LKT1011, S_CP_LKT1100,
#                          S_CP_LKT1101, S_CP_LKT1110, S_CP_LKT1111]}

# TS_RCT_L00_S = ('L--00--+S------_LST00--')
# TS_RCT_L01_S = ('L--01--+S------_LSI01--')
# TS_RCT_L10_S = ('L--10--+S------_LST10--')
# TS_RCT_L11_S = ('L--11--+S------_LST11--')

# TS_RCT_L00_K00 = ('L--00--+K----00_LKT0000')
# TS_RCT_L00_K01 = ('L--00--+K----01_LKT0001')
# TS_RCT_L00_K10 = ('L--00--+K----10_LKT0010')
# TS_RCT_L00_K11 = ('L--00--+K----11_LKT0011')
# TS_RCT_L01_K00 = ('L--01--+K----00_LKT0100')
# TS_RCT_L01_K01 = ('L--01--+K----01_LKT0101')
# TS_RCT_L01_K10 = ('L--01--+K----10_LKT0110')
# TS_RCT_L01_K11 = ('L--01--+K----11_LKT0111')
# TS_RCT_L10_K00 = ('L--10--+K----00_LKT1000')
# TS_RCT_L10_K01 = ('L--10--+K----01_LKI1001')
# TS_RCT_L10_K10 = ('L--10--+K----10_LKT1010')
# TS_RCT_L10_K11 = ('L--10--+K----11_LKT1011')
# TS_RCT_L11_K00 = ('L--11--+K----00_LKT1100')
# TS_RCT_L11_K01 = ('L--11--+K----01_LKT1101')
# TS_RCT_L11_K10 = ('L--11--+K----10_LKT1110')
# TS_RCT_L11_K11 = ('L--11--+K----11_LKT1111')

# TS_RCT_L00 = ('L--00--_L--01--', 'L--00--_L--10--')
# TS_RCT_L01 = ('L--01--_L--00--', 'L--01--_L--11--')
# TS_RCT_L10 = ('L--10--_L--00--', 'L--10--_L--11--')
# TS_RCT_L11 = ('L--11--_L--01--', 'L--11--_L--10--')

# TS_RCT_K00 = ('K----00_K----01', 'K----00_K----10')
# TS_RCT_K01 = ('K----01_K----00', 'K----01_K----11')
# TS_RCT_K10 = ('K----10_K----00', 'K----10_K----11')
# TS_RCT_K11 = ('K----11_K----01', 'K----11_K----10')

# TS_RCT_LSI01 = ('LSI01--_LST00--', 'LSI01--_LST11--', 'LSI01--_L--01--+S------')
# TS_RCT_LST00 = ('LST00--_LSI01--', 'LST00--_LST10--', 'LST00--_L--00--+S------')
# TS_RCT_LST10 = ('LST10--_LST00--', 'LST10--_LST11--', 'LST10--_L--10--+S------')
# TS_RCT_LST11 = ('LST11--_LSI01--', 'LST11--_LST10--', 'LST11--_L--11--+S------')

# TS_RCT_LKI1001 = ('LKI1001_LKT0001', 'LKI1001_LKT1000', 'LKI1001_LKT1011', 'LKI1001_LKT1101', 'LKI1001_L--10--+K----01')
# TS_RCT_LKT0000 = ('LKT0000_LKT0001', 'LKT0000_LKT0010', 'LKT0000_LKT0100', 'LKT0000_LKT1000', 'LKT0000_L--00--+K----00')
# TS_RCT_LKT0001 = ('LKT0001_LKT0000', 'LKT0001_LKT0011', 'LKT0001_LKT0101', 'LKT0001_LKI1001', 'LKT0001_L--00--+K----01')
# TS_RCT_LKT0010 = ('LKT0010_LKT0000', 'LKT0010_LKT0011', 'LKT0010_LKT0110', 'LKT0010_LKT1010', 'LKT0010_L--00--+K----10')
# TS_RCT_LKT0011 = ('LKT0011_LKT0001', 'LKT0011_LKT0010', 'LKT0011_LKT0111', 'LKT0011_LKT1011', 'LKT0011_L--00--+K----11')
# TS_RCT_LKT0100 = ('LKT0100_LKT0000', 'LKT0100_LKT0101', 'LKT0100_LKT0110', 'LKT0100_LKT1100', 'LKT0100_L--01--+K----00')
# TS_RCT_LKT0101 = ('LKT0101_LKT0001', 'LKT0101_LKT0100', 'LKT0101_LKT0111', 'LKT0101_LKT1101', 'LKT0101_L--01--+K----01')
# TS_RCT_LKT0110 = ('LKT0110_LKT0010', 'LKT0110_LKT0100', 'LKT0110_LKT0111', 'LKT0110_LKT1110', 'LKT0110_L--01--+K----10', 'LKT0110_LSI01--+K----10')
# TS_RCT_LKT0111 = ('LKT0111_LKT0011', 'LKT0111_LKT0101', 'LKT0111_LKT0110', 'LKT0111_LKT1111', 'LKT0111_L--01--+K----11')
# TS_RCT_LKT1000 = ('LKT1000_LKT0000', 'LKT1000_LKI1001', 'LKT1000_LKT1010', 'LKT1000_LKT1100', 'LKT1000_L--10--+K----00')
# TS_RCT_LKT1010 = ('LKT1010_LKT0010', 'LKT1010_LKT1000', 'LKT1010_LKT1011', 'LKT1010_LKT1110', 'LKT1010_L--10--+K----10')
# TS_RCT_LKT1011 = ('LKT1011_LKT0011', 'LKT1011_LKI1001', 'LKT1011_LKT1010', 'LKT1011_LKT1111', 'LKT1011_L--10--+K----11')
# TS_RCT_LKT1100 = ('LKT1100_LKT0100', 'LKT1100_LKT1000', 'LKT1100_LKT1101', 'LKT1100_LKT1110', 'LKT1100_L--11--+K----00')
# TS_RCT_LKT1101 = ('LKT1101_LKT0101', 'LKT1101_LKI1001', 'LKT1101_LKT1100', 'LKT1101_LKT1111', 'LKT1101_L--11--+K----01')
# TS_RCT_LKT1110 = ('LKT1110_LKT0110', 'LKT1110_LKT1010', 'LKT1110_LKT1100', 'LKT1110_LKT1111', 'LKT1110_L--11--+K----10')
# TS_RCT_LKT1111 = ('LKT1111_LKT0111', 'LKT1111_LKT1011', 'LKT1111_LKT1101', 'LKT1111_LKT1110', 'LKT1111_L--11--+K----11')

# DS_RCT = {S_CP_L00: TS_RCT_L00,
#           S_CP_L01: TS_RCT_L01,
#           S_CP_L10: TS_RCT_L10,
#           S_CP_L11: TS_RCT_L11,

#           S_CP_K00: TS_RCT_K00,
#           S_CP_K01: TS_RCT_K01,
#           S_CP_K10: TS_RCT_K10,
#           S_CP_K11: TS_RCT_K11,

#           S_CP_LSI01: TS_RCT_LSI01,
#           S_CP_LST00: TS_RCT_LST00,
#           S_CP_LST10: TS_RCT_LST10,
#           S_CP_LST11: TS_RCT_LST11,

#           S_CP_LKI1001: TS_RCT_LKI1001,
#           S_CP_LKT0000: TS_RCT_LKT0000,
#           S_CP_LKT0001: TS_RCT_LKT0001,
#           S_CP_LKT0010: TS_RCT_LKT0010,
#           S_CP_LKT0011: TS_RCT_LKT0011,
#           S_CP_LKT0100: TS_RCT_LKT0100,
#           S_CP_LKT0101: TS_RCT_LKT0101,
#           S_CP_LKT0110: TS_RCT_LKT0110,
#           S_CP_LKT0111: TS_RCT_LKT0111,
#           S_CP_LKT1000: TS_RCT_LKT1000,
#           S_CP_LKT1010: TS_RCT_LKT1010,
#           S_CP_LKT1011: TS_RCT_LKT1011,
#           S_CP_LKT1100: TS_RCT_LKT1100,
#           S_CP_LKT1101: TS_RCT_LKT1101,
#           S_CP_LKT1110: TS_RCT_LKT1110,
#           S_CP_LKT1111: TS_RCT_LKT1111}

SET_01 = {'0', '1'}
SET_01_USC = {'0', '1', '_'}
SET_01_DASH = {'0', '1', '-'}

# --- constants related to phosphorylations and dephosphorylations of sites ---
DS_SITES_PYL = {'0': S_DO_DEPYL, '1': S_DO_PYL}

# --- constants related to model output ---------------------------------------
S_TS = 'TimeStep'
S_TIME = 'Time'
S_COMP = 'Comp'
S_CONC_NO3_1M = 'Conc_NO3-'
S_CONC_H2PO4_1M = 'Conc_H2PO4-'
S_MEAN = 'Mean'
S_SUM = 'Sum'

# --- constants related to plots ----------------------------------------------
S_D_PLT = 'dPlt'
S_CP_CNC = 'A_CpConc'

# --- other constants ---------------------------------------------------------
M_DETER = 'Deterministic'
M_STOCH = 'Stochastic'
SEP_STD = ';'
S_USC = '_'
S_PLUS = '+'
S_COM_BL = ', '
R04 = 4

###############################################################################
