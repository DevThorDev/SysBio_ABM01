# -*- coding: utf-8 -*-
###############################################################################
# --- O_00__Base.py -----------------------------------------------------------
###############################################################################
import pprint

import Core.C_00__GenConstants as GC
import Core.F_03__OTpFunctions as TF

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class Base:
    def __init__(self, inpDat, iTp=0, sPat01=GC.S_4DASH, lITpU=[0]):
        self.idO = GC.ID_BAS
        self.descO = 'Base class'
        self.sPt01 = sPat01
        self.dIG = inpDat.dI
        self.dITp = TF.getDITp(self.dIG, iTp, lITpU)
        self.cM = self.dIG['Mode']
        self.nSpS = 0                       # number of "special sites"
        self.sSpS = ''                      # string of "special site"
        # print('Initiated "Base" object.')

    def __str__(self):
        sIn = ('~'*24 + ' ' + self.descO + ' with ID ' + str(self.idO) + ' ' +
               '~'*24 + '\nMode: ' + str(self.cM) + '\n' + '~'*80 + '\n')
        return sIn

    def yieldIDDesc(self):
        return (self.idO, self.descO)

    def printDType(self):
        print(GC.S_DASH*20, 'Type dictionary:', GC.S_DASH*20)
        pprint.pprint(self.dITp)

    def overwInpV(self, dDOvw={}, i=0):
        if self.idO in dDOvw:
            for cK, cArr in dDOvw[self.idO].items():
                if cK in self.dITp and i < cArr.size:
                    self.dITp[cK] = cArr[i]
                    # write back class attributes
                    if cK == GC.S_CNC_INI:
                        self.cCnc = cArr[i]
                    print('Changed', cK, 'to', round(cArr[i], 4))

###############################################################################
