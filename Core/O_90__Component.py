# -*- coding: utf-8 -*-
###############################################################################
# --- O_90__Component.py ------------------------------------------------------
###############################################################################
import Core.C_00__GenConstants as GC
import Core.F_00__GenFunctions as GF
import Core.F_01__SpcFunctions as SF

from Core.O_00__Base import Base
from Core.O_02__Protein import (KinaseK, KinaseX, KinaseY, PhosphataseA,
                                PhosphataseB, PhosphataseC, PhosphataseD,
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

    def adaptPSites(self, inpDat, cO):
        for sSpS, dI in GC.DS_SPS[cO.idO].items():
            sPylDPy, idAs = SF.setPylDPy(dI, self.sCp)
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
        self.sCp, sCp1, sCp3 = sComp, sComp[:1], sComp[:3]
        self.createDOComp(inpDat)
        if sCp3 == GC.S_L__:
            self.ini_Cp_L(inpDat, iTp = iTp)
        elif sCp3 == GC.S_S__:
            self.ini_Cp_S(inpDat, iTp = iTp)
        elif sCp3 == GC.S_K__:
            self.ini_Cp_K(inpDat, iTp = iTp)
        elif sCp1 in [GC.S_X, GC.S_Y, GC.S_A, GC.S_B, GC.S_C, GC.S_D]:
            self.ini_Cp_As(inpDat, sIDAs = sCp1, iTp = iTp)
        elif sCp3 == GC.S_LSI:
            self.ini_Cp_LSI(inpDat, iTp = iTp)
        elif sCp3 == GC.S_LSJ:
            self.ini_Cp_LSJ(inpDat, iTp = iTp)
        elif sCp3 == GC.S_LST:
            self.ini_Cp_LST(inpDat, iTp = iTp)
        elif sCp3 == GC.S_LKI:
            self.ini_Cp_LKI(inpDat, iTp = iTp)
        elif sCp3 == GC.S_LKJ:
            self.ini_Cp_LKJ(inpDat, iTp = iTp)
        elif sCp3 == GC.S_LKT:
            self.ini_Cp_LKT(inpDat, iTp = iTp)
        else:
            self.idO = GC.ID_CPN
            self.descO = 'Component'
        # print('Initiated "Component" object ' + sComp + '.')

    def createDOComp(self, inpDat, iV = 0):
        # Large protein NRT2.1 ------------------------------------------------
        NRT2p1 = Protein_NRT2p1(inpDat)
        # Small protein NAR2.1 ------------------------------------------------
        NAR2p1 = Protein_NAR2p1(inpDat)
        # Kinases KAsK, KAsX, KAsY --------------------------------------------
        KAsK = KinaseK(inpDat)
        KAsX = KinaseX(inpDat)
        KAsY = KinaseY(inpDat)
        # Phosphatases PAsA, PAsB, PAsC, PAsD ---------------------------------
        PAsA = PhosphataseA(inpDat)
        PAsB = PhosphataseB(inpDat)
        PAsC = PhosphataseC(inpDat)
        PAsD = PhosphataseD(inpDat)
        # Create initial component --------------------------------------------
        self.dOCp = {GC.ID_KAS_K: KAsK,
                     GC.ID_KAS_X: KAsX,
                     GC.ID_KAS_Y: KAsY,
                     GC.ID_PAS_A: PAsA,
                     GC.ID_PAS_B: PAsB,
                     GC.ID_PAS_C: PAsC,
                     GC.ID_PAS_D: PAsD,
                     GC.ID_LPR_NRT2P1: NRT2p1,
                     GC.ID_SPR_NAR2P1: NAR2p1}

    def ini_Cp_L(self, inpDat, iTp = 90):
        llOI = []
        lOO = [self.dOCp[GC.ID_LPR_NRT2P1]]
        super().__init__(inpDat, self.dOCp, llOI, lOO, iTp = iTp)
        self.idO = self.inFr.dSCpSL[self.sCp[:3]]
        self.descO = 'Component NRT2.1'
        self.adaptPSites(inpDat, self.dOCp[GC.ID_LPR_NRT2P1])

    def ini_Cp_S(self, inpDat, iTp = 90):
        llOI = []
        lOO = [self.dOCp[GC.ID_SPR_NAR2P1]]
        super().__init__(inpDat, self.dOCp, llOI, lOO, iTp = iTp)
        self.idO = self.inFr.dSCpSL[self.sCp[:3]]
        self.descO = 'Component NAR2.1'

    def ini_Cp_K(self, inpDat, iTp = 90):
        llOI = []
        lOO = [self.dOCp[GC.ID_KAS_K]]
        super().__init__(inpDat, self.dOCp, llOI, lOO, iTp = iTp)
        self.idO = self.inFr.dSCpSL[self.sCp[:3]]
        self.descO = 'Component K (HPCAL1)'
        self.adaptPSites(inpDat, self.dOCp[GC.ID_KAS_K])

    def ini_Cp_As(self, inpDat, sIDAs, iTp = 90):
        llOI = []
        lOO = [self.dOCp[GC.D_ID_AS[sIDAs]]]
        super().__init__(inpDat, self.dOCp, llOI, lOO, iTp = iTp)
        self.idO = self.inFr.dSCpSL[self.sCp[:3]]
        self.descO = 'Component ' + sIDAs

    def ini_Cp_LSI(self, inpDat, iTp = 90):
        llOI = [[self.dOCp[GC.ID_SPR_NAR2P1], self.dOCp[GC.ID_LPR_NRT2P1]]]
        lOO = []
        super().__init__(inpDat, self.dOCp, llOI, lOO, iTp = iTp)
        self.idO = self.inFr.dSCpSL[self.sCp[:3]]
        self.descO = 'Component NRT2.1-NAR2.1 strong interaction'
        self.adaptPSites(inpDat, self.dOCp[GC.ID_LPR_NRT2P1])

    def ini_Cp_LSJ(self, inpDat, iTp = 90):
        llOI = [[self.dOCp[GC.ID_SPR_NAR2P1], self.dOCp[GC.ID_LPR_NRT2P1]]]
        lOO = []
        super().__init__(inpDat, self.dOCp, llOI, lOO, iTp = iTp)
        self.idO = self.inFr.dSCpSL[self.sCp[:3]]
        self.descO = 'Component NRT2.1-NAR2.1 weak interaction'
        self.adaptPSites(inpDat, self.dOCp[GC.ID_LPR_NRT2P1])

    def ini_Cp_LST(self, inpDat, iTp = 90):
        llOI = [[self.dOCp[GC.ID_SPR_NAR2P1], self.dOCp[GC.ID_LPR_NRT2P1]]]
        lOO = []
        super().__init__(inpDat, self.dOCp, llOI, lOO, iTp = iTp)
        self.idO = self.inFr.dSCpSL[self.sCp[:3]]
        self.descO = 'Component NRT2.1-NAR2.1 transition'
        self.adaptPSites(inpDat, self.dOCp[GC.ID_LPR_NRT2P1])

    def ini_Cp_LKI(self, inpDat, iTp = 90):
        llOI = [[self.dOCp[GC.ID_KAS_K], self.dOCp[GC.ID_LPR_NRT2P1]]]
        lOO = []
        super().__init__(inpDat, self.dOCp, llOI, lOO, iTp = iTp)
        self.idO = self.inFr.dSCpSL[self.sCp[:3]]
        self.descO = 'Component NRT2.1-HPCAL1 strong interaction'
        self.adaptPSites(inpDat, self.dOCp[GC.ID_LPR_NRT2P1])
        self.adaptPSites(inpDat, self.dOCp[GC.ID_KAS_K])

    def ini_Cp_LKJ(self, inpDat, iTp = 90):
        llOI = [[self.dOCp[GC.ID_KAS_K], self.dOCp[GC.ID_LPR_NRT2P1]]]
        lOO = []
        super().__init__(inpDat, self.dOCp, llOI, lOO, iTp = iTp)
        self.idO = self.inFr.dSCpSL[self.sCp[:3]]
        self.descO = 'Component NRT2.1-HPCAL1 weak interaction'
        self.adaptPSites(inpDat, self.dOCp[GC.ID_LPR_NRT2P1])
        self.adaptPSites(inpDat, self.dOCp[GC.ID_KAS_K])

    def ini_Cp_LKT(self, inpDat, iTp = 90):
        llOI = [[self.dOCp[GC.ID_KAS_K], self.dOCp[GC.ID_LPR_NRT2P1]]]
        lOO = []
        super().__init__(inpDat, self.dOCp, llOI, lOO, iTp = iTp)
        self.idO = self.inFr.dSCpSL[self.sCp[:3]]
        self.descO = 'Component NRT2.1-HPCAL1 transition'
        self.adaptPSites(inpDat, self.dOCp[GC.ID_LPR_NRT2P1])
        self.adaptPSites(inpDat, self.dOCp[GC.ID_KAS_K])

###############################################################################
