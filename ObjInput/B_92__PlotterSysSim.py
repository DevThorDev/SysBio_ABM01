# -*- coding: utf-8 -*-
###############################################################################
# --- B_92__PlotterSysSim.py --------------------------------------------------
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

sPlt_SCpCnc = '01_SelCpConc'            # name of sel. comps and conc. plot
sPlt_SCp = '02_SelCp'                   # name of sel. comps plot
sPlt_SCnc = '03_SelConc'                # name of sel. conc. plot

title_CpCnc = None                      # title of plot
xLbl_CpCnc = GC.S_TIME                  # x-label of plot
yLbl_CpCnc = 'Component incidence and molecule concentration (mM)'
yLbl_Cp = 'Component incidence'
yLbl_Cnc = 'Molecule concentration (mM)'
yLbl_Cnc_N = '$[NO_3^-]$ (mM)'          # y-label of NO3- concentration plot
yLbl_Cnc_P = '$[H_2PO_4^-]$ (mM)'       # y-label of H2PO4- concentration plot
# xLim = None                             # x limits of plot (None: autom.)
# yLim = None                             # x limits of plot (None: autom.)
tpMark_CpCnc = None                     # marker type of plot
szMark_CpCnc = 1                        # marker size of plot
ewMark_CpCnc = 1                        # marker edge width of plot
ecMark_CpCnc = (1., 0., 0.)             # marker edge colour of plot
fcMark_CpCnc = (1., 0.5, 0.)            # marker face colour of plot
pltAxXY_CpCnc = (True, True)            # plot x- and/or y-axis

# --- definitions for component, component group and concentration plots ------
# group A - 9 main component groups ...........................................
sPltNm_A = GC.S_PLT_GR_A
sPltTp_A = sPlt_SCp
lSCpCnc_A = GC.L_S_CP_SHORT_ALL
lSOp_A = [GC.S_MEAN_GR, GC.S_SUM_GR]
dCHdGr_A = {'L--': ['L--'], 'S--': ['S--'], 'K--': ['K--'],
            'LSI': ['LSI'], 'LSJ': ['LSJ'], 'LST': ['LST'],
            'LKI': ['LKI'], 'LKJ': ['LKJ'], 'LKT': ['LKT']}
yLbl_A = yLbl_Cp
styLnCt_A = 'solid'
styLnCI_A = 'solid'
wdthLnCt_A = 1
wdthLnCI_A = 0.5
dCol_A =  {'L--': (0., 0., 0.9),
           'S--': (0.9, 0.1, 0.),
           'K--': (0.8, 0.8, 0.05),
           'LSI': (0.4, 0.2, 0.9),
           'LSJ': (0.9, 0., 0.8),
           'LST': (0.8, 0.3, 0.8),
           'LKI': (0.2, 0.9, 0.4),
           'LKJ': (0.3, 1., 0.8),
           'LKT': (0., 0.9, 0.8)}
alpCol_A = 0.33

dPltG_A = {'sPltNm': sPltNm_A,
           'sPltTp': sPltTp_A,
           'lSCpCnc': lSCpCnc_A,
           'lSOp': lSOp_A,
           'dCHdGr': dCHdGr_A,
           'yLbl': yLbl_A,
           'styLnCt': styLnCt_A,
           'styLnCI': styLnCI_A,
           'wdthLnCt': wdthLnCt_A,
           'wdthLnCI': wdthLnCI_A,
           'dCol': dCol_A,
           'alpCol': alpCol_A}

# group B - all complexes .....................................................
sPltNm_B = GC.S_PLT_GR_B
sPltTp_B = sPlt_SCp
lSCpCnc_B = GC.L_S_CP_SHORT_ALL
lSOp_B = [GC.S_MEAN_GR, GC.S_SUM_GR]
dCHdGr_B = {'LSI': ['LSI'], 'LSJ': ['LSJ'], 'LST': ['LST'],
            'LKI': ['LKI'], 'LKJ': ['LKJ'], 'LKT': ['LKT']}
yLbl_B = yLbl_Cp
styLnCt_B = 'solid'
styLnCI_B = 'solid'
wdthLnCt_B = 1
wdthLnCI_B = 0.5
dCol_B =  {'LSI': (0.2, 0., 0.8),
           'LSJ': (0.9, 0., 0.),
           'LST': (0.8, 0.0, 0.7),
           'LKI': (0., 0.8, 0.),
           'LKJ': (0.3, 0.5, 0.),
           'LKT': (0.8, 0.6, 0.)}
