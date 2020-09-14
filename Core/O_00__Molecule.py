# -*- coding: utf-8 -*-
###############################################################################
# --- O_00__Molecule.py -------------------------------------------------------
###############################################################################
import pprint

import Core.F_00__GenFunctions as GF

class SpecSite:
    def __init__(self, tInSpS):
        assert len(tInSpS) >= 2
        self.idSpS = tInSpS[0]
        self.stPTM = tInSpS[1]      # status of PTM ('P-', 'P+',...)

    def __str__(self):
        sIn = ('Special site ' +  self.idSpS + ' with PTM ' + str(self.stPTM))
        return sIn

class Molecule:
    def __init__(self, inpDat, iTp):
        self.idO = 'Mol'
        self.descO = 'Molecule'
        self.dIG = inpDat.dI
        self.dITp = self.dIG[iTp]
        self.cM = self.dIG['Mode']
        self.nSpS = len(self.dITp['lInfSpS'])   # number of "special sites"
        self.createLSpecSites(self.dITp['lInfSpS'])
#        GF.seedRNG(self.cM)
        print('Initiated "Molecule" base object.')

    def __str__(self):
        sIn = ('~'*24 + ' ' + self.descO + ' with ID ' + str(self.idO) + ' ' +
               '~'*24 + '\nMode: ' + str(self.cM) + '\n' + '~'*80 + '\n')
        return sIn
    
    def yieldIDDesc(self):
        return (self.idO, self.descO)
    
    def printDType(self):
        print('-'*20, 'Type dictionary:', '-'*20)
        pprint.pprint(self.dITp)
    
    def createLSpecSites(self, lInSpS):
        self.lSpS = []
        for tInSpS in lInSpS:
            self.lSpS.append(SpecSite(tInSpS))
    
    def printLSpecSites(self):
        print('-'*24 + ' Special sites: ' + '-'*24)
        for cSpS in self.lSpS:
            print(cSpS)
#    def react(self, nmRP = 'Default'):
#        print('Name of reaction partner:', nmRP)
