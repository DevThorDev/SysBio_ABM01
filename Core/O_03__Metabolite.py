# -*- coding: utf-8 -*-
###############################################################################
# --- O_03__Metabolite.py -----------------------------------------------------
###############################################################################
import Core.C_00__GenConstants as GC
import Core.F_03__OTpFunctions as TF

from Core.O_01__Molecule import Molecule

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class Metabolite(Molecule):
    def __init__(self, inpDat, iTp, dStat = {}):
        super().__init__(inpDat, iTp)
        self.idO = 'Met'
        self.descO = 'Metabolite'
        print('Initiated "Metabolite" object.')

class LargeMolecule(Metabolite):
    def __init__(self, inpDat, iTp, dStat = {}):
        super().__init__(inpDat, iTp, dStat)
        self.idO = 'LMo'
        self.descO = 'Large molecule'
        print('Initiated "LargeMolecule" object.')

class SmallMolecule(Metabolite):
    def __init__(self, inpDat, iTp, dStat = {}):
        super().__init__(inpDat, iTp, dStat)
        self.idO = 'SMo'
        self.descO = 'Small molecule'
        self.setIniConc()
        print('Initiated "SmallMolecule" object.')
    
    def setIniConc(self):
        self.cCnc = self.dITp[GC.S_CONC_INI]
        self.stCnc = self.dITp[GC.S_CONC_INI]
        self.sCncCh = self.dITp[GC.S_MD_CONC_CH]
        self.perCncCh = self.dITp[GC.S_PER_CONC_CH]
        self.amplCncCh = self.dITp[GC.S_AMPL_CONC_CH]
        self.thrLowCnc = self.dITp[GC.S_THR_LOW_CONC]
        self.thrHighCnc = self.dITp[GC.S_THR_HIGH_CONC]

    def changeConc(self, t, idSt):
        cCnc_t, cCncChSt = self.cCnc, 0
        if self.sCncCh == GC.S_NO:
            cCnc_t = self.cCnc
        elif self.sCncCh == GC.S_CH_SIN:
            cCnc_t += TF.doSinChange(t, self.perCncCh, self.amplCncCh)
        if idSt in [GC.S_ST_A_INT_AT5G49770_NRT2P1,
                    GC.S_ST_B_TRANS_AT5G49770_NRT2P1]:
            cCncChSt = -self.cCnc*self.dITp['propDecStAB']
        elif idSt in [GC.S_ST_C_INT_NAR2P1_NRT2P1,
                      GC.S_ST_D_TRANS_NAR2P1_NRT2P1]:
            cCncChSt = self.cCnc*self.dITp['propIncStCD']
        self.cCnc = max(0, cCnc_t + cCncChSt)
        # print('cID:', self.idO, '- t:', t, '- idSt:', idSt, '- cCnc_t:',
        #       cCnc_t, '- cCncChSt:', cCncChSt, '- self.cCnc:', self.cCnc)

class SMo_NO3_1m(SmallMolecule):
    def __init__(self, inpDat, iTp = 501, dStat = {}):
        super().__init__(inpDat, iTp, dStat)
        self.idO = GC.ID_NO3_1M
        self.descO = 'Small molecule NO3-'
        self.createDSpecSites(self.dITp['dInfSpS'])
        print('Initiated "SMo_NO3_1m" object.')
    
class SMo_H2PO4_1m(SmallMolecule):
    def __init__(self, inpDat, iTp = 502, dStat = {}):
        super().__init__(inpDat, iTp, dStat)
        self.idO = GC.ID_H2PO4_1M
        self.descO = 'Small molecule H2PO4-'
        self.createDSpecSites(self.dITp['dInfSpS'])
        print('Initiated "SMo_H2PO4_1m" object.')

###############################################################################
