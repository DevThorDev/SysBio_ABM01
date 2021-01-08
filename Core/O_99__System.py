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
from Core.O_03__Metabolite import SMo_NO3_1m, SMo_H2PO4_1m

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class System(Base):
    def __init__(self, inpDat, inpFr, lCpObj = [], iTp = 99):
        super().__init__(inpDat, iTp)
        self.idO = GC.ID_SYS
        self.descO = 'System'
        self.inFr = inpFr
        self.lCpO = lCpObj
        self.dCncSMo = TF.createDCnc(self.inFr)
        self.updateObjDicts(inpDat)
        # print('Initiated "System" object.')

    def updateObjDicts(self, inpDat, refresh = False):
        self.addCpObj(inpDat, refresh = refresh)
        self.getDictCpObj(refresh = refresh)
        self.getDictSMoObj(inpDat)
        self.dResEvo = None

    def createDICp(self, lOSy, iCp = 0):
        if iCp == 0:
            for cOSy in lOSy:
                if len(cOSy.dITp['dInfSpS']) > 0:
                    for cKS, cD in cOSy.dITp['dInfSpS'].items():
                        for cKI in cD:
                            if cKI in [GC.S_DO_PYL, GC.S_DO_DPY]:
                                for cAs in cD[cKI]:
                                    GF.addToDictL(self.dICp, (cKI, cKS), cAs,
                                                  lUnique = True)

    def addCpObj(self, inpDat, refresh = False):
        dNCpO, self.dICp = self.inFr.dNCpObj, {}
        if refresh:
            self.lCpO = []
            dNCpO = self.dNCpO
        for sCp, nCp in dNCpO.items():
            for iCp in range(nCp):
                cCpO = Component(inpDat, self.inFr, sCp)
                self.createDICp(cCpO.lOSy, iCp)
                self.lCpO.append(cCpO)

    def getDictCpObj(self, refresh = False):
        self.dCpO = {}
        if not refresh:
            self.dNCpO = {}
        for cCpO in self.lCpO:
            GF.addToDictL(self.dCpO, cCpO.idO, cCpO)
            if not refresh:
                GF.addToDictCt(self.dNCpO, cCpO.idO)

    def getDictSMoObj(self, inpDat):
        NO3_1m = SMo_NO3_1m(inpDat)
        H2PO4_1m = SMo_H2PO4_1m(inpDat)
        self.dSMo = {NO3_1m.idO: NO3_1m, H2PO4_1m.idO: H2PO4_1m}
        for sSMo, cSMoO in self.dSMo.items():
            cSMoO.setConc(self.dCncSMo[sSMo])

    def printDICp(self):
        for cK, cAs in self.dICp.items():
            print(str(cK) + ': ' + str(cAs))

    def printNCompObjSys(self):
        print(GC.S_STAR*16, 'Counts of comp. objects contained in System:',
              GC.S_STAR*18)
        for sCp, ctCpO in self.dNCpO.items():
            print(sCp + ':', ctCpO)
        print('- Total:', sum(self.dNCpO.values()))
        print(GC.S_STAR*80)

    def printAllCompObjSys(self):
        print(GC.S_STAR*16, 'Details of comp. objects contained in System:',
              GC.S_STAR*17)
        for sCp, lCpO in self.dCpO.items():
            print('~'*20, 'Components with ID', sCp, '~'*20)
            for cCpO in lCpO:
                cCpO.printComponentDetails()
        print(GC.S_STAR*80)

    def printSMo(self):
        print(GC.S_DASH*8, 'Small molecules in system:', GC.S_DASH*8)
        for k, (sSMo, cSMoO) in enumerate(self.dSMo.items()):
            print(GC.S_DASH*3, 'Small molecule', k + 1, '(ID', sSMo + '):')
            print(cSMoO)

    def printCncSMo(self):
        print('--- Concentrations of small molecules in system', self.idO)
        for s, cCnc in self.dCncSMo.items():
            print(s + ':\t' + str(round(cCnc, GC.R04)))

    def printFinalSimuTime(self):
        if self.dResEvo is not None and len(self.dResEvo[GC.S_TIME]) > 0:
            print(GC.S_DASH*8, 'Simulation time elapsed after',
                  len(self.dResEvo[GC.S_TIME]), 'time steps:',
                  round(self.dResEvo[GC.S_TIME][-1], GC.R04), GC.S_DASH*8)
        else:
            print(GC.S_DASH*8, 'Simulation has not even started!', GC.S_DASH*8)

    def plotResEvo(self, sFRes = None, overWr = True):
        dParPlt = self.dITp[GC.S_D_PLT][GC.S_CP_CNC]
        if sFRes is not None:
            self.dfrResEvo = TF.getPFResEvo(self.dIG, self.dITp, sFRs = sFRes)
        else:
            self.dfrResEvo = GF.iniPdDfr(self.dResEvo)
        for cK, cT in dParPlt['dlSY'].items():
            assert len(cK) == 2 and len(cT) == 3
            dPPltF = TF.getDPFPltEvo(self.dIG, self.dITp, cK, dMS = cT[2])
            if self.dResEvo is not None and self.dfrResEvo is not None:
                PF.plotEvo(dParPlt, self.dfrResEvo, dPPltF, self.inFr.dSCpSL,
                           tDat = cT[:2], overWr = overWr)

    def evolveOverTime(self, inpDat, doPlots = True):
        self.dResEvo, self.dNCpO = TF.evolveGillespie(self.dIG, self.dICp,
                                                      self.inFr, self.dCncSMo)
        self.updateObjDicts(inpDat, refresh = True)
        # self.printCncSMo()
        # self.printNCompObjSys()
        # self.printAllCompObjSys()
        dR, sD, sF = self.dResEvo, self.dITp['sD_Sys'], self.dITp['sF_SysEvo']
        self.pFResEvo = TF.saveAsPdDfr(self.dIG, dR, sD, sF, overWr = True)
        if doPlots:
            self.plotResEvo()

###############################################################################
