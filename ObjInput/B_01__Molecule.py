# -*- coding: utf-8 -*-
###############################################################################
# --- B_01__Molecule.py -------------------------------------------------------
###############################################################################
import Core.C_00__GenConstants as GC

# --- general -----------------------------------------------------------------
strOType = 'Molecule'
strNSpec = 'Molecule Base'
strCS = 'Mol'
strCL = 'Molecule Base'

# --- names of directories and files ------------------------------------------
sD_SMo = '80_SMo'
sF_SMo = 'SMo'

# --- graphics parameters molecule concentrations plot ------------------------
sPlt_Conc = 'Conc'     # name of the plot and key of the input dict
title_Conc = None       # title of plot
xLbl_Conc = 'Time step' # x-label of plot
yLbl_Conc = 'Concentration [mMol]'    # y-label of plot
tpMark_Conc = 'x'       # marker type of plot
szMark_Conc = 1         # marker size of plot
ewMark_Conc = 1         # marker edge width of plot
ecMark_Conc = (1., 0., 0.)     # marker edge colour of plot
fcMark_Conc = (1., 0.5, 0.)    # marker face colour of plot
styLn_Conc = 'solid'    # line style of plot
wdthLn_Conc = 1         # line width of plot
colLn_Conc = (1., 0.5, 0.)     # line colour of plot
pltAxXY_Conc = (True, True)    # plot x- and/or y-axis

# --- create input dictionary -------------------------------------------------
dIO = {# --- general
       'strOType': strOType,
       'strNSpec': strNSpec,
       'strCS': strCS,
       'strCL': strCL,
       # --- names of directories and files
       'sD_SMo': sD_SMo,
       'sF_SMo': sF_SMo,
       # --- graphics parameters molecule concentrations plot
       'sPlt_Conc': sPlt_Conc,
       GC.S_D_PLT: {sPlt_Conc: {'title': title_Conc,
                                'xLbl': xLbl_Conc,
                                'yLbl': yLbl_Conc,
                                'tpMark': tpMark_Conc,
                                'szMark': szMark_Conc,
                                'ewMark': ewMark_Conc,
                                'ecMark': ecMark_Conc,
                                'fcMark': fcMark_Conc,
                                'styLn': styLn_Conc,
                                'wdthLn': wdthLn_Conc,
                                'colLn': colLn_Conc,
                                'pltAxXY_Conc': pltAxXY_Conc}},
       }
###############################################################################
