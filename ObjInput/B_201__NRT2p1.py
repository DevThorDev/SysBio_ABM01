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
                   'Pyl': [GC.ID_KAS_3],
                   'DePyl': [GC.ID_PAS_3]},
           'S28': {'Stat': GC.B_NOT_PYL,
                   'Pyl': [GC.ID_KAS_X],
                   'DePyl': [GC.ID_PAS_4]}}

# --- create input dictionary -------------------------------------------------
dIO = {'strOType': strOType,
       'strNSpec': strNSpec,
       'strCS': strCS,
       'strCL': strCL,
       'dInfSpS': dInfSpS}
###############################################################################
