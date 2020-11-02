# -*- coding: utf-8 -*-
###############################################################################
# --- I_02__InpFrames.py ------------------------------------------------------
###############################################################################
import Core.C_00__GenConstants as GC
import Core.F_00__GenFunctions as GF

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class InputFrames:
    def __init__(self, inpDat):
        self.dIG = inpDat.dI
        self.dDfrIn, sK00 = {}, '00'
        for sK, (sFInD, iC) in self.dIG['dSFInD'].items():
            sP = GF.joinToPath(self.dIG['sPInD'], sFInD + '.' + GC.S_EXT_CSV)
            self.dDfrIn[sK] = GF.readCSV(sP, iCol = iC)
        self.getDSCp7(sK = sK00)

    def getDSCp7(self, sK = '00'):
        self.dSCp7, lTK, lTV = {}, [], []
        if sK in self.dDfrIn:
            assert GC.S_COMPSTR in self.dDfrIn[sK].columns
            for sI in self.dDfrIn[sK].index:
                sLeft = GC.S_USC.join(sI.split(GC.S_USC)[:-1])
                if sI.endswith(GC.S_SHORT):
                    lTK.append((sLeft, sI))
                elif sI.endswith(GC.S_LONG):
                    lTV.append((sLeft, sI))
            for tK in lTK:
                for tV in lTV:
                    if tK[0] == tV[0]:
                        cK = self.dDfrIn[sK].at[tK[1], GC.S_COMPSTR]
                        cV = self.dDfrIn[sK].at[tV[1], GC.S_COMPSTR]
                        self.dSCp7[cK] = cV
                        break
        else:
            print('ERROR: Key', sK, 'not in DataFrames dictionary!')

    def __str__(self):
        sIn = ('*'*24 + ' "InputFrames" type ' + '*'*24 +
               '\nDictionary of input DataFrames:\n' + str(self.dDfrIn))
        return sIn

    def printInputFrame(self, sK):
        if sK in self.dDfrIn:
            print('-'*8, 'Input DataFrame with key', sK + ':', '-'*8)
            print(self.dDfrIn[sK])
        else:
            print('-'*8, 'Key', sK, 'not in DataFrames dictionary!', '-'*8)

    def printInputFrames(self):
        for (k, (sK, cDfrIn)) in enumerate(self.dDfrIn.items()):
            print('-'*8, 'Input DataFrame', k, 'with key', sK + ':', '-'*8)
            print(cDfrIn)

    def getViaIdx(self, sK, iL = 0, iC = 0):
        if sK in self.dDfrIn:
            if iL < self.dDfrIn[sK].shape[0]:
                if iC < self.dDfrIn[sK].shape[1]:
                    return self.dDfrIn[sK].iloc[iL, iC]
                else:
                    print('ERROR: Column index is', iC, '>=',
                          self.dDfrIn[sK].shape[1], '(number of columns).')
                    return None
            else:
                print('ERROR: Line index is', iL, '>=',
                      self.dDfrIn[sK].shape[0], '(number of lines).')
                return None
        else:
            print('ERROR: Key', sK, 'not in DataFrames dictionary!')
            return None

    def getViaLbl(self, sK, sL, sC):
        if sK in self.dDfrIn:
            if sL in self.dDfrIn[sK].index:
                if sC in self.dDfrIn[sK].columns:
                    return self.dDfrIn[sK].loc[sL, sC]
                else:
                    print('ERROR: Column label', sC, 'not in columns',
                          list (self.dDfrIn[sK].columns))
                    return None
            else:
                print('ERROR: Line label', sL, 'not in lines',
                      list (self.dDfrIn[sK].index))
                return None
        else:
            print('ERROR: Key', sK, 'not in DataFrames dictionary!')
            return None

###############################################################################
