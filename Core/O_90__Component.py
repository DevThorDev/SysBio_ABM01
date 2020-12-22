# -*- coding: utf-8 -*-
###############################################################################
# --- O_90__Component.py ------------------------------------------------------
###############################################################################
import Core.C_00__GenConstants as GC
import Core.F_00__GenFunctions as GF
import Core.F_01__SpcFunctions as SF

from Core.O_00__Base import Base
from Core.O_02__Protein import (KinaseHPCAL1, KinaseX, KinaseY, Phosphatase1,
                                Phosphatase2, Phosphatase3, Phosphatase4,
                                Protein_NRT2p1, Protein_NAR2p1)
from Core.O_80__Interaction import Phosphorylation, Dephosphorylation

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class ComponentBase(Base):
    def __init__(self, inpDat, dOComp, llOInt = [], lOOth = [], iTp = 90):
        super().__init__(inpDat, iTp = iTp)
        for cLOInt in llOInt:
            assert len(cLOInt) >= 2
        self.idO = GC.ID_CPB
        self.descO = 'ComponentBase'
        if not hasattr(self, 'sCp'):
            self.sCp = GC.S_USC*7
        if not hasattr(self, 'dOCp'):
            self.dOCp = dOComp
        self.llOI = llOInt
        self.lOO = lOOth
        self.lOSy = list(set(GF.lItToUniqueList(self.llOI) + self.lOO))
        self.prTrans = 0
        # print('Initiated "ComponentBase" object.')

    def __str__(self):
        sIn = ('++++ Component ' + self.idO + ' (' + self.sCp + ' / ' +
               self.descO + '):')
        return sIn

    def printDetails(self):
        for k, lOI in enumerate(self.llOI):
            print('- Interacting pair ' + str(k + 1) + ': (' + lOI[0].idO +
                  ', ' + lOI[1].idO + ')')
        for k, cO in enumerate(self.lOO):
            s = '- Further component ' + str(k + 1) + ': ' + cO.idO
            if hasattr(cO, 'cCnc'):
                s += ' with conc. ' + str(round(cO.cCnc, GC.R04))
            print(s)
        print('-- Component details:')
        for cO in self.lOSy:
            cO.printMolSpecSites()

    def printComponentDetails(self):
        print(self)
        self.printDetails()

    def adaptPSites(self, inpDat, cO, sCp):
        for sSpS, dI in GC.DS_SPS[cO.idO].items():
            sPylDPy, idAs = SF.setPylDPy(dI, sCp)
            cAs = self.dOCp[dI[idAs]]
            if sPylDPy == GC.S_DO_PYL:
                _ = Phosphorylation(inpDat, cO, cAs, sSpS).doPyl()
                # if Phosphorylation(inpDat, cO, cAs, sSpS).doPyl():
                #     print('Phosphorylation at site', sSpS, 'happened!')
            elif sPylDPy == GC.S_DO_DPY:
                _ = Dephosphorylation(inpDat, cO, cAs, sSpS).doDePyl()
                # if Dephosphorylation(inpDat, cO, cAs, sSpS).doDePyl():
                #     print('Dephosphorylation at site', sSpS, 'happened!')

