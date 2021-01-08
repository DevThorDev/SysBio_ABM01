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

# --- string constants --------------------------------------------------------
S_0 = '0'
S_1 = '1'
S_2 = '2'
S_3 = '3'
S_4 = '4'
S_5 = '5'
S_6 = '6'
S_7 = '7'
S_00 = S_0 + S_0
S_01 = S_0 + S_1
S_02 = S_0 + S_2
S_03 = S_0 + S_3
S_04 = S_0 + S_4
S_05 = S_0 + S_5
S_06 = S_0 + S_6
S_07 = S_0 + S_7

SEP_STD = ';'
S_USC = '_'
S_DASH = '-'
S_WAVE = '~'
S_PLUS = '+'
S_STAR = '*'
S_COM_BL = ', '

# --- sets --------------------------------------------------------------------
SET_01 = {S_0, S_1}
SET_01_USC = {S_0, S_1, S_USC}
SET_01_DASH = {S_0, S_1, S_DASH}

# --- constants related to molecule objects -----------------------------------

ID_BAS = 'Base'
ID_LPR_NRT2P1 = 'LPrNRT2p1'
ID_SPR_NAR2P1 = 'SPrNAR2p1'
ID_KAS_K, ID_KAS_X, ID_KAS_Y = 'KAsK', 'KAsX', 'KAsY'
ID_PAS_A, ID_PAS_B, ID_PAS_C, ID_PAS_D = 'PAsA', 'PAsB', 'PAsC', 'PAsD'
ID_NO3_1M = 'NO3_1m'
ID_H2PO4_1M = 'H2PO4_1m'

S_CL_BASE = ID_BAS
S_CL_MOLEC = 'Molecule'
S_CL_LPR_NRT2P1 = 'NRT2.1'
S_CL_SPR_NAR2P1 = 'NAR2.1'
S_CL_KAS_K, S_CL_KAS_X, S_CL_KAS_Y = 'HPCAL1', ID_KAS_X, ID_KAS_Y
S_CL_PAS_A, S_CL_PAS_B, S_CL_PAS_C, S_CL_PAS_D = (ID_PAS_A, ID_PAS_B,
                                                  ID_PAS_C, ID_PAS_D)
S_CL_NO3_1M = 'NO3-'
S_CL_H2PO4_1M = 'H2PO4-'
S_CL_INTERACTION = 'Interaction'
S_CL_COMPONENT = 'SystemComponent'
S_CL_SYSTEM = 'System'

S_A = 'A'   # for phosphatase A
S_B = 'B'   # for phosphatase B
S_C = 'C'   # for phosphatase C
S_D = 'D'   # for phosphatase D
S_I = 'I'   # for strong interaction state
S_J = 'J'   # for weak interaction state
S_K = 'K'   # for kinase K (HPCAL1)
S_L = 'L'   # for large protein L (NRT2.1)
S_N = 'N'   # for small molecule NO3-
S_P = 'P'   # for small molecule H2PO4-
S_S = 'S'   # for small protein S (NAR2.1)
S_T = 'T'   # for transition state
S_X = 'X'   # for kinase X
S_Y = 'Y'   # for kinase Y

S_L__ = S_L + S_DASH + S_DASH
S_S__ = S_S + S_DASH + S_DASH
S_K__ = S_K + S_DASH + S_DASH
S_LSI = S_L + S_S + S_I
S_LSJ = S_L + S_S + S_J
S_LST = S_L + S_S + S_T
S_LKI = S_L + S_K + S_I
S_LKJ = S_L + S_K + S_J
S_LKT = S_L + S_K + S_T

ID_CPB = 'CpBase'
ID_CPN = 'Cp'
ID_SYS = 'Sys'
ID_MOL = 'Mol'
ID_PRO = 'Pro'
ID_LPR = 'LPr'
ID_SPR = 'SPr'
ID_ENZ = 'Enz'
ID_KAS = 'KAs'
ID_PAS = 'PAs'
ID_MET = 'Met'
ID_LMO = 'LMo'
ID_SMO = 'SMo'
ID_INT = 'Int'
ID_PYL = 'Pyl'
ID_DPY = 'DPy'

L_ID_MOL = [ID_MOL]
L_ID_PRO = [ID_PRO]
L_ID_LPR = [ID_LPR, ID_LPR_NRT2P1]
L_ID_SPR = [ID_SPR, ID_SPR_NAR2P1]
L_ID_ENZ = [ID_ENZ]
L_ID_KAS = [ID_KAS, ID_KAS_K, ID_KAS_X, ID_KAS_Y]
L_ID_PAS = [ID_PAS, ID_PAS_A, ID_PAS_B, ID_PAS_C, ID_PAS_D]
L_ID_MET = [ID_MET]
L_ID_LMO = [ID_LMO]
L_ID_SMO = [ID_SMO, ID_NO3_1M, ID_H2PO4_1M]
L_ID_SMO_USED = [ID_NO3_1M, ID_H2PO4_1M]
L_ID_INT = [ID_INT]
L_ID_PYL = [ID_PYL]
L_ID_DPY = [ID_DPY]

