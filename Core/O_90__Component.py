# -*- coding: utf-8 -*-
###############################################################################
# --- O_90__Component.py ------------------------------------------------------
###############################################################################
import Core.C_00__GenConstants as GC
import Core.F_00__GenFunctions as GF
import Core.F_01__SpcFunctions as SF
import Core.F_03__OTpFunctions as TF

from Core.O_00__Base import Base
from Core.O_02__Protein import (Kinase_HPCAL1, Kinase_X, Kinase0,
                                Phosphatase0, Protein_NRT2p1, Protein_NAR2p1)
from Core.O_80__Interaction import Phosphorylation, Dephosphorylation

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class ComponentBase(Base):
    def __init__(self, inpDat, dOComp, llOInt = [], lOOth = [], iTp = 90):
        super().__init__(inpDat, iTp = iTp)
        for cLOInt in llOInt:
            assert len(cLOInt) >= 2
        self.idO = 'CpBase'
        self.descO = 'ComponentBase'
        if not hasattr(self, 'sCp'):
            self.sCp = '_'*7
        if not hasattr(self, 'dOCp'):
            self.dOCp = dOComp
        self.llOI = llOInt
        self.lOO = lOOth
        self.complementLO(inpDat, dOComp)
        self.prTrans = 0
        # print('Initiated "ComponentBase" object.')

    def complementLO(self, inpDat, dOComp):
        lOSy = GF.lItToUniqueList(self.llOI) + self.lOO
        lIDK = TF.complLSpec(inpDat, lOSy, sTp = 'KAs', sD = 'Pyl')
        self.lKAs0 = [Kinase0(inpDat, cID = ID) for ID in lIDK if ID not in
                      [GC.ID_KAS_X]]        # as Kinase_X is a specific kinase
        lIDP = TF.complLSpec(inpDat, lOSy, sTp = 'PAs', sD = 'DPy')
        self.lPAs0 = [Phosphatase0(inpDat, cID = ID) for ID in lIDP]
        self.lKAs = [self.lKAs0[k] for k in range(len(self.lKAs0))]
        if GC.SPC_KAS_X in lIDK:
            self.lKAs += [self.dOCp[GC.SPC_KAS_X]]
        self.lPAs = [self.lPAs0[k] for k in range(len(self.lPAs0))]

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
        for k, cK in enumerate(self.lKAs0):
            print('- Kinase ' + str(k + 1) + ': ' + cK.idO)
        for k, cP in enumerate(self.lPAs0):
            print('- Phosphatase ' + str(k + 1) + ': ' + cP.idO)
        print('-- Component details:')
        for cO in list(set(GF.lItToUniqueList(self.llOI) + self.lOO +
                           self.lKAs0 + self.lPAs0)):
            cO.printMolSpecSites()

    def printComponentDetails(self):
        print(self)
        self.printDetails()

    def adaptPSites(self, inpDat, cO, sCp):
        for sSpS, dI in GC.DS_SPS[cO.idO].items():
            sPylDPy, cAs = SF.setPylDPy(dI, sCp, self.lKAs, self.lPAs)
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
        self.createdOComp(inpDat)
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
            self.idO = 'Cp'
            self.descO = 'Component'
        # print('Initiated "Component" object ' + sComp + '.')

    def createdOComp(self, inpDat, iV = 0):
        # Large protein NRT2.1 ------------------------------------------------
        NRT2p1 = Protein_NRT2p1(inpDat)
        # Small protein NAR2.1 ------------------------------------------------
        NAR2p1 = Protein_NAR2p1(inpDat)
        # Kinases KAsHPCAL1, KAsX ---------------------------------------------
        KAsHPCAL1 = Kinase_HPCAL1(inpDat)
        KAsX = Kinase_X(inpDat)
        # Create initial component --------------------------------------------
        self.dOCp = {GC.SPC_KAS_A: KAsHPCAL1,
                     GC.SPC_KAS_X: KAsX,
                     GC.SPC_LPR_A: NRT2p1,
                     GC.SPC_SPR_A: NAR2p1}

    def ini_Cp_L(self, inpDat, sCp, iTp = 90):
        llOI = []
        lOO = [self.dOCp[GC.SPC_LPR_A], self.dOCp[GC.SPC_KAS_X]]
        super().__init__(inpDat, self.dOCp, llOI, lOO, iTp = iTp)
        self.idO = self.inFr.lSCpTpL[0]
        self.descO = 'Component NRT2.1'
        self.adaptPSites(inpDat, self.dOCp[GC.SPC_LPR_A], sCp)

    def ini_Cp_S(self, inpDat, sCp, iTp = 90):
        llOI = []
        lOO = [self.dOCp[GC.SPC_SPR_A]]
        super().__init__(inpDat, self.dOCp, llOI, lOO, iTp = iTp)
        self.idO = self.inFr.lSCpTpL[1]
        self.descO = 'Component NAR2.1'

    def ini_Cp_K(self, inpDat, sCp, iTp = 90):
        llOI = []
        lOO = [self.dOCp[GC.SPC_KAS_A]]
        super().__init__(inpDat, self.dOCp, llOI, lOO, iTp = iTp)
        self.idO = self.inFr.lSCpTpL[2]
        self.descO = 'Component HPCAL1'
        self.adaptPSites(inpDat, self.dOCp[GC.SPC_KAS_A], sCp)

    def ini_Cp_LSI(self, inpDat, sCp, iTp = 90):
        llOI = [[self.dOCp[GC.SPC_SPR_A], self.dOCp[GC.SPC_LPR_A]]]
        lOO = [self.dOCp[GC.SPC_KAS_X]]
        super().__init__(inpDat, self.dOCp, llOI, lOO, iTp = iTp)
        self.idO = self.inFr.lSCpTpL[3]
        self.descO = 'Component NRT2.1-NAR2.1 interaction'
        self.adaptPSites(inpDat, self.dOCp[GC.SPC_LPR_A], sCp)

    def ini_Cp_LST(self, inpDat, sCp, iTp = 90):
        llOI = [[self.dOCp[GC.SPC_SPR_A], self.dOCp[GC.SPC_LPR_A]]]
        lOO = [self.dOCp[GC.SPC_KAS_X]]
        super().__init__(inpDat, self.dOCp, llOI, lOO, iTp = iTp)
        self.idO = self.inFr.lSCpTpL[4]
        self.descO = 'Component NRT2.1-NAR2.1 transition'
        self.adaptPSites(inpDat, self.dOCp[GC.SPC_LPR_A], sCp)

    def ini_Cp_LKI(self, inpDat, sCp, iTp = 90):
        llOI = [[self.dOCp[GC.SPC_KAS_A], self.dOCp[GC.SPC_LPR_A]],
                [self.dOCp[GC.SPC_KAS_X], self.dOCp[GC.SPC_LPR_A]]]
        lOO = []
        super().__init__(inpDat, self.dOCp, llOI, lOO, iTp = iTp)
        self.idO = self.inFr.lSCpTpL[5]
        self.descO = 'Component NRT2.1-HPCAL1 interaction'
        self.adaptPSites(inpDat, self.dOCp[GC.SPC_LPR_A], sCp)
        self.adaptPSites(inpDat, self.dOCp[GC.SPC_KAS_A], sCp)

    def ini_Cp_LKT(self, inpDat, sCp, iTp = 90):
        llOI = [[self.dOCp[GC.SPC_KAS_A], self.dOCp[GC.SPC_LPR_A]],
                [self.dOCp[GC.SPC_KAS_X], self.dOCp[GC.SPC_LPR_A]]]
        lOO = []
        super().__init__(inpDat, self.dOCp, llOI, lOO, iTp = iTp)
        self.idO = self.inFr.lSCpTpL[6]
        self.descO = 'Component NRT2.1-HPCAL1 transition'
        self.adaptPSites(inpDat, self.dOCp[GC.SPC_LPR_A], sCp)
        self.adaptPSites(inpDat, self.dOCp[GC.SPC_KAS_A], sCp)

###############################################################################
