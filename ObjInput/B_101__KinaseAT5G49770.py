# -*- coding: utf-8 -*-
###############################################################################
# --- B_101__KinaseAT5G49770.py -----------------------------------------------
###############################################################################
import Core.C_00__GenConstants as GC

# --- general -----------------------------------------------------------------
strOType = 'Kinase'
strNSpec = 'Kinase001'
strCS = 'AT5G49770'
strCL = 'AT5G49770'
dInfSpS = {'S839': {'Stat': GC.B_NOT_PYL,
                    'Pyl': ['Phosphatase1'],
                    'DePyl': ['Phosphatase1']},
           'S870': {'Stat': GC.B_NOT_PYL,
                    'Pyl': ['Phosphatase2'],
                    'DePyl': ['Phosphatase2']}}

# --- create input dictionary --------------------------------------------------
dIO = {'strOType': strOType,
       'strNSpec': strNSpec,
       'strCS': strCS,
       'strCL': strCL,
       'dInfSpS': dInfSpS}
###############################################################################
