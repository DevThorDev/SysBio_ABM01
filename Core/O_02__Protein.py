# -*- coding: utf-8 -*-
###############################################################################
# --- O_02__Protein.py --------------------------------------------------------
###############################################################################
import Core.C_00__GenConstants as GC
# import Core.F_00__GenFunctions as GF

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
        print('Initiated "Protein" object.')

class Enzyme(Protein):
    def __init__(self, inpDat, iTp, dStat = {}):
        super().__init__(inpDat, iTp, dStat)
        self.idO = 'Enz'
        self.descO = 'Enzyme'
        print('Initiated "Enzyme" object.')

class Kinase(Enzyme):
    def __init__(self, inpDat, iTp, dStat = {}):
        super().__init__(inpDat, iTp, dStat)
        self.idO = 'KAs'
        self.descO = 'Kinase'
        print('Initiated "Kinase" object.')

class Kinase_AT5G49770(Kinase):
    def __init__(self, inpDat, iTp = 101, dStat = {'S839': GC.B_NOT_PYL,
                                                   'S870': GC.B_IS_PYL}):
        super().__init__(inpDat, iTp, dStat)
        self.idO = 'KAs_AT5G49770'
        self.descO = 'Kinase AT5G49770'
        self.createDSpecSites(self.dITp['dInfSpS'])
        print('Initiated "Kinase_AT5G49770" object.')

class Kinase_X(Kinase):
    def __init__(self, inpDat, iTp = 102, dStat = {}):
        super().__init__(inpDat, iTp, dStat)
        self.idO = 'KAs_X'
        self.descO = 'Kinase X'
        self.createDSpecSites(self.dITp['dInfSpS'])
        print('Initiated "Kinase_X" object.')

class Phosphatase(Enzyme):
    def __init__(self, inpDat, iTp, dStat = {}):
        super().__init__(inpDat, iTp, dStat)
        self.idO = 'PAs'
        self.descO = 'Phosphatase'
        print('Initiated "Phosphatase" object.')

class Phosphatase1(Phosphatase):
    def __init__(self, inpDat, iTp = 151, dStat = {}):
        super().__init__(inpDat, iTp, dStat)
        self.idO = 'PAs1'
        self.descO = 'Phosphatase1'
        self.createDSpecSites(self.dITp['dInfSpS'])
        print('Initiated "Phosphatase1" object.')

class Phosphatase2(Phosphatase):
    def __init__(self, inpDat, iTp = 152, dStat = {}):
        super().__init__(inpDat, iTp, dStat)
        self.idO = 'PAs2'
        self.descO = 'Phosphatase2'
        self.createDSpecSites(self.dITp['dInfSpS'])
        print('Initiated "Phosphatase2" object.')

class Phosphatase3(Phosphatase):
    def __init__(self, inpDat, iTp = 153, dStat = {}):
        super().__init__(inpDat, iTp, dStat)
        self.idO = 'PAs3'
        self.descO = 'Phosphatase3'
        self.createDSpecSites(self.dITp['dInfSpS'])
        print('Initiated "Phosphatase3" object.')

class Phosphatase4(Phosphatase):
    def __init__(self, inpDat, iTp = 154, dStat = {}):
        super().__init__(inpDat, iTp, dStat)
        self.idO = 'PAs4'
        self.descO = 'Phosphatase4'
        self.createDSpecSites(self.dITp['dInfSpS'])
        print('Initiated "Phosphatase4" object.')

class LargeProtein(Protein):
    def __init__(self, inpDat, iTp, dStat = {}):
        super().__init__(inpDat, iTp, dStat)
        self.idO = 'LPr'
        self.descO = 'Large protein'
        print('Initiated "LargeProtein" object.')

class Protein_NRT2p1(LargeProtein):
    def __init__(self, inpDat, iTp = 201, dStat = {'S21': GC.B_IS_PYL,
                                                   'S28': GC.B_NOT_PYL}):
        super().__init__(inpDat, iTp, dStat)
        self.idO = 'LPr_NRT2p1'
        self.descO = 'Large protein NRT2.1'
        self.createDSpecSites(self.dITp['dInfSpS'])
        print('Initiated "Protein_NRT2p1" object.')

class SmallProtein(Protein):
    def __init__(self, inpDat, iTp, dStat = {}):
        super().__init__(inpDat, iTp, dStat)
        self.idO = 'SPr'
        self.descO = 'Small protein'
        print('Initiated "SmallProtein" object.')

class Protein_NAR2p1(SmallProtein):
    def __init__(self, inpDat, iTp = 301, dStat = {}):
        super().__init__(inpDat, iTp, dStat)
        self.idO = 'SPr_NAR2p1'
        self.descO = 'Small protein NAR2.1'
        self.createDSpecSites(self.dITp['dInfSpS'])
        print('Initiated "Protein_NAR2p1" object.')

###############################################################################
