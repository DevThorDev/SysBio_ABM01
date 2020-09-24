# -*- coding: utf-8 -*-
###############################################################################
# --- O_03__Metabolite.py -----------------------------------------------------
###############################################################################
# import Core.F_00__GenFunctions as GF

from Core.O_01__Molecule import Molecule

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class Metabolite(Molecule):
    def __init__(self, inpDat, iTp, dStat = {}):
        super().__init__(inpDat, iTp)
        self.idO = 'Met'
        self.descO = 'Metabolite'
        print('Initiated "Metabolite" object.')

class LargeMolecule(Metabolite):
    def __init__(self, inpDat, iTp, dStat = {}):
        super().__init__(inpDat, iTp, dStat)
        self.idO = 'LMo'
        self.descO = 'Large molecule'
        print('Initiated "LargeMolecule" object.')

class SmallMolecule(Metabolite):
    def __init__(self, inpDat, iTp, dStat = {}):
        super().__init__(inpDat, iTp, dStat)
        self.idO = 'SMo'
        self.descO = 'Small molecule'
        print('Initiated "SmallMolecule" object.')

class SMo_NO3_1m(SmallMolecule):
    def __init__(self, inpDat, iTp = 501, dStat = {}):
        super().__init__(inpDat, iTp, dStat)
        self.idO = 'NO3_1m'
        self.descO = 'Small molecule NO3-'
        self.createDSpecSites(self.dITp['dInfSpS'])
        print('Initiated "SMo_NO3_1m" object.')

class SMo_H2PO4_1m(SmallMolecule):
    def __init__(self, inpDat, iTp = 501, dStat = {}):
        super().__init__(inpDat, iTp, dStat)
        self.idO = 'H2PO4_1m'
        self.descO = 'Small molecule H2PO4-'
        self.createDSpecSites(self.dITp['dInfSpS'])
        print('Initiated "SMo_H2PO4_1m" object.')

###############################################################################
