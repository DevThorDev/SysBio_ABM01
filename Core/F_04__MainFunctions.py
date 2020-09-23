# -*- coding: utf-8 -*-
###############################################################################
# --- F_04__MainFunctions.py --------------------------------------------------
###############################################################################
import Core.C_00__GenConstants as GC
# import Core.F_00__GenFunctions as GF

# from Core.O_01__Molecule import Molecule
from Core.O_02__Protein import (Kinase_AT5G49770, Kinase_X, Phosphatase1,
                                Phosphatase2, Phosphatase3, Phosphatase4,
                                Protein_NRT2p1, Protein_NAR2p1)
from Core.O_03__Metabolite import Metabolite, LargeMolecule, SmallMolecule
from Core.O_80__Interaction import (Interaction, Phosphorylation,
                                    Dephosphorylation)
from Core.O_90__State import (Sta_Int_AT5G49770_NRT2p1,
                              Sta_Trans_AT5G49770_NRT2p1,
                              Sta_Int_NAR2p1_NRT2p1,
                              Sta_Trans_NAR2p1_NRT2p1)
from Core.O_99__System import System

# --- Functions (initialisation) ----------------------------------------------
def iniSystem(inpDG):
    # KAsAT5G49770 ---------------------------------------------------------
    KAsAT5G49770 = Kinase_AT5G49770(inpDG)
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
    Pyl01 = Phosphorylation(inpDG, KAsAT5G49770, PAs1, 'S839')
    Pyl02 = Phosphorylation(inpDG, KAsAT5G49770, PAs2, 'S870')
    Pyl03 = Phosphorylation(inpDG, NRT2p1, PAs3, 'S21')
    Pyl04 = Phosphorylation(inpDG, NRT2p1, PAs4, 'S28')
    DePyl01 = Dephosphorylation(inpDG, KAsAT5G49770, PAs1, 'S839')
    DePyl02 = Dephosphorylation(inpDG, KAsAT5G49770, PAs2, 'S870')
    DePyl03 = Dephosphorylation(inpDG, NRT2p1, PAs3, 'S21')
    DePyl04 = Dephosphorylation(inpDG, NRT2p1, PAs4, 'S28')
    # List of system components -----------------------------------------------
    lSysCmp = [KAsAT5G49770, PAs1, PAs2, PAs3, PAs4, NRT2p1, NAR2p1, Pyl01,
               Pyl02, Pyl03, Pyl04, DePyl01, DePyl02, DePyl03, DePyl04]
    return System(inpDG, lOSys = lSysCmp)

def initialState(inpDG):
    # Kinases AT5G49770 and X -------------------------------------------------
    KAsAT5G49770 = Kinase_AT5G49770(inpDG)
    KAsX = Kinase_X(inpDG)
    # Phosphatases 1 - 4 ------------------------------------------------------
    PAs1 = Phosphatase1(inpDG)
    PAs2 = Phosphatase2(inpDG)
    PAs3 = Phosphatase3(inpDG)
    PAs4 = Phosphatase4(inpDG)
    # Large protein NRT2.1 ----------------------------------------------------
    NRT2p1 = Protein_NRT2p1(inpDG)
    # Small protein NAR2.1 ----------------------------------------------------
    NAR2p1 = Protein_NAR2p1(inpDG)
    # Create initial state ----------------------------------------------------
    if inpDG.dI['sStIni'] == GC.S_ST_INT_AT5G49770_NRT2P1:
        cSta = Sta_Int_AT5G49770_NRT2p1(inpDG, cLPr = NRT2p1, cSPr = NAR2p1,
                                          lKAs = [KAsAT5G49770],
                                          lPAs = [PAs1, PAs2, PAs3, PAs4])
    elif inpDG.dI['sStIni'] == GC.S_ST_TRANS_AT5G49770_NRT2P1:
        cSta = Sta_Trans_AT5G49770_NRT2p1(inpDG, cLPr = NRT2p1, cSPr = NAR2p1,
                                          lKAs = [KAsAT5G49770, KAsX],
                                          lPAs = [PAs1, PAs2, PAs3, PAs4])
    elif inpDG.dI['sStIni'] == GC.S_ST_INT_NAR2P1_NRT2P1:
        cSta = Sta_Int_NAR2p1_NRT2p1(inpDG, cLPr = NRT2p1, cSPr = NAR2p1,
                                     lKAs = [KAsAT5G49770],
                                     lPAs = [PAs1, PAs2, PAs3, PAs4])
    elif inpDG.dI['sStIni'] == GC.S_ST_TRANS_NAR2P1_NRT2P1:
        cSta = Sta_Trans_NAR2p1_NRT2p1(inpDG,  cLPr = NRT2p1, cSPr = NAR2p1,
                                       lKAs = [KAsAT5G49770],
                                       lPAs = [PAs1, PAs2, PAs3, PAs4])
    # Create system from state ------------------------------------------------
    cSys = cSta.createSystem(inpDG)
    cSys.printSystem()
    for cO in cSys.lKAs + cSys.lPAs + cSys.lLPr + cSys.lSPr:
        cO.printSpecSites()

###############################################################################
