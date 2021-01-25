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
    def __init__(self, inpDat, llOInt=[], lOOth=[], iTp=90):
        super().__init__(inpDat, iTp=iTp)
        for cLOInt in llOInt:
            assert len(cLOInt) >= 2
        self.idO = GC.ID_CPB
        self.descO = 'ComponentBase'
        if not hasattr(self, 'sCp'):
            self.sCp = GC.S_USC*7
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
        for i, sSpS in enumerate(GC.L_S_SPS):
            if 'dInfSpS' in cO.dITp and sSpS in cO.dITp['dInfSpS']:
                sPylDPy = SF.setPylDPy(self.sCp, i)
                lSCpAs = cO.dITp['dInfSpS'][sSpS][sPylDPy]
                if sPylDPy == GC.S_DO_PYL:
                    _ = Phosphorylation(inpDat, cO, lSCpAs, sSpS).doPyl()
                    # if Phosphorylation(inpDat, cO, lSCpAs, sSpS).doPyl():
                    #     print('Phosphorylation at site', sSpS, 'happened!')
                elif sPylDPy == GC.S_DO_DPY:
                    _ = Dephosphorylation(inpDat, cO, lSCpAs, sSpS).doDePyl()
                    # if Dephosphorylation(inpDat, cO, lSCpAs, sSpS).doDePyl():
                    #     print('Dephosphorylation at site', sSpS, 'happened!')

