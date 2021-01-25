# -*- coding: utf-8 -*-
###############################################################################
# --- I_02__InpFrames.py ------------------------------------------------------
###############################################################################
import pprint

import Core.C_00__GenConstants as GC
import Core.F_00__GenFunctions as GF

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class InputFrames:
    def __init__(self, dITp):
        self.dDfrIn = {}
        for sK, (sFInD, iC) in dITp['dSFInD'].items():
            sP = GF.joinToPath([dITp['sPInD']], sFInD + '.' + GC.S_EXT_CSV)
            self.dDfrIn[sK] = GF.readCSV(sP, iCol=iC)
        self.getDSCpSL()
        self.getDSCpTp()
        self.getIniSysCpObj()
        self.getDParCnc()
        self.getDRct()
        self.getDCpDepOnSMoCnc()
        self.getDSMoCncDepOnCp()
        self.getDOthInpV()

    def getDSCpSL(self, sK=GC.S_00):
        self.dSCpSL, lTK, lTV = {}, [], []
        if sK in self.dDfrIn:
            cDfr = self.dDfrIn[sK]
            assert GC.S_CPSTR in cDfr.columns
            for sI in cDfr.index:
                sLeft = GC.S_USC.join(sI.split(GC.S_USC)[:-1])
                if sI.endswith(GC.S_SHORT):
                    lTK.append((sLeft, sI))
                elif sI.endswith(GC.S_LONG):
                    lTV.append((sLeft, sI))
            for tK in lTK:
                for tV in lTV:
                    if tK[0] == tV[0]:
                        cK = cDfr.at[tK[1], GC.S_CPSTR]
                        cV = cDfr.at[tV[1], GC.S_CPSTR]
                        self.dSCpSL[cK] = cV
                        break
        else:
            print('ERROR: Key', sK, 'not in DataFrames dictionary!')

    def getDSCpTp(self, sK1=GC.S_00, sK2=GC.S_01):
        self.dSCpTpL, self.dSCpTpS, self.lSCpTpL, self.lSCpTpS = {}, {}, [], []
        colDfrK1, colDfrK2 = self.dDfrIn[sK1].columns, self.dDfrIn[sK2].columns
        if sK1 in self.dDfrIn and sK2 in self.dDfrIn:
            assert GC.S_CPSTR in colDfrK1 and GC.S_CPSTR in colDfrK2
            for sL in self.dDfrIn[sK1].index:
                sCp = self.dDfrIn[sK1].at[sL, GC.S_CPSTR]
                if sL.endswith(GC.S_LONG) or sL.endswith(GC.S_SHORT):
                    if sL.endswith(GC.S_LONG):
                        cS, dS, lS = GC.S_LONG, self.dSCpTpL, self.lSCpTpL
                    else:
                        cS, dS, lS = GC.S_SHORT, self.dSCpTpS, self.lSCpTpS
                    lS.append(sCp)
                    sInd = sL.replace(cS, '').strip(GC.S_USC)
                    for sCpV in self.dDfrIn[sK2].index:
                        if len(sCpV) > len(sInd) and sCpV.startswith(sInd):
                            if sCpV[len(sInd)] in GC.SET_0_1_USC:
                                cV = self.dDfrIn[sK2].at[sCpV, GC.S_CPSTR]
                                GF.addToDictL(dS, sCp, cV)
        else:
            print('ERROR: Key', sK1, 'or key', sK2, 'not in DataFrames',
                  'dictionary!')

    def getIniSysCpObj(self, sK=GC.S_01):
        self.dNCpObj, self.nCpObj = {}, 0
        if sK in self.dDfrIn:
            cDfr = self.dDfrIn[sK]
            assert GC.S_CPSTR in cDfr.columns and GC.S_NUM in cDfr.columns
            for sI in cDfr.index:
                cK = cDfr.at[sI, GC.S_CPSTR]
                cV = cDfr.at[sI, GC.S_NUM]
                self.dNCpObj[cK] = cV
            self.nCpObj = sum(self.dNCpObj.values())
        else:
            print('ERROR: Key', sK, 'not in DataFrames dictionary!')

    def getDParCnc(self, sK=GC.S_02):
        self.dParCnc, sICD, sCCM = {}, GC.S_INI_CNC_DISTR, GC.S_CNC_CHG_MODE
        lSIni, lVIni = GC.L_S_STR_PAR_INI, GC.L_S_VAL_PAR_INI
        lSTChg, lVTChg = GC.L_S_STR_PAR_TCHG, GC.L_S_VAL_PAR_TCHG
        if sK in self.dDfrIn:
            cDfr = self.dDfrIn[sK]
            for x in ([GC.S_CNC_MIN, GC.S_CNC_MAX, sICD, sCCM] +
                      GC.L_S_STR_PAR_INI + GC.L_S_VAL_PAR_INI +
                      GC.L_S_STR_PAR_TCHG + GC.L_S_VAL_PAR_TCHG):
                assert x in cDfr.columns
            assert len(GC.L_S_STR_PAR_INI) == len(GC.L_S_VAL_PAR_INI)
            assert len(GC.L_S_STR_PAR_TCHG) == len(GC.L_S_VAL_PAR_TCHG)
            for sSMo in cDfr.index:
                cMdI = cDfr.at[sSMo, sICD]
                dPaI = {cDfr.at[sSMo, lSIni[k]]: cDfr.at[sSMo, lVIni[k]] for
                        k in range(len(lSIni))}
                cMdT = cDfr.at[sSMo, sCCM]
                dPaT = {cDfr.at[sSMo, lSTChg[k]]: cDfr.at[sSMo, lVTChg[k]] for
                        k in range(len(lSTChg))}
                self.dParCnc[sSMo] = {sICD: (cMdI, dPaI), sCCM: (cMdT, dPaT)}
                self.dParCnc[sSMo][GC.S_CNC_MIN] = cDfr.at[sSMo, GC.S_CNC_MIN]
                self.dParCnc[sSMo][GC.S_CNC_MAX] = cDfr.at[sSMo, GC.S_CNC_MAX]

    def getDRct(self, sK1=GC.S_03, sK2=GC.S_04):
        self.dTpRct, self.dClRct, self.dRct = {}, {}, {}
        if sK2 in self.dDfrIn:
            cDfr = self.dDfrIn[sK2]
            assert GC.S_RCTSTR in cDfr.columns and GC.S_WT in cDfr.columns
            for sI in cDfr.index:
                sRct = cDfr.at[sI, GC.S_RCTSTR]
                wtRct = cDfr.at[sI, GC.S_WT]
                sRctType, sRctClass, lSRctAddI = GF.analyseSRct(sRct)
                if wtRct < 0 and sK1 in self.dDfrIn:
                    wtRct = GF.calcRctWeight(self.dDfrIn[sK1], sRctClass)
                self.dTpRct[sRct] = sRctType, sRctClass, lSRctAddI
                GF.addToDictL(self.dClRct, sRctClass.split(GC.S_USC)[0],
                              sRctClass, lUnique=True)
                self.dRct[sRct] = wtRct
        else:
            print('ERROR: Key', sK2, 'not in DataFrames dictionary!')

    def getDCpDepOnSMoCnc(self, sK=GC.S_05):
        self.dCpDepOnSMoCnc = {}
        if sK in self.dDfrIn:
            cDfr = self.dDfrIn[sK]
            for sHdCol in GC.L_S_PAR_TAB05:
                assert sHdCol in cDfr.columns
            for sI in cDfr.index:
                assert sI[0] in GC.L_S_SMO
                cKM = GC.L_ID_SMO_SYS[GC.L_S_SMO.index(sI[0])]
                dV = {s: cDfr.at[sI, s] for s in GC.L_S_PAR_TAB05}
                GF.addToDictD(self.dCpDepOnSMoCnc, cKM, sI[(1 + 1):], dV)
        else:
            print('ERROR: Key', sK, 'not in DataFrames dictionary!')

    def getDSMoCncDepOnCp(self, sK=GC.S_06):
        self.dSMoCncDepOnCp = {}
        if sK in self.dDfrIn:
            cDfr = self.dDfrIn[sK]
            assert GC.S_VAL_ABS_CH in cDfr.columns
            for sI in cDfr.index:
                assert sI[0] in GC.L_S_SMO
                cKM = GC.L_ID_SMO_SYS[GC.L_S_SMO.index(sI[0])]
                cV = cDfr.at[sI, GC.S_VAL_ABS_CH]
                GF.addToDictD(self.dSMoCncDepOnCp, cKM, sI[(1 + 1):], cV)
        else:
            print('ERROR: Key', sK, 'not in DataFrames dictionary!')

    def getDOthInpV(self, sK=GC.S_07):
        self.dOthInpV = {}
        if sK in self.dDfrIn:
            cDfr = self.dDfrIn[sK]
            assert GC.S_VAL in cDfr.columns
            for sI in cDfr.index:
                self.dOthInpV[sI] = cDfr.at[sI, GC.S_VAL]

    def __str__(self):
        sIn = (GC.S_STAR*24 + ' "InputFrames" type ' + GC.S_STAR*24 +
               '\nDictionary of input DataFrames:\n' + str(self.dDfrIn))
        return sIn

    def printInputFrames(self, sK=None):
        if sK is None:
            print(GC.S_DASH*16, 'Input DataFrames', GC.S_DASH*16)
            for (k, (sK, cDfrIn)) in enumerate(self.dDfrIn.items()):
                print(GC.S_DASH*8, 'Input DataFrame', k, 'with key', sK + ':',
                      GC.S_DASH*8)
                print(cDfrIn)
            print(GC.S_DASH*60)
        else:
            if sK in self.dDfrIn:
                print(GC.S_DASH*8, 'Input DataFrame with key', sK + ':',
                      GC.S_DASH*8)
                print(self.dDfrIn[sK])
                print(GC.S_DASH*60)
            else:
                print(GC.S_DASH*8, 'Key', sK, 'not in DataFrames dictionary!',
                      GC.S_DASH*8)

    def printDSCpSL(self, sCpSL=None):
        if sCpSL is None:
            print(GC.S_DASH*8, 'Component string dictionary:', GC.S_DASH*8)
            pprint.pprint(self.dSCpSL)
            print(GC.S_DASH*60)
        else:
            if sCpSL in self.dSCpSL:
                print(sCpSL + ':', self.dSCpSL[sCpSL])

    def printDSCpTp(self, sCpTp=None):
        if sCpTp is None:
            print(GC.S_DASH*8, 'Component type dictionary (L):', GC.S_DASH*8)
            pprint.pprint(self.dSCpTpL)
            print(GC.S_DASH*60)
            print(GC.S_DASH*8, 'Component type dictionary (S):', GC.S_DASH*8)
            pprint.pprint(self.dSCpTpS)
            print(GC.S_DASH*60)
        else:
            if sCpTp in self.dSCpTpL:
                print('(L)', sCpTp + ':', self.dSCpTpL[sCpTp])
                print('(S)', sCpTp + ':', self.dSCpTpS[sCpTp])

    def printDNCpObj(self, sCp=None):
        if sCp is None:
            print(GC.S_DASH*8, 'Dictionary of number of component objets:',
                  GC.S_DASH*8)
            pprint.pprint(self.dNCpObj)
            print(GC.S_DASH*60)
        else:
            if sCp in self.dNCpObj:
                print(sCp + ':', self.dNCpObj[sCp])

    def printDParCnc(self, sSMo=None):
        if sSMo is None:
            print(GC.S_DASH*8, 'Dictionary of parameters / small molecule',
                  'concentrations:', GC.S_DASH*8)
            pprint.pprint(self.dParCnc)
            print(GC.S_DASH*60)
        else:
            if sSMo in self.dParCnc:
                print(sSMo + ':', self.dParCnc[sSMo])

    def printDTpRct(self, sRct=None):
        if sRct is None:
            print(GC.S_DASH*8, 'Reaction type dictionary:', GC.S_DASH*8)
            for sK in self.dTpRct:
                print(sK + ':', self.dTpRct[sK])
            print(GC.S_DASH*60)
        else:
            if sRct in self.dTpRct:
                print(sRct + ':', self.dTpRct[sRct])

    def printDClRct(self, sRct=None):
        if sRct is None:
            print(GC.S_DASH*8, 'Reaction class dictionary:', GC.S_DASH*8)
            for sK in self.dClRct:
                print(sK + ':', self.dClRct[sK])
            print(GC.S_DASH*60)
        else:
            if sRct in self.dClRct:
                print(sRct + ':', self.dClRct[sRct])

    def printDRct(self, sRct=None):
        if sRct is None:
            print(GC.S_DASH*8, 'Reaction dictionary:', GC.S_DASH*8)
            pprint.pprint(self.dRct)
            print(GC.S_DASH*60)
        else:
            if sRct in self.dRct:
                print(sRct + ':', self.dRct[sRct])

    def printDCpDepOnSMoCnc(self, sSMo=None):
        if sSMo is None:
            print(GC.S_DASH*8, 'Components depending on small molecule',
                  'concentrations dictionary:', GC.S_DASH*8)
            pprint.pprint(self.dCpDepOnSMoCnc)
            print(GC.S_DASH*60)
        else:
            if sSMo in self.dCpDepOnSMoCnc:
                print(sSMo + ':', self.dCpDepOnSMoCnc[sSMo])

    def printDSMoCncDepOnCp(self, sSMo=None):
        if sSMo is None:
            print(GC.S_DASH*8, 'Small molecule concentrations depending on',
                  'components dictionary:', GC.S_DASH*8)
            pprint.pprint(self.dSMoCncDepOnCp)
            print(GC.S_DASH*60)
        else:
            if sSMo in self.dSMoCncDepOnCp:
                print(sSMo + ':', self.dSMoCncDepOnCp[sSMo])

    def printDOthInpV(self, sK=None):
        if sK is None:
            print(GC.S_DASH*8, 'Other input values dictionary:', GC.S_DASH*8)
            pprint.pprint(self.dOthInpV)
            print(GC.S_DASH*60)
        else:
            if sK in self.dOthInpV:
                print(sK + ':', self.dOthInpV[sK])

    def getViaIdx(self, sK, iL=0, iC=0):
        if sK in self.dDfrIn:
            cDfr = self.dDfrIn[sK]
            if iL < cDfr.shape[0]:
                if iC < cDfr.shape[1]:
                    return cDfr.iloc[iL, iC]
                else:
                    print('ERROR: Column index is', iC, '>=',
                          cDfr.shape[1], '(number of columns).')
                    return None
            else:
                print('ERROR: Line index is', iL, '>=',
                      cDfr.shape[0], '(number of lines).')
                return None
        else:
            print('ERROR: Key', sK, 'not in DataFrames dictionary!')
            return None

    def getViaLbl(self, sK, sL, sC):
        if sK in self.dDfrIn:
            cDfr = self.dDfrIn[sK]
            if sL in cDfr.index:
                if sC in cDfr.columns:
                    return cDfr.loc[sL, sC]
                else:
                    print('ERROR: Column label', sC, 'not in columns',
                          list (cDfr.columns))
                    return None
            else:
                print('ERROR: Line label', sL, 'not in lines',
                      list (cDfr.index))
                return None
        else:
            print('ERROR: Key', sK, 'not in DataFrames dictionary!')
            return None

###############################################################################
