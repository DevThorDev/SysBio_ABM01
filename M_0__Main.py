# -*- coding: utf-8 -*-
###############################################################################
# --- M_0__Main.py ------------------------------------------------------------
###############################################################################
import os

import Core.F_00__GenFunctions as GF
import Core.F_04__MainFunctions as MF

from Control.A_00__GenInput import dictInpG
from Core.C_00__GenConstants import NMD_OBJINP
from Core.I_01__InpData import InputData

from Core.O_02__Protein import Kinase, Phosphatase, LargeProtein, SmallProtein
from Core.O_03__Metabolite import LargeMolecule, SmallMolecule
from Core.O_80__Interaction import (Interaction, Phosphorylation,
                                    Dephosphorylation)

# ### MAIN ####################################################################
startTime = GF.startSimu()
# -----------------------------------------------------------------------------
print('='*80, '\n', '-'*33, 'M_0__Main.py', '-'*33, '\n')
print('Current working directory:', os.getcwd())
inDG = InputData(dictInpG)
inDG.addObjTps(NMD_OBJINP)
print('Added object types.')
# -----------------------------------------------------------------------------
cSystem = MF.iniSystem(inDG)
cSystem.printSystem()

# -----------------------------------------------------------------------------
MF.initialState(inDG)

# # -----------------------------------------------------------------------------
# print('-'*80)
# LargeProteinNRT2p1 = LargeProtein(inDG, 201)
# print('*'*20, 'LargeProtein_NRT2p1:', '*'*20)
# print(LargeProteinNRT2p1)
# LargeProteinNRT2p1.printDType()
# # -----------------------------------------------------------------------------
# print('-'*80)
# SmallProteinNAR2p1 = SmallProtein(inDG, 301)
# print('*'*20, 'SmallProtein_NAR2p1:', '*'*20)
# print(SmallProteinNAR2p1)
# SmallProteinNAR2p1.printDType()
# # -----------------------------------------------------------------------------
# print('-'*80)
# MetaboliteNO3 = SmallMolecule(inDG, 501)
# print('*'*20, 'Metabolite_NO3_1m:', '*'*20)
# print(MetaboliteNO3)
# MetaboliteNO3.printDType()
# KinaseAT5G49770.printSpecSites()
# # -----------------------------------------------------------------------------
# print('-'*80)
# MetaboliteH2PO4 = SmallMolecule(inDG, 502)
# print('*'*20, 'Metabolite_H2PO4_1m:', '*'*20)
# print(MetaboliteH2PO4)
# MetaboliteH2PO4.printDType()
# # -----------------------------------------------------------------------------
# print('-'*80)
# lObjInteraction = [KinaseAT5G49770, LargeProteinNRT2p1, MetaboliteH2PO4]
# Interaction001 = Interaction(inDG, lObjInteraction)
# print('*'*20, 'Interaction001:', '*'*20)
# print(Interaction001)
# Interaction001.printObjInt()
# -----------------------------------------------------------------------------
# print('-'*80)
# lObjInteraction, sSpecSite = [KinaseAT5G49770, Phosphatase1], 'S839'
# Phosphorylation001 = Phosphorylation(inDG, lObjInteraction, sSpecSite)
# print('*'*20, 'Phosphorylation001:', '*'*20)
# print(Phosphorylation001)
# Phosphorylation001.printObjInt()
# idInterSucc = Phosphorylation001.doPyl()
# print('Interaction', Phosphorylation001.idO, '/' , Phosphorylation001.descO,
#       'at site', sSpecSite, 'was a success:', idInterSucc)
# # -----------------------------------------------------------------------------
# lObjInteraction, sSpecSite = [KinaseAT5G49770, Phosphatase2],  'S870'
# Phosphorylation002 = Phosphorylation(inDG, lObjInteraction, sSpecSite)
# print('*'*20, 'Phosphorylation002:', '*'*20)
# print(Phosphorylation002)
# Phosphorylation002.printObjInt()
# idInterSucc = Phosphorylation002.doPyl()
# print('Interaction', Phosphorylation002.idO, '/' , Phosphorylation002.descO,
#       'at site', sSpecSite, 'was a success:', idInterSucc)

# # -----------------------------------------------------------------------------
# print('-'*80)
# print('*'*20, 'Kinase_AT5G49770:', '*'*20)
# print(KinaseAT5G49770)
# KinaseAT5G49770.printDType()
# KinaseAT5G49770.printSpecSites()
# # -----------------------------------------------------------------------------
# print('-'*80)
# lObjInteraction, sSpecSite = [KinaseAT5G49770, Phosphatase2], 'S870'
# Dephosphorylation001 = Dephosphorylation(inDG, lObjInteraction, sSpecSite)
# print('*'*20, 'Dephosphorylation001:', '*'*20)
# print(Dephosphorylation001)
# Dephosphorylation001.printObjInt()
# idInterSucc = Dephosphorylation001.doDePyl()
# print('Interaction', Dephosphorylation001.idO, '/' ,
#       Dephosphorylation001.descO, 'at site', sSpecSite, 'was a success:',
#       idInterSucc)
# # -----------------------------------------------------------------------------
# print('-'*80)
# print('*'*20, 'Kinase_AT5G49770:', '*'*20)
# print(KinaseAT5G49770)
# KinaseAT5G49770.printDType()
# KinaseAT5G49770.printSpecSites()
# # -----------------------------------------------------------------------------
print('-'*80)
GF.endSimu(startTime)

###############################################################################
