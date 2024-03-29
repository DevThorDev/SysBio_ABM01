# -*- coding: utf-8 -*-
###############################################################################
# --- O_95__System.py ---------------------------------------------------------
###############################################################################
import pprint

import Core.C_00__GenConstants as GC
import Core.F_00__GenFunctions as GF
import Core.F_01__SpcFunctions as SF

from Core.O_00__Base import Base
from Core.O_03__Metabolite import SMo_NO3_1m, SMo_H2PO4_1m
from Core.O_75__Component import Component
from Core.O_80__PlotterSysSim import PlotterSysSim
from Core.O_90__PlotterData import PlotterData

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class System(Base):
    def __init__(self, inpDat, inpFr, cRp=0, lCpObj=[], iTp=95):
        super().__init__(inpDat, iTp)
        self.idO = GC.ID_SYS
        self.descO = 'System'
        self.inFr = inpFr
        self.cRp = cRp
        self.lCpO = lCpObj
        self.dCncSMo = SF.createDCnc(self.inFr)
        self.sFRes = self.dITp['sFObj'] + GC.S_USC + GC.S_REP + str(self.cRp)
        self.sFRed = self.dITp['sFRed'] + GC.S_USC + GC.S_REP + str(self.cRp)
        self.updateObjDicts(inpDat)
        # print('Initiated "System" object.')

    def updateObjDicts(self, inpDat, refresh=False):
        self.addCpObj(inpDat, refresh=refresh)
        self.getDictCpObj(refresh=refresh)
        self.getDictSMoObj(inpDat)
        if not hasattr(self, 'dResEvo'):
            self.dResEvo = None
        if not hasattr(self, 'dfrResEvo'):
            self.dfrResEvo = None

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

    def prepAndPlotData(self, inpDat, PltD, cRp=0, overWr=True):
        for sOp in PltD.lSOp:
            Pltr = PlotterSysSim(inpDat, self.inFr, PltD, cOp=sOp, cRp=cRp)
            if sOp is None:     # no groups - PltD.lSOp = [None]
                dfrRes = self.dfrResEvo
                dSHdCY = {sHd: [sHd] for sHd in Pltr.lSHdCY}
            else:               # groups - PltD.lSOp = [S_MEAN_GR, S_SUM_GR]
                t = SF.collapseColumns(PltD, self.dfrResEvo, Pltr.sHdCX,
                                       Pltr.lSHdCY, sOp)
                dfrRes, dSHdCY = t
            Pltr.setPropPlotSys(PltD, dfrRes, dSHdCY, sD=self.dITp['sDObj'],
                                sOp=sOp, cRp=cRp, overWr=overWr)

    def plotSysResults(self, inpDat, dITp, cRp=0):
        if self.dResEvo is not None:
            self.dfrResEvo = GF.iniPdDfr(self.dResEvo)
        assert self.dfrResEvo is not None
        for sI in dITp['lIPltDat']:
            PltD = PlotterData(inpDat, iTp=int(sI)+self.dIG['o_B_PltDt'])
            self.prepAndPlotData(inpDat, PltD, cRp=cRp,
                                 overWr=dITp['overWrPDF'])

    def evolveOverTime(self, inpDat, dITp, cRp=0):
        self.dResEvo, self.dNCpO = SF.evolveGillespie(dITp, self.dICp,
                                                      self.inFr, self.dCncSMo)
        self.dfrResEvo = GF.iniPdDfr(self.dResEvo)
        self.updateObjDicts(inpDat, refresh=True)
        dR, sD, oWC = self.dResEvo, self.dITp['sDObj'], dITp['overWrCSV']
        self.pFResEvo = SF.saveAsPdDfr(dITp, dR, [sD], self.sFRes, overWr=oWC)
        if self.dITp['doPlots']:
            self.plotSysResults(inpDat, dITp, cRp=cRp)

###############################################################################
