# -*- coding: utf-8 -*-
###############################################################################
# --- B_85__PlotterData05.py --------------------------------------------------
###############################################################################
import Core.C_00__GenConstants as GC

# --- general -----------------------------------------------------------------
strOType = 'PlotterData05'
strNSpec = 'Plotter data for system and simulation (05)'
strCS = GC.ID_PDT
strCL = GC.S_CL_PLTRDAT + GC.S_05

# --- definitions for component, component group and concentration plots ------
# component plot of the first nine components of L_S_CP_SHORT_ALL .............
sPltNm = GC.S_PLT_NM_CP_SET01           # name of plot (needs to be unique)
sPltCl = GC.S_PLT_CL_CP_CNC             # class of the plot (e.g. comp.-conc.)
sPltTp = GC.S_PLT_TP_SEL_CP             # type of the plot (e.g. comp., conc.)
lSCpCnc = GC.L_S_CP_SHORT_ALL[:9]       # list of short comp. names considered
lSOp = [None]                           # list of operation strings (mean, sum)
# dict. of assignment of components into groups; key: representing column hdr.
dCHdGr = None
yLbl = GC.S_Y_LBL_CP                    # y-label (components)
styLnCt = 'solid'
styLnCI = 'solid'
wdthLnCt = 1
wdthLnCI = 0.5
dCol = {GC.L_S_CP_SHORT_ALL[0]: (0.2, 0.2, 1.),    # 'L--00--'
        GC.L_S_CP_SHORT_ALL[1]: (0., 0., 1.),      # 'L--01--'
        GC.L_S_CP_SHORT_ALL[2]: (0., 0., 0.8),     # 'L--10--'
        GC.L_S_CP_SHORT_ALL[3]: (0., 0., 0.5),     # 'L--11--'
        GC.L_S_CP_SHORT_ALL[4]: (0.9, 0.1, 0.),    # 'S------'
        GC.L_S_CP_SHORT_ALL[5]: (1., 1., 0.1),     # 'K----00'
        GC.L_S_CP_SHORT_ALL[6]: (0.85, 0.85, 0.),  # 'K----01'
        GC.L_S_CP_SHORT_ALL[7]: (0.7, 0.7, 0.),    # 'K----10'
        GC.L_S_CP_SHORT_ALL[8]: (0.5, 0.5, 0.)}    # 'K----11'
alpCol = 0.25

# --- create input dictionary -------------------------------------------------
dIO = {# --- general
       'strOType': strOType,
       'strNSpec': strNSpec,
       'strCS': strCS,
       'strCL': strCL,
       # component plot of the first nine components of L_S_CP_SHORT_ALL
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
