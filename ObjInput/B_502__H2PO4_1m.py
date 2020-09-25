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
dInfSpS = {}

# --- initial state -----------------------------------------------------------
concIni = 2                             # initial concentration of NO3-

# --- changes over time in deterministic mode ---------------------------------
mdConcCh = GC.S_CH_SIN                  # conc. change mode (S_CH_SIN)
perConcCh = 500                         # conc. change period (time steps)
amplConcCh = 1                          # conc. change amplitude
thrLowConc = 1.4                        # threshold for "low" concentration
thrHighConc = 2.5                       # threshold for "high" concentration

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
       'amplConcCh': amplConcCh,
       'thrLowConc': thrLowConc,
       'thrHighConc': thrHighConc}
###############################################################################
