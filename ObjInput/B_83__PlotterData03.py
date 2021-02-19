###############################################################################
# --- B_83__PlotterData03.py --------------------------------------------------
###############################################################################
import Core.C_00__GenConstants as GC

# --- general -----------------------------------------------------------------
strOType = 'PlotterData03'
strNSpec = 'Plotter data for system and simulation (03)'
strCS = GC.ID_PDT
strCL = GC.S_CL_PLTRDAT + GC.S_03

# --- definitions for component, component group and concentration plots ------
# group C - "I" complexes vs. "J" complexes vs. "T" complexes .................
sPltNm = GC.S_PLT_GR_C                  # name of plot (needs to be unique)
sPltCl = GC.S_PLT_CL_CP_CNC             # class of the plot (e.g. comp.-conc.)
sPltTp = GC.S_PLT_TP_SEL_CP             # type of the plot (e.g. comp., conc.)
lSCpCnc = GC.L_S_CP_SHORT_ALL           # list of short comp. names considered
lSOp = [GC.S_MEAN_GR, GC.S_SUM_GR]      # list of operation strings (mean, sum)
# dict. of assignment of components into groups; key: representing column hdr.
dCHdGr = {'LSI': ['LSI', 'LKI'],
          'LSJ': ['LSJ', 'LKJ'],
          'LST': ['LST', 'LKT']}
yLbl = GC.S_Y_LBL_CP                    # y-label (components)
styLnCt = 'solid'
styLnCI = 'solid'
wdthLnCt = 1
wdthLnCI = 0.5
dCol = {'LSI': (0., 0., 0.8),
        'LSJ': (0.9, 0., 0.),
        'LST': (0.8, 0.4, 0.)}
alpCol = 0.25

# --- create input dictionary -------------------------------------------------
dIO = {# --- general
       'strOType': strOType,
       'strNSpec': strNSpec,
       'strCS': strCS,
       'strCL': strCL,
       # group C - "I" complexes vs. "J" complexes vs. "T" complexes
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
