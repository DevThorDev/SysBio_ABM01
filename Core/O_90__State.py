# -*- coding: utf-8 -*-
###############################################################################
# --- O_90__State.py ----------------------------------------------------------
###############################################################################
import Core.C_00__GenConstants as GC
# import Core.F_00__GenFunctions as GF
# import Core.F_03__OTpFunctions as TF

from Core.O_00__Base import Base
from Core.O_80__Interaction import (Interaction, Phosphorylation,
                                    Dephosphorylation)
from Core.O_99__System import System

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class State(Base):
    def __init__(self, inpDat, lOInt = [], lPAs = [], lOOth = [], iTp = 90):
        super().__init__(inpDat, iTp = iTp)
        assert len(lOInt) >= 2
        self.idO = 'Sta'
        self.descO = 'State'
        self.lOI = lOInt
        self.lPs = lPAs
        self.lOO = lOOth
        print('Initiated "State" object.')

class State_Int_AT5G49770_NRT2p1(State):
    def __init__(self, inpDat, cKAs, cLPr, cSPr, lPAs = [], iTp = 90):
        assert len(lPAs) >= 4
        super().__init__(inpDat, lOInt = [cKAs, cLPr], lPAs = lPAs,
                         lOOth = [cSPr], iTp = iTp)
        KinaseAT5G49770, NRT2p1 = self.lOI      # order!
        self.idO = 'St_Int_AT5G49770_NRT2p1'
        self.descO = 'State interaction AT5G49770-NRT2p1'
        self.adaptPSites_AT5G49770(inpDat, KinaseAT5G49770)
        self.adaptPSites_NRT2p1(inpDat, NRT2p1)
        print('Initiated "State_Int_AT5G49770_NRT2p1" object.')
        
    def adaptPSites_AT5G49770(self, inpDat, cOKin):
        s1, s2 = GC.S_SPS_KAS1_S839, GC.S_SPS_KAS1_S870
        if Dephosphorylation(inpDat, cOKin, self.lPs[0], s1).doDePyl():
            print('Dephosphorylation at site', s1, 'happened!')
        if Phosphorylation(inpDat, cOKin, self.lPs[1], s2).doPyl():
            print('Phosphorylation at site', s2, 'happened!')
        self.lOI[0] = cOKin
        self.lOI[0].printSpecSites()
        
    def adaptPSites_NRT2p1(self, inpDat, cOProt):
        s1, s2 = GC.S_SPS_LPR1_S21, GC.S_SPS_LPR1_S28
        if Phosphorylation(inpDat, cOProt, self.lPs[2], s1).doPyl():
            print('Phosphorylation at site', s1, 'happened!')
        if Dephosphorylation(inpDat, cOProt, self.lPs[3], s2).doDePyl():
            print('Dephosphorylation at site', s2, 'happened!')
        self.lOI[1] = cOProt
        self.lOI[1].printSpecSites()
        
    def createSystem(self, inpDat):
        return System(inpDat, lOSys = self.lOI + self.lPs + self.lOO)

###############################################################################
