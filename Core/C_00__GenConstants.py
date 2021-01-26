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
S_8 = '8'
S_9 = '9'

S_00 = S_0 + S_0
S_01 = S_0 + S_1
S_02 = S_0 + S_2
S_03 = S_0 + S_3
S_04 = S_0 + S_4
S_05 = S_0 + S_5
S_06 = S_0 + S_6
S_07 = S_0 + S_7
S_08 = S_0 + S_8
S_09 = S_0 + S_9
S_10 = S_1 + S_0
S_11 = S_1 + S_1

SEP_STD = ';'
S_USC = '_'
S_DASH = '-'
S_2DASH = S_DASH + S_DASH
S_4DASH = S_2DASH + S_2DASH
S_2DASH00 = S_2DASH + S_00
S_2DASH01 = S_2DASH + S_01
S_2DASH10 = S_2DASH + S_10
S_2DASH11 = S_2DASH + S_11
S_WAVE = '~'
S_PLUS = '+'
S_STAR = '*'
S_COM_BL = ', '

# --- sets --------------------------------------------------------------------
SET_0_1 = {S_0, S_1}
SET_0_1_USC = {S_0, S_1, S_USC}
SET_0_1_DASH = {S_0, S_1, S_DASH}

# --- constants related to molecule objects -----------------------------------

ID_BAS = 'Base'
ID_LPR_NRT2P1 = 'L_Pr_NRT2p1'
ID_SPR_NAR2P1 = 'S_Pr_NAR2p1'
ID_KAS_K, ID_KAS_X, ID_KAS_Y = 'K_KAs', 'X_KAs', 'Y_KAs'
ID_PAS_A, ID_PAS_B, ID_PAS_C, ID_PAS_D = 'A_PAs', 'B_PAs', 'C_PAs', 'D_PAs'
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
S_CL_SIMULATION = 'Simulation'

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
S_X__ = S_X + S_DASH + S_DASH
S_Y__ = S_Y + S_DASH + S_DASH
S_A__ = S_A + S_DASH + S_DASH
S_B__ = S_B + S_DASH + S_DASH
S_C__ = S_C + S_DASH + S_DASH
S_D__ = S_D + S_DASH + S_DASH
S_LSI = S_L + S_S + S_I
S_LSJ = S_L + S_S + S_J
S_LST = S_L + S_S + S_T
S_LKI = S_L + S_K + S_I
S_LKJ = S_L + S_K + S_J
S_LKT = S_L + S_K + S_T

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
ID_CPB = 'CpBase'
ID_CPN = 'Cp'
ID_SYS = 'Sys'
ID_SIM = 'Sim'

L_ID_LPR_SYS = [ID_LPR_NRT2P1]
L_ID_SPR_SYS = [ID_SPR_NAR2P1]
L_ID_KAS_SYS = [ID_KAS_K, ID_KAS_X, ID_KAS_Y]
L_ID_PAS_SYS = [ID_PAS_A, ID_PAS_B, ID_PAS_C, ID_PAS_D]
L_ID_ENZ_SYS = L_ID_KAS_SYS + L_ID_PAS_SYS
L_ID_PRO_SYS = L_ID_LPR_SYS + L_ID_SPR_SYS + L_ID_ENZ_SYS
L_ID_LMO_SYS = []
L_ID_SMO_SYS = [ID_NO3_1M, ID_H2PO4_1M]
L_ID_MET_SYS = L_ID_LMO_SYS + L_ID_SMO_SYS
L_ID_MOL_SYS = L_ID_PRO_SYS + L_ID_MET_SYS

D_CPS_TO_ID_AS = {S_K: ID_KAS_K, S_X: ID_KAS_X, S_Y: ID_KAS_Y,
                  S_A: ID_PAS_A, S_B: ID_PAS_B, S_C: ID_PAS_C, S_D: ID_PAS_D}

D_ID_TO_CPSX = {ID_LPR_NRT2P1: S_L__, ID_SPR_NAR2P1: S_S__,
                ID_KAS_K: S_K__, ID_KAS_X: S_X__, ID_KAS_Y: S_Y__,
                ID_PAS_A: S_A__, ID_PAS_B: S_B__, ID_PAS_C: S_C__,
                ID_PAS_D: S_D__}

S_REP = 'Rep'

S_CNC_INI = 'concIni'
S_THR_HIGH_CNC = 'thrHighConc'

S_QMIX = 'qMix'
S_PERIOD_CHG = 'periodChg'
S_AMPL_CHG = 'amplitudeChg'
S_STEP_T1 = 'stepTime1'
S_STEP_T2 = 'stepTime2'
S_STEP_V01 = 'stepVal01'
S_STEP_V12 = 'stepVal12'
S_STEP_V_T = 'stepVal_T'
S_DLT_SM_1 = 'deltaSm1'
S_DLT_SM_2 = 'deltaSm2'
S_SM_ORD = 'smOrd'

S_PROP_INC_CP_LS = 'propIncCpLS'
S_PROP_DEC_CP_LK = 'propDecCpLK'

S_NO = 'no'
S_CH_SIN = 'sin'
S_CH_STEP = 'step'
S_CH_MXDQ = 'mixedQ'

# --- constants related to specific sites -------------------------------------
S_SPS_L_S21 = 'S21'
S_SPS_L_S28 = 'S28'
S_SPS_K_S839 = 'S839'
S_SPS_K_S870 = 'S870'
L_S_SPS = [S_SPS_L_S21, S_SPS_L_S28, S_SPS_K_S839, S_SPS_K_S870]

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

