# -*- coding: utf-8 -*-
###############################################################################
# --- O_02__Protein.py --------------------------------------------------------
###############################################################################
import Core.C_00__GenConstants as GC

from Core.O_01__Molecule import Molecule

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class Protein(Molecule):
    def __init__(self, inpDat, iTp, sPat01 = GC.S_4DASH, dStat = {}):
        super().__init__(inpDat, iTp, sPat01)
        self.idO = GC.ID_PRO
        self.descO = 'Protein'
        # set the phosphorylation status
        for sSpS in dStat:
            if sSpS in self.dITp:
                self.dITp[sSpS][GC.S_STAT] = dStat[sSpS]
        # print('Initiated "Protein" object.')

class LargeProtein(Protein):
    def __init__(self, inpDat, iTp, sPat01 = GC.S_4DASH, dStat = {}):
        super().__init__(inpDat, iTp, sPat01, dStat)
        self.idO = GC.ID_LPR
        self.descO = 'Large protein'
        # print('Initiated "LargeProtein" object.')

class Protein_NRT2p1(LargeProtein):
    def __init__(self, inpDat, iTp = 21, sPat01 = GC.S_4DASH,
                 dStat = {GC.S_SPS_L_S21: GC.S_IS_PYL,
                          GC.S_SPS_L_S28: GC.S_NOT_PYL}):
        super().__init__(inpDat, iTp, sPat01, dStat)
        self.idO = GC.ID_LPR_NRT2P1
        self.descO = 'Large protein NRT2.1'
        self.createDSpecSites()
        # print('Initiated "Protein_NRT2p1" object.')

class SmallProtein(Protein):
    def __init__(self, inpDat, iTp, sPat01 = GC.S_4DASH, dStat = {}):
        super().__init__(inpDat, iTp, sPat01, dStat)
        self.idO = GC.ID_SPR
        self.descO = 'Small protein'
        # print('Initiated "SmallProtein" object.')

class Protein_NAR2p1(SmallProtein):
    def __init__(self, inpDat, iTp = 31, sPat01 = GC.S_4DASH, dStat = {}):
        super().__init__(inpDat, iTp, sPat01, dStat)
        self.idO = GC.ID_SPR_NAR2P1
        self.descO = 'Small protein NAR2.1'
        self.createDSpecSites()
        # print('Initiated "Protein_NAR2p1" object.')

class Enzyme(Protein):
    def __init__(self, inpDat, iTp, sPat01 = GC.S_4DASH, dStat = {}):
        super().__init__(inpDat, iTp, sPat01, dStat)
        self.idO = GC.ID_ENZ
        self.descO = 'Enzyme'
        # print('Initiated "Enzyme" object.')

class Kinase(Enzyme):
    def __init__(self, inpDat, iTp, sPat01 = GC.S_4DASH, dStat = {}):
        super().__init__(inpDat, iTp, sPat01, dStat)
        self.idO = GC.ID_KAS
        self.descO = 'Kinase'
        # print('Initiated "Kinase" object.')

class KinaseK(Kinase):
    def __init__(self, inpDat, iTp = 41, sPat01 = GC.S_4DASH,
                 dStat = {GC.S_SPS_K_S839: GC.S_NOT_PYL,
                          GC.S_SPS_K_S870: GC.S_IS_PYL}):
        super().__init__(inpDat, iTp, sPat01, dStat)
        self.idO = GC.ID_KAS_K
        self.descO = 'Kinase K (HPCAL1)'
        self.createDSpecSites()
        # print('Initiated "KinaseK" object.')

class KinaseX(Kinase):
    def __init__(self, inpDat, iTp = 42, sPat01 = GC.S_4DASH, dStat = {}):
        super().__init__(inpDat, iTp, sPat01, dStat)
        self.idO = GC.ID_KAS_X
        self.descO = 'Kinase X'
        self.createDSpecSites()
        # print('Initiated "KinaseX" object.')

class KinaseY(Kinase):
    def __init__(self, inpDat, iTp = 43, sPat01 = GC.S_4DASH, dStat = {}):
        super().__init__(inpDat, iTp, sPat01, dStat)
        self.idO = GC.ID_KAS_Y
        self.descO = 'Kinase Y'
        self.createDSpecSites()
        # print('Initiated "KinaseY" object.')

class Phosphatase(Enzyme):
    def __init__(self, inpDat, iTp, sPat01 = GC.S_4DASH, dStat = {}):
        super().__init__(inpDat, iTp, sPat01, dStat)
        self.idO = GC.ID_PAS
        self.descO = 'Phosphatase'
        # print('Initiated "Phosphatase" object.')

class PhosphataseA(Phosphatase):
    def __init__(self, inpDat, iTp = 51, sPat01 = GC.S_4DASH, dStat = {}):
        super().__init__(inpDat, iTp, sPat01, dStat)
        self.idO = GC.ID_PAS_A
        self.descO = 'Phosphatase A'
        self.createDSpecSites()
        # print('Initiated "PhosphataseA" object.')

class PhosphataseB(Phosphatase):
    def __init__(self, inpDat, iTp = 52, sPat01 = GC.S_4DASH, dStat = {}):
        super().__init__(inpDat, iTp, sPat01, dStat)
        self.idO = GC.ID_PAS_B
        self.descO = 'Phosphatase B'
        self.createDSpecSites()
        # print('Initiated "PhosphataseB" object.')

class PhosphataseC(Phosphatase):
    def __init__(self, inpDat, iTp = 53, sPat01 = GC.S_4DASH, dStat = {}):
        super().__init__(inpDat, iTp, sPat01, dStat)
        self.idO = GC.ID_PAS_C
        self.descO = 'Phosphatase C'
        self.createDSpecSites()
        # print('Initiated "PhosphataseC" object.')

class PhosphataseD(Phosphatase):
    def __init__(self, inpDat, iTp = 54, sPat01 = GC.S_4DASH, dStat = {}):
        super().__init__(inpDat, iTp, sPat01, dStat)
        self.idO = GC.ID_PAS_D
        self.descO = 'Phosphatase D'
        self.createDSpecSites()
        # print('Initiated "PhosphataseD" object.')

###############################################################################
