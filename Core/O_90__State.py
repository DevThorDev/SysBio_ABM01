# -*- coding: utf-8 -*-
###############################################################################
# --- O_90__State.py ----------------------------------------------------------
###############################################################################
import Core.C_00__GenConstants as GC
import Core.F_00__GenFunctions as GF
# import Core.F_03__OTpFunctions as TF

from Core.O_00__Base import Base
from Core.O_80__Interaction import (Interaction, Phosphorylation,
                                    Dephosphorylation)
from Core.O_99__System import System

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class State(Base):
    def __init__(self, inpDat, lSeOInt = [], lPAs = [], lOOth = [], iTp = 90):
        super().__init__(inpDat, iTp = iTp)
        for cSeOInt in lSeOInt:
            assert len(cSeOInt) >= 2
        self.idO = 'Sta'
        self.descO = 'State'
        self.lSeOI = lSeOInt
        self.lPs = lPAs
        self.lOO = lOOth
        print('Initiated "State" object.')
        
    def createSystem(self, inpDat):
        lOSy = GF.lSeToUniqueList(self.lSeOI) + self.lPs + self.lOO
        return System(inpDat, lOSys = lOSy)

class State_Int(State):
    def __init__(self, inpDat, lSeOInt = [], lPAs = [], lOOth = [], iTp = 90):
        super().__init__(inpDat, lSeOInt, lPAs, lOOth, iTp = iTp)
        self.idO = 'St_Int'
        self.descO = 'State interaction'
        print('Initiated "State_Int" object.')
        
    def set_Sta_Int_AT5G49770_NRT2p1(self, inpDat):
        self.idO = GC.S_ST_INT_AT5G49770_NRT2P1
        self.descO = 'State interaction AT5G49770-NRT2p1'
        dSts = {GC.S_SPS_KAS1_S839: (GC.B_DO_DEPYL, self.lPs[0]),
                GC.S_SPS_KAS1_S870: (GC.B_DO_PYL, self.lPs[1])}
        self.adaptPSites(inpDat, lKAs[0], dSites = dSts)
        dSts = {GC.S_SPS_LPR1_S21: (GC.B_DO_PYL, self.lPs[2]),
                GC.S_SPS_LPR1_S28: (GC.B_DO_DEPYL, self.lPs[3])}
        self.adaptPSites(inpDat, cLPr, dSites = dSts)
        
    def stateTrans(self, idTargSta):
        if idTargSta == self.idO:
            print('WARNING: Target state equals current state ID', self.idO)
        else:
            if idTargSta == GC.S_ST_INT_AT5G49770_NRT2P1:
                pass
    def adaptPSites(self, inpDat, cO, dSites = {}):
        for cSite, (bMod, cPAs) in dSites.items():
            if bMod == GC.B_DO_PYL:
                if Phosphorylation(inpDat, cO, cPAs, cSite).doPyl():
                    print('Phosphorylation at site', cSite, 'happened!')
            elif bMod == GC.B_DO_DEPYL:
                if Dephosphorylation(inpDat, cO, cPAs, cSite).doDePyl():
                    print('Dephosphorylation at site', cSite, 'happened!')
        
class Sta_Int_AT5G49770_NRT2p1(State_Int):
    def __init__(self, inpDat, cLPr, cSPr, lKAs = [], lPAs = [], iTp = 90):
        assert len(lKAs) == 1 and len(lPAs) >= 4
        super().__init__(inpDat, lSeOInt = [{lKAs[0], cLPr}], lPAs = lPAs,
                         lOOth = [cSPr], iTp = iTp)
        self.idO = GC.S_ST_INT_AT5G49770_NRT2P1
        self.descO = 'State interaction AT5G49770-NRT2p1'
        dSts = {GC.S_SPS_KAS1_S839: (GC.B_DO_DEPYL, self.lPs[0]),
                GC.S_SPS_KAS1_S870: (GC.B_DO_PYL, self.lPs[1])}
        self.adaptPSites(inpDat, lKAs[0], dSites = dSts)
        dSts = {GC.S_SPS_LPR1_S21: (GC.B_DO_PYL, self.lPs[2]),
                GC.S_SPS_LPR1_S28: (GC.B_DO_DEPYL, self.lPs[3])}
        self.adaptPSites(inpDat, cLPr, dSites = dSts)
        print('Initiated "Sta_Int_AT5G49770_NRT2p1" object.')

