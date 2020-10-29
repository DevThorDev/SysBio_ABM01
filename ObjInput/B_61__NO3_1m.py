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

# --- dictionary of parameters for special sites ------------------------------
dInfSpS = {}

# --- initial state -----------------------------------------------------------
concIni = 5                             # initial concentration of NO3-

# --- changes over time in deterministic mode ---------------------------------
mdConcCh = GC.S_NO                      # conc. change mode (S_NO, S_CH_SIN)
perConcCh = 100                         # conc. change period (time steps)
amplConcCh = 4                          # conc. change amplitude
thrLowConc = 4                          # threshold for "low" concentration
thrHighConc = 7                         # threshold for "high" concentration

propIncCpLS = 0.04                      # prop. increase in states LSI, LST
propDecCpLK = 0.03                      # prop. decrease in states LKI, LKT

# --- graphics parameters molecule concentrations plot ------------------------
sPlt_Conc = 'Conc'                  # name of plot and key of input dict
yLbl_Conc = '$[NO_3^-]$ (mM)'       # y-label of plot

# --- create input dictionary -------------------------------------------------
dIO = {# --- general
       'strOType': strOType,
       'strNSpec': strNSpec,
       'strCS': strCS,
       'strCL': strCL,
       # --- dictionary of parameters for special sites
       'dInfSpS': dInfSpS,
       # --- initial state
       GC.S_CONC_INI: concIni,
       # --- changes over time in deterministic mode
       GC.S_MD_CONC_CH: mdConcCh,
       GC.S_PER_CONC_CH: perConcCh,
       GC.S_AMPL_CONC_CH: amplConcCh,
       GC.S_THR_LOW_CONC: thrLowConc,
       GC.S_THR_HIGH_CONC: thrHighConc,
       GC.S_PROP_INC_CP_LS: propIncCpLS,
       GC.S_PROP_DEC_CP_LK: propDecCpLK,
       # --- graphics parameters molecule concentrations plot
       GC.S_D_PLT: {sPlt_Conc: {'yLbl': yLbl_Conc}}}
###############################################################################
