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
mdConcCh = GC.S_CH_SIN                  # conc. change mode (S_CH_SIN)
perConcCh = 100                         # conc. change period (time steps)
amplConcCh = 4                          # conc. change amplitude

# --- create input dictionary -------------------------------------------------
dIO = {'strOType': strOType,
       'strNSpec': strNSpec,
       'strCS': strCS,
       'strCL': strCL,
       'dInfSpS': dInfSpS,
       # --- initial state
       'concIni': concIni,
       # --- changes over time in deterministic mode
       'mdConcCh': mdConcCh,
       'perConcCh': perConcCh,
       'amplConcCh': amplConcCh}
###############################################################################