D_ID_AS = {S_K: ID_KAS_K, S_X: ID_KAS_X, S_Y: ID_KAS_Y,
           S_A: ID_PAS_A, S_B: ID_PAS_B, S_C: ID_PAS_C, S_D: ID_PAS_D}

S_CNC_INI = 'concIni'
S_PERIOD_CHG = 'periodChg'
S_AMPL_CHG = 'amplitudeChg'
S_THR_LOW_CNC = 'thrLowConc'
S_THR_HIGH_CNC = 'thrHighConc'

S_PROP_INC_CP_LS = 'propIncCpLS'
S_PROP_DEC_CP_LK = 'propDecCpLK'

S_NO = 'no'
S_CH_SIN = 'sin'
S_CH_STEP = 'step'

# --- constants related to specific sites -------------------------------------
S_SPS_L_S21 = 'S21'
S_SPS_L_S28 = 'S28'
S_SPS_K_S839 = 'S839'
S_SPS_K_S870 = 'S870'
L_S_SPS = [S_SPS_L_S21, S_SPS_L_S28, S_SPS_K_S839, S_SPS_K_S870]

DS_SPS_L = {S_SPS_L_S21: {'iSP': 3, ID_KAS: ID_KAS_K, ID_PAS: ID_PAS_C},
            S_SPS_L_S28: {'iSP': 4, ID_KAS: ID_KAS_X, ID_PAS: ID_PAS_D}}
DS_SPS_K = {S_SPS_K_S839: {'iSP': 5, ID_KAS: ID_KAS_Y, ID_PAS: ID_PAS_A},
            S_SPS_K_S870: {'iSP': 6, ID_KAS: ID_KAS_K, ID_PAS: ID_PAS_B}}
DS_SPS = {ID_LPR_NRT2P1: DS_SPS_L, ID_KAS_K: DS_SPS_K}

# --- constants related to interactions ---------------------------------------
L_S_LSK = [S_L, S_S, S_K]
L_S_IJT = [S_I, S_J, S_T]
L_S_SMO = [S_N, S_P]

S_STAT = 'Stat'
S_DO_PYL = ID_PYL
S_DO_DPY = ID_DPY
S_DO_FRM = 'Frm'
S_DO_DIS = 'Dis'
S_DO_IPC = 'IPC'
L_RCT_TYPE = [S_DO_PYL, S_DO_DPY, S_DO_FRM, S_DO_DIS, S_DO_IPC]
DS_SITES_PYL = {S_0: (S_DO_DPY, ID_PAS), S_1: (S_DO_PYL, ID_KAS)}

S_IS_PYL = 'P+'
S_NOT_PYL = 'P-'
L_PYL_OR_NOT = [S_IS_PYL, S_NOT_PYL]

S_FRM_L_S_LSI = 'LpS_LSI'
S_FRM_L_S_LSJ = 'LpS_LSJ'
S_FRM_L_S_LST = 'LpS_LST'
S_FRM_L_K_LKI = 'LpK_LKI'
S_FRM_L_K_LKJ = 'LpK_LKJ'
S_FRM_L_K_LKT = 'LpK_LKT'
L_S_FRM = [S_FRM_L_S_LSI, S_FRM_L_S_LSJ, S_FRM_L_S_LST,
           S_FRM_L_K_LKI, S_FRM_L_K_LKJ, S_FRM_L_K_LKT]

S_DIS_LSI_L_S = 'LSI_LpS'
S_DIS_LSJ_L_S = 'LSJ_LpS'
S_DIS_LST_L_S = 'LST_LpS'
S_DIS_LKI_L_K = 'LKI_LpK'
S_DIS_LKJ_L_K = 'LKJ_LpK'
S_DIS_LKT_L_K = 'LKT_LpK'
L_S_DIS = [S_DIS_LSI_L_S, S_DIS_LSJ_L_S, S_DIS_LST_L_S,
           S_DIS_LKI_L_K, S_DIS_LKJ_L_K, S_DIS_LKT_L_K]

S_IPC_LSI_LKT = 'LSI_LKT'
S_IPC_LSJ_LKT = 'LSJ_LKT'
S_IPC_LST_LKI = 'LST_LKI'
S_IPC_LST_LKJ = 'LST_LKJ'
S_IPC_LKI_LST = 'LKI_LST'
S_IPC_LKJ_LST = 'LKJ_LST'
S_IPC_LKT_LSI = 'LKT_LSI'
S_IPC_LKT_LSJ = 'LKT_LSJ'
L_S_IPC = [S_IPC_LSI_LKT, S_IPC_LSJ_LKT, S_IPC_LST_LKI, S_IPC_LST_LKJ,
           S_IPC_LKI_LST, S_IPC_LKJ_LST, S_IPC_LKT_LSI, S_IPC_LKT_LSJ]