class Component(ComponentBase):
    def __init__(self, inpDat, inpFr, sComp, iTp = 90):
        self.inFr = inpFr
        assert len(self.inFr.lSCpTpL) >= 7
        self.sCp = sComp
        self.createDOComp(inpDat)
        if sComp in self.inFr.dSCpTpL[self.inFr.lSCpTpL[0]]:
            self.ini_Cp_L(inpDat, sComp, iTp = iTp)
        elif sComp in self.inFr.dSCpTpL[self.inFr.lSCpTpL[1]]:
            self.ini_Cp_S(inpDat, sComp, iTp = iTp)
        elif sComp in self.inFr.dSCpTpL[self.inFr.lSCpTpL[2]]:
            self.ini_Cp_K(inpDat, sComp, iTp = iTp)
        elif sComp in self.inFr.dSCpTpL[self.inFr.lSCpTpL[3]]:
            self.ini_Cp_LSI(inpDat, sComp, iTp = iTp)
        elif sComp in self.inFr.dSCpTpL[self.inFr.lSCpTpL[4]]:
            self.ini_Cp_LST(inpDat, sComp, iTp = iTp)
        elif sComp in self.inFr.dSCpTpL[self.inFr.lSCpTpL[5]]:
            self.ini_Cp_LKI(inpDat, sComp, iTp = iTp)
        elif sComp in self.inFr.dSCpTpL[self.inFr.lSCpTpL[6]]:
            self.ini_Cp_LKT(inpDat, sComp, iTp = iTp)
        else:
            self.idO = GC.ID_CPN
            self.descO = 'Component'
        # print('Initiated "Component" object ' + sComp + '.')

    def createDOComp(self, inpDat, iV = 0):
        # Large protein NRT2.1 ------------------------------------------------
        NRT2p1 = Protein_NRT2p1(inpDat)
        # Small protein NAR2.1 ------------------------------------------------
        NAR2p1 = Protein_NAR2p1(inpDat)
        # Kinases KAsHPCAL1, KAsX, KAsY ---------------------------------------
        KAsHPCAL1 = KinaseHPCAL1(inpDat)
        KAsX = KinaseX(inpDat)
        KAsY = KinaseY(inpDat)
        # Phosphatases PAs1, PAs2, PAs3, PAs4 ---------------------------------
        PAs1 = Phosphatase1(inpDat)
        PAs2 = Phosphatase2(inpDat)
        PAs3 = Phosphatase3(inpDat)
        PAs4 = Phosphatase4(inpDat)
        # Create initial component --------------------------------------------
        self.dOCp = {GC.ID_KAS_HPCAL1: KAsHPCAL1,
                     GC.ID_KAS_X: KAsX,
                     GC.ID_KAS_Y: KAsY,
                     GC.ID_PAS_1: PAs1,
                     GC.ID_PAS_2: PAs2,
                     GC.ID_PAS_3: PAs3,
                     GC.ID_PAS_4: PAs4,
                     GC.ID_LPR_NRT2P1: NRT2p1,
                     GC.ID_SPR_NAR2P1: NAR2p1}

    def ini_Cp_L(self, inpDat, sCp, iTp = 90):
        llOI = []
        lOO = [self.dOCp[GC.ID_LPR_NRT2P1], self.dOCp[GC.ID_KAS_X]]
        super().__init__(inpDat, self.dOCp, llOI, lOO, iTp = iTp)
        self.idO = self.inFr.lSCpTpL[0]
        self.descO = 'Component NRT2.1'
        self.adaptPSites(inpDat, self.dOCp[GC.ID_LPR_NRT2P1], sCp)

    def ini_Cp_S(self, inpDat, sCp, iTp = 90):
        llOI = []
        lOO = [self.dOCp[GC.ID_SPR_NAR2P1]]
        super().__init__(inpDat, self.dOCp, llOI, lOO, iTp = iTp)
        self.idO = self.inFr.lSCpTpL[1]
        self.descO = 'Component NAR2.1'

    def ini_Cp_K(self, inpDat, sCp, iTp = 90):
        llOI = []
        lOO = [self.dOCp[GC.ID_KAS_HPCAL1]]
        super().__init__(inpDat, self.dOCp, llOI, lOO, iTp = iTp)
        self.idO = self.inFr.lSCpTpL[2]
        self.descO = 'Component HPCAL1'
        self.adaptPSites(inpDat, self.dOCp[GC.ID_KAS_HPCAL1], sCp)

    def ini_Cp_LSI(self, inpDat, sCp, iTp = 90):
        llOI = [[self.dOCp[GC.ID_SPR_NAR2P1], self.dOCp[GC.ID_LPR_NRT2P1]]]
        lOO = [self.dOCp[GC.ID_KAS_X]]
        super().__init__(inpDat, self.dOCp, llOI, lOO, iTp = iTp)
        self.idO = self.inFr.lSCpTpL[3]
        self.descO = 'Component NRT2.1-NAR2.1 interaction'
        self.adaptPSites(inpDat, self.dOCp[GC.ID_LPR_NRT2P1], sCp)

    def ini_Cp_LST(self, inpDat, sCp, iTp = 90):
        llOI = [[self.dOCp[GC.ID_SPR_NAR2P1], self.dOCp[GC.ID_LPR_NRT2P1]]]
        lOO = [self.dOCp[GC.ID_KAS_X]]
        super().__init__(inpDat, self.dOCp, llOI, lOO, iTp = iTp)
        self.idO = self.inFr.lSCpTpL[4]
        self.descO = 'Component NRT2.1-NAR2.1 transition'
        self.adaptPSites(inpDat, self.dOCp[GC.ID_LPR_NRT2P1], sCp)

    def ini_Cp_LKI(self, inpDat, sCp, iTp = 90):
        llOI = [[self.dOCp[GC.ID_KAS_HPCAL1], self.dOCp[GC.ID_LPR_NRT2P1]],
                [self.dOCp[GC.ID_KAS_X], self.dOCp[GC.ID_LPR_NRT2P1]]]
        lOO = []
        super().__init__(inpDat, self.dOCp, llOI, lOO, iTp = iTp)
        self.idO = self.inFr.lSCpTpL[5]
        self.descO = 'Component NRT2.1-HPCAL1 interaction'
        self.adaptPSites(inpDat, self.dOCp[GC.ID_LPR_NRT2P1], sCp)
        self.adaptPSites(inpDat, self.dOCp[GC.ID_KAS_HPCAL1], sCp)

    def ini_Cp_LKT(self, inpDat, sCp, iTp = 90):
        llOI = [[self.dOCp[GC.ID_KAS_HPCAL1], self.dOCp[GC.ID_LPR_NRT2P1]],
                [self.dOCp[GC.ID_KAS_X], self.dOCp[GC.ID_LPR_NRT2P1]]]
        lOO = []
        super().__init__(inpDat, self.dOCp, llOI, lOO, iTp = iTp)
        self.idO = self.inFr.lSCpTpL[6]
        self.descO = 'Component NRT2.1-HPCAL1 transition'
        self.adaptPSites(inpDat, self.dOCp[GC.ID_LPR_NRT2P1], sCp)
        self.adaptPSites(inpDat, self.dOCp[GC.ID_KAS_HPCAL1], sCp)

###############################################################################
