# -*- coding: utf-8 -*-
###############################################################################
# --- O_03__Metabolite.py -----------------------------------------------------
###############################################################################
import numpy as np

import Core.C_00__GenConstants as GC

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
        self.setIniConc()
        print('Initiated "SmallMolecule" object.')
    
    def setIniConc(self):
        self.stCnc = self.dITp['concIni']
        self.sCncCh = self.dITp['mdConcCh']
        self.perCncCh = self.dITp['perConcCh']
        self.amplCncCh = self.dITp['amplConcCh']
        self.cCnc = self.dITp['concIni']

    def changeConc(self, cTS):
        if self.sCncCh == GC.S_CH_SIN:
            self.cCnc = (self.stCnc +
                         self.amplCncCh*np.sin(cTS*2*np.pi/self.perCncCh))

class SMo_NO3_1m(SmallMolecule):
    def __init__(self, inpDat, iTp = 501, dStat = {}):
        super().__init__(inpDat, iTp, dStat)
        self.idO = 'NO3_1m'
        self.descO = 'Small molecule NO3-'
        self.createDSpecSites(self.dITp['dInfSpS'])
        print('Initiated "SMo_NO3_1m" object.')
    
class SMo_H2PO4_1m(SmallMolecule):
    def __init__(self, inpDat, iTp = 502, dStat = {}):
        super().__init__(inpDat, iTp, dStat)
        self.idO = 'H2PO4_1m'
        self.descO = 'Small molecule H2PO4-'
        self.createDSpecSites(self.dITp['dInfSpS'])
        print('Initiated "SMo_H2PO4_1m" object.')

###############################################################################