# --- constants related to input frames ---------------------------------------
S_CPDESC = 'ComponentDescription'
S_CPVAR = 'ComponentVariable'
S_CPSTR = 'ComponentString'
S_NUM = 'Number'
S_ID_SMO = 'ID_SmallMolecule'
S_INI_CNC_DISTR = 'IniConcDistributionType'
S_STR_PAR_1_INI = 'StrPar1_Ini'
S_STR_PAR_2_INI = 'StrPar2_Ini'
L_S_STR_PAR_INI = [S_STR_PAR_1_INI, S_STR_PAR_2_INI]
S_VAL_PAR_1_INI = 'ValPar1_Ini'
S_VAL_PAR_2_INI = 'ValPar2_Ini'
L_S_VAL_PAR_INI = [S_VAL_PAR_1_INI, S_VAL_PAR_2_INI]
S_CNC_MIN = 'ConcMin'
S_CNC_MAX = 'ConcMax'
S_CNC_CHG_MODE = 'ConcChgMode'
S_STR_PAR_1_TCHG = 'StrPar1_TChg'
S_STR_PAR_2_TCHG = 'StrPar2_TChg'
S_STR_PAR_3_TCHG = 'StrPar3_TChg'
S_STR_PAR_4_TCHG = 'StrPar4_TChg'
L_S_STR_PAR_TCHG = [S_STR_PAR_1_TCHG, S_STR_PAR_2_TCHG, S_STR_PAR_3_TCHG,
                    S_STR_PAR_4_TCHG]
S_VAL_PAR_1_TCHG = 'ValPar1_TChg'
S_VAL_PAR_2_TCHG = 'ValPar2_TChg'
S_VAL_PAR_3_TCHG = 'ValPar3_TChg'
S_VAL_PAR_4_TCHG = 'ValPar4_TChg'
L_S_VAL_PAR_TCHG = [S_VAL_PAR_1_TCHG, S_VAL_PAR_2_TCHG, S_VAL_PAR_3_TCHG,
                    S_VAL_PAR_4_TCHG]
S_VAL = 'Value'
S_VAL_ABS_CH = 'ValueAbsoluteChange'
S_PAR_DESC = 'ParameterDescription'
S_PAR_VAR = 'ParameterVariable'
S_PAR_PMIN = 'ProbMin'
S_PAR_PMAX = 'ProbMax'
S_PAR_B = 'B'
S_PAR_C = 'C'
S_PAR_D = 'D'
L_S_PAR_TAB05 = [S_PAR_PMIN, S_PAR_PMAX, S_PAR_B, S_PAR_C, S_PAR_D]
S_RCTDESC = 'ReactionDescription'
S_RCTVAR = 'ReactionVariable'
S_RCTSTR = 'ReactionString'
S_WT = 'Weight'
S_VARDESC = 'VariableDescription'
S_VAR = 'Variable'

# --- constants related to components (short and long form) -------------------
S_SHORT = 'SHORT'
S_LONG = 'LONG'

# --- constants related to reactions ------------------------------------------
S_RCT_11 = S_1 + S_1
# S_RCT_11_K = S_RCT_11 + S_K
# S_RCT_11_X = S_RCT_11 + S_X
# S_RCT_11_Y = S_RCT_11 + S_Y
# S_RCT_11_A = S_RCT_11 + S_A
# S_RCT_11_B = S_RCT_11 + S_B
# S_RCT_11_C = S_RCT_11 + S_C
# S_RCT_11_D = S_RCT_11 + S_D
S_RCT_12 = S_1 + S_2
S_RCT_21 = S_2 + S_1
S_RCT_22 = S_2 + S_2
# L_S_RCT_ASES = [S_RCT_11_K, S_RCT_11_X, S_RCT_11_Y,
#                 S_RCT_11_A, S_RCT_11_B, S_RCT_11_C, S_RCT_11_D]
L_S_RCT_2ORD = [S_RCT_21, S_RCT_22]
LEN_S_CP = 7
I_S_CP_SEP = 3

P_DUMMY = 0.5

# --- constants related to model output ---------------------------------------
S_TS = 'TimeStep'
S_TIME = 'Time'
S_CP = 'Comp'
S_CNC_NO3_1M = 'Conc_NO3-'
S_CNC_H2PO4_1M = 'Conc_H2PO4-'
S_MEAN = 'Mean'
S_SUM = 'Sum'

# --- constants related to plots ----------------------------------------------
S_D_PLT = 'dPlt'
S_CP_CNC = 'A_CpConc'

# --- other constants ---------------------------------------------------------
M_DETER = 'Deterministic'
M_STOCH = 'Stochastic'

R04 = 4

###############################################################################
