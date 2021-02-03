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

# --- plot parameters: component numbers and molecule conc. plot --------------
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
styLn_CpCnc = 'solid'                   # line style of plot
wdthLn_CpCnc = 1                        # line width of plot
colLn_CpCnc = None                      # line colour of plot
pltAxXY_CpCnc = (True, True)            # plot x- and/or y-axis

# --- colours (incl. alpha) for the plots of component groups -----------------
# alpCol = 0.33
# lColA = [(0., 0., 0.9), (0.9, 0.1, 0.), (0.8, 0.8, 0.05),
#          (0.4, 0.2, 0.9), (0.9, 0., 0.8), (0.8, 0.3, 0.8),
#          (0.2, 0.9, 0.4), (0.3, 1., 0.8), (0., 0.9, 0.8)]
# lColB = [(0.2, 0., 0.8), (0.9, 0., 0.), (0.8, 0.0, 0.7),
#          (0., 0.8, 0.), (0.3, 0.5, 0.), (0.8, 0.6, 0.)]
# lColC = [(0., 0., 0.8), (0.9, 0., 0.), (0.8, 0.4, 0.)]
# lColD = [(0., 0., 0.8), (0.9, 0., 0.)]
# dColLn = {GC.S_PLT_GRP_A: lColA, GC.S_PLT_GRP_B: lColB, GC.S_PLT_GRP_C: lColC,
#           GC.S_PLT_GRP_D: lColD}

# dict. of concentration or component strings to be plotted, incl. y-label
# key: (start string of plot, number or string of plot)
# value: (list of components to be considered, y-label of plot, dictionary L)
# dictionary L: key: operation; value: {legend entry: list of components}

# --- definitions for component, component group and concentration plots ------
# group A - 9 main component groups
sPltNm_A = GC.S_PLT_GRP_A
sPltTp_A = sPlt_SCp
lSCpCnc_A = GC.L_S_CP_SHORT_ALL
lSOp_A = [GC.S_MEAN_GR, GC.S_SUM_GR]
dCHdLeg_A = {'L--': ['L--'], 'S--': ['S--'], 'K--': ['K--'],
             'LSI': ['LSI'], 'LSJ': ['LSJ'], 'LST': ['LST'],
             'LKI': ['LKI'], 'LKJ': ['LKJ'], 'LKT': ['LKT']}
yLbl_A = yLbl_Cp
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
           'dCHdLeg': dCHdLeg_A,
           'yLbl': yLbl_A,
           'dCol': dCol_A,
           'alpCol': alpCol_A}

# group B - all complexes
sPltNm_B = GC.S_PLT_GRP_B
sPltTp_B = sPlt_SCp
lSCpCnc_B = GC.L_S_CP_SHORT_ALL
lSOp_B = [GC.S_MEAN_GR, GC.S_SUM_GR]
dCHdLeg_B = {'LSI': ['LSI'], 'LSJ': ['LSJ'], 'LST': ['LST'],
             'LKI': ['LKI'], 'LKJ': ['LKJ'], 'LKT': ['LKT']}
yLbl_B = yLbl_Cp
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
           'dCHdLeg': dCHdLeg_B,
           'yLbl': yLbl_B,
           'dCol': dCol_B,
           'alpCol': alpCol_B}

# group C - "I" complexes vs. "J" complexes vs. "T" complexes
sPltNm_C = GC.S_PLT_GRP_C
sPltTp_C = sPlt_SCp
lSCpCnc_C = GC.L_S_CP_SHORT_ALL
lSOp_C = [GC.S_MEAN_GR, GC.S_SUM_GR]
dCHdLeg_C =  {'LSI': ['LSI', 'LKI'],
              'LSJ': ['LSJ', 'LKJ'],
              'LST': ['LST', 'LKT']}
yLbl_C = yLbl_Cp
dCol_C =  {'LSI': (0., 0., 0.8),
           'LSJ': (0.9, 0., 0.),
           'LST': (0.8, 0.4, 0.)}
alpCol_C = 0.33

dPltG_C = {'sPltNm': sPltNm_C,
           'sPltTp': sPltTp_C,
           'lSCpCnc': lSCpCnc_C,
           'lSOp': lSOp_C,
           'dCHdLeg': dCHdLeg_C,
           'yLbl': yLbl_C,
           'dCol': dCol_C,
           'alpCol': alpCol_C}

# group D - "LS" complexes vs. "LK" complexes
sPltNm_D = GC.S_PLT_GRP_D
sPltTp_D = sPlt_SCp
lSCpCnc_D = GC.L_S_CP_SHORT_ALL
lSOp_D = [GC.S_MEAN_GR, GC.S_SUM_GR]
dCHdLeg_D = {'LSI': ['LSI', 'LSJ', 'LST'], 'LKI': ['LKI', 'LKJ', 'LKT']}
yLbl_D = yLbl_Cp
dCol_D =  {'LSI': (0.9, 0.1, 0.),
           'LKI': (0.8, 0.8, 0.05)}
alpCol_D = 0.33

dPltG_D = {'sPltNm': sPltNm_D,
           'sPltTp': sPltTp_D,
           'lSCpCnc': lSCpCnc_D,
           'lSOp': lSOp_D,
           'dCHdLeg': dCHdLeg_D,
           'yLbl': yLbl_D,
           'dCol': dCol_D,
           'alpCol': alpCol_D}

