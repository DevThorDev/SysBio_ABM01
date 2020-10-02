# -*- coding: utf-8 -*-
###############################################################################
# --- F_04__MainFunctions.py --------------------------------------------------
###############################################################################
import Core.C_00__GenConstants as GC

from Core.O_02__Protein import (Kinase_AT5G49770, Kinase_X, Kinase0,
                                Phosphatase0, Protein_NRT2p1, Protein_NAR2p1)
from Core.O_03__Metabolite import SMo_NO3_1m, SMo_H2PO4_1m
from Core.O_80__Interaction import Phosphorylation, Dephosphorylation
from Core.O_90__State import State_Int_Trans
from Core.O_99__System import System

# --- Functions (initialisation) ----------------------------------------------
def iniSystem(inpDG):
    # Kinases KAsAT5G49770, KAsX, KAs1, KAs2, KAs3 ----------------------------
    KAsAT5G49770 = Kinase_AT5G49770(inpDG)
    KAsX = Kinase_X(inpDG)
    KAs1 = Kinase0(inpDG, cID = GC.ID_KAS_1)
    KAs2 = Kinase0(inpDG, cID = GC.ID_KAS_2)
    KAs3 = Kinase0(inpDG, cID = GC.ID_KAS_3)
    # Phosphatases 1 - 4 ------------------------------------------------------
    PAs1 = Phosphatase0(inpDG, cID = GC.ID_PAS_1)
    PAs2 = Phosphatase0(inpDG, cID = GC.ID_PAS_2)
    PAs3 = Phosphatase0(inpDG, cID = GC.ID_PAS_3)
    PAs4 = Phosphatase0(inpDG, cID = GC.ID_PAS_4)
    # Large protein NRT2.1 ----------------------------------------------------
    NRT2p1 = Protein_NRT2p1(inpDG)
    # Small protein NAR2.1 ----------------------------------------------------
    NAR2p1 = Protein_NAR2p1(inpDG)
    # Small molecules NO3- and H2PO4- -----------------------------------------
    NO3_1m = SMo_NO3_1m(inpDG)
    H2PO4_1m = SMo_H2PO4_1m(inpDG)
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
    lSysCmp = [KAsAT5G49770, KAsX, KAs1, KAs2, KAs3, PAs1, PAs2, PAs3, PAs4,
               NRT2p1, NAR2p1, NO3_1m, H2PO4_1m, Pyl01, Pyl02, Pyl03, Pyl04,
               DePyl01, DePyl02, DePyl03, DePyl04]
    return System(inpDG, lOSys = lSysCmp)

def initialState(inpDG, ddVOvwr = {}, iV = 0):
    # Kinases KAsAT5G49770, KAsX ----------------------------------------------
    KAsAT5G49770 = Kinase_AT5G49770(inpDG)
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
    dOSta = {GC.SPC_KAS_A: KAsAT5G49770,
             GC.SPC_KAS_X: KAsX,
             GC.SPC_LPR_A: NRT2p1,
             GC.SPC_SPR_A: NAR2p1,
             GC.SPC_L_SMO: [NO3_1m, H2PO4_1m]}
    cSta = State_Int_Trans(inpDG, dOState = dOSta)
    # Create system from state ------------------------------------------------
    return cSta, cSta.createSystem(inpDG)

def changeStateConcDep(inpDG, cSta):
    if cSta.dCnc[GC.ID_NO3_1M][0] < cSta.dCnc[GC.ID_NO3_1M][1]:
        if cSta.idO == GC.S_ST_A_INT_AT5G49770_NRT2P1:
            cSta.to_St_B_Trans_AT5G49770_NRT2p1(inpDG)
            cSta.to_St_C_Int_NAR2p1_NRT2p1(inpDG)
        elif cSta.idO == GC.S_ST_B_TRANS_AT5G49770_NRT2P1:
            cSta.to_St_C_Int_NAR2p1_NRT2p1(inpDG)
    elif cSta.dCnc[GC.ID_NO3_1M][0] > cSta.dCnc[GC.ID_NO3_1M][2]:
        if cSta.idO == GC.S_ST_C_INT_NAR2P1_NRT2P1:
            cSta.to_St_D_Trans_NAR2p1_NRT2p1(inpDG)
            cSta.to_St_A_Int_AT5G49770_NRT2p1(inpDG)
        elif cSta.idO == GC.S_ST_D_TRANS_NAR2P1_NRT2P1:
            cSta.to_St_A_Int_AT5G49770_NRT2p1(inpDG)

def evolveIni(inpDG, nSt = 1, ddVOvwr = {}):
    lSt = []
    for iSt in range(nSt):
        cSt, cSys = initialState(inpDG, ddVOvwr, iSt)
        lSt.append(cSt)
    print('--- Initialisation done.')
    return lSt

def evolveTS(inpDG, lSt, curTS, nSt = 1, ddVOvwr = {}):
    print('--- Current time step:', curTS)
    for iSt in range(nSt):
        print('- State', iSt + 1)
        lSt[iSt].changeConcSMo(curTS)
        lSt[iSt].printDCnc(prID = GC.ID_NO3_1M)
        changeStateConcDep(inpDG, lSt[iSt])

def evolveOverTime(inpDG, nSta = 1, ddVOvwr = {}):
    for curTS in range(inpDG.dI['maxTS'] + 1):
        if curTS == 0:
            lSta = evolveIni(inpDG, nSta, ddVOvwr)
        else:
            evolveTS(inpDG, lSta, curTS, nSta, ddVOvwr)
    for k, cSta in enumerate(lSta):
        print('++++++++ State ' + str(k + 1) + ':')
        cSta.printStateDetails()
        print(cSta.dfrEvo)
        cSta.savePlotDfrEvo(kSt = k + 1, llIPlot = [[0, 1], [0, 2]], iSMo = 0)
        cSta.savePlotDfrEvo(kSt = k + 1, llIPlot = [[0, 1], [0, 2]], iSMo = 1)

###############################################################################
