# -*- coding: utf-8 -*-
###############################################################################
# --- O_00__Base.py -----------------------------------------------------------
###############################################################################
import pprint

import Core.C_00__GenConstants as GC
# import Core.F_00__GenFunctions as GF
import Core.F_03__OTpFunctions as TF

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class Base:
    def __init__(self, inpDat, iTp = 0):
        self.idO = 'Base'
        self.descO = 'Base class'
        self.dIG = inpDat.dI
        self.dITp = TF.getDITp(self.dIG, 0, iTp)
        self.cM = self.dIG['Mode']
        self.nSpS = 0                       # number of "special sites"
        self.sSpS = ''                      # string of "special site"
        print('Initiated "Base" object.')

    def __str__(self):
        sIn = ('~'*24 + ' ' + self.descO + ' with ID ' + str(self.idO) + ' ' +
               '~'*24 + '\nMode: ' + str(self.cM) + '\n' + '~'*80 + '\n')
        return sIn
    
    def yieldIDDesc(self):
        return (self.idO, self.descO)
    
    def printDType(self):
        print('-'*20, 'Type dictionary:', '-'*20)
        pprint.pprint(self.dITp)
    
    def overwInpV(self, dDOvw = {}, i = 0):
        if self.idO in dDOvw:
            for cK, cArr in dDOvw[self.idO].items():
                if cK in self.dITp and i < cArr.size:
                    self.dITp[cK] = cArr[i]
                    # write back class attributes
                    if cK == GC.S_CONC_INI:
                        self.cCnc = cArr[i]
                        self.stCnc = cArr[i]
                    elif cK == GC.S_MD_CONC_CH:
                        self.sCncCh = cArr[i]
                    elif cK == GC.S_PER_CONC_CH:
                        self.perCncCh = cArr[i]
                    elif cK == GC.S_AMPL_CONC_CH:
                        self.amplCncCh = cArr[i]
                    elif cK == GC.S_THR_LOW_CONC:
                        self.thrLowCnc = cArr[i]
                    elif cK == GC.S_THR_HIGH_CONC:
                        self.thrHighCnc = cArr[i]
                    print('Changed', cK, 'to', round(cArr[i], 4))
            

###############################################################################
