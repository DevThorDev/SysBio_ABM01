# -*- coding: utf-8 -*-
###############################################################################
# --- B_201__NRT2p1.py --------------------------------------------------------
###############################################################################
import Core.C_00__GenConstants as GC

# --- general -----------------------------------------------------------------
strOType = 'Large protein'
strNSpec = 'NRT2.1'
strCS = 'NRT2.1'
strCL = 'NRT2p1'

# --- dictionary of parameters for special sites ------------------------------
dParP_S21_KAs3_Pyl = {'prMin': 0, 'prMax': 0.2,
                      'B': 10., 'C': 1., 'D': 0.025}
dParP_S21_PAs3_DePyl = {'prMin': 0, 'prMax': 0.3,
                        'B': 1., 'C': 20., 'D': 0.035}
dParP_S28_KAsX_Pyl = {'prMin': 0, 'prMax': 0.3,
                      'B': 5., 'C': 1.5, 'D': 0.02}
dParP_S28_PAs4_DePyl = {'prMin': 0, 'prMax': 0.4,
                        'B': 12., 'C': 2.75, 'D': 0.01}
dInfSpS = {'S21': {'Stat': GC.B_NOT_PYL,
                   'Pyl': [(GC.ID_KAS_3, dParP_S21_KAs3_Pyl)],
                   'DePyl': [(GC.ID_PAS_3, dParP_S21_PAs3_DePyl)]},
           'S28': {'Stat': GC.B_NOT_PYL,
                   'Pyl': [(GC.ID_KAS_X, dParP_S28_KAsX_Pyl)],
                   'DePyl': [(GC.ID_PAS_4, dParP_S28_PAs4_DePyl)]}}

# --- create input dictionary -------------------------------------------------
dIO = {# --- general
       'strOType': strOType,
       'strNSpec': strNSpec,
       'strCS': strCS,
       'strCL': strCL,
       # --- dictionary of parameters for special sites
       'dInfSpS': dInfSpS}
###############################################################################
