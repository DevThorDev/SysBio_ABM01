# -*- coding: utf-8 -*-
###############################################################################
# --- B_502__H2PO4_1m.py ------------------------------------------------------
###############################################################################
import Core.C_00__GenConstants as GC

# --- general -----------------------------------------------------------------
strOType = 'Small molecule'
strNSpec = 'Dihydrogenphosphate'
strCS = 'H2PO4-'
strCL = 'H2PO4_1m'

# --- dictionary of parameters for special sites ------------------------------
dInfSpS = {}

# --- initial state -----------------------------------------------------------
concIni = 2                             # initial concentration of NO3-

# --- changes over time in deterministic mode ---------------------------------
mdConcCh = GC.S_CH_SIN                  # conc. change mode (S_NO, S_CH_SIN)
perConcCh = 500                         # conc. change period (time steps)
amplConcCh = 1                          # conc. change amplitude
thrLowConc = 1.4                        # threshold for "low" concentration
thrHighConc = 2.5                       # threshold for "high" concentration

propDecStAB = 0.07                      # prop. decrease in states A, B
propIncStCD = 0.05                      # prop. increase in states C, D

# --- graphics parameters molecule concentrations plot ------------------------
sPlt_Conc = 'Conc'                  # name of plot and key of input dict
yLbl_Conc = '$[H_2PO_4^-]$ (mM)'    # y-label of plot

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
       GC.S_PROP_DEC_ST_AB: propDecStAB,
       GC.S_PROP_INC_ST_CD: propIncStCD,
       # --- graphics parameters molecule concentrations plot
       GC.S_D_PLT: {sPlt_Conc: {'yLbl': yLbl_Conc}}}
###############################################################################
