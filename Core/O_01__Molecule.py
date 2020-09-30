# -*- coding: utf-8 -*-
###############################################################################
# --- O_01__Molecule.py -------------------------------------------------------
###############################################################################
from Core.O_00__Base import Base

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class Molecule(Base):
    def __init__(self, inpDat, iTp, lITpU = [0, 1]):
        super().__init__(inpDat, iTp, lITpU = lITpU)
        self.idO = 'Mol'
        self.descO = 'Molecule'
        print('Initiated "Molecule" object.')

    def __str__(self):
        sIn = ('-- Molecule ' + self.idO + ' (' + self.descO + ')')
        return sIn

    def createDSpecSites(self, dInSpS):
        self.nSpS = len(self.dITp['dInfSpS'])   # number of "special sites"
        self.dSpS = {}
        for sSpS in dInSpS:
            self.dSpS[sSpS] = SpecSite(dInSpS, sSpS, self.idO, self.descO)
    
    def extractLSpecSitesS(self):
        lTInf = []
        for cSpS in self.dSpS.values():
            lTInf.append((cSpS.idSpS, cSpS.sSPTM))
        return lTInf
    
    def printSpecSites(self):
        if len(self.dSpS) > 0:
            # print('-'*1 + ' Special sites: ' + '-'*24)
            for cSpS in self.dSpS.values():
                print(cSpS)
    
    def printMolSpecSites(self):
        print(self)
        self.printSpecSites()

class SpecSite:
    def __init__(self, dInSpS, sIDSpS, idMol, descMol):
        self.idSpS = sIDSpS                         # ID string of site
        self.sSPTM = dInSpS[self.idSpS]['Stat']     # status of PTM ('P-',...)
        self.lPyl = dInSpS[self.idSpS]['Pyl']       # list of Pyl agents
        self.lDePyl = dInSpS[self.idSpS]['DePyl']   # list of DePyl agents
        self.idMol = idMol                          # ID of molecule
        self.descMol = descMol                      # description of molecule

    def __str__(self):
        sIn = ('- Special site ' +  self.idSpS + ' of molecule ' + self.idMol +
               ' (' + self.descMol + ') with PTM ' + str(self.sSPTM) +
               ' has phosphorylation agents ' + str(self.lPyl) +
               ' and dephosphorylation agents ' + str(self.lDePyl) + '.')
        return sIn

###############################################################################
