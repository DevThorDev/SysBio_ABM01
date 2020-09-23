# -*- coding: utf-8 -*-
###############################################################################
# --- F_04__MainFunctions.py --------------------------------------------------
###############################################################################
# import Core.C_00__GenConstants as GC
# import Core.F_00__GenFunctions as GF

# from Core.O_01__Molecule import Molecule
from Core.O_02__Protein import (Kinase_AT5G49770, Phosphatase1, Phosphatase2,
                                Phosphatase3, Phosphatase4, Protein_NRT2p1,
                                Protein_NAR2p1)
from Core.O_03__Metabolite import Metabolite, LargeMolecule, SmallMolecule
from Core.O_80__Interaction import (Interaction, Phosphorylation,
                                    Dephosphorylation)
from Core.O_90__State import State_Int_AT5G49770_NRT2p1
from Core.O_99__System import System

# --- Functions (initialisation) ----------------------------------------------
def iniSystem(inpDG):
    # KAs_AT5G49770 ---------------------------------------------------------
    KAs_AT5G49770 = Kinase_AT5G49770(inpDG)
    # Phosphatases 1 - 4 ------------------------------------------------------
    PAs1 = Phosphatase1(inpDG)
    PAs2 = Phosphatase2(inpDG)
    PAs3 = Phosphatase3(inpDG)
    PAs4 = Phosphatase4(inpDG)
    # Large protein NRT2.1 ----------------------------------------------------
    NRT2p1 = Protein_NRT2p1(inpDG)
    # Small protein NAR2.1 ----------------------------------------------------
    NAR2p1 = Protein_NAR2p1(inpDG)
    # Interactions: phosphorylation and dephosphorylation ---------------------
    Pyl01 = Phosphorylation(inpDG, KAs_AT5G49770, PAs1, 'S839')
    Pyl02 = Phosphorylation(inpDG, KAs_AT5G49770, PAs2, 'S870')
    Pyl03 = Phosphorylation(inpDG, NRT2p1, PAs3, 'S21')
    Pyl04 = Phosphorylation(inpDG, NRT2p1, PAs4, 'S28')
    DePyl01 = Dephosphorylation(inpDG, KAs_AT5G49770, PAs1, 'S839')
    DePyl02 = Dephosphorylation(inpDG, KAs_AT5G49770, PAs2, 'S870')
    DePyl03 = Dephosphorylation(inpDG, NRT2p1, PAs3, 'S21')
    DePyl04 = Dephosphorylation(inpDG, NRT2p1, PAs4, 'S28')
    # List of system components -----------------------------------------------
    lSysCmp = [KAs_AT5G49770, PAs1, PAs2, PAs3, PAs4, NRT2p1, NAR2p1, Pyl01,
               Pyl02, Pyl03, Pyl04, DePyl01, DePyl02, DePyl03, DePyl04]
    return System(inpDG, lOSys = lSysCmp)

def initialState(inpDG):
    # KAs_AT5G49770 ---------------------------------------------------------
    KAs_AT5G49770 = Kinase_AT5G49770(inpDG)
    # Phosphatases 1 - 4 ------------------------------------------------------
    PAs1 = Phosphatase1(inpDG)
    PAs2 = Phosphatase2(inpDG)
    PAs3 = Phosphatase3(inpDG)
    PAs4 = Phosphatase4(inpDG)
    # Large protein NRT2.1 ----------------------------------------------------
    NRT2p1 = Protein_NRT2p1(inpDG)
    # Small protein NAR2.1 ----------------------------------------------------
    NAR2p1 = Protein_NAR2p1(inpDG)
    cState = State_Int_AT5G49770_NRT2p1(inpDG, cKAs = KAs_AT5G49770,
                                        cLPr = NRT2p1, cSPr = NAR2p1,
                                        lPAs = [PAs1, PAs2, PAs3, PAs4])
    cSys = cState.createSystem(inpDG)
    cSys.printSystem()
    for cO in cSys.lKAs + cSys.lLPr + cSys.lSPr:
        cO.printSpecSites()

###############################################################################
