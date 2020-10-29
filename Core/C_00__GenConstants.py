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

S_PROP_INC_CP_LS = 'propIncCpLS'
S_PROP_DEC_CP_LK = 'propDecCpLK'

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

# --- constants related to components (short form) ----------------------------
S_CP_L_SHORT = 'L--'
S_CP_S_SHORT = 'S--'
S_CP_K_SHORT = 'K--'
S_CP_LSI_SHORT = 'LSI'
S_CP_LST_SHORT = 'LST'
S_CP_LKI_SHORT = 'LKI'
S_CP_LKT_SHORT = 'LKT'

S_CP_L_LONG = 'Cp_L_NRT2p1'
S_CP_S_LONG = 'Cp_S_NAR2p1'
S_CP_K_LONG = 'Cp_K_HPCAL1'
S_CP_LSI_LONG = 'Cp_NRT2p1_NAR2p1_Int'
S_CP_LST_LONG = 'Cp_NRT2p1_NAR2p1_Trans'
S_CP_LKI_LONG = 'Cp_NRT2p1_HPCAL1_Int'
S_CP_LKT_LONG = 'Cp_NRT2p1_HPCAL1_Trans'

DS_CP_7 = {S_CP_L_SHORT: S_CP_L_LONG, S_CP_S_SHORT: S_CP_S_LONG,
           S_CP_K_SHORT: S_CP_K_LONG, S_CP_LSI_SHORT: S_CP_LSI_LONG,
           S_CP_LST_SHORT: S_CP_LST_LONG, S_CP_LKI_SHORT: S_CP_LKI_LONG,
           S_CP_LKT_SHORT: S_CP_LKT_LONG}

# --- constants related to components (extended form) -------------------------
S_CP_L00 = 'L--00--'
S_CP_L01 = 'L--01--'
S_CP_L10 = 'L--10--'
S_CP_L11 = 'L--11--'
S_CP_S__ = 'S------'
S_CP_K00 = 'K--00--'
S_CP_K01 = 'K--01--'
S_CP_K10 = 'K--10--'
S_CP_K11 = 'K--11--'
S_CP_LSI01 = 'LSI01--'
S_CP_LST00 = 'LST00--'
S_CP_LST10 = 'LST10--'
S_CP_LST11 = 'LST11--'
S_CP_LKI1001 = 'LKI1001'
S_CP_LKT0000 = 'LKT0000'
S_CP_LKT0001 = 'LKT0001'
S_CP_LKT0010 = 'LKT0010'
S_CP_LKT0011 = 'LKT0011'
S_CP_LKT0100 = 'LKT0100'
S_CP_LKT0101 = 'LKT0101'
S_CP_LKT0110 = 'LKT0110'
S_CP_LKT0111 = 'LKT0111'
S_CP_LKT1000 = 'LKT1000'
S_CP_LKT1010 = 'LKT1010'
S_CP_LKT1011 = 'LKT1011'
S_CP_LKT1100 = 'LKT1100'
S_CP_LKT1101 = 'LKT1101'
S_CP_LKT1110 = 'LKT1110'
S_CP_LKT1111 = 'LKT1111'

DS_CP = {S_CP_L_LONG: [S_CP_L00, S_CP_L01, S_CP_L10, S_CP_L11],
         S_CP_S_LONG: [S_CP_S__],
         S_CP_K_LONG: [S_CP_K00, S_CP_K01, S_CP_K10, S_CP_K11],
         S_CP_LSI_LONG: [S_CP_LSI01],
         S_CP_LST_LONG: [S_CP_LST00,  S_CP_LST10, S_CP_LST11],
         S_CP_LKI_LONG: [S_CP_LKI1001],
         S_CP_LKT_LONG: [S_CP_LKT0000, S_CP_LKT0001, S_CP_LKT0010,
                         S_CP_LKT0011, S_CP_LKT0100, S_CP_LKT0101,
                         S_CP_LKT0110, S_CP_LKT0111, S_CP_LKT1000,
                         S_CP_LKT1010, S_CP_LKT1011, S_CP_LKT1100,
                         S_CP_LKT1101, S_CP_LKT1110, S_CP_LKT1111]}

TS_RCT_L00 = ('L--00--_L--01--', 'L--00--_L--10--')
TS_RCT_L01 = ('L--01--_L--00--', 'L--01--_L--11--', 'L--01--+S------_LSI01--')
TS_RCT_L10 = ('L--10--_L--00--', 'L--10--_L--11--', 'L--10--+K--01--_LKI1001')
TS_RCT_L11 = ('L--11--_L--01--', 'L--11--_L--10--')

TS_RCT_S__ = ('L--01--+S------_LSI01--')

TS_RCT_K00 = ('K--00--_K--01--', 'K--00--_K--10--')
TS_RCT_K01 = ('K--01--_K--00--', 'K--01--_K--11--', 'L--10--+K--01--_LKI1001')
TS_RCT_K10 = ('K--10--_K--00--', 'K--10--_K--11--')
TS_RCT_K11 = ('K--11--_K--01--', 'K--11--_K--10--')

TS_RCT_LSI01 = ('LSI01--_LST00--', 'LSI01--_LST11--',
                'LSI01--_L--01--+S------')
TS_RCT_LST00 = ('LST00--_LSI01--', 'LST00--_LST10--',
                'LST00--_L--00--+S------')
TS_RCT_LST10 = ('LST10--_LST00--', 'LST10--_LST11--',
                'LST10--_L--10--+S------')
TS_RCT_LST11 = ('LST11--_LSI01--', 'LST11--_LST10--',
                'LST11--_L--11--+S------')

