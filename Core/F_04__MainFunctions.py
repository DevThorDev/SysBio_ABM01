# -*- coding: utf-8 -*-
###############################################################################
# --- F_04__MainFunctions.py --------------------------------------------------
###############################################################################
import Core.C_00__GenConstants as GC

from Core.O_02__Protein import (KinaseHPCAL1, KinaseX, KinaseY, Phosphatase1,
                                Phosphatase2, Phosphatase3, Phosphatase4,
                                Protein_NRT2p1, Protein_NAR2p1)
from Core.O_03__Metabolite import SMo_NO3_1m, SMo_H2PO4_1m
# from Core.O_80__Interaction import Phosphorylation, Dephosphorylation
from Core.O_90__Component import Component
# from Core.O_99__System import System

# --- Functions (initialisation) ----------------------------------------------
# def iniSystem(inpDG):
#     # Kinases KAsHPCAL1, KAsX, KAsY -------------------------------------------
#     KAsHPCAL1 = KinaseHPCAL1(inpDG)
#     KAsX = KinaseX(inpDG)
#     KAsY = KinaseY(inpDG)
#     # Phosphatases 1 - 4 ------------------------------------------------------
#     PAs1 = Phosphatase1(inpDG)
#     PAs2 = Phosphatase2(inpDG)
#     PAs3 = Phosphatase3(inpDG)
#     PAs4 = Phosphatase4(inpDG)
#     # Large protein NRT2.1 ----------------------------------------------------
#     NRT2p1 = Protein_NRT2p1(inpDG)
#     # Small protein NAR2.1 ----------------------------------------------------
#     NAR2p1 = Protein_NAR2p1(inpDG)
#     # Small molecules NO3- and H2PO4- -----------------------------------------
#     NO3_1m = SMo_NO3_1m(inpDG)
#     H2PO4_1m = SMo_H2PO4_1m(inpDG)
#     # Interactions: phosphorylation and dephosphorylation ---------------------
#     Pyl01 = Phosphorylation(inpDG, KAsHPCAL1, PAs1, 'S839')
#     Pyl02 = Phosphorylation(inpDG, KAsHPCAL1, PAs2, 'S870')
#     Pyl03 = Phosphorylation(inpDG, NRT2p1, PAs3, 'S21')
#     Pyl04 = Phosphorylation(inpDG, NRT2p1, PAs4, 'S28')
#     DePyl01 = Dephosphorylation(inpDG, KAsHPCAL1, PAs1, 'S839')
#     DePyl02 = Dephosphorylation(inpDG, KAsHPCAL1, PAs2, 'S870')
#     DePyl03 = Dephosphorylation(inpDG, NRT2p1, PAs3, 'S21')
#     DePyl04 = Dephosphorylation(inpDG, NRT2p1, PAs4, 'S28')
#     # List of system components -----------------------------------------------
#     lSysCmp = [KAsHPCAL1, KAsX, KAsY, PAs1, PAs2, PAs3, PAs4,
#                NRT2p1, NAR2p1, NO3_1m, H2PO4_1m, Pyl01, Pyl02, Pyl03, Pyl04,
#                DePyl01, DePyl02, DePyl03, DePyl04]
#     return System(inpDG, lOSys = lSysCmp)

