# -*- coding: utf-8 -*-
###############################################################################
# --- O_90__System.py ---------------------------------------------------------
###############################################################################
import pprint

import Core.C_00__GenConstants as GC
# import Core.F_00__GenFunctions as GF
import Core.F_03__OTpFunctions as TF

from Core.O_00__Base import Base
from Core.O_80__Interaction import (Interaction, Phosphorylation,
                                    Dephosphorylation)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class System(Base):
    def __init__(self, inpDat, iTp = 90, lOSys = []):
        super().__init__(inpDat, iTp)
        self.idO = 'Sys'
        self.descO = 'System'
        self.lOS = lOSys
        self.lMol = [cO for cO in self.lOS if cO.idO in GC.L_ID_MOL]
        self.lPro = [cO for cO in self.lOS if cO.idO in GC.L_ID_PRO]
        self.lEnz = [cO for cO in self.lOS if cO.idO in GC.L_ID_ENZ]
        self.lKAs = [cO for cO in self.lOS if cO.idO in GC.L_ID_KAS]
        self.lPAs = [cO for cO in self.lOS if cO.idO in GC.L_ID_PAS]
        self.lLPr = [cO for cO in self.lOS if cO.idO in GC.L_ID_LPR]
        self.lSPr = [cO for cO in self.lOS if cO.idO in GC.L_ID_SPR]
        self.lMet = [cO for cO in self.lOS if cO.idO in GC.L_ID_MET]
        self.lLMo = [cO for cO in self.lOS if cO.idO in GC.L_ID_LMO]
        self.lSMo = [cO for cO in self.lOS if cO.idO in GC.L_ID_SMO]
        self.lInt = [cO for cO in self.lOS if cO.idO in GC.L_ID_INT]
        self.lPyl = [cO for cO in self.lOS if cO.idO in GC.L_ID_PYL]
        self.lDePyl = [cO for cO in self.lOS if cO.idO in GC.L_ID_DEPYL]
        self.dCmp = {'Molecules': self.lMol,
                     'Proteins': self.lPro,
                     'Enzymes': self.lEnz,
                     'Kinases': self.lKAs,
                     'Phosphatase': self.lPAs,
                     'LargeProteins': self.lLPr,
                     'SmallProteins': self.lSPr,
                     'Metabolites': self.lMet,
                     'LargeMolecules': self.lLMo,
                     'SmallMolecules': self.lSMo,
                     'Interactions': self.lInt,
                     'Phosphorylations': self.lPyl,
                     'Dephosphorylations': self.lDePyl}
        print('Initiated "System" object.')
    
    def printSystem(self):
        print('+'*16, 'System consists of:', '+'*43)
        for s, lCmp in self.dCmp.items():
            if len(lCmp) > 0:
                TF.printSysComp(s, lCmp)
        print('+'*80)
        
    def setToState(self, inpDat, lOIntSt, lPAsSt = []):
        cSt = State(inpDat, lOInt = lOIntSt, lPAs = lPAsSt)

    def setToState_Int_AT5G49770_NRT2p1(self, inpDat):
        
        cSt = State_Int_AT5G49770_NRT2p1(inpDat, lOInt = lOIntSt, lPAs = lPAsSt)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class State(Base):
    def __init__(self, inpDat, iTp = 90, lOInt = [], lPAs = []):
        super().__init__(inpDat, iTp = iTp)
        assert len(lOInt) >= 2
        self.idO = 'Sta'
        self.descO = 'State'
        self.lOI = lOInt
        self.lPs = lPAs
        print('Initiated "State" object.')

class State_Int_AT5G49770_NRT2p1(State):
    def __init__(self, inpDat, iTp = 90, lOInt = [], lPAs = []):
        assert len(lOInt) == 2 and len(lPAs) >= 4
        super().__init__(inpDat, iTp = iTp, lOInt = lOInt, lPAs = lPAs)
        KinaseAT5G49770, NRT2p1 = self.lOI
        self.idO = 'St_Int_AT5G49770_NRT2p1'
        self.descO = 'State interaction AT5G49770-NRT2p1'
        self.adaptPSites_AT5G49770(inpDat, KinaseAT5G49770)
        self.adaptPSites_NRT2p1(inpDat, NRT2p1)
        print('Initiated "State_Int_AT5G49770_NRT2p1" object.')
        
    def adaptPSites_AT5G49770(self, inpDat, cOKin):
        lOIP1, sSpS = [cOKin, self.lPs[0]], 'S839'
        isSucc = Dephosphorylation(inpDat, lOInt = lOIP1,
                                   sSpSite = sSpS).doDePyl()
        print('Dephosphorylation at site', sSpS, 'happened:', isSucc)
        lOIP2, sSpS = [cOKin, self.lPs[1]], 'S870'
        isSucc = Phosphorylation(inpDat, lOInt = lOIP2,
                                 sSpSite = sSpS).doPyl()
        print('Phosphorylation at site', sSpS, 'happened:', isSucc)
        
    def adaptPSites_NRT2p1(self, inpDat, cOProt):
        lOIP3, sSpS = [cOProt, self.lPs[2]], 'S21'
        isSucc = Phosphorylation(inpDat, lOInt = lOIP3,
                                 sSpSite = sSpS).doPyl()
        print('Phosphorylation at site', sSpS, 'happened:', isSucc)
        lOIP4, sSpS = [cOProt, self.lPs[3]], 'S28'
        isSucc = Dephosphorylation(inpDat, lOInt = lOIP4,
                                   sSpSite = sSpS).doDePyl()
        print('Dephosphorylation at site', sSpS, 'happened:', isSucc)

###############################################################################
