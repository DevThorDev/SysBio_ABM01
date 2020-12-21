# -*- coding: utf-8 -*-
###############################################################################
# --- O_02__Protein.py --------------------------------------------------------
###############################################################################
import Core.C_00__GenConstants as GC

from Core.O_01__Molecule import Molecule

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class Protein(Molecule):
    def __init__(self, inpDat, iTp, dStat = {}):
        super().__init__(inpDat, iTp)
        self.idO = GC.ID_PRO
        self.descO = 'Protein'
        # set the phosphorylation status
        for sSpS in dStat:
            if sSpS in self.dITp:
                self.dITp[sSpS]['Stat'] = dStat[sSpS]
        # print('Initiated "Protein" object.')

class LargeProtein(Protein):
    def __init__(self, inpDat, iTp, dStat = {}):
        super().__init__(inpDat, iTp, dStat)
        self.idO = GC.ID_LPR
        self.descO = 'Large protein'
        # print('Initiated "LargeProtein" object.')

class Protein_NRT2p1(LargeProtein):
    def __init__(self, inpDat, iTp = 21, dStat = {'S21': GC.S_IS_PYL,
                                                  'S28': GC.S_NOT_PYL}):
        super().__init__(inpDat, iTp, dStat)
        self.idO = GC.ID_LPR_NRT2P1
        self.descO = 'Large protein NRT2.1'
        self.createDSpecSites()
        # print('Initiated "Protein_NRT2p1" object.')

class SmallProtein(Protein):
    def __init__(self, inpDat, iTp, dStat = {}):
        super().__init__(inpDat, iTp, dStat)
        self.idO = GC.ID_SPR
        self.descO = 'Small protein'
        # print('Initiated "SmallProtein" object.')

class Protein_NAR2p1(SmallProtein):
    def __init__(self, inpDat, iTp = 31, dStat = {}):
        super().__init__(inpDat, iTp, dStat)
        self.idO = GC.ID_SPR_NAR2P1
        self.descO = 'Small protein NAR2.1'
        self.createDSpecSites()
        # print('Initiated "Protein_NAR2p1" object.')

class Enzyme(Protein):
    def __init__(self, inpDat, iTp, dStat = {}):
        super().__init__(inpDat, iTp, dStat)
        self.idO = GC.ID_ENZ
        self.descO = 'Enzyme'
        # print('Initiated "Enzyme" object.')

class Kinase(Enzyme):
    def __init__(self, inpDat, iTp, dStat = {}):
        super().__init__(inpDat, iTp, dStat)
        self.idO = GC.ID_KAS
        self.descO = 'Kinase'
        # print('Initiated "Kinase" object.')

class KinaseHPCAL1(Kinase):
    def __init__(self, inpDat, iTp = 41, dStat = {'S839': GC.S_NOT_PYL,
                                                  'S870': GC.S_IS_PYL}):
        super().__init__(inpDat, iTp, dStat)
        self.idO = GC.ID_KAS_HPCAL1
        self.descO = 'Kinase HPCAL1'
        self.createDSpecSites()
        # print('Initiated "KinaseHPCAL1" object.')

class KinaseX(Kinase):
    def __init__(self, inpDat, iTp = 42, dStat = {}):
        super().__init__(inpDat, iTp, dStat)
        self.idO = GC.ID_KAS_X
        self.descO = 'Kinase X'
        self.createDSpecSites()
        # print('Initiated "KinaseX" object.')

class KinaseY(Kinase):
    def __init__(self, inpDat, iTp = 43, dStat = {}):
        super().__init__(inpDat, iTp, dStat)
        self.idO = GC.ID_KAS_Y
        self.descO = 'Kinase Y'
        self.createDSpecSites()
        # print('Initiated "KinaseY" object.')

class Phosphatase(Enzyme):
    def __init__(self, inpDat, iTp, dStat = {}):
        super().__init__(inpDat, iTp, dStat)
        self.idO = GC.ID_PAS
        self.descO = 'Phosphatase'
        # print('Initiated "Phosphatase" object.')

class Phosphatase1(Phosphatase):
    def __init__(self, inpDat, iTp = 51, dStat = {}):
        super().__init__(inpDat, iTp, dStat)
        self.idO = GC.ID_PAS_1
        self.descO = 'Phosphatase 1'
        self.createDSpecSites()
        # print('Initiated "Phosphatase1" object.')

class Phosphatase2(Phosphatase):
    def __init__(self, inpDat, iTp = 52, dStat = {}):
        super().__init__(inpDat, iTp, dStat)
        self.idO = GC.ID_PAS_2
        self.descO = 'Phosphatase 2'
        self.createDSpecSites()
        # print('Initiated "Phosphatase2" object.')

class Phosphatase3(Phosphatase):
    def __init__(self, inpDat, iTp = 53, dStat = {}):
        super().__init__(inpDat, iTp, dStat)
        self.idO = GC.ID_PAS_3
        self.descO = 'Phosphatase 3'
        self.createDSpecSites()
        # print('Initiated "Phosphatase3" object.')

class Phosphatase4(Phosphatase):
    def __init__(self, inpDat, iTp = 54, dStat = {}):
        super().__init__(inpDat, iTp, dStat)
        self.idO = GC.ID_PAS_4
        self.descO = 'Phosphatase 4'
        self.createDSpecSites()
        # print('Initiated "Phosphatase4" object.')

###############################################################################
