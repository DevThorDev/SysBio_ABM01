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
        self.idO = 'Pro'
        self.descO = 'Protein'
        # set the phosphorylation status
        for sSpS in dStat:
            if sSpS in self.dITp:
                self.dITp[sSpS]['Stat'] = dStat[sSpS]
        # print('Initiated "Protein" object.')

class LargeProtein(Protein):
    def __init__(self, inpDat, iTp, dStat = {}):
        super().__init__(inpDat, iTp, dStat)
        self.idO = 'LPr'
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
        self.idO = 'SPr'
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
        self.idO = 'Enz'
        self.descO = 'Enzyme'
        # print('Initiated "Enzyme" object.')

class Kinase(Enzyme):
    def __init__(self, inpDat, iTp, dStat = {}):
        super().__init__(inpDat, iTp, dStat)
        self.idO = 'KAs'
        self.descO = 'Kinase'
        # print('Initiated "Kinase" object.')

class Kinase_HPCAL1(Kinase):
    def __init__(self, inpDat, iTp = 41, dStat = {'S839': GC.S_NOT_PYL,
                                                  'S870': GC.S_IS_PYL}):
        super().__init__(inpDat, iTp, dStat)
        self.idO = GC.ID_KAS_HPCAL1
        self.descO = 'Kinase HPCAL1'
        self.createDSpecSites()
        # print('Initiated "Kinase_HPCAL1" object.')

class Kinase_X(Kinase):
    def __init__(self, inpDat, iTp = 44, dStat = {}):
        super().__init__(inpDat, iTp, dStat)
        self.idO = GC.ID_KAS_X
        self.descO = 'Kinase X'
        self.createDSpecSites()
        # print('Initiated "Kinase_X" object.')

class Kinase0(Kinase):
    def __init__(self, inpDat, cID, iTp = 45, dStat = {}):
        super().__init__(inpDat, iTp, dStat)
        self.idO = cID
        self.descO = 'Kinase 0'
        self.createDSpecSites()
        # print('Initiated "Kinase0" object.')

class Phosphatase(Enzyme):
    def __init__(self, inpDat, iTp, dStat = {}):
        super().__init__(inpDat, iTp, dStat)
        self.idO = 'PAs'
        self.descO = 'Phosphatase'
        # print('Initiated "Phosphatase" object.')

class Phosphatase0(Phosphatase):
    def __init__(self, inpDat, cID, iTp = 55, dStat = {}):
        super().__init__(inpDat, iTp, dStat)
        self.idO = cID
        self.descO = 'Phosphatase 0'
        self.createDSpecSites()
        # print('Initiated "Phosphatase0" object.')

###############################################################################