# component plot of the first nine components of L_S_CP_SHORT_ALL
sPltNm_1 = '1__L--_S--_K--'
sPltTp_1 = sPlt_SCp
lSCpCnc_1 = GC.L_S_CP_SHORT_ALL[:9]
lSOp_1 = None
dCHdLeg_1 = None
yLbl_1 = yLbl_Cp
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
           'dCHdLeg': dCHdLeg_1,
           'yLbl': yLbl_1,
           'dCol': dCol_1,
           'alpCol': alpCol_1}

# concentrations plot of small molecule concentrations
sPltNm_CncNP = '0__NO3-_H2PO4-'
sPltTp_CncNP = sPlt_SCnc
lSCpCnc_CncNP = [GC.ID_NO3_1M, GC.ID_H2PO4_1M]
lSOp_CncNP = None
dCHdLeg_CncNP = None
yLbl_CncNP = yLbl_Cnc
dCol_CncNP =  {GC.ID_NO3_1M: (0.3, 0.3, 0.3),
               GC.ID_H2PO4_1M: (0.55, 0.55, 0.55)}
alpCol_CncNP = 0.33

dPltG_CncNP = {'sPltNm': sPltNm_CncNP,
               'sPltTp': sPltTp_CncNP,
               'lSCpCnc': lSCpCnc_CncNP,
               'lSOp': lSOp_CncNP,
               'dCHdLeg': dCHdLeg_CncNP,
               'yLbl': yLbl_CncNP,
               'dCol': dCol_CncNP,
               'alpCol': alpCol_CncNP}

# dictionary of plots generated (including additional plot infos)
dPltG_CpCnc = {'A': dPltG_A,
               'B': dPltG_B,
               'C': dPltG_C,
               'D': dPltG_D
               # ,
               # '1': dPltG_1,
               # 'CncNP': dPltG_CncNP
               }

# d_9_Groups = {cK: {'L--': ['L--'], 'S--': ['S--'], 'K--': ['K--'],
#                    'LSI': ['LSI'], 'LSJ': ['LSJ'], 'LST': ['LST'],
#                    'LKI': ['LKI'], 'LKJ': ['LKJ'], 'LKT': ['LKT']}
#               for cK in [GC.S_MEAN_GR, GC.S_SUM_GR]}
# d_4_Int_Tra = {cK: {'LSI': ['LSI'], 'LSJ': ['LSJ'], 'LST': ['LST'],
#                     'LKI': ['LKI'], 'LKJ': ['LKJ'], 'LKT': ['LKT']}
#                for cK in [GC.S_MEAN_GR, GC.S_SUM_GR]}
# d_I_vs_J_vs_T = {cK: {'LSI': ['LSI', 'LKI'],
#                       'LSJ': ['LSJ', 'LKJ'],
#                       'LST': ['LST', 'LKT']}
#                 for cK in [GC.S_MEAN_GR, GC.S_SUM_GR]}
# d_S_vs_K = {cK: {'LSI': ['LSI', 'LSJ', 'LST'], 'LKI': ['LKI', 'LKJ', 'LKT']}
#             for cK in [GC.S_MEAN_GR, GC.S_SUM_GR]}
# dlSY = {(sPlt_SCp, GC.S_PLT_GRP_A): (lSCpAll, yLbl_Cp, d_9_Groups),
#         (sPlt_SCp, GC.S_PLT_GRP_B): (lSCpAll, yLbl_Cp, d_4_Int_Tra),
#         (sPlt_SCp, GC.S_PLT_GRP_C): (lSCpAll, yLbl_Cp, d_I_vs_J_vs_T),
#         (sPlt_SCp, GC.S_PLT_GRP_D): (lSCpAll, yLbl_Cp, d_S_vs_K),
#         # (sPlt_SCpCnc, 'A__9_Main_Groups'): (lSCpAll + [GC.ID_NO3_1M], yLbl_CpCnc,
#         #                                  d_9_Groups),
#         # (sPlt_SCpCnc, 'B__Complexes'): (lSCpAll + [GC.ID_NO3_1M], yLbl_CpCnc,
#         #                              d_4_Int_Tra),
#         # (sPlt_SCpCnc, 'C__I_vs_J_vs_T'): (lSCpAll + [GC.ID_NO3_1M], yLbl_CpCnc,
#         #                                d_I_vs_J_vs_T),
#         # (sPlt_SCpCnc, 'D__LS-_vs_LK-'): (lSCpAll + [GC.ID_NO3_1M], yLbl_CpCnc,
#         #                               d_S_vs_K),
#         (sPlt_SCp, 1): (lSCpAll[:9], yLbl_Cp, None),
#         (sPlt_SCnc, None): ([GC.ID_NO3_1M, GC.ID_H2PO4_1M], yLbl_Cnc, None)}

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
                     'styLn': styLn_CpCnc,
                     'wdthLn': wdthLn_CpCnc,
                     'colLn': colLn_CpCnc,
                     'pltAxXY': pltAxXY_CpCnc,
                     'dPltG': dPltG_CpCnc}
       }

###############################################################################
