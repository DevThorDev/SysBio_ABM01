# -*- coding: utf-8 -*-
###############################################################################
# --- B_101__KinaseAT5G49770.py -----------------------------------------------
###############################################################################
import Core.C_00__GenConstants as GC

# --- general -----------------------------------------------------------------
strOType = 'Kinase'
strNSpec = 'Kinase A'
strCS = 'AT5G49770'
strCL = 'AT5G49770'
# 
dParP_S839_KAs1_Pyl = {'prMin': 0, 'prMax': 0.15,
                       'B': 3., 'C': 2.5, 'D': 0.03}
dParP_S839_PAs1_DePyl = {'prMin': 0, 'prMax': 0.25,
                         'B': 25., 'C': 5., 'D': 0.03}
dParP_S870_KAs2_Pyl = {'prMin': 0, 'prMax': 0.4,
                       'B': 20., 'C': 0.5, 'D': 0.015}
dParP_S870_PAs2_DePyl = {'prMin': 0, 'prMax': 0.5,
                         'B': 8., 'C': 0.2, 'D': 0.02}
dInfSpS = {'S839': {'Stat': GC.B_NOT_PYL,
                    'Pyl': [(GC.ID_KAS_1, dParP_S839_KAs1_Pyl)],
                    'DePyl': [(GC.ID_PAS_1, dParP_S839_PAs1_DePyl)]},
           'S870': {'Stat': GC.B_NOT_PYL,
                    'Pyl': [(GC.ID_KAS_2, dParP_S870_KAs2_Pyl)],
                    'DePyl': [(GC.ID_PAS_2, dParP_S870_PAs2_DePyl)]}}

# --- create input dictionary -------------------------------------------------
dIO = {'strOType': strOType,
       'strNSpec': strNSpec,
       'strCS': strCS,
       'strCL': strCL,
       'dInfSpS': dInfSpS}
###############################################################################
