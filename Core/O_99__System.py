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
        self.idO = 'Sys'
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

    def addCpObj(self, inpDat, refresh = False):
        dNCpO = self.inFr.dNCpObj
        if refresh:
            self.lCpO = []
            dNCpO = self.dNCpO
        for sCp, nCp in dNCpO.items():
            for cCp in range(nCp):
                self.lCpO.append(Component(inpDat, self.inFr, sCp))

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

    def printNCompObjSys(self):
        print('*'*16, 'Counts of comp. objects contained in System:', '*'*18)
        for sCp, ctCpO in self.dNCpO.items():
            print(sCp + ':', ctCpO)
        print('- Total:', sum(self.dNCpO.values()))
        print('*'*80)

    def printAllCompObjSys(self):
        print('*'*16, 'Details of comp. objects contained in System:', '*'*17)
        for sCp, lCpO in self.dCpO.items():
            print('~'*20, 'Components with ID', sCp, '~'*20)
            for cCpO in lCpO:
                cCpO.printComponentDetails()
        print('*'*80)

    def printSMo(self):
        print('-'*8, 'Small molecules in system:', '-'*8)
        for k, (sSMo, cSMoO) in enumerate(self.dSMo.items()):
            print('-'*3, 'Small molecule', k + 1, '(with ID', sSMo + '):')
            print(cSMoO)

    def printCncSMo(self):
        print('--- Concentrations of small molecules in system', self.idO)
        for s, cCnc in self.dCncSMo.items():
            print(s + ':\t' + str(round(cCnc, GC.R04)))

    def printFinalSimuTime(self):
        if len(self.dResEvo[GC.S_TIME]) > 0:
            print('-'*8, 'Simulation time elapsed after',
                  len(self.dResEvo[GC.S_TIME]), 'time steps:',
                  round(self.dResEvo[GC.S_TIME][-1], GC.R04), '-'*8)
        else:
            print('-'*8, 'Simulation has not even started!', '-'*8)

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
                PF.plotEvo(dParPlt, self.dfrResEvo, dPPltF, self.inFr.dSCp7,
                           tDat = cT[:2], overWr = overWr)

    def evolveOverTime(self, inpDat, doPlots = True):
        self.dResEvo, self.dNCpO = TF.evolveGillespie(self.dIG,  self.inFr,
                                                      self.dCncSMo)
        self.updateObjDicts(inpDat, refresh = True)
        # self.printCncSMo()
        # self.printNCompObjSys()
        # self.printAllCompObjSys()
        dR, sD, sF = self.dResEvo, self.dITp['sD_Sys'], self.dITp['sF_SysEvo']
        self.pFResEvo = TF.saveAsPdDfr(self.dIG, dR, sD, sF, overWr = True)
        if doPlots:
            self.plotResEvo()

###############################################################################
