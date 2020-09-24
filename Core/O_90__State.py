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
        sIn = ('---- State ' + self.idO + ' (' + self.descO + '):\n' +
               'Interacting components: ' + str(self.llOI) + '\n' +
               'Phosphatases: ' + str(self.lPs) + '\n' +
               'Other components: ' + str(self.lOO))
        return sIn
    
    def printDetails(self):
        print('-- State component details:')
        for lOI in self.llOI:
            for cO in lOI:
                cO.printMolSpecSites()
        for cO in self.lPs + self.lOO:
            cO.printMolSpecSites()
    
    def printStateDetails(self):
        print(self)
        self.printDetails()
        
    def createSystem(self, inpDat):
        lOSy = GF.lItToUniqueList(self.llOI) + self.lPs + self.lOO
        return System(inpDat, lOSys = lOSy)

class State_Int_Trans(State):
    def __init__(self, inpDat, llOInt = [], lPAs = [], lOOth = [], iTp = 90):
        super().__init__(inpDat, llOInt, lPAs, lOOth, iTp = iTp)
        self.idO = 'St_Int_Trans'
        self.descO = 'State interaction or transition'
        print('Initiated "State_Int_Trans" object.')
        
    def stateTransition(self, idTargSta):
        if idTargSta == self.idO:
            print('WARNING: Target state equals current state ID', self.idO)
        else:
            if idTargSta == GC.S_ST_A_INT_AT5G49770_NRT2P1:
                pass
            
    def adaptPSites(self, inpDat, cO, dSites = {}):
        for cSite, (bMod, cPAs) in dSites.items():
            if bMod == GC.B_DO_PYL:
                if Phosphorylation(inpDat, cO, cPAs, cSite).doPyl():
                    print('Phosphorylation at site', cSite, 'happened!')
            elif bMod == GC.B_DO_DEPYL:
                if Dephosphorylation(inpDat, cO, cPAs, cSite).doDePyl():
                    print('Dephosphorylation at site', cSite, 'happened!')
        
class St_A_Int_AT5G49770_NRT2p1(State_Int_Trans):
    def __init__(self, inpDat, cLPr, cSPr, lKAs, lPAs, lSMo = [], iTp = 90):
        assert len(lKAs) >= 2 and len(lPAs) >= 4
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
        print('Initiated "St_A_Int_AT5G49770_NRT2p1" object.')

class St_B_Trans_AT5G49770_NRT2p1(State_Int_Trans):
    def __init__(self, inpDat, cLPr, cSPr, lKAs, lPAs, lSMo = [], iTp = 90):
        assert len(lKAs) == 2 and len(lPAs) >= 4
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
        print('Initiated "St_B_Trans_AT5G49770_NRT2p1" object.')

class St_C_Int_NAR2p1_NRT2p1(State_Int_Trans):
    def __init__(self, inpDat, cLPr, cSPr, lKAs, lPAs, lSMo = [], iTp = 90):
        assert len(lKAs) >= 2 and len(lPAs) >= 4
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
        print('Initiated "St_C_Int_NAR2p1_NRT2p1" object.')

class St_D_Trans_NAR2p1_NRT2p1(State_Int_Trans):
    def __init__(self, inpDat, cLPr, cSPr, lKAs, lPAs, lSMo = [], iTp = 90):
        assert len(lKAs) >= 2 and len(lPAs) >= 4
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
        print('Initiated "St_D_Trans_NAR2p1_NRT2p1" object.')

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
        
###############################################################################