TS_RCT_LKI1001 = ('LKI1001_LKT0001', 'LKI1001_LKT1000', 'LKI1001_LKT1011',
                  'LKI1001_LKT1101', 'LKI1001_L--10--+K--01--')
TS_RCT_LKT0000 = ('LKT0000_LKT0001', 'LKT0000_LKT0010', 'LKT0000_LKT0100',
                  'LKT0000_LKT1000', 'LKT0000_L--00--+K--00--')
TS_RCT_LKT0001 = ('LKT0001_LKT0000', 'LKT0001_LKT0011', 'LKT0001_LKT0101',
                  'LKT0001_LKI1001', 'LKT0001_L--00--+K--01--')
TS_RCT_LKT0010 = ('LKT0010_LKT0000', 'LKT0010_LKT0011', 'LKT0010_LKT0110',
                  'LKT0010_LKT1010', 'LKT0010_L--00--+K--10--')
TS_RCT_LKT0011 = ('LKT0011_LKT0001', 'LKT0011_LKT0010', 'LKT0011_LKT0111',
                  'LKT0011_LKT1011', 'LKT0011_L--00--+K--11--')
TS_RCT_LKT0100 = ('LKT0100_LKT0000', 'LKT0100_LKT0101', 'LKT0100_LKT0110',
                  'LKT0100_LKT1100', 'LKT0100_L--01--+K--00--')
TS_RCT_LKT0101 = ('LKT0101_LKT0001', 'LKT0101_LKT0100', 'LKT0101_LKT0111',
                  'LKT0101_LKT1101', 'LKT0101_L--01--+K--01--')
TS_RCT_LKT0110 = ('LKT0110_LKT0010', 'LKT0110_LKT0100', 'LKT0110_LKT0111',
                  'LKT0110_LKT1110', 'LKT0110_L--01--+K--10--',
                  'LKT0110_LSI01--+K--10--')
TS_RCT_LKT0111 = ('LKT0111_LKT0011', 'LKT0111_LKT0101', 'LKT0111_LKT0110',
                  'LKT0111_LKT1111', 'LKT0111_L--01--+K--11--')
TS_RCT_LKT1000 = ('LKT1000_LKT0000', 'LKT1000_LKI1001', 'LKT1000_LKT1010',
                  'LKT1000_LKT1100', 'LKT1000_L--10--+K--00--')
TS_RCT_LKT1010 = ('LKT1010_LKT0010', 'LKT1010_LKT1000', 'LKT1010_LKT1011',
                  'LKT1010_LKT1110', 'LKT1010_L--10--+K--10--')
TS_RCT_LKT1011 = ('LKT1011_LKT0011', 'LKT1011_LKI1001', 'LKT1011_LKT1010',
                  'LKT1011_LKT1111', 'LKT1011_L--10--+K--11--')
TS_RCT_LKT1100 = ('LKT1100_LKT0100', 'LKT1100_LKT1000', 'LKT1100_LKT1101',
                  'LKT1100_LKT1110', 'LKT1100_L--11--+K--00--')
TS_RCT_LKT1101 = ('LKT1101_LKT0101', 'LKT1101_LKI1001', 'LKT1101_LKT1100',
                  'LKT1101_LKT1111', 'LKT1101_L--11--+K--01--')
TS_RCT_LKT1110 = ('LKT1110_LKT0110', 'LKT1110_LKT1010', 'LKT1110_LKT1100',
                  'LKT1110_LKT1111', 'LKT1110_L--11--+K--10--')
TS_RCT_LKT1111 = ('LKT1111_LKT0111', 'LKT1111_LKT1011', 'LKT1111_LKT1101',
                  'LKT1111_LKT1110', 'LKT1111_L--11--+K--11--')

DS_RCT = {S_CP_L00: TS_RCT_L00,
          S_CP_L01: TS_RCT_L01,
          S_CP_L10: TS_RCT_L10,
          S_CP_L11: TS_RCT_L11,

          S_CP_S__: TS_RCT_S__,

          S_CP_K00: TS_RCT_K00,
          S_CP_K01: TS_RCT_K01,
          S_CP_K10: TS_RCT_K10,
          S_CP_K11: TS_RCT_K11,

          S_CP_LSI01: TS_RCT_LSI01,
          S_CP_LST00: TS_RCT_LST00,
          S_CP_LST10: TS_RCT_LST10,
          S_CP_LST11: TS_RCT_LST11,

          S_CP_LKI1001: TS_RCT_LKI1001,
          S_CP_LKT0000: TS_RCT_LKT0000,
          S_CP_LKT0001: TS_RCT_LKT0001,
          S_CP_LKT0010: TS_RCT_LKT0010,
          S_CP_LKT0011: TS_RCT_LKT0011,
          S_CP_LKT0100: TS_RCT_LKT0100,
          S_CP_LKT0101: TS_RCT_LKT0101,
          S_CP_LKT0110: TS_RCT_LKT0110,
          S_CP_LKT0111: TS_RCT_LKT0111,
          S_CP_LKT1000: TS_RCT_LKT1000,
          S_CP_LKT1010: TS_RCT_LKT1010,
          S_CP_LKT1011: TS_RCT_LKT1011,
          S_CP_LKT1100: TS_RCT_LKT1100,
          S_CP_LKT1101: TS_RCT_LKT1101,
          S_CP_LKT1110: TS_RCT_LKT1110,
          S_CP_LKT1111: TS_RCT_LKT1111}

SET_01 = {'0', '1'}
SET_01_ = {'0', '1', '_'}

# --- constants related to phosphorylations and dephosphorylations of sites ---
DS_SITES_PYL = {'0': B_DO_DEPYL, '1': B_DO_PYL}

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
