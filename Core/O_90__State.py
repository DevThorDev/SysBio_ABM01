# -*- coding: utf-8 -*-
###############################################################################
# --- O_90__State.py ----------------------------------------------------------
###############################################################################
import Core.C_00__GenConstants as GC
import Core.F_00__GenFunctions as GF
# import Core.F_03__OTpFunctions as TF

from Core.O_00__Base import Base
from Core.O_80__Interaction import Phosphorylation, Dephosphorylation
from Core.O_99__System import System

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class State(Base):
    def __init__(self, inpDat, llOInt = [], lPAs = [], lOOth = [], iTp = 90):
        super().__init__(inpDat, iTp = iTp)
        for cLOInt in llOInt:
            assert len(cLOInt) >= 2
        self.idO = 'Sta'
        self.descO = 'State'
        self.llOI = llOInt
        self.lPs = lPAs
        self.lOO = lOOth
        print('Initiated "State" object.')
        
    def __str__(self):
        sIn = ('++++ State ' + self.idO + ' (' + self.descO + '):')
        return sIn
    
    def printDetails(self):
        for k, lOI in enumerate(self.llOI):
            print('- Interacting pair ' + str(k + 1) + ': (' + lOI[0].idO +
                  ', ' + lOI[1].idO + ')')
        for k, cP in enumerate(self.lPs):
            print('- Phosphatase ' + str(k + 1) + ': ' + cP.idO)
        for k, cO in enumerate(self.lOO):
            print('- Further component ' + str(k + 1) + ': ' + cO.idO)
        print('-- State component details:')
        for cO in GF.lItToUniqueList(self.llOI) + self.lPs + self.lOO:
            cO.printMolSpecSites()
    
    def printStateDetails(self):
        print(self)
        self.printDetails()
        
    def createSystem(self, inpDat):
        lOSy = GF.lItToUniqueList(self.llOI) + self.lPs + self.lOO
        return System(inpDat, lOSys = lOSy)

