# -*- coding: utf-8 -*-
###############################################################################
# --- F_04__MainFunctions.py --------------------------------------------------
###############################################################################
import Core.F_00__GenFunctions as GF

from Core.O_01__Molecule import Molecule
from Core.O_02__Protein import (Protein, Enzyme, Kinase, Phosphatase,
                                LargeProtein, SmallProtein)
from Core.O_03__Metabolite import Metabolite, LargeMolecule, SmallMolecule
from Core.O_80__Interaction import (Interaction, Phosphorylation,
                                    Dephosphorylation)
from Core.O_90__System import System

# --- Functions (initialisation) ----------------------------------------------
def iniSystem(inpDG):
    # KinaseAT5G49770 ---------------------------------------------------------
    KinaseAT5G49770 = Kinase(inpDG, 101)
    # Phosphatases 1 - 4 ------------------------------------------------------
    Phosphatase1 = Phosphatase(inpDG, 151)
    Phosphatase2 = Phosphatase(inpDG, 152)
    Phosphatase3 = Phosphatase(inpDG, 153)
    Phosphatase4 = Phosphatase(inpDG, 154)
    # Large protein NRT2.1 ----------------------------------------------------
    NRT2p1 = LargeProtein(inpDG, 201)
    # Small protein NAR2.1 ----------------------------------------------------
    NAR2p1 = SmallProtein(inpDG, 301)
    # Interactions: phosphorylation and dephosphorylation ---------------------
    Pyl01 = Phosphorylation(inpDG, 80, [KinaseAT5G49770, Phosphatase1], 'S839')
    Pyl02 = Phosphorylation(inpDG, 80, [KinaseAT5G49770, Phosphatase2], 'S870')
    Pyl03 = Phosphorylation(inpDG, 80, [NRT2p1, Phosphatase3], 'S21')
    Pyl04 = Phosphorylation(inpDG, 80, [NRT2p1, Phosphatase4], 'S28')
    DePyl01 = Dephosphorylation(inpDG, 80, [KinaseAT5G49770, Phosphatase1],
                                'S839')
    DePyl02 = Dephosphorylation(inpDG, 80, [KinaseAT5G49770, Phosphatase2],
                                'S870')
    DePyl03 = Dephosphorylation(inpDG, 80, [NRT2p1, Phosphatase3], 'S21')
    DePyl04 = Dephosphorylation(inpDG, 80, [NRT2p1, Phosphatase4], 'S28')
    # List of system components -----------------------------------------------
    lSysCmp = [KinaseAT5G49770, Phosphatase1, Phosphatase2, Phosphatase3,
               Phosphatase4, NRT2p1, NAR2p1, Pyl01, Pyl02, Pyl03, Pyl04,
               DePyl01, DePyl02, DePyl03, DePyl04]
    return System(inpDG, 90, lSysCmp)
    

###############################################################################
