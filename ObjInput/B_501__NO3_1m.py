# -*- coding: utf-8 -*-
###############################################################################
# --- B_501__NO3_1m.py --------------------------------------------------------
###############################################################################
import Core.C_00__GenConstants as GC

# --- general -----------------------------------------------------------------
strOType = 'Small molecule'
strNSpec = 'Nitrate'
strCS = 'NO3-'
strCL = 'NO3_1m'
dInfSpS = {}

# --- initial state -----------------------------------------------------------
concIni = 5                             # initial concentration of NO3-

# --- changes over time in deterministic mode ---------------------------------
mdConcCh = GC.S_NO                      # conc. change mode (S_NO, S_CH_SIN)
perConcCh = 100                         # conc. change period (time steps)
amplConcCh = 4                          # conc. change amplitude
thrLowConc = 4                          # threshold for "low" concentration
thrHighConc = 7                         # threshold for "high" concentration

propDecStAB = 0.03                      # prop. decrease in states A, B
propIncStCD = 0.04                      # prop. increase in states C, D

# --- graphics parameters molecule concentrations plot ------------------------
sPlt_Conc = 'Conc'     # name of the plot and key of the input dict
yLbl_Conc = 'Concentration NO3- [mMol]'    # y-label of plot

# --- create input dictionary -------------------------------------------------
dIO = {'strOType': strOType,
       'strNSpec': strNSpec,
       'strCS': strCS,
       'strCL': strCL,
       'dInfSpS': dInfSpS,
       # --- initial state
       GC.S_CONC_INI: concIni,
       # --- changes over time in deterministic mode
       GC.S_MD_CONC_CH: mdConcCh,
       GC.S_PER_CONC_CH: perConcCh,
       GC.S_AMPL_CONC_CH: amplConcCh,
       GC.S_THR_LOW_CONC: thrLowConc,
       GC.S_THR_HIGH_CONC: thrHighConc,
       GC.S_PROP_DEC_ST_AB: propDecStAB,
       GC.S_PROP_INC_ST_CD: propIncStCD,
       # --- graphics parameters molecule concentrations plot
       GC.S_D_PLT: {sPlt_Conc: {'yLbl': yLbl_Conc}}}
###############################################################################
