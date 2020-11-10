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
concIni = 2                             # initial concentration of H2PO4-

# --- changes over time in deterministic mode ---------------------------------
mdConcCh = GC.S_CH_SIN                  # conc. change mode (S_NO, S_CH_SIN)
perConcCh = 500                         # conc. change period (time steps)
amplConcCh = 1                          # conc. change amplitude
thrLowConc = 1.4                        # threshold for "low" concentration
thrHighConc = 2.5                       # threshold for "high" concentration

propIncCpLS = 0.05                      # prop. increase in states LSI, LST
propDecCpLK = 0.07                      # prop. decrease in states LKI, LKT

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
       GC.S_MODE_CHG: mdConcCh,
       GC.S_PERIOD_CHG: perConcCh,
       GC.S_AMPL_CHG: amplConcCh,
       GC.S_THR_LOW_CONC: thrLowConc,
       GC.S_THR_HIGH_CONC: thrHighConc,
       GC.S_PROP_INC_CP_LS: propIncCpLS,
       GC.S_PROP_DEC_CP_LK: propDecCpLK,
       # --- graphics parameters molecule concentrations plot
       GC.S_D_PLT: {sPlt_Conc: {'yLbl': yLbl_Conc}}}
###############################################################################
