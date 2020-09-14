# -*- coding: utf-8 -*-
###############################################################################
# --- O_01__Protein.py --------------------------------------------------------
###############################################################################
import Core.F_00__GenFunctions as GF

from Core.O_00__Molecule import Molecule

class Protein(Molecule):
    def __init__(self, inpDat, iTp):
        super().__init__(inpDat, iTp)
        self.idO = 'Pro'
        self.descO = 'Protein'
        self.dIG = inpDat.dI
        self.dITp = {}  # !!!
        self.cM = self.dIG['Mode']
#        GF.seedRNG(self.cM)
        print('Initiated "Protein" base object.')

class Enzyme(Protein):
    def __init__(self, inpDat, iTp):
        super().__init__(inpDat, iTp)
        self.idO = 'Enz'
        self.descO = 'Enzyme'
        self.dITp = self.dIG[iTp]
        print('Initiated "Enzyme" base object.')

class Kinase(Enzyme):
    def __init__(self, inpDat, iTp):
        super().__init__(inpDat, iTp)
        self.idO = 'KAs'
        self.descO = 'Kinase'
        print('Initiated "Kinase" base object.')

class Phosphatase(Enzyme):
    def __init__(self, inpDat, iTp):
        super().__init__(inpDat, iTp)
        self.idO = 'PAs'
        self.descO = 'Phosphatase'
        print('Initiated "Phosphatase" base object.')

class LargeProtein(Protein):
    def __init__(self, inpDat, iTp):
        super().__init__(inpDat, iTp)
        self.idO = 'LPr'
        self.descO = 'Large protein'
        self.dITp = self.dIG[iTp]
        print('Initiated "Large protein" base object.')

class SmallProtein(Protein):
    def __init__(self, inpDat, iTp):
        super().__init__(inpDat, iTp)
        self.idO = 'SPr'
        self.descO = 'Small protein'
        self.dITp = self.dIG[iTp]
        print('Initiated "Small protein" base object.')

###############################################################################
