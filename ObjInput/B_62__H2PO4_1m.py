# -*- coding: utf-8 -*-
###############################################################################
# --- B_62__H2PO4_1m.py -------------------------------------------------------
###############################################################################
import Core.C_00__GenConstants as GC

# --- general -----------------------------------------------------------------
strOType = 'Small molecule'
strNSpec = 'Dihydrogenphosphate'
strCS = 'H2PO4-'
strCL = 'H2PO4_1m'

# --- dictionary of parameters for special sites ------------------------------
dInfSpS = {}

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
       # --- graphics parameters molecule concentrations plot
       GC.S_D_PLT: {sPlt_Conc: {'yLbl': yLbl_Conc}}}
###############################################################################
