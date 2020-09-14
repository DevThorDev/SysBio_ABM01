# -*- coding: utf-8 -*-
###############################################################################
# --- O_80__Interaction.py ----------------------------------------------------
###############################################################################
import pprint

import Core.F_00__GenFunctions as GF

class Interaction:
    def __init__(self, inpDat, lOInt):
        self.idO = 'Int'
        self.descO = 'Interaction'
        self.dIG = inpDat.dI
        self.cM = self.dIG['Mode']
        self.lOI = lOInt
#        GF.seedRNG(self.cM)
        print('Initiated "Interaction" base object.')

    def __str__(self):
        sIn = ('~'*24 + ' ' + self.descO + ' with ID ' + str(self.idO) + ' ' +
               '~'*24 + '\nMode: ' + str(self.cM) + '\n' + '~'*80 + '\n')
        return sIn
    
    def printObjInt(self):
        lTIP = []
        for cO in self.lOI:
            idO, descO = cO.yieldIDDesc()
            (strNSpec, strCS) = (cO.dITp['strNSpec'], cO.dITp['strCS'])
            lTIP.append((idO, descO, strNSpec, strCS))
        print('Interaction partners:')
        for cT in lTIP:
            print('\t' + str(cT))
    
    def printDType(self):
        print('-'*20, 'Type dictionary:', '-'*20)
        pprint.pprint(self.dITp)

###############################################################################
