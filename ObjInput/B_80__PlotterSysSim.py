# -*- coding: utf-8 -*-
###############################################################################
# --- B_80__PlotterSysSim.py --------------------------------------------------
###############################################################################
import os

import Core.C_00__GenConstants as GC

# --- general -----------------------------------------------------------------
strOType = 'PlotterSysSim'
strNSpec = 'Plotter for system and simulation'
strCS = GC.ID_PSS
strCL = GC.S_CL_PLTRSYSSIM

# --- paths -------------------------------------------------------------------
sPPlt = os.path.join('..', '..', '11_SysBio01_ABM01', '50_ModelPlots')

# --- plot parameters: component numbers and molecule conc. plot (general) ----
plotSpread_CpCnc = GC.S_SEM             # GC.S_SGL / GC.S_STDDEV / GC.S_SEM
alphaSpread_CpCnc = 0.95                # 0.9 / 0.95 / 0.99 (confidence int.)

title_CpCnc = None                      # title of plot
xLbl_CpCnc = GC.S_X_LBL                 # x-label of plot
# xLim = None                             # x limits of plot (None: autom.)
# yLim = None                             # x limits of plot (None: autom.)
tpMark_CpCnc = None                     # marker type of plot
szMark_CpCnc = 1                        # marker size of plot
ewMark_CpCnc = 1                        # marker edge width of plot
ecMark_CpCnc = (1., 0., 0.)             # marker edge colour of plot
fcMark_CpCnc = (1., 0.5, 0.)            # marker face colour of plot
pltAxXY_CpCnc = (True, True)            # plot x- and/or y-axis

# --- create input dictionary -------------------------------------------------
dIO = {# --- general
       'strOType': strOType,
       'strNSpec': strNSpec,
       'strCS': strCS,
       'strCL': strCL,
       # --- paths
       'sPPlt': sPPlt,
       # --- plot parameters: component numbers and molecule conc. plot
       GC.S_PLT_CL_CP_CNC: {'plotSpread': plotSpread_CpCnc,
                            'alphaSpread': alphaSpread_CpCnc,
                            'title': title_CpCnc,
                            'xLbl': xLbl_CpCnc,
                            'tpMark': tpMark_CpCnc,
                            'szMark': szMark_CpCnc,
                            'ewMark': ewMark_CpCnc,
                            'ecMark': ecMark_CpCnc,
                            'fcMark': fcMark_CpCnc,
                            'pltAxXY': pltAxXY_CpCnc}
       }

###############################################################################