alpCol_B = 0.33

dPltG_B = {'sPltNm': sPltNm_B,
           'sPltTp': sPltTp_B,
           'lSCpCnc': lSCpCnc_B,
           'lSOp': lSOp_B,
           'dCHdGr': dCHdGr_B,
           'yLbl': yLbl_B,
           'styLnCt': styLnCt_B,
           'styLnCI': styLnCI_B,
           'wdthLnCt': wdthLnCt_B,
           'wdthLnCI': wdthLnCI_B,
           'dCol': dCol_B,
           'alpCol': alpCol_B}

# group C - "I" complexes vs. "J" complexes vs. "T" complexes .................
sPltNm_C = GC.S_PLT_GR_C
sPltTp_C = sPlt_SCp
lSCpCnc_C = GC.L_S_CP_SHORT_ALL
lSOp_C = [GC.S_MEAN_GR, GC.S_SUM_GR]
dCHdGr_C =  {'LSI': ['LSI', 'LKI'],
             'LSJ': ['LSJ', 'LKJ'],
             'LST': ['LST', 'LKT']}
yLbl_C = yLbl_Cp
styLnCt_C = 'solid'
styLnCI_C = 'solid'
wdthLnCt_C = 1
wdthLnCI_C = 0.5
dCol_C =  {'LSI': (0., 0., 0.8),
           'LSJ': (0.9, 0., 0.),
           'LST': (0.8, 0.4, 0.)}
alpCol_C = 0.33

dPltG_C = {'sPltNm': sPltNm_C,
           'sPltTp': sPltTp_C,
           'lSCpCnc': lSCpCnc_C,
           'lSOp': lSOp_C,
           'dCHdGr': dCHdGr_C,
           'yLbl': yLbl_C,
           'styLnCt': styLnCt_C,
           'styLnCI': styLnCI_C,
           'wdthLnCt': wdthLnCt_C,
           'wdthLnCI': wdthLnCI_C,
           'dCol': dCol_C,
           'alpCol': alpCol_C}

# group D - "LS" complexes vs. "LK" complexes .................................
sPltNm_D = GC.S_PLT_GR_D
sPltTp_D = sPlt_SCp
lSCpCnc_D = GC.L_S_CP_SHORT_ALL
lSOp_D = [GC.S_MEAN_GR, GC.S_SUM_GR]
dCHdGr_D = {'LSI': ['LSI', 'LSJ', 'LST'], 'LKI': ['LKI', 'LKJ', 'LKT']}
yLbl_D = yLbl_Cp
styLnCt_D = 'solid'
styLnCI_D = 'solid'
wdthLnCt_D = 1
wdthLnCI_D = 0.5
dCol_D =  {'LSI': (0.9, 0.1, 0.),
           'LKI': (0.8, 0.8, 0.05)}
alpCol_D = 0.33

dPltG_D = {'sPltNm': sPltNm_D,
           'sPltTp': sPltTp_D,
           'lSCpCnc': lSCpCnc_D,
           'lSOp': lSOp_D,
           'dCHdGr': dCHdGr_D,
           'yLbl': yLbl_D,
           'styLnCt': styLnCt_D,
           'styLnCI': styLnCI_D,
           'wdthLnCt': wdthLnCt_D,
           'wdthLnCI': wdthLnCI_D,
           'dCol': dCol_D,
           'alpCol': alpCol_D}

# component plot of the first nine components of L_S_CP_SHORT_ALL .............
sPltNm_1 = '1__L--_S--_K--'
sPltTp_1 = sPlt_SCp
lSCpCnc_1 = GC.L_S_CP_SHORT_ALL[:9]
lSOp_1 = None
dCHdGr_1 = None
yLbl_1 = yLbl_Cp
styLnCt_1 = 'solid'
styLnCI_1 = 'solid'
wdthLnCt_1 = 1
wdthLnCI_1 = 0.5
dCol_1 =  {lSCpCnc_1[0]: (0.2, 0.2, 1.), lSCpCnc_1[1]: (0., 0., 1.),
           lSCpCnc_1[2]: (0., 0., 0.8), lSCpCnc_1[3]: (0., 0., 0.5),
           lSCpCnc_1[4]: (0.9, 0.1, 0.),
           lSCpCnc_1[5]: (1., 1., 0.1), lSCpCnc_1[6]: (0.85, 0.85, 0.),
           lSCpCnc_1[7]: (0.7, 0.7, 0.), lSCpCnc_1[8]: (0.5, 0.5, 0.)}
