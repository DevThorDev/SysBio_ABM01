# -*- coding: utf-8 -*-
###############################################################################
# --- B_99__Simulation.py -----------------------------------------------------
###############################################################################
import os

import Core.C_00__GenConstants as GC

# --- general -----------------------------------------------------------------
strOType = 'Simulation'
strNSpec = 'Simulation including all repetitions'
strCS = GC.ID_SIM
strCL = GC.S_CL_SIMULATION

cSep = GC.SEP_STD

# --- flow control ------------------------------------------------------------
doEvoT = False
doPlots = True
nReps = 5                   # 10
nTSAllRep = 200             # 500
tStart = 0                  # 0
tMax = 10.                  # 10.
maxTS = 10000000            # 10000000
minDispTS = 0
modDispTS = 10000           # 10000
assert tMax >= tStart and maxTS > 0

# --- path, directory and file names ------------------------------------------
sD_Obj = GC.S_DIR_SIM
sF_Obj = GC.S_RES_SIM

sPInD = os.path.join('..', '..', '11_SysBio01_ABM01', '20_InputData')
sPRes = os.path.join('..', '..', '11_SysBio01_ABM01', '40_ModelResults')
sPPlt = os.path.join('..', '..', '11_SysBio01_ABM01', '50_ModelPlots')

dSFInD = {GC.S_00: (GC.S_00 + GC.S_USC + 'Strings', 1),
          GC.S_01: (GC.S_01 + GC.S_USC + 'InitialSysComp', 1),
          GC.S_02: (GC.S_02 + GC.S_USC + 'ConcSMo', 0),
          GC.S_03: (GC.S_03 + GC.S_USC + 'WeightsReactionTypes', 1),
          GC.S_04: (GC.S_04 + GC.S_USC + 'WeightsReactions', 2),
          GC.S_05: (GC.S_05 + GC.S_USC + 'CompDependOnSMoConc', 1),
          GC.S_06: (GC.S_06 + GC.S_USC + 'SMoConcDependOnComp', 1),
          GC.S_07: (GC.S_07 + GC.S_USC + 'OtherInputValues', 1)}

# --- graphics parameters: component numbers and molecule conc. plot ----------
plotSpread = GC.S_STDDEV                # GC.S_SGL / GC.S_STDDEV / GC.S_SEM

sPlt_SSC = '01_SelCpConc'               # name of sel. comps and conc. plot
sPlt_SCp = '02_SelCp'                   # name of sel. comps plot
sPlt_SCn = '03_SelConc'                 # name of sel. conc. plot

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

# dict. of concentration or component strings to be plotted, incl. y-label
# key: (start string of plot, number or string of plot)
# value: (list of components to be considered, y-label of plot, dictionary L)
# dictionary L: key: operation; value: {legend entry: list of components}
lSCpAll = ['L--00--', 'L--01--', 'L--10--', 'L--11--',
           'S------', 'K----00', 'K----01', 'K----10', 'K----11',
           'X------', 'Y------', 'A------', 'B------', 'C------', 'D------',
           'LST00--', 'LSI01--', 'LST10--', 'LSJ11--',
           'LKT0000', 'LKJ0001', 'LKT0010', 'LKT0011', 'LKT0100', 'LKT0101',
           'LKT0110', 'LKT0111', 'LKT1000', 'LKI1001', 'LKT1010', 'LKT1011',
           'LKT1100', 'LKT1101', 'LKT1110', 'LKT1111']
d_9_Groups = {cK: {'L--': ['L--'], 'S--': ['S--'], 'K--': ['K--'],
                   'LSI': ['LSI'], 'LSJ': ['LSJ'], 'LST': ['LST'],
                   'LKI': ['LKI'], 'LKJ': ['LKJ'], 'LKT': ['LKT']}
              for cK in [GC.S_MEAN, GC.S_SUM]}
d_I_vs_J_vs_T = {cK: {'LSI': ['LSI', 'LKI'],
                      'LSJ': ['LSJ', 'LKJ'],
                      'LST': ['LST', 'LKT']}
                for cK in [GC.S_MEAN, GC.S_SUM]}
d_S_vs_K = {cK: {'LSI': ['LSI', 'LSJ', 'LST'], 'LKI': ['LKI', 'LKJ', 'LKT']}
            for cK in [GC.S_MEAN, GC.S_SUM]}
d_4_Int_Tra = {cK: {'LSI': ['LSI'], 'LSJ': ['LSJ'], 'LST': ['LST'],
                    'LKI': ['LKI'], 'LKJ': ['LKJ'], 'LKT': ['LKT']}
               for cK in [GC.S_MEAN, GC.S_SUM]}
dlSY = {(sPlt_SCp, 'A__9_Main_Groups'): (lSCpAll, yLbl_Cp, d_9_Groups),
        (sPlt_SCp, 'B__Complexes'): (lSCpAll, yLbl_Cp, d_4_Int_Tra),
        (sPlt_SCp, 'C__I_vs_J_vs_T'): (lSCpAll, yLbl_Cp, d_I_vs_J_vs_T),
        (sPlt_SCp, 'D__LS-_vs_LK-'): (lSCpAll, yLbl_Cp, d_S_vs_K),
        # (sPlt_SSC, 'A__9_Main_Groups'): (lSCpAll + [GC.ID_NO3_1M], yLbl_CpCnc,
        #                                  d_9_Groups),
        # (sPlt_SSC, 'B__Complexes'): (lSCpAll + [GC.ID_NO3_1M], yLbl_CpCnc,
        #                              d_4_Int_Tra),
        # (sPlt_SSC, 'C__I_vs_J_vs_T'): (lSCpAll + [GC.ID_NO3_1M], yLbl_CpCnc,
        #                                d_I_vs_J_vs_T),
        # (sPlt_SSC, 'D__LS-_vs_LK-'): (lSCpAll + [GC.ID_NO3_1M], yLbl_CpCnc,
        #                               d_S_vs_K),
        (sPlt_SCp, 1): (lSCpAll[:9], yLbl_Cp, None),
        (sPlt_SCp, None): (lSCpAll, yLbl_Cp, d_9_Groups),
        (sPlt_SCn, None): ([GC.ID_NO3_1M, GC.ID_H2PO4_1M], yLbl_Cnc, None)}

# --- create input dictionary -------------------------------------------------
dIO = {# --- general
       'strOType': strOType,
       'strNSpec': strNSpec,
       'strCS': strCS,
       'strCL': strCL,
       'cSep': cSep,
       # --- flow control
       'doEvoT': doEvoT,
       'doPlots': doPlots,
       'nReps': nReps,
       'nTSAllRep': nTSAllRep,
       'tStart': tStart,
       'tMax': tMax,
       'maxTS': maxTS,
       'minDispTS': minDispTS,
       'modDispTS': modDispTS,
       # --- path, directory and file names
       'sD_Obj': sD_Obj,
       'sF_Obj': sF_Obj,
       'sPInD': sPInD,
       'sPRes': sPRes,
       'sPPlt': sPPlt,
       'dSFInD': dSFInD,
       # --- graphics parameters: component numbers and molecule conc. plot
       GC.S_D_PLT: {GC.S_CP_CNC: {'plotSpread': plotSpread,
                                  'sPlt_SSC': sPlt_SSC,
                                  'sPlt_SCp': sPlt_SCp,
                                  'sPlt_SCn': sPlt_SCn,
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
                                  'dlSY': dlSY}}}

###############################################################################
