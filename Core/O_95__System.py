# -*- coding: utf-8 -*-
###############################################################################
# --- O_95__System.py ---------------------------------------------------------
###############################################################################
import pprint

import Core.C_00__GenConstants as GC
import Core.F_00__GenFunctions as GF
import Core.F_01__SpcFunctions as SF

from Core.O_00__Base import Base
from Core.O_90__Component import Component
from Core.O_03__Metabolite import SMo_NO3_1m, SMo_H2PO4_1m
from Core.O_92__PlotterSysSim import PlotterSysSim

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class System(Base):
    def __init__(self, inpDat, inpFr, cRp=0, lCpObj=[], iTp=95):
        super().__init__(inpDat, iTp)
        self.idO = GC.ID_SYS
        self.descO = 'System'
        self.inFr = inpFr
        self.cRep = cRp
        self.lCpO = lCpObj
        self.dCncSMo = SF.createDCnc(self.inFr)
        self.sFRes = self.dITp['sF_Obj'] + GC.S_USC + GC.S_REP + str(self.cRep)
        self.sFRed = self.dITp['sFRed'] + GC.S_USC + GC.S_REP + str(self.cRep)
        self.updateObjDicts(inpDat)
        # print('Initiated "System" object.')

    def updateObjDicts(self, inpDat, refresh=False):
        self.addCpObj(inpDat, refresh=refresh)
        self.getDictCpObj(refresh=refresh)
        self.getDictSMoObj(inpDat)
        if not hasattr(self, 'dResEvo'):
            self.dResEvo = None

    def complDICp(self, lOSy):
        for cOSy in lOSy:
            if len(cOSy.dITp['dInfSpS']) > 0:
                for cKSpS, cD in cOSy.dITp['dInfSpS'].items():
                    for cKSPD in cD:
                        if cKSPD in [GC.S_DO_PYL, GC.S_DO_DPY]:
                            for sPDAgent in cD[cKSPD]:
                                GF.addToDictDL(self.dICp, cKSPD, cKSpS,
                                               sPDAgent, lUnique=True)

    def addCpObj(self, inpDat, refresh=False):
        dNCpO, self.dICp = self.inFr.dNCpObj, {}
        if refresh:
            self.lCpO = []
            dNCpO = self.dNCpO
        for sCp, nCp in dNCpO.items():
            for iCp in range(nCp):
                cCpO = Component(inpDat, self.inFr, sCp)
                self.lCpO.append(cCpO)
                if iCp == 0:
                    self.complDICp(cCpO.lOSy)

    def getDictCpObj(self, refresh=False):
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

    def printDICp(self, sPD=None):
        if sPD is None:
            print(GC.S_DASH*8, 'Component info dictionary:', GC.S_DASH*8)
            pprint.pprint(self.dICp)
        else:
            if sPD in self.dICp:
                print(GC.S_DASH*8, 'Component info dictionary of', sPD + ':',
                      GC.S_DASH*8)
                pprint.pprint(self.dICp[sPD])
        print(GC.S_DASH*60)

    def printDSCpSL(self, sCpSL=None):
        if sCpSL is None:
            print(GC.S_DASH*8, 'Component string dictionary:', GC.S_DASH*8)
            pprint.pprint(self.dSCpSL)
            print(GC.S_DASH*60)
        else:
            if sCpSL in self.dRct:
                print(sCpSL + ':', self.dRct[sCpSL])

    def printNCompObjSys(self):
        print(GC.S_PLUS*16, 'Counts of comp. objects contained in System:',
              GC.S_PLUS*18)
        for sCp, ctCpO in self.dNCpO.items():
            print(sCp + ':', ctCpO)
        print('- Total:', sum(self.dNCpO.values()))
        print(GC.S_PLUS*80)

    def printAllCompObjSys(self):
        print(GC.S_PLUS*16, 'Details of comp. objects contained in System:',
              GC.S_PLUS*17)
        for sCp, lCpO in self.dCpO.items():
            print('~'*20, 'Components with ID', sCp, '~'*20)
            for cCpO in lCpO:
                cCpO.printComponentDetails()
        print(GC.S_PLUS*80)

    def printSMo(self):
        print(GC.S_DASH*8, 'Small molecules in system:', GC.S_DASH*8)
        for k, (sSMo, cSMoO) in enumerate(self.dSMo.items()):
            print(GC.S_DASH*3, 'Small molecule', k + 1, '(ID', sSMo + '):')
            print(cSMoO)

    def printCncSMo(self):
        print('--- Concentrations of small molecules in system', self.idO)
        for s, cCnc in self.dCncSMo.items():
            print(s + ':\t' + str(round(cCnc, GC.R04)))

    def printRepDone(self, cRp, nRp, stT):
        if self.dResEvo is not None and len(self.dResEvo[GC.S_TIME]) > 0:
            print(GC.S_DASH*8, 'Simulation time elapsed after',
                  len(self.dResEvo[GC.S_TIME]), 'time steps:',
                  round(self.dResEvo[GC.S_TIME][-1], GC.R04), GC.S_DASH*8)
        else:
            print(GC.S_DASH*8, 'Simulation has not even started!', GC.S_DASH*8)
        print(GC.S_PLUS*8, 'Finished repetition', cRp, 'of', nRp,
              '| Real time elapsed:', round(GF.getTime() - stT, GC.R08),
              'seconds.', GC.S_PLUS*8)

    def plotResEvo(self, inpDat, dITp, overWr=True):
        if self.dResEvo is None:
            self.dfrResEvo = SF.readDfrResEvo(self.dITp, sPRs=dITp['sPRes'],
                                              sFRs=self.sFRes, iCol=0)
        else:
            self.dfrResEvo = GF.iniPdDfr(self.dResEvo)
        Pltr = PlotterSysSim(inpDat, self.inFr, self.cRep)
        Pltr.plotResEvoSgl(self.dfrResEvo, sDSub=self.dITp['sD_Obj'])

    def evolveOverTime(self, inpDat, dITp, doPlots=True):
        self.dResEvo, self.dNCpO = SF.evolveGillespie(dITp, self.dICp,
                                                      self.inFr, self.dCncSMo)
        self.dfrResEvo = GF.iniPdDfr(self.dResEvo)
        self.updateObjDicts(inpDat, refresh=True)
        dR, sD = self.dResEvo, self.dITp['sD_Obj']
        self.pFResEvo = SF.saveAsPdDfr(dITp, dR, [sD], self.sFRes)
        if doPlots:
            self.plotResEvo(inpDat, dITp)

###############################################################################
