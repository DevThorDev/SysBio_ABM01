# -*- coding: utf-8 -*-
###############################################################################
# --- B_61__NO3_1m.py ---------------------------------------------------------
###############################################################################
import Core.C_00__GenConstants as GC

# --- general -----------------------------------------------------------------
strOType = 'Small molecule'
strNSpec = 'Small molecule nitrate'
strCS = GC.S_N
strCL = GC.ID_NO3_1M

# --- dictionary of parameters for special sites ------------------------------
dInfSpS = {}

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
       # --- graphics parameters molecule concentrations plot
       GC.S_D_PLT: {sPlt_Conc: {'yLbl': yLbl_Conc}}}

###############################################################################
