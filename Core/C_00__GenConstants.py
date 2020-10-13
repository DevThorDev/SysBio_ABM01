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
S_ST_A_KIN_INT = 'St_A_Int_AT5G49770_NRT2p1'
S_ST_B_KIN_TRA = 'St_B_Trans_AT5G49770_NRT2p1'
S_ST_C_SPR_INT = 'St_C_Int_NAR2p1_NRT2p1'
S_ST_D_SPR_TRA = 'St_D_Trans_NAR2p1_NRT2p1'

S_STCH_A_B = 'A_B'
S_STCH_B_C = 'B_C'
S_STCH_C_D = 'C_D'
S_STCH_D_A = 'D_A'

# --- constants related to model output ---------------------------------------
S_TS = 'TimeStep'
S_TIME = 'Time'
S_STATE = 'State'
S_CONC_NO3_1M = 'Conc_NO3-'
S_CONC_H2PO4_1M = 'Conc_H2PO4-'

# --- constants related to plots ----------------------------------------------
S_D_PLT = 'dPlt'

# --- other constants ---------------------------------------------------------
M_DETER = 'Deterministic'
M_STOCH = 'Stochastic'
SEP_STD = ';'
R04 = 4

###############################################################################
