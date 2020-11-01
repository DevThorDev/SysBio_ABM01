# -*- coding: utf-8 -*-
###############################################################################
# --- I_02__InpFrames.py ------------------------------------------------------
###############################################################################
# import Core.C_00__GenConstants as GC
import Core.F_00__GenFunctions as GF

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class InputFrames:
    def __init__(self, inpDat):
        self.dIG = inpDat.dI
        self.dDfrIn = {}
        for sFInD in self.dIG['dSFInD']:
            sPInD = GF.joinToPath(self.dIG['sPInD'], sFInD)
            self.dDfrIn[sFInD[:2]] = GF.readCSV(sPInD, iCol = 1)

    def __str__(self):
        sIn = ('*'*24 + ' "InputFrame" type ' + '*'*24 +
               '\nDictionary of inpt DataFrames:\n' + str(self.dDfrIn))
        return sIn

    def printInputFrames(self):
        for k, cDfrIn in enumerate(self.dDfrIn):
            print('-'*8, 'Input DataFrame ' + str(k) + ':', '-'*8)
            print(cDfrIn)

###############################################################################
