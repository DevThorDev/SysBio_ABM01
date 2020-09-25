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
dInfSpS = {'S21': {'Stat': GC.B_NOT_PYL,
                   'Pyl': ['Phosphatase3'],
                   'DePyl': ['Phosphatase3']},
           'S28': {'Stat': GC.B_NOT_PYL,
                   'Pyl': ['Phosphatase4'],
                   'DePyl': ['Phosphatase4']}}

# --- create input dictionary -------------------------------------------------
dIO = {'strOType': strOType,
       'strNSpec': strNSpec,
       'strCS': strCS,
       'strCL': strCL,
       'dInfSpS': dInfSpS}
###############################################################################