class State_Int_Trans(State):
    def __init__(self, inpDat, cLPr, cSPr, lKAs, lPAs, lSMo, iTp = 90):
        assert len(lKAs) >= 2 and len(lPAs) >= 4
        self.cLPr, self.cSPr = cLPr, cSPr
        self.lKAs, self.lPAs, self.lSMo = lKAs, lPAs, lSMo
        if inpDat.dI['sStIni'] == GC.S_ST_A_INT_AT5G49770_NRT2P1:
            self.ini_St_A_Int_AT5G49770_NRT2p1(inpDat, cLPr, cSPr, lKAs, lPAs,
                                               lSMo, iTp = iTp)
        elif inpDat.dI['sStIni'] == GC.S_ST_B_TRANS_AT5G49770_NRT2P1:
            self.ini_St_B_Trans_AT5G49770_NRT2p1(inpDat, cLPr, cSPr, lKAs,
                                                 lPAs, lSMo, iTp = iTp)
        elif inpDat.dI['sStIni'] == GC.S_ST_C_INT_NAR2P1_NRT2P1:
            self.ini_St_C_Int_NAR2p1_NRT2p1(inpDat, cLPr, cSPr, lKAs, lPAs,
                                            lSMo, iTp = iTp)
        elif inpDat.dI['sStIni'] == GC.S_ST_D_TRANS_NAR2P1_NRT2P1:
            self.ini_St_D_Trans_NAR2p1_NRT2p1(inpDat, cLPr, cSPr, lKAs, lPAs,
                                              lSMo, iTp = iTp)
        else:
            self.idO = 'St_Int_Trans'
            self.descO = 'State interaction or transition'
        self.dCnc = {cSMo.idO: cSMo.cCnc for cSMo in lSMo}
        print('Initiated "State_Int_Trans" object.')
    
    def printDCnc(self):
        print('Dictionary of small molecule concentrations:')
        for cID, cCnc in self.dCnc.items():
            print(cID + ': ' + str(round(cCnc, GC.R04)))
    
    def adaptPSites(self, inpDat, cO, dSites = {}):
        for cSite, (bMod, cPAs) in dSites.items():
            if bMod == GC.B_DO_PYL:
                if Phosphorylation(inpDat, cO, cPAs, cSite).doPyl():
                    print('Phosphorylation at site', cSite, 'happened!')
            elif bMod == GC.B_DO_DEPYL:
                if Dephosphorylation(inpDat, cO, cPAs, cSite).doDePyl():
                    print('Dephosphorylation at site', cSite, 'happened!')

    def ini_St_A_Int_AT5G49770_NRT2p1(self, inpDat, cLPr, cSPr, lKAs, lPAs,
                                      lSMo, iTp = 90):
        super().__init__(inpDat, llOInt = [[lKAs[0], cLPr]], lPAs = lPAs,
                         lOOth = [cSPr, lKAs[1], lSMo[0], lSMo[1]], iTp = iTp)
        self.idO = GC.S_ST_A_INT_AT5G49770_NRT2P1
        self.descO = 'State interaction AT5G49770-NRT2p1'
        dSts = {GC.S_SPS_KAS1_S839: (GC.B_DO_DEPYL, self.lPs[0]),
                GC.S_SPS_KAS1_S870: (GC.B_DO_PYL, self.lPs[1])}
        self.adaptPSites(inpDat, lKAs[0], dSites = dSts)
        dSts = {GC.S_SPS_LPR1_S21: (GC.B_DO_PYL, self.lPs[2]),
                GC.S_SPS_LPR1_S28: (GC.B_DO_DEPYL, self.lPs[3])}
        self.adaptPSites(inpDat, cLPr, dSites = dSts)

    def ini_St_B_Trans_AT5G49770_NRT2p1(self, inpDat, cLPr, cSPr, lKAs, lPAs,
                                        lSMo, iTp = 90):
        super().__init__(inpDat, llOInt = [[lKAs[0], cLPr], [lKAs[1], cLPr]],
                         lPAs = lPAs, lOOth = [cSPr, lSMo[0], lSMo[1]],
                         iTp = iTp)
        self.idO = GC.S_ST_B_TRANS_AT5G49770_NRT2P1
        self.descO = 'State transition from AT5G49770-NRT2p1'
        dSts = {GC.S_SPS_KAS1_S839: (GC.B_DO_PYL, self.lPs[0]),
                GC.S_SPS_KAS1_S870: (GC.B_DO_PYL, self.lPs[1])}
        self.adaptPSites(inpDat, lKAs[0], dSites = dSts)
        dSts = {GC.S_SPS_LPR1_S21: (GC.B_DO_PYL, self.lPs[2]),
                GC.S_SPS_LPR1_S28: (GC.B_DO_DEPYL, self.lPs[3])}
        self.adaptPSites(inpDat, cLPr, dSites = dSts)

    def ini_St_C_Int_NAR2p1_NRT2p1(self, inpDat, cLPr, cSPr, lKAs, lPAs, lSMo,
                                   iTp = 90):
        super().__init__(inpDat, llOInt = [[cSPr, cLPr]], lPAs = lPAs,
                         lOOth = [lKAs[0], lKAs[1], lSMo[0], lSMo[1]],
                         iTp = iTp)
        self.idO = GC.S_ST_C_INT_NAR2P1_NRT2P1
        self.descO = 'State interaction NAR2p1-NRT2p1'
        dSts = {GC.S_SPS_KAS1_S839: (GC.B_DO_PYL, self.lPs[0]),
                GC.S_SPS_KAS1_S870: (GC.B_DO_DEPYL, self.lPs[1])}
        self.adaptPSites(inpDat, lKAs[0], dSites = dSts)
        dSts = {GC.S_SPS_LPR1_S21: (GC.B_DO_DEPYL, self.lPs[2]),
                GC.S_SPS_LPR1_S28: (GC.B_DO_PYL, self.lPs[3])}
        self.adaptPSites(inpDat, cLPr, dSites = dSts)

    def ini_St_D_Trans_NAR2p1_NRT2p1(self, inpDat, cLPr, cSPr, lKAs, lPAs,
                                     lSMo, iTp = 90):
        super().__init__(inpDat, llOInt = [[cSPr, cLPr]], lPAs = lPAs,
                         lOOth = [lKAs[0], lKAs[1], lSMo[0], lSMo[1]],
                         iTp = iTp)
        self.idO = GC.S_ST_D_TRANS_NAR2P1_NRT2P1
        self.descO = 'State transition from NAR2p1-NRT2p1'
        dSts = {GC.S_SPS_KAS1_S839: (GC.B_DO_PYL, self.lPs[0]),
                GC.S_SPS_KAS1_S870: (GC.B_DO_DEPYL, self.lPs[1])}
        self.adaptPSites(inpDat, lKAs[0], dSites = dSts)
        dSts = {GC.S_SPS_LPR1_S21: (GC.B_DO_DEPYL, self.lPs[2]),
                GC.S_SPS_LPR1_S28: (GC.B_DO_PYL, self.lPs[3])}
        self.adaptPSites(inpDat, cLPr, dSites = dSts)

    def to_St_A_Int_AT5G49770_NRT2p1(self, inpDat):
        self.idO = GC.S_ST_A_INT_AT5G49770_NRT2P1
        self.descO = 'State interaction AT5G49770-NRT2p1'
        self.lOO[0], self.llOI[0][0] = self.llOI[0][0], self.lOO[0]
        dSts = {GC.S_SPS_KAS1_S839: (GC.B_DO_DEPYL, self.lPs[0]),
                GC.S_SPS_KAS1_S870: (GC.B_DO_PYL, self.lPs[1])}
        self.adaptPSites(inpDat, self.llOI[0][0], dSites = dSts)
        dSts = {GC.S_SPS_LPR1_S21: (GC.B_DO_PYL, self.lPs[2]),
                GC.S_SPS_LPR1_S28: (GC.B_DO_DEPYL, self.lPs[3])}
        self.adaptPSites(inpDat, self.llOI[0][1], dSites = dSts)

    def to_St_B_Trans_AT5G49770_NRT2p1(self, inpDat):
        self.idO = GC.S_ST_B_TRANS_AT5G49770_NRT2P1
        self.descO = 'State transition from AT5G49770-NRT2p1'
        self.llOI.append([self.lOO[1], self.llOI[0][1]])
        self.lOO = self.lOO[:1] + self.lOO[2:]
        dSts = {GC.S_SPS_KAS1_S839: (GC.B_DO_PYL, self.lPs[0])}
        self.adaptPSites(inpDat, self.llOI[0][0], dSites = dSts)

    def to_St_C_Int_NAR2p1_NRT2p1(self, inpDat):
        self.idO = GC.S_ST_C_INT_NAR2P1_NRT2P1
        self.descO = 'State interaction NAR2p1-NRT2p1'
        llOInt = [[self.lOO[0], self.llOI[0][1]]]
        lOOth = [self.llOI[0][0], self.llOI[1][0]] + self.lOO[1:]
        self.llOI, self.lOO = llOInt, lOOth
        dSts = {GC.S_SPS_KAS1_S870: (GC.B_DO_DEPYL, self.lPs[1])}
        self.adaptPSites(inpDat, self.lOO[0], dSites = dSts)
        dSts = {GC.S_SPS_LPR1_S21: (GC.B_DO_DEPYL, self.lPs[2]),
                GC.S_SPS_LPR1_S28: (GC.B_DO_PYL, self.lPs[3])}
        self.adaptPSites(inpDat, self.llOI[0][1], dSites = dSts)

    def to_St_D_Trans_NAR2p1_NRT2p1(self, inpDat):
        self.idO = GC.S_ST_D_TRANS_NAR2P1_NRT2P1
        self.descO = 'State transition from NAR2p1-NRT2p1'
    
    def changeConcSMo(self, cTS):
        for cSMo in self.lSMo:
            cSMo.changeConc(cTS)
            assert cSMo.idO in self.dCnc
            self.dCnc[cSMo.idO] = cSMo.cCnc
        
###############################################################################
