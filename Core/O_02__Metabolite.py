# -*- coding: utf-8 -*-
###############################################################################
# --- O_02__Metabolite.py -----------------------------------------------------
###############################################################################
import Core.F_00__GenFunctions as GF

from Core.O_00__Molecule import Molecule

class Metabolite(Molecule):
    def __init__(self, inpDat, iTp):
        super().__init__(inpDat, iTp)
        self.idO = 'Met'
        self.descO = 'Metabolite'
        self.dIG = inpDat.dI
#        self.dITp = {}
        self.cM = self.dIG['Mode']
#        GF.seedRNG(self.cM)
        print('Initiated "Metabolite" base object.')

class LargeMolecule(Metabolite):
    def __init__(self, inpDat, iTp):
        super().__init__(inpDat, iTp)
        self.idO = 'LMo'
        self.descO = 'Large molecule'
#        self.dITp = self.dIG[iTp]
        print('Initiated "Large molecule" base object.')

class SmallMolecule(Metabolite):
    def __init__(self, inpDat, iTp):
        super().__init__(inpDat, iTp)
        self.idO = 'SMo'
        self.descO = 'Small molecule'
        print('Initiated "Small molecule" base object.')

###############################################################################