def iniComponent(inpDG, ddVOvwr = {}, iV = 0):
    # Kinases KAsHPCAL1, KAsX, KAsY -------------------------------------------
    KAsHPCAL1 = KinaseHPCAL1(inpDG)
    KAsX = KinaseX(inpDG)
    KAsY = KinaseY(inpDG)
    # Phosphatases PAs1, PAs2, PAs3, PAs4  ------------------------------------
    PAs1 = Phosphatase1(inpDG)
    PAs2 = Phosphatase2(inpDG)
    PAs3 = Phosphatase3(inpDG)
    PAs4 = Phosphatase4(inpDG)
    # Large protein NRT2.1 ----------------------------------------------------
    NRT2p1 = Protein_NRT2p1(inpDG)
    # Small protein NAR2.1 ----------------------------------------------------
    NAR2p1 = Protein_NAR2p1(inpDG)
    # Small molecules NO3- and H2PO4- -----------------------------------------
    NO3_1m = SMo_NO3_1m(inpDG)
    H2PO4_1m = SMo_H2PO4_1m(inpDG)
    # overwrite type dict. input of small molecules with values of ddVOvwr ----
    NO3_1m.overwInpV(ddVOvwr, iV)
    H2PO4_1m.overwInpV(ddVOvwr, iV)
    # Create initial state ----------------------------------------------------
    dOCp = {GC.ID_KAS_HPCAL1: KAsHPCAL1,
            GC.ID_KAS_X: KAsX,
            GC.ID_KAS_Y: KAsY,
            GC.ID_PAS_1: PAs1,
            GC.ID_PAS_2: PAs2,
            GC.ID_PAS_3: PAs3,
            GC.ID_PAS_4: PAs4,
            GC.ID_LPR_NRT2P1: NRT2p1,
            GC.ID_SPR_NAR2P1: NAR2p1,
            'lSMo': [NO3_1m, H2PO4_1m]}
    cCp = Component(inpDG, dOComp = dOCp)
    # Create system from state ------------------------------------------------
    # return cCp, cCp.createSystem(inpDG)
    # Return the current state ------------------------------------------------
    return cCp

def changeComponentCncDep(inpDG, cCp):
    if cCp.dCnc[GC.ID_NO3_1M][0] > cCp.dCnc[GC.ID_NO3_1M][2]:
        if cCp.idO == GC.S_CP_LSI_LONG:
            cCp.to_Cp_LST(inpDG)
            cCp.to_Cp_LKI(inpDG)
        elif cCp.idO == GC.S_CP_LST_LONG:
            cCp.to_Cp_LKI(inpDG)
    elif cCp.dCnc[GC.ID_NO3_1M][0] < cCp.dCnc[GC.ID_NO3_1M][1]:
        if cCp.idO == GC.S_CP_LKI_LONG:
            cCp.to_Cp_LKT(inpDG)
            cCp.to_Cp_LSI(inpDG)
        elif cCp.idO == GC.S_CP_LKT_LONG:
            cCp.to_Cp_LSI(inpDG)

def evolveIni(inpDG, nCpO = 1, ddVOvwr = {}):
    lCpO = []
    for iCpO in range(nCpO):
        # cCpO, cSys = iniComponent(inpDG, ddVOvwr, iCpO)
        cCpO = iniComponent(inpDG, ddVOvwr, iCpO)
        lCpO.append(cCpO)
    print('--- Initialisation done.')
    return lCpO

def evolveTS(inpDG, lCpO, curTS, nCpO = 1, ddVOvwr = {}):
    print('--- Current time step:', curTS)
    for iCpO in range(nCpO):
        print('- Component', iCpO + 1)
        lCpO[iCpO].changeCncSMo(curTS)
        lCpO[iCpO].printDCnc(prID = GC.ID_NO3_1M)
        changeComponentCncDep(inpDG, lCpO[iCpO])

def evolve_TimeSteps(inpDG, nObj = 1, ddVOvwr = {}):
    lCpO = evolveIni(inpDG, nObj, ddVOvwr)
    for curTS in range(1, inpDG.dI['maxTS'] + 1):
        evolveTS(inpDG, lCpO, curTS, nObj, ddVOvwr)
    for k, cCpO in enumerate(lCpO):
        print('++++++++ Component ' + str(k + 1) + ':')
        cCpO.printComponentDetails()
        print(cCpO.dfrEvo)
        cCpO.savePlotDfrEvo(kCp = k + 1, llIPlot = [[0, 1], [0, 2]], iSMo = 0)
        cCpO.savePlotDfrEvo(kCp = k + 1, llIPlot = [[0, 1], [0, 2]], iSMo = 1)

###############################################################################
