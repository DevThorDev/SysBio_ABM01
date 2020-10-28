# -*- coding: utf-8 -*-
###############################################################################
# --- F_04__MainFunctions.py --------------------------------------------------
###############################################################################
import Core.C_00__GenConstants as GC

from Core.O_02__Protein import (Kinase_HPCAL1, Kinase_X, Kinase0,
                                Phosphatase0, Protein_NRT2p1, Protein_NAR2p1)
from Core.O_03__Metabolite import SMo_NO3_1m, SMo_H2PO4_1m
# from Core.O_80__Interaction import Phosphorylation, Dephosphorylation
from Core.O_90__Component import Component
# from Core.O_99__System import System

# --- Functions (initialisation) ----------------------------------------------
# def iniSystem(inpDG):
#     # Kinases KAsHPCAL1, KAsX, KAs1, KAs2, KAs3 -------------------------------
#     KAsHPCAL1 = Kinase_HPCAL1(inpDG)
#     KAsX = Kinase_X(inpDG)
#     KAs1 = Kinase0(inpDG, cID = GC.ID_KAS_1)
#     KAs2 = Kinase0(inpDG, cID = GC.ID_KAS_2)
#     KAs3 = Kinase0(inpDG, cID = GC.ID_KAS_3)
#     # Phosphatases 1 - 4 ------------------------------------------------------
#     PAs1 = Phosphatase0(inpDG, cID = GC.ID_PAS_1)
#     PAs2 = Phosphatase0(inpDG, cID = GC.ID_PAS_2)
#     PAs3 = Phosphatase0(inpDG, cID = GC.ID_PAS_3)
#     PAs4 = Phosphatase0(inpDG, cID = GC.ID_PAS_4)
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
#     lSysCmp = [KAsHPCAL1, KAsX, KAs1, KAs2, KAs3, PAs1, PAs2, PAs3, PAs4,
#                NRT2p1, NAR2p1, NO3_1m, H2PO4_1m, Pyl01, Pyl02, Pyl03, Pyl04,
#                DePyl01, DePyl02, DePyl03, DePyl04]
#     return System(inpDG, lOSys = lSysCmp)

def initialState(inpDG, ddVOvwr = {}, iV = 0):
    # Kinases KAsHPCAL1, KAsX -------------------------------------------------
    KAsHPCAL1 = Kinase_HPCAL1(inpDG)
    KAsX = Kinase_X(inpDG)
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
    dOSta = {GC.SPC_KAS_A: KAsHPCAL1,
             GC.SPC_KAS_X: KAsX,
             GC.SPC_LPR_A: NRT2p1,
             GC.SPC_SPR_A: NAR2p1,
             GC.SPC_L_SMO: [NO3_1m, H2PO4_1m]}
    cSta = Component(inpDG, dOState = dOSta)
    # Create system from state ------------------------------------------------
    # return cSta, cSta.createSystem(inpDG)
    # Return the current state ------------------------------------------------
    return cSta

def changeStateConcDep(inpDG, cSta):
    if cSta.dCnc[GC.ID_NO3_1M][0] < cSta.dCnc[GC.ID_NO3_1M][1]:
        if cSta.idO == GC.S_ST_A_KIN_INT:
            cSta.to_St_B_Trans_HPCAL1_NRT2p1(inpDG)
            cSta.to_St_C_Int_NAR2p1_NRT2p1(inpDG)
        elif cSta.idO == GC.S_ST_B_KIN_TRA:
            cSta.to_St_C_Int_NAR2p1_NRT2p1(inpDG)
    elif cSta.dCnc[GC.ID_NO3_1M][0] > cSta.dCnc[GC.ID_NO3_1M][2]:
        if cSta.idO == GC.S_ST_C_SPR_INT:
            cSta.to_St_D_Trans_NAR2p1_NRT2p1(inpDG)
            cSta.to_St_A_Int_HPCAL1_NRT2p1(inpDG)
        elif cSta.idO == GC.S_ST_D_SPR_TRA:
            cSta.to_St_A_Int_HPCAL1_NRT2p1(inpDG)

def evolveIni(inpDG, nStO = 1, ddVOvwr = {}):
    lStO = []
    for iStO in range(nStO):
        # cStO, cSys = initialState(inpDG, ddVOvwr, iStO)
        cStO = initialState(inpDG, ddVOvwr, iStO)
        lStO.append(cStO)
    print('--- Initialisation done.')
    return lStO

def evolveTS(inpDG, lStO, curTS, nStO = 1, ddVOvwr = {}):
    print('--- Current time step:', curTS)
    for iStO in range(nStO):
        print('- State', iStO + 1)
        lStO[iStO].changeConcSMo(curTS)
        lStO[iStO].printDCnc(prID = GC.ID_NO3_1M)
        changeStateConcDep(inpDG, lStO[iStO])

def evolve_TimeSteps(inpDG, nObj = 1, ddVOvwr = {}):
    lStO = evolveIni(inpDG, nObj, ddVOvwr)
    for curTS in range(1, inpDG.dI['maxTS'] + 1):
        evolveTS(inpDG, lStO, curTS, nObj, ddVOvwr)
    for k, cStO in enumerate(lStO):
        print('++++++++ State ' + str(k + 1) + ':')
        cStO.printStateDetails()
        print(cStO.dfrEvo)
        cStO.savePlotDfrEvo(kSt = k + 1, llIPlot = [[0, 1], [0, 2]], iSMo = 0)
        cStO.savePlotDfrEvo(kSt = k + 1, llIPlot = [[0, 1], [0, 2]], iSMo = 1)

###############################################################################