S_IS_PYL = 'P+'
S_NOT_PYL = 'P-'
L_PYL_OR_NOT = [S_IS_PYL, S_NOT_PYL]

D_STAT_INI_L = {S_SPS_L_S21: S_IS_PYL, S_SPS_L_S28: S_NOT_PYL}
D_STAT_INI_K = {S_SPS_K_S839: S_NOT_PYL, S_SPS_K_S870: S_IS_PYL}

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
S_STR_PAR_0_TCHG = 'StrPar0_TChg'
S_STR_PAR_1_TCHG = 'StrPar1_TChg'
S_STR_PAR_2_TCHG = 'StrPar2_TChg'
S_STR_PAR_3_TCHG = 'StrPar3_TChg'
S_STR_PAR_4_TCHG = 'StrPar4_TChg'
S_STR_PAR_5_TCHG = 'StrPar5_TChg'
S_STR_PAR_6_TCHG = 'StrPar6_TChg'
S_STR_PAR_7_TCHG = 'StrPar7_TChg'
S_STR_PAR_8_TCHG = 'StrPar8_TChg'
S_STR_PAR_9_TCHG = 'StrPar9_TChg'
S_STR_PAR_10_TCHG = 'StrPar10_TChg'
L_S_STR_PAR_TCHG = [S_STR_PAR_0_TCHG, S_STR_PAR_1_TCHG, S_STR_PAR_2_TCHG,
                    S_STR_PAR_3_TCHG, S_STR_PAR_4_TCHG, S_STR_PAR_5_TCHG,
                    S_STR_PAR_6_TCHG, S_STR_PAR_7_TCHG, S_STR_PAR_8_TCHG,
                    S_STR_PAR_9_TCHG, S_STR_PAR_10_TCHG]
S_VAL_PAR_0_TCHG = 'ValPar0_TChg'
S_VAL_PAR_1_TCHG = 'ValPar1_TChg'
S_VAL_PAR_2_TCHG = 'ValPar2_TChg'
S_VAL_PAR_3_TCHG = 'ValPar3_TChg'
S_VAL_PAR_4_TCHG = 'ValPar4_TChg'
S_VAL_PAR_5_TCHG = 'ValPar5_TChg'
S_VAL_PAR_6_TCHG = 'ValPar6_TChg'
S_VAL_PAR_7_TCHG = 'ValPar7_TChg'
S_VAL_PAR_8_TCHG = 'ValPar8_TChg'
S_VAL_PAR_9_TCHG = 'ValPar9_TChg'
S_VAL_PAR_10_TCHG = 'ValPar10_TChg'
L_S_VAL_PAR_TCHG = [S_VAL_PAR_0_TCHG, S_VAL_PAR_1_TCHG, S_VAL_PAR_2_TCHG,
                    S_VAL_PAR_3_TCHG, S_VAL_PAR_4_TCHG, S_VAL_PAR_5_TCHG,
                    S_VAL_PAR_6_TCHG, S_VAL_PAR_7_TCHG, S_VAL_PAR_8_TCHG,
                    S_VAL_PAR_9_TCHG, S_VAL_PAR_10_TCHG]
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

S_DESC_L__ = 'Component NRT2.1 (L)'
S_DESC_S__ = 'Component NAR2.1 (S)'
S_DESC_K__ = 'Component HPCAL1 (K)'
S_DESC_OAS = 'Component '
S_DESC_LSI = 'Component NRT2.1-NAR2.1 (LS) strong interaction'
S_DESC_LSJ = 'Component NRT2.1-NAR2.1 (LS) weak interaction'
S_DESC_LST = 'Component NRT2.1-NAR2.1 (LS) transition'
S_DESC_LKI = 'Component NRT2.1-HPCAL1 (LK) strong interaction'
S_DESC_LKJ = 'Component NRT2.1-HPCAL1 (LK) weak interaction'
S_DESC_LKT = 'Component NRT2.1-HPCAL1 (LK) transition'
D_DESC = {S_L__: S_DESC_L__, S_S__: S_DESC_S__, S_K__: S_DESC_K__,
          S_LSI: S_DESC_LSI, S_LSJ: S_DESC_LSJ, S_LST: S_DESC_LST,
          S_LKI: S_DESC_LKI, S_LKJ: S_DESC_LKJ, S_LKT: S_DESC_LKT}

# --- constants related to reactions ------------------------------------------
S_RCT_11 = S_1 + S_1
S_RCT_12 = S_1 + S_2
S_RCT_21 = S_2 + S_1
S_RCT_22 = S_2 + S_2
L_S_RCT_2ORD = [S_RCT_21, S_RCT_22]
LEN_S_CP = 7
I_S_CP_SEP1 = 3
I_S_CP_SEP2 = 5

P_DUMMY = 0.5

# --- constants related to model output ---------------------------------------
S_TS = 'TimeStep'
S_TIME = 'Time'
S_CP = 'Comp'
S_CNC_NO3_1M = 'Conc_NO3-'
S_CNC_H2PO4_1M = 'Conc_H2PO4-'
S_MEAN = 'Mean'
S_SUM = 'Sum'
S_M2 = 'M2'
S_VARIANCE = 'Variance'
S_STDDEV = 'StdDev'
S_SEM = 'SEM'
L_S_STATS_OUT = [S_MEAN, S_STDDEV, S_SEM]

# --- constants related to plots ----------------------------------------------
S_D_PLT = 'dPlt'
S_CP_CNC = 'A_CpConc'

# --- other constants ---------------------------------------------------------
M_DETER = 'Deterministic'
M_STOCH = 'Stochastic'

R04 = 4

###############################################################################