class Sta_Trans_AT5G49770_NRT2p1(State_Int):
    def __init__(self, inpDat, cLPr, cSPr, lKAs = [], lPAs = [], iTp = 90):
        assert len(lKAs) == 2 and len(lPAs) >= 4
        super().__init__(inpDat, lSeOInt = [{lKAs[0], cLPr}, {lKAs[1], cLPr}],
                         lPAs = lPAs, lOOth = [cSPr], iTp = iTp)
        self.idO = GC.S_ST_TRANS_AT5G49770_NRT2P1
        self.descO = 'State transition from AT5G49770-NRT2p1'
        dSts = {GC.S_SPS_KAS1_S839: (GC.B_DO_PYL, self.lPs[0]),
                GC.S_SPS_KAS1_S870: (GC.B_DO_PYL, self.lPs[1])}
        self.adaptPSites(inpDat, lKAs[0], dSites = dSts)
        dSts = {GC.S_SPS_LPR1_S21: (GC.B_DO_PYL, self.lPs[2]),
                GC.S_SPS_LPR1_S28: (GC.B_DO_DEPYL, self.lPs[3])}
        self.adaptPSites(inpDat, cLPr, dSites = dSts)
        print('Initiated "Sta_Trans_AT5G49770_NRT2p1" object.')

class Sta_Int_NAR2p1_NRT2p1(State_Int):
    def __init__(self, inpDat, cLPr, cSPr, lKAs = [], lPAs = [], iTp = 90):
        assert len(lKAs) == 1 and len(lPAs) >= 4
        super().__init__(inpDat, lSeOInt = [{cSPr, cLPr}], lPAs = lPAs,
                         lOOth = [lKAs[0]], iTp = iTp)
        self.idO = GC.S_ST_INT_NAR2P1_NRT2P1
        self.descO = 'State interaction NAR2p1-NRT2p1'
        dSts = {GC.S_SPS_KAS1_S839: (GC.B_DO_PYL, self.lPs[0]),
                GC.S_SPS_KAS1_S870: (GC.B_DO_DEPYL, self.lPs[1])}
        self.adaptPSites(inpDat, lKAs[0], dSites = dSts)
        dSts = {GC.S_SPS_LPR1_S21: (GC.B_DO_DEPYL, self.lPs[2]),
                GC.S_SPS_LPR1_S28: (GC.B_DO_PYL, self.lPs[3])}
        self.adaptPSites(inpDat, cLPr, dSites = dSts)
        print('Initiated "Sta_Int_NAR2p1_NRT2p1" object.')

class Sta_Trans_NAR2p1_NRT2p1(State_Int):
    def __init__(self, inpDat, cLPr, cSPr, lKAs = [], lPAs = [], iTp = 90):
        assert len(lKAs) == 1 and len(lPAs) >= 4
        super().__init__(inpDat, lSeOInt = [{cSPr, cLPr}], lPAs = lPAs,
                         lOOth = [lKAs[0]], iTp = iTp)
        self.idO = GC.S_ST_TRANS_NAR2P1_NRT2P1
        self.descO = 'State transition from NAR2p1-NRT2p1'
        dSts = {GC.S_SPS_KAS1_S839: (GC.B_DO_PYL, self.lPs[0]),
                GC.S_SPS_KAS1_S870: (GC.B_DO_DEPYL, self.lPs[1])}
        self.adaptPSites(inpDat, lKAs[0], dSites = dSts)
        dSts = {GC.S_SPS_LPR1_S21: (GC.B_DO_DEPYL, self.lPs[2]),
                GC.S_SPS_LPR1_S28: (GC.B_DO_PYL, self.lPs[3])}
        self.adaptPSites(inpDat, cLPr, dSites = dSts)
        print('Initiated "Sta_Trans_NAR2p1_NRT2p1" object.')

###############################################################################