alpCol_1 = 0.33

dPltG_1 = {'sPltNm': sPltNm_1,
           'sPltTp': sPltTp_1,
           'lSCpCnc': lSCpCnc_1,
           'lSOp': lSOp_1,
           'dCHdGr': dCHdGr_1,
           'yLbl': yLbl_1,
           'styLnCt': styLnCt_1,
           'styLnCI': styLnCI_1,
           'wdthLnCt': wdthLnCt_1,
           'wdthLnCI': wdthLnCI_1,
           'dCol': dCol_1,
           'alpCol': alpCol_1}

# concentrations plot of small molecule concentrations ........................
sPltNm_CncNP = '0__NO3-_H2PO4-'
sPltTp_CncNP = sPlt_SCnc
lSCpCnc_CncNP = [GC.ID_NO3_1M, GC.ID_H2PO4_1M]
lSOp_CncNP = None
dCHdGr_CncNP = None
yLbl_CncNP = yLbl_Cnc
styLnCt_CncNP = 'solid'
styLnCI_CncNP = 'solid'
wdthLnCt_CncNP = 1
wdthLnCI_CncNP = 0.5
dCol_CncNP =  {GC.ID_NO3_1M: (0.1, 0.6, 0.1),
               GC.ID_H2PO4_1M: (0.4, 0.1, 0.5)}
alpCol_CncNP = 0.33

dPltG_CncNP = {'sPltNm': sPltNm_CncNP,
               'sPltTp': sPltTp_CncNP,
               'lSCpCnc': lSCpCnc_CncNP,
               'lSOp': lSOp_CncNP,
               'dCHdGr': dCHdGr_CncNP,
               'yLbl': yLbl_CncNP,
               'styLnCt': styLnCt_CncNP,
               'styLnCI': styLnCI_CncNP,
               'wdthLnCt': wdthLnCt_CncNP,
               'wdthLnCI': wdthLnCI_CncNP,
               'dCol': dCol_CncNP,
               'alpCol': alpCol_CncNP}

# dictionary of plots generated (including additional plot infos) -------------
dPltG_CpCnc = {'A': dPltG_A,
               'B': dPltG_B,
               'C': dPltG_C,
               'D': dPltG_D,
               '1': dPltG_1,
               'CncNP': dPltG_CncNP}

# --- create input dictionary -------------------------------------------------
dIO = {# --- general
       'strOType': strOType,
       'strNSpec': strNSpec,
       'strCS': strCS,
       'strCL': strCL,
       # --- paths
       'sPPlt': sPPlt,
       # --- plot parameters: component numbers and molecule conc. plot
       GC.S_CP_CNC: {'plotSpread': plotSpread_CpCnc,
                     'alphaSpread': alphaSpread_CpCnc,
                     'sPlt_SCpCnc': sPlt_SCpCnc,
                     'sPlt_SCp': sPlt_SCp,
                     'sPlt_SCnc': sPlt_SCnc,
                     'title': title_CpCnc,
                     'xLbl': xLbl_CpCnc,
                     'yLbl_CpCnc': yLbl_CpCnc,
                     'yLbl_Cp': yLbl_Cp,
                     'yLbl_Cnc': yLbl_Cnc,
                     'yLbl_Cnc_N': yLbl_Cnc_N,
                     'yLbl_Cnc_P': yLbl_Cnc_P,
                     'tpMark': tpMark_CpCnc,
                     'szMark': szMark_CpCnc,
                     'ewMark': ewMark_CpCnc,
                     'ecMark': ecMark_CpCnc,
                     'fcMark': fcMark_CpCnc,
                     'pltAxXY': pltAxXY_CpCnc,
                     # def. for component, component group and conc. plots
                     'dPltG': dPltG_CpCnc}
       }

###############################################################################
