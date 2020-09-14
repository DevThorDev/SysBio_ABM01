# -*- coding: utf-8 -*-
###############################################################################
# --- M_0__Main.py ------------------------------------------------------------
###############################################################################
import os

import Core.F_00__GenFunctions as GF

from Control.A_00__GenInput import dictInpG
from Core.C_00__GenConstants import NMD_OBJINP
from Core.I_01__InpData import InputData

from Core.O_01__Protein import Kinase, Phosphatase, LargeProtein, SmallProtein
from Core.O_02__Metabolite import LargeMolecule, SmallMolecule
from Core.O_80__Interaction import Interaction

# ### MAIN ####################################################################
startTime = GF.startSimu()
# -----------------------------------------------------------------------------
print('='*80, '\n', '-'*33, 'M_0__Main.py', '-'*33, '\n')
print('Current working directory:', os.getcwd())
inDG = InputData(dictInpG)
inDG.addObjTps(NMD_OBJINP)
print('Added object types.')
# -----------------------------------------------------------------------------
print('-'*80)
print('*'*20, 'Input data:', '*'*20)
print(inDG)
# -----------------------------------------------------------------------------
print('-'*80)
KinaseAT5G49770 = Kinase(inDG, 101)
print('*'*20, 'Kinase_AT5G49770:', '*'*20)
print(KinaseAT5G49770)
KinaseAT5G49770.printDType()
KinaseAT5G49770.printLSpecSites()
# -----------------------------------------------------------------------------
print('-'*80)
LargeProteinNRT2p1 = LargeProtein(inDG, 201)
print('*'*20, 'LargeProtein_NRT2p1:', '*'*20)
print(LargeProteinNRT2p1)
LargeProteinNRT2p1.printDType()
# -----------------------------------------------------------------------------
print('-'*80)
SmallProteinNAR2p1 = SmallProtein(inDG, 301)
print('*'*20, 'SmallProtein_NAR2p1:', '*'*20)
print(SmallProteinNAR2p1)
SmallProteinNAR2p1.printDType()
# -----------------------------------------------------------------------------
print('-'*80)
MetaboliteNO3 = SmallMolecule(inDG, 501)
print('*'*20, 'Metabolite_NO3_1m:', '*'*20)
print(MetaboliteNO3)
MetaboliteNO3.printDType()
KinaseAT5G49770.printLSpecSites()
# -----------------------------------------------------------------------------
print('-'*80)
MetaboliteH2PO4 = SmallMolecule(inDG, 502)
print('*'*20, 'Metabolite_H2PO4_1m:', '*'*20)
print(MetaboliteH2PO4)
MetaboliteH2PO4.printDType()
# -----------------------------------------------------------------------------
print('-'*80)
lObjInteraction = [KinaseAT5G49770, LargeProteinNRT2p1, MetaboliteH2PO4]
Interaction001 = Interaction(inDG, lObjInteraction)
print('*'*20, 'Interaction001:', '*'*20)
print(Interaction001)
Interaction001.printObjInt()
# -----------------------------------------------------------------------------
print('-'*80)
GF.endSimu(startTime)

###############################################################################
