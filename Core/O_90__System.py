# -*- coding: utf-8 -*-
###############################################################################
# --- O_90__System.py ---------------------------------------------------------
###############################################################################
import pprint

# import Core.C_00__GenConstants as GC
# import Core.F_00__GenFunctions as GF
import Core.F_03__OTpFunctions as TF

from Core.O_00__Base import Base

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class System(Base):
    def __init__(self, inpDat, iTp, lOSys):
        super().__init__(inpDat, iTp)
        self.idO = 'Sys'
        self.descO = 'System'
        self.lOS = lOSys
        self.lMol = [cO for cO in self.lOS if cO.idO == 'Mol']
        self.lPro = [cO for cO in self.lOS if cO.idO == 'Pro']
        self.lEnz = [cO for cO in self.lOS if cO.idO == 'Enz']
        self.lKAs = [cO for cO in self.lOS if cO.idO == 'KAs']
        self.lPAs = [cO for cO in self.lOS if cO.idO == 'PAs']
        self.lLPr = [cO for cO in self.lOS if cO.idO == 'LPr']
        self.lSPr = [cO for cO in self.lOS if cO.idO == 'SPr']
        self.lMet = [cO for cO in self.lOS if cO.idO == 'Met']
        self.lLMo = [cO for cO in self.lOS if cO.idO == 'LMo']
        self.lSMo = [cO for cO in self.lOS if cO.idO == 'SMo']
        self.lInt = [cO for cO in self.lOS if cO.idO == 'Int']
        self.lPyl = [cO for cO in self.lOS if cO.idO == 'Pyl']
        self.lDePyl = [cO for cO in self.lOS if cO.idO == 'DePyl']
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
        print('Initiated "System" base object.')
    
    def printSystem(self):
        print('+'*16, 'System consists of:', '+'*43)
        for s, lCmp in self.dCmp.items():
            if len(lCmp) > 0:
                TF.printSysComp(s, lCmp)
        print('+'*80)

###############################################################################
