# -*- coding: utf-8 -*-
###############################################################################
# --- O_01__Molecule.py -------------------------------------------------------
###############################################################################
import Core.C_00__GenConstants as GC

from Core.O_00__Base import Base

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class Molecule(Base):
    def __init__(self, inpDat, iTp, sPat01 = GC.S_4DASH, lITpU = [0, 1]):
        super().__init__(inpDat, iTp, sPat01, lITpU = lITpU)
        self.idO = GC.ID_MOL
        self.descO = 'Molecule'
        # print('Initiated "Molecule" object.')

    def __str__(self):
        sIn = ('-- Molecule ' + self.idO + ' (' + self.descO + ')')
        return sIn

    def createDSpecSites(self):
        self.nSpS = len(self.dITp['dInfSpS'])   # number of "special sites"
        self.dSpS = {}
        for sSpS in self.dITp['dInfSpS']:
            self.dSpS[sSpS] = SpecSite(self.dITp['dInfSpS'], sSpS, self.idO,
                                       self.descO)

    def extractLSpecSitesS(self):
        lTInf = []
        for cSpS in self.dSpS.values():
            lTInf.append((cSpS.idSpS, cSpS.sSPTM))
        return lTInf

    def printSpecSites(self):
        if len(self.dSpS) > 0:
            for cSpS in self.dSpS.values():
                print(cSpS)

    def printMolSpecSites(self):
        print(self)
        self.printSpecSites()

class SpecSite:
    def __init__(self, dISpS, sIDSpS, idMol, descMol):
        self.idSpS = sIDSpS                         # ID string of site
        self.sSPTM = dISpS[self.idSpS][GC.S_STAT]   # status of PTM ('P-',...)
        self.lPyl = dISpS[self.idSpS][GC.S_DO_PYL]  # list Pyl agents
        self.lDPy = dISpS[self.idSpS][GC.S_DO_DPY]  # list DPy agents
        self.idMol = idMol                          # ID of molecule
        self.descMol = descMol                      # description of molecule

    def __str__(self):
        sIn = ('- Special site ' +  self.idSpS + ' of molecule ' + self.idMol +
               ' (' + self.descMol + ') with PTM ' + str(self.sSPTM) +
               ' has phosphorylation agents ' + str(self.lPyl) +
               ' and dephosphorylation agents ' + str(self.lDPy) + '.')
        return sIn

###############################################################################
