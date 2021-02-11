# -*- coding: utf-8 -*-
###############################################################################
# --- B_81__PlotterData01.py --------------------------------------------------
###############################################################################
import Core.C_00__GenConstants as GC

# --- general -----------------------------------------------------------------
strOType = 'PlotterData01'
strNSpec = 'Plotter data for system and simulation (01)'
strCS = GC.ID_PDT
strCL = GC.S_CL_PLTRDAT + GC.S_01

# --- definitions for component, component group and concentration plots ------
# group A - 9 main component groups ...........................................
sPltNm = GC.S_PLT_GR_A                  # name of plot (needs to be unique)
sPltCl = GC.S_PLT_CL_CP_CNC             # class of the plot (e.g. comp.-conc.)
sPltTp = GC.S_PLT_TP_SEL_CP             # type of the plot (e.g. comp., conc.)
lSCpCnc = GC.L_S_CP_SHORT_ALL           # list of short comp. names considered
lSOp = [GC.S_MEAN_GR, GC.S_SUM_GR]      # list of operation strings (mean, sum)
# dict. of assignment of components into groups; key: representing column hdr.
dCHdGr = {'L--': ['L--'], 'S--': ['S--'], 'K--': ['K--'],
          'LSI': ['LSI'], 'LSJ': ['LSJ'], 'LST': ['LST'],
          'LKI': ['LKI'], 'LKJ': ['LKJ'], 'LKT': ['LKT']}
yLbl = GC.S_Y_LBL_CP                    # y-label (components)
styLnCt = 'solid'
styLnCI = 'solid'
wdthLnCt = 1
wdthLnCI = 0.5
dCol = {'L--': (0., 0., 0.9),
        'S--': (0.9, 0.1, 0.),
        'K--': (0.8, 0.8, 0.05),
        'LSI': (0.4, 0.2, 0.9),
        'LSJ': (0.9, 0., 0.8),
        'LST': (0.8, 0.3, 0.8),
        'LKI': (0.2, 0.9, 0.4),
        'LKJ': (0.3, 1., 0.8),
        'LKT': (0., 0.9, 0.8)}
alpCol = 0.33

# --- create input dictionary -------------------------------------------------
dIO = {# --- general
       'strOType': strOType,
       'strNSpec': strNSpec,
       'strCS': strCS,
       'strCL': strCL,
       # group A - 9 main component groups
       'sPltNm': sPltNm,
       'sPltCl': sPltCl,
       'sPltTp': sPltTp,
       'lSCpCnc': lSCpCnc,
       'lSOp': lSOp,
       'dCHdGr': dCHdGr,
       'yLbl': yLbl,
       'styLnCt': styLnCt,
       'styLnCI': styLnCI,
       'wdthLnCt': wdthLnCt,
       'wdthLnCI': wdthLnCI,
       'dCol': dCol,
       'alpCol': alpCol}

###############################################################################
