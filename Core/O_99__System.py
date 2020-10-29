# -*- coding: utf-8 -*-
###############################################################################
# --- O_99__System.py ---------------------------------------------------------
###############################################################################
import Core.C_00__GenConstants as GC
import Core.F_00__GenFunctions as GF
import Core.F_02__PltFunctions as PF
import Core.F_03__OTpFunctions as TF

from Core.O_00__Base import Base
from Core.O_90__Component import Component

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class System(Base):
    def __init__(self, inpDat, lCpObj = [], iTp = 99):
        super().__init__(inpDat, iTp)
        self.idO = 'Sys'
        self.descO = 'System'
        self.lCpO = lCpObj
        self.dCncSMo = TF.createDCnc(self.dITp)
        self.addCpObj(inpDat)
        self.getDictsCpObj()
        # print('Initiated "System" object.')

    def addCpObj(self, inpDat, refreshCpO = False):
        dNCpO = self.dITp['dNCpObj']
        if refreshCpO:
            self.lCpO = []
            dNCpO = self.dNCpO
        for sCp, nCp in dNCpO.items():
            for cCp in range(nCp):
                self.lCpO.append(Component(inpDat, sCp))

    def getDictsCpObj(self):
        self.dNCpO, self.dCpO = {}, {}
        for cCpO in self.lCpO:
            GF.addToDictCt(self.dNCpO, cCpO.idO)
            GF.addToDictL(self.dCpO, cCpO.idO, cCpO)

    def printCncSMo(self):
        print('--- Concentrations of small molecules in system', self.idO)
        for s, cCnc in self.dCncSMo.items():
            print(s + ':\t' + str(cCnc))

    def printNCompObjSys(self):
        print('*'*16, 'Counts of comp. objects contained in System:', '*'*18)
        for sCp, ctCpO in self.dNCpO.items():
            print(sCp + ':', ctCpO)
        print('- Total:', self.dITp['nCpObj'], '/', sum(self.dNCpO.values()))
        print('*'*80)

    def printAllCompObjSys(self):
        print('*'*16, 'Details of comp. objects contained in System:', '*'*17)
        for sCp, lCpO in self.dCpO.items():
            print('~'*20, 'Components with ID', sCp, '~'*20)
            for cCpO in lCpO:
                cCpO.printComponentDetails()
        print('*'*80)

    def plotResEvo(self, sFRes = None, overWr = True):
        dParPlt = self.dITp[GC.S_D_PLT][GC.S_CP_CNC]
        if sFRes is not None:
            self.dResEvo = TF.getPFResEvo(self.dIG, self.dITp, sFRs = sFRes)
        for cK, cT in dParPlt['dlSY'].items():
            assert len(cK) == 2 and len(cT) == 3
            dPPltF = TF.getDPFPltEvo(self.dIG, self.dITp, cK, dMS = cT[2])
            if self.dResEvo is not None:
                PF.plotEvo(dParPlt, self.dResEvo, dPPltF, tDat = cT[:2],
                           overWr = overWr)

    def evolveOverTime(self, inpDat, doPlots = True):
        self.dResEvo, self.dNCpO = TF.evolveGillespie(self.dIG, self.dITp,
                                                      self.dCncSMo)
        self.addCpObj(inpDat, refreshCpO = True)
        self.getDictsCpObj()
        # self.printCncSMo()
        # self.printNCompObjSys()
        # self.printAllCompObjSys()
        dR, sD, sF = self.dResEvo, self.dITp['sD_Sys'], self.dITp['sF_SysEvo']
        self.pFResEvo = TF.saveAsPdDfr(self.dIG, dR, sD, sF, overWr = True)
        if doPlots:
            self.plotResEvo()

# # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# class System(Base):
#     def __init__(self, inpDat, lOSys = [], iTp = 99):
#         super().__init__(inpDat, iTp)
#         self.idO = 'Sys'
#         self.descO = 'System'
#         self.lOS = lOSys
#         self.lMol = [cO for cO in self.lOS if cO.idO in GC.L_ID_MOL]
#         self.lPro = [cO for cO in self.lOS if cO.idO in GC.L_ID_PRO]
#         self.lEnz = [cO for cO in self.lOS if cO.idO in GC.L_ID_ENZ]
#         self.lKAs = [cO for cO in self.lOS if cO.idO in GC.L_ID_KAS]
#         self.lPAs = [cO for cO in self.lOS if cO.idO in GC.L_ID_PAS]
#         self.lLPr = [cO for cO in self.lOS if cO.idO in GC.L_ID_LPR]
#         self.lSPr = [cO for cO in self.lOS if cO.idO in GC.L_ID_SPR]
#         self.lMet = [cO for cO in self.lOS if cO.idO in GC.L_ID_MET]
#         self.lLMo = [cO for cO in self.lOS if cO.idO in GC.L_ID_LMO]
#         self.lSMo = [cO for cO in self.lOS if cO.idO in GC.L_ID_SMO]
#         self.lInt = [cO for cO in self.lOS if cO.idO in GC.L_ID_INT]
#         self.lPyl = [cO for cO in self.lOS if cO.idO in GC.L_ID_PYL]
#         self.lDePyl = [cO for cO in self.lOS if cO.idO in GC.L_ID_DEPYL]
#         self.dCmp = {'Molecules': self.lMol,
#                      'Proteins': self.lPro,
#                      'Enzymes': self.lEnz,
#                      'Kinases': self.lKAs,
#                      'Phosphatases': self.lPAs,
#                      'LargeProteins': self.lLPr,
#                      'SmallProteins': self.lSPr,
#                      'Metabolites': self.lMet,
#                      'LargeMolecules': self.lLMo,
#                      'SmallMolecules': self.lSMo,
#                      'Interactions': self.lInt,
#                      'Phosphorylations': self.lPyl,
#                      'Dephosphorylations': self.lDePyl}
#         print('Initiated "System" object.')

#     def printSystem(self):
#         print('+'*16, 'System consists of:', '+'*43)
#         for s, lCmp in self.dCmp.items():
#             if len(lCmp) > 0:
#                 TF.printSysComp(s, lCmp)
#         print('+'*80)

#     def printSystemDetails(self):
#         self.printSystem()
#         for cO in self.lKAs + self.lPAs + self.lLPr + self.lSPr:
#             cO.printSpecSites()

#     def setToComp(self, inpDat, lOIntCp, lPAsCp = []):
#         pass

###############################################################################
