# -*- coding: utf-8 -*-
###############################################################################
# --- B_86__PlotterData06.py --------------------------------------------------
###############################################################################
import Core.C_00__GenConstants as GC

# --- general -----------------------------------------------------------------
strOType = 'PlotterData06'
strNSpec = 'Plotter data for system and simulation (06)'
strCS = GC.ID_PDT
strCL = GC.S_CL_PLTRDAT + GC.S_06

# --- definitions for component, component group and concentration plots ------
# concentrations plot of small molecule concentrations ........................
sPltNm = GC.S_PLT_NM_CNC_N_P            # name of plot (needs to be unique)
sPltCl = GC.S_PLT_CL_CP_CNC             # class of the plot (e.g. comp.-conc.)
sPltTp = GC.S_PLT_TP_SEL_CNC            # type of the plot (e.g. comp., conc.)
lSCpCnc = GC.L_ID_SMO_SYS               # list of IDs of small mol. considered
lSOp = [None]                           # list of operation strings (mean, sum)
# dict. of assignment of components into groups; key: representing column hdr.
dCHdGr = None
yLbl = GC.S_Y_LBL_CNC                   # y-label (concentrations)
styLnCt = 'solid'
styLnCI = 'solid'
wdthLnCt = 2
wdthLnCI = 0.5
dCol = {GC.ID_NO3_1M: (0.1, 0.6, 0.1),
        GC.ID_H2PO4_1M: (0.4, 0.1, 0.5)}
alpCol = 0.25

# --- create input dictionary -------------------------------------------------
dIO = {# --- general
       'strOType': strOType,
       'strNSpec': strNSpec,
       'strCS': strCS,
       'strCL': strCL,
       # concentrations plot of small molecule concentrations
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
