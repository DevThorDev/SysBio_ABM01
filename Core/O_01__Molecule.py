# -*- coding: utf-8 -*-
###############################################################################
# --- O_01__Molecule.py -------------------------------------------------------
###############################################################################
import pprint

import Core.F_00__GenFunctions as GF

from Core.O_00__Base import Base

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class SpecSite:
    def __init__(self, dInSpS, sIDSpS):
        self.idSpS = sIDSpS                         # ID string of site
        self.sSPTM = dInSpS[self.idSpS]['Stat']     # status of PTM ('P-',...)
        self.lPyl = dInSpS[self.idSpS]['Pyl']       # list of Pyl agents
        self.lDePyl = dInSpS[self.idSpS]['DePyl']   # list of DePyl agents

    def __str__(self):
        sIn = ('Special site ' +  self.idSpS + ' with PTM ' + str(self.sSPTM) +
               ' has phosphorylation agents ' + str(self.lPyl) +
               ' and dephosphorylation agents ' + str(self.lDePyl) + '.')
        return sIn

class Molecule(Base):
    def __init__(self, inpDat, iTp):
        super().__init__(inpDat, iTp)
        self.idO = 'Mol'
        self.descO = 'Molecule'
        self.nSpS = len(self.dITp['dInfSpS'])   # number of "special sites"
        self.createDSpecSites(self.dITp['dInfSpS'])
        print('Initiated "Molecule" base object.')

    def createDSpecSites(self, dInSpS):
        self.dSpS = {}
        for sSpS in dInSpS:
            self.dSpS[sSpS] = SpecSite(dInSpS, sSpS)
    
    def extractLSpecSitesS(self):
        lTInf = []
        for cSpS in self.dSpS.values():
            lTInf.append((cSpS.idSpS, cSpS.sSPTM))
        return lTInf
            
    
    def printDSpecSites(self):
        print('-'*24 + ' Special sites: ' + '-'*24)
        for cSpS in self.dSpS.values():
            print(cSpS)

###############################################################################
