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
        self.dDfrIn = {}
        for sK, (sFInD, iC) in self.dIG['dSFInD'].items():
            sP = GF.joinToPath(self.dIG['sPInD'], sFInD + '.' + GC.S_EXT_CSV)
            self.dDfrIn[sK] = GF.readCSV(sP, iCol = iC)
        self.getDSCp7()
        self.getDSCpTp()
        self.getIniSysCpObj()
        self.getDRct()
        self.getDChgConcDep()
        self.getDConcChg()

    def getDSCp7(self, sK = GC.S_00):
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

    def getDSCpTp(self, sK1 = GC.S_00, sK2 = GC.S_01):
        self.dSCpTp, self.lSCpShort, self.lSCpLong = {}, [], []
        if sK1 in self.dDfrIn and sK2 in self.dDfrIn:
            assert (GC.S_COMPSTR in self.dDfrIn[sK1].columns and
                    GC.S_COMPSTR in self.dDfrIn[sK2].columns)
            for sL in self.dDfrIn[sK1].index:
                sCp = self.dDfrIn[sK1].at[sL, GC.S_COMPSTR]
                if sL.endswith(GC.S_LONG):
                    self.lSCpLong.append(sCp)
                    sInd = sL.strip(GC.S_LONG).strip(GC.S_USC)
                    for sCpV in self.dDfrIn[sK2].index:
                        if len(sCpV) > len(sInd) and sCpV[:len(sInd)] == sInd:
                            if sCpV[len(sInd)] in GC.SET_01_USC:
                                cK = sCp
                                cV = self.dDfrIn[sK2].at[sCpV, GC.S_COMPSTR]
                                GF.addToDictL(self.dSCpTp, cK, cV)
                elif sL.endswith(GC.S_SHORT):
                    self.lSCpShort.append(sCp)
        else:
            print('ERROR: Key', sK1, 'or key', sK2, 'not in DataFrames',
                  'dictionary!')

    def getIniSysCpObj(self, sK = GC.S_01):
        self.dNCpObj, self.nCpObj = {}, 0
        if sK in self.dDfrIn:
            assert (GC.S_COMPSTR in self.dDfrIn[sK].columns and
                    GC.S_NUM in self.dDfrIn[sK].columns)
            for sI in self.dDfrIn[sK].index:
                cK = self.dDfrIn[sK].at[sI, GC.S_COMPSTR]
                cV = self.dDfrIn[sK].at[sI, GC.S_NUM]
                self.dNCpObj[cK] = cV
            self.nCpObj = sum(self.dNCpObj.values())
        else:
            print('ERROR: Key', sK, 'not in DataFrames dictionary!')

    def getDRct(self, sK = GC.S_04):
        self.dRct = {}
        if sK in self.dDfrIn:
            assert (GC.S_RCTSTR in self.dDfrIn[sK].columns and
                    GC.S_WT in self.dDfrIn[sK].columns)
            for sI in self.dDfrIn[sK].index:
                cK = self.dDfrIn[sK].at[sI, GC.S_RCTSTR]
                cV = self.dDfrIn[sK].at[sI, GC.S_WT]
                self.dRct[cK] = cV
        else:
            print('ERROR: Key', sK, 'not in DataFrames dictionary!')

    def getDChgConcDep(self, sK = GC.S_05):
        self.dChgConcDep = {}
        if sK in self.dDfrIn:
            for sHdCol in GC.L_S_PAR_TAB05:
                assert sHdCol in self.dDfrIn[sK].columns
            for sI in self.dDfrIn[sK].index:
                assert sI[0] in GC.L_S_1DIG_SMO
                cKM = GC.L_ID_SMO_USED[GC.L_S_1DIG_SMO.index(sI[0])]
                dV = {s: self.dDfrIn[sK].at[sI, s] for s in GC.L_S_PAR_TAB05}
                GF.addToDictD(self.dChgConcDep, cKM, sI[(1 + 1):], dV)
        else:
            print('ERROR: Key', sK, 'not in DataFrames dictionary!')

    def getDConcChg(self, sK = GC.S_06):
        self.dConcChg = {}
        if sK in self.dDfrIn:
            assert GC.S_VAL_ABS_CH in self.dDfrIn[sK].columns
            for sI in self.dDfrIn[sK].index:
                assert sI[0] in GC.L_S_1DIG_SMO
                cKM = GC.L_ID_SMO_USED[GC.L_S_1DIG_SMO.index(sI[0])]
                cV = self.dDfrIn[sK].at[sI, GC.S_VAL_ABS_CH]
                GF.addToDictD(self.dConcChg, cKM, sI[(1 + 1):], cV)
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
