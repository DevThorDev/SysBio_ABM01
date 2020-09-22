# -*- coding: utf-8 -*-
###############################################################################
# --- O_03__Metabolite.py -----------------------------------------------------
###############################################################################
import Core.F_00__GenFunctions as GF

from Core.O_01__Molecule import Molecule

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class Metabolite(Molecule):
    def __init__(self, inpDat, iTp):
        super().__init__(inpDat, iTp)
        self.idO = 'Met'
        self.descO = 'Metabolite'
        print('Initiated "Metabolite" object.')

class LargeMolecule(Metabolite):
    def __init__(self, inpDat, iTp):
        super().__init__(inpDat, iTp)
        self.idO = 'LMo'
        self.descO = 'Large molecule'
        print('Initiated "Large molecule" object.')

class SmallMolecule(Metabolite):
    def __init__(self, inpDat, iTp):
        super().__init__(inpDat, iTp)
        self.idO = 'SMo'
        self.descO = 'Small molecule'
        print('Initiated "Small molecule" object.')

###############################################################################
