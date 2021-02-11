# -*- coding: utf-8 -*-
###############################################################################
# --- O_90__PlotterData.py ----------------------------------------------------
###############################################################################
import Core.C_00__GenConstants as GC
# import Core.F_00__GenFunctions as GF
# import Core.F_01__SpcFunctions as SF
# import Core.F_02__PltFunctions as PF

from Core.O_00__Base import Base

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class PlotterData(Base):
    def __init__(self, inpDat, iTp):
        super().__init__(inpDat, iTp)
        self.idO = GC.ID_PDT
        self.descO = 'PlotterData'
        self.getData()
        # print('Initiated "PlotterData" object.')

    def getData(self):
        # get data from object input files
        self.sPltNm = self.dITp['sPltNm']
        self.sPltCl = self.dITp['sPltCl']
        self.sPltTp = self.dITp['sPltTp']
        self.lSCpCnc = self.dITp['lSCpCnc']
        self.lSOp = self.dITp['lSOp']
        self.dCHdGr = self.dITp['dCHdGr']
        self.yLbl = self.dITp['yLbl']
        self.styLnCt = self.dITp['styLnCt']
        self.styLnCI = self.dITp['styLnCI']
        self.wdthLnCt = self.dITp['wdthLnCt']
        self.wdthLnCI = self.dITp['wdthLnCI']
        self.dCol = self.dITp['dCol']
        self.alpCol = self.dITp['alpCol']

    def printData(self):
        # print the class attribute data contained in the object input files
        print('*', self.sPltNm, '(name of plot, must be unique - used as key)')
        print('*', self.sPltCl, '(class of the plot, e.g. comp.-conc.)')
        print('*', self.sPltTp, '(type of the plot, e.g. comp., conc.)')
        print('*', self.lSCpCnc, '(list of short comp. names considered)')
        print('*', self.lSOp, '(list of operation strings: mean, sum)')
        print('*', self.dCHdGr, '(grouping dict.; key: column header)')
        print('*', self.yLbl, '(y-label of plot)')
        print('*', self.styLnCt, '(line style of the plot of centres)')
        print('*', self.styLnCI, '(line style of the plot of CIs)')
        print('*', self.wdthLnCt, '(line width of the plot of centres)')
        print('*', self.wdthLnCI, '(line width of the plot of CIs)')
        print('*', self.dCol, '(dictionary of colours used in the plot)')
        print('*', self.alpCol, '(transparency of colours used in the plot)')

###############################################################################
