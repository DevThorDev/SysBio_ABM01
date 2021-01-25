# -*- coding: utf-8 -*-
###############################################################################
# --- O_03__Metabolite.py -----------------------------------------------------
###############################################################################
import Core.C_00__GenConstants as GC

from Core.O_01__Molecule import Molecule

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class Metabolite(Molecule):
    def __init__(self, inpDat, iTp, dStat={}):
        super().__init__(inpDat, iTp)
        self.idO = GC.ID_MET
        self.descO = 'Metabolite'
        # print('Initiated "Metabolite" object.')

    def setConc(self, cConc=0.0):
        self.cCnc = cConc

    def __str__(self):
        sIn = ('-- Metabolite ' + self.idO + ' (' + self.descO + ') has a co' +
               'ncentration of ' + str(round(self.cCnc, GC.R04)) + ' mMol/L.')
        return sIn

class LargeMolecule(Metabolite):
    def __init__(self, inpDat, iTp, dStat={}):
        super().__init__(inpDat, iTp, dStat)
        self.idO = GC.ID_LMO
        self.descO = 'Large molecule'
        # print('Initiated "LargeMolecule" object.')

class SmallMolecule(Metabolite):
    def __init__(self, inpDat, iTp, dStat={}):
        super().__init__(inpDat, iTp, dStat)
        self.idO = GC.ID_SMO
        self.descO = 'Small molecule'
        # print('Initiated "SmallMolecule" object.')

class SMo_NO3_1m(SmallMolecule):
    def __init__(self, inpDat, iTp=61, dStat={}):
        super().__init__(inpDat, iTp, dStat)
        self.idO = GC.ID_NO3_1M
        self.descO = 'Small molecule NO3-'
        self.createDSpecSites()
        # print('Initiated "SMo_NO3_1m" object.')

class SMo_H2PO4_1m(SmallMolecule):
    def __init__(self, inpDat, iTp=62, dStat={}):
        super().__init__(inpDat, iTp, dStat)
        self.idO = GC.ID_H2PO4_1M
        self.descO = 'Small molecule H2PO4-'
        self.createDSpecSites()
        # print('Initiated "SMo_H2PO4_1m" object.')

###############################################################################