class Component(ComponentBase):
    def __init__(self, inpDat, inpFr, sComp, iTp=90):
        self.inFr = inpFr
        self.sCp, sCp1, sCpSp1 = sComp, sComp[:1], sComp[:GC.I_S_CP_SEP1]
        sPat01_L = self.sCp[GC.I_S_CP_SEP1:GC.I_S_CP_SEP2] + GC.S_2DASH
        sPat01_K = GC.S_2DASH + self.sCp[GC.I_S_CP_SEP2:]
        if sCpSp1 == GC.S_L__:
            NRT2p1 = Protein_NRT2p1(inpDat, sPat01=sPat01_L)
            self.ini_Cp_L(inpDat, LPr=NRT2p1, iTp=iTp)
        elif sCpSp1 == GC.S_S__:
            NAR2p1 = Protein_NAR2p1(inpDat)
            self.ini_Cp_S(inpDat, SPr=NAR2p1, iTp=iTp)
        elif sCpSp1 == GC.S_K__:
            HPCAL1 = KinaseK(inpDat, sPat01=sPat01_K)
            self.ini_Cp_K(inpDat, KAsK=HPCAL1, iTp=iTp)
        elif sCp1 in [GC.S_X, GC.S_Y, GC.S_A, GC.S_B, GC.S_C, GC.S_D]:
            OAs = self.selAs(inpDat, sCp1=sCp1)
            self.ini_Cp_OAs(inpDat, As=OAs, iTp=iTp)
        elif sCpSp1 in [GC.S_LSI, GC.S_LSJ, GC.S_LST]:
            NRT2p1 = Protein_NRT2p1(inpDat, sPat01=sPat01_L)
            NAR2p1 = Protein_NAR2p1(inpDat)
            self.ini_Cp_LS(inpDat, LPr=NRT2p1, SPr=NAR2p1, sCpSp1=sCpSp1,
                           iTp=iTp)
        elif sCpSp1 in [GC.S_LKI, GC.S_LKJ, GC.S_LKT]:
            NRT2p1 = Protein_NRT2p1(inpDat, sPat01=sPat01_L)
            HPCAL1 = KinaseK(inpDat, sPat01=sPat01_K)
            self.ini_Cp_LK(inpDat, LPr=NRT2p1, KAsK=HPCAL1, sCpSp1=sCpSp1,
                           iTp=iTp)
        else:
            self.idO = GC.ID_CPN
            self.descO = 'Component'
        # print('Initiated "Component" object ' + sComp + '.')

    def selAs(self, inpDat, sCp1):
        if sCp1 == GC.S_X:
            cAs = KinaseX(inpDat)
        elif sCp1 == GC.S_Y:
            cAs = KinaseY(inpDat)
        elif sCp1 == GC.S_A:
            cAs = PhosphataseA(inpDat)
        elif sCp1 == GC.S_B:
            cAs = PhosphataseB(inpDat)
        elif sCp1 == GC.S_C:
            cAs = PhosphataseC(inpDat)
        elif sCp1 == GC.S_D:
            cAs = PhosphataseD(inpDat)
        return cAs

    def ini_Cp_L(self, inpDat, LPr, iTp=90):
        llOI, lOO = [], [LPr]
        super().__init__(inpDat, llOI, lOO, iTp=iTp)
        self.idO = self.inFr.dSCpSL[self.sCp[:GC.I_S_CP_SEP1]]
        self.descO = GC.S_DESC_L__
        self.adaptPSites(inpDat, LPr)

    def ini_Cp_S(self, inpDat, SPr, iTp=90):
        llOI, lOO = [], [SPr]
        super().__init__(inpDat, llOI, lOO, iTp=iTp)
        self.idO = self.inFr.dSCpSL[self.sCp[:GC.I_S_CP_SEP1]]
        self.descO = GC.S_DESC_S__

    def ini_Cp_K(self, inpDat, KAsK, iTp=90):
        llOI, lOO = [], [KAsK]
        super().__init__(inpDat, llOI, lOO, iTp=iTp)
        self.idO = self.inFr.dSCpSL[self.sCp[:GC.I_S_CP_SEP1]]
        self.descO = GC.S_DESC_K__
        self.adaptPSites(inpDat, KAsK)

    def ini_Cp_OAs(self, inpDat, As, iTp=90):
        llOI, lOO = [], [As]
        super().__init__(inpDat, llOI, lOO, iTp=iTp)
        self.idO = self.inFr.dSCpSL[self.sCp[:GC.I_S_CP_SEP1]]
        self.descO = GC.S_DESC_OAS + As.idO

    def ini_Cp_LS(self, inpDat, LPr, SPr, sCpSp1, iTp=90):
        llOI, lOO = [[SPr, LPr]], []
        super().__init__(inpDat, llOI, lOO, iTp=iTp)
        self.idO = self.inFr.dSCpSL[self.sCp[:GC.I_S_CP_SEP1]]
        self.descO = GC.D_DESC[sCpSp1]
        self.adaptPSites(inpDat, LPr)

    def ini_Cp_LK(self, inpDat, LPr, KAsK, sCpSp1, iTp=90):
        llOI, lOO = [[KAsK, LPr]], []
        super().__init__(inpDat, llOI, lOO, iTp=iTp)
        self.idO = self.inFr.dSCpSL[self.sCp[:GC.I_S_CP_SEP1]]
        self.descO = GC.D_DESC[sCpSp1]
        self.adaptPSites(inpDat, LPr)
        self.adaptPSites(inpDat, KAsK)

    def ini_Cp_LSI(self, inpDat, LPr, SPr, iTp=90):
        llOI, lOO = [[SPr, LPr]], []
        super().__init__(inpDat, llOI, lOO, iTp=iTp)
        self.idO = self.inFr.dSCpSL[self.sCp[:GC.I_S_CP_SEP1]]
        self.descO = 'Component NRT2.1-NAR2.1 strong interaction'
        self.adaptPSites(inpDat, LPr)

    def ini_Cp_LSJ(self, inpDat, LPr, SPr, iTp=90):
        llOI, lOO = [[SPr, LPr]], []
        super().__init__(inpDat, llOI, lOO, iTp=iTp)
        self.idO = self.inFr.dSCpSL[self.sCp[:GC.I_S_CP_SEP1]]
        self.descO = 'Component NRT2.1-NAR2.1 weak interaction'
        self.adaptPSites(inpDat, LPr)

    def ini_Cp_LST(self, inpDat, LPr, SPr, iTp=90):
        llOI, lOO = [[SPr, LPr]], []
        super().__init__(inpDat, llOI, lOO, iTp=iTp)
        self.idO = self.inFr.dSCpSL[self.sCp[:GC.I_S_CP_SEP1]]
        self.descO = 'Component NRT2.1-NAR2.1 transition'
        self.adaptPSites(inpDat, LPr)

    def ini_Cp_LKI(self, inpDat, LPr, KAsK, iTp=90):
        llOI, lOO = [[KAsK, LPr]], []
        super().__init__(inpDat, llOI, lOO, iTp=iTp)
        self.idO = self.inFr.dSCpSL[self.sCp[:GC.I_S_CP_SEP1]]
        self.descO = 'Component NRT2.1-HPCAL1 strong interaction'
        self.adaptPSites(inpDat, LPr)
        self.adaptPSites(inpDat, KAsK)

    def ini_Cp_LKJ(self, inpDat, LPr, KAsK, iTp=90):
        llOI, lOO = [[KAsK, LPr]], []
        super().__init__(inpDat, llOI, lOO, iTp=iTp)
        self.idO = self.inFr.dSCpSL[self.sCp[:GC.I_S_CP_SEP1]]
        self.descO = 'Component NRT2.1-HPCAL1 weak interaction'
        self.adaptPSites(inpDat, LPr)
        self.adaptPSites(inpDat, KAsK)

    def ini_Cp_LKT(self, inpDat, LPr, KAsK, iTp=90):
        llOI, lOO = [[KAsK, LPr]], []
        super().__init__(inpDat, llOI, lOO, iTp=iTp)
        self.idO = self.inFr.dSCpSL[self.sCp[:GC.I_S_CP_SEP1]]
        self.descO = 'Component NRT2.1-HPCAL1 transition'
        self.adaptPSites(inpDat, LPr)
        self.adaptPSites(inpDat, KAsK)

###############################################################################
