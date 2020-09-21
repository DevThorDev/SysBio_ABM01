# -*- coding: utf-8 -*-
###############################################################################
# --- O_00__Base.py -----------------------------------------------------------
###############################################################################
import pprint

import Core.F_00__GenFunctions as GF
import Core.F_03__OTpFunctions as TF

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class Base:
    def __init__(self, inpDat, iTp = 0):
        self.idO = 'Base'
        self.descO = 'Base class'
        self.dIG = inpDat.dI
        self.dITp = TF.getDITp(self.dIG, 0, iTp)
        self.cM = self.dIG['Mode']
        # GF.seedRNG(self.cM)
        self.nSpS = 0                       # number of "special sites"
        self.sSpS = ''                      # string of "special site"
        print('Initiated "Base" base object.')

    def __str__(self):
        sIn = ('~'*24 + ' ' + self.descO + ' with ID ' + str(self.idO) + ' ' +
               '~'*24 + '\nMode: ' + str(self.cM) + '\n' + '~'*80 + '\n')
        return sIn
    
    def yieldIDDesc(self):
        return (self.idO, self.descO)
    
    def printDType(self):
        print('-'*20, 'Type dictionary:', '-'*20)
        pprint.pprint(self.dITp)

###############################################################################
