# -*- coding: utf-8 -*-
###############################################################################
# --- O_90__State.py ----------------------------------------------------------
###############################################################################
import Core.C_00__GenConstants as GC
import Core.F_00__GenFunctions as GF
import Core.F_02__PltFunctions as PF
import Core.F_03__OTpFunctions as TF

from Core.O_00__Base import Base
from Core.O_02__Protein import Kinase0, Phosphatase0
from Core.O_80__Interaction import Phosphorylation, Dephosphorylation
from Core.O_99__System import System

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class State(Base):
    def __init__(self, inpDat, dOState, llOInt = [], lOOth = [], iTp = 90):
        super().__init__(inpDat, iTp = iTp)
        for cLOInt in llOInt:
            assert len(cLOInt) >= 2
        self.idO = 'Sta'
        self.descO = 'State'
        self.llOI = llOInt
        self.lOO = lOOth
        self.complementLO(inpDat, dOState)
        lSCol = [GC.S_TS, GC.S_CONC_NO3_1M, GC.S_CONC_H2PO4_1M, GC.S_STATE]
        dfrShape = (self.dIG['maxTS'] + 1, len(lSCol))
        self.dfrEvo = GF.iniPdDfr(lSNmC = lSCol, shape = dfrShape)
        self.dfrEvo.iloc[0, :] = [0, self.lSMo[0].cCnc, self.lSMo[1].cCnc,
                                  self.idO]
        print('Initiated "State" object.')
        
    def complementLO(self, inpDat, dOState):
        self.lSMo = dOState[GC.SPC_L_SMO]
        self.dCnc = {cO.idO: [cO.cCnc, cO.dITp['thrLowConc'],
                              cO.dITp['thrHighConc']] for cO in self.lSMo}
        lOSy = GF.lItToUniqueList(self.llOI) + self.lOO + self.lSMo
        lID = TF.complLSpec(inpDat, lOSy, sTp = 'KAs', sD = 'Pyl')
        print('lID (KAs) =', lID)
        self.lKAs0 = [Kinase0(inpDat, cID = ID) for ID in lID if ID not in
                      [GC.ID_KAS_X]]        # as Kinase_X is a specific kinase
        lID = TF.complLSpec(inpDat, lOSy, sTp = 'PAs', sD = 'DePyl')
        print('lID (PAs) =', lID)
        self.lPAs0 = [Phosphatase0(inpDat, cID = ID) for ID in lID]
    
    def __str__(self):
        sIn = ('++++ State ' + self.idO + ' (' + self.descO + '):')
        return sIn
    
    def printDetails(self):
        for k, lOI in enumerate(self.llOI):
            print('- Interacting pair ' + str(k + 1) + ': (' + lOI[0].idO +
                  ', ' + lOI[1].idO + ')')
        for k, cO in enumerate(self.lOO):
            s = '- Further component ' + str(k + 1) + ': ' + cO.idO
            if hasattr(cO, 'cCnc'):
                s += ' with conc. ' + str(round(cO.cCnc, GC.R04))
            print(s)
        for k, cK in enumerate(self.lKAs0):
            print('- Kinase ' + str(k + 1) + ': ' + cK.idO)
        for k, cP in enumerate(self.lPAs0):
            print('- Phosphatase ' + str(k + 1) + ': ' + cP.idO)
        for k, cS in enumerate(self.lSMo):
            print('- Small molecule ' + str(k + 1) + ': ' + cS.idO)
        print('-- State component details:')
        for cO in list(set(GF.lItToUniqueList(self.llOI) + self.lOO +
                           self.lKAs0 + self.lPAs0 + self.lSMo)):
            cO.printMolSpecSites()
    
    def printStateDetails(self):
        print(self)
        self.printDetails()
        
    def printDCnc(self, prID = None, prFull = False):
        if prFull:
            print('Dictionary of small molecule concentrations:')
        for cID, (cCnc, thrLow, thrHigh) in self.dCnc.items():
            if prFull and (prID is None or cID == prID):
                print(cID + ': Current conc. ' + str(round(cCnc, GC.R04)) +
                      '; "low" thr. ' + str(round(thrLow, GC.R04)) +
                      '; "high" thr. ' + str(round(thrHigh, GC.R04)))
            elif not prFull and (prID is None or cID == prID):
                print(cID + ': Current conc. ' + str(round(cCnc, GC.R04)))
    
    def savePlotDfrEvo(self, kSt = 0, llIPlot = None):
        assert len(self.lSMo) > 0
        dITpSMo = self.lSMo[0].dITp
        sNSt, sKSt = str(self.dIG['nStates']), str(kSt)
        sF =  dITpSMo['sF_SMo'] + '_' + '0'*(len(sNSt) - len(sKSt)) + sKSt
        TF.savePdDfr(self.dIG, self.dfrEvo, self.dIG['sPRes'],
                     dITpSMo['sD_SMo'], sF)
        if llIPlot is not None:
            for lIPlot in llIPlot:
                sFPlt = sF + '__' + '_'.join([str(iPlot) for iPlot in lIPlot])
                sP = TF.getPF(self.dIG['sPPlt'], dITpSMo['sD_SMo'], sFPlt,
                              sFExt = GC.NM_EXT_PDF)
                PF.plotDfrEvo(self.dfrEvo, sP, lIPlot)
    
    def adaptPSites(self, inpDat, cO, dSites = {}):
        for cSite, (bMod, cAs) in dSites.items():
            if bMod == GC.B_DO_PYL:
                if Phosphorylation(inpDat, cO, cAs, cSite).doPyl():
                    print('Phosphorylation at site', cSite, 'happened!')
            elif bMod == GC.B_DO_DEPYL:
                if Dephosphorylation(inpDat, cO, cAs, cSite).doDePyl():
                    print('Dephosphorylation at site', cSite, 'happened!')

    def getConcSMo(self, cID = None):
        lConc = []
        for cSMo in self.lSMo:
            if cID is None or cSMo.idO == cID:
                lConc.append(cSMo.cCnc)
        return lConc
        
    def changeConcSMo(self, cTS, cID = None):
        for cSMo in self.lSMo:
            if cID is None or cSMo.idO == cID:
                cSMo.changeConc(cTS, self.idO)
                assert cSMo.idO in self.dCnc
                self.dCnc[cSMo.idO][0] = cSMo.cCnc
        self.dfrEvo.iloc[cTS, :] = [cTS, self.lSMo[0].cCnc, self.lSMo[1].cCnc,
                                    self.idO]
        
    def createSystem(self, inpDat):
        lOSy = GF.lItToUniqueList(self.llOI) + self.lOO
        lOSy += self.lKAs0 + self.lPAs0 + self.lSMo
        return System(inpDat, lOSys = lOSy)

class State_Int_Trans(State):
    def __init__(self, inpDat, dOState, iTp = 90):
        if inpDat.dI['sStIni'] == GC.S_ST_A_INT_AT5G49770_NRT2P1:
            self.ini_St_A_Int_AT5G49770_NRT2p1(inpDat, dOState, iTp = iTp)
        elif inpDat.dI['sStIni'] == GC.S_ST_B_TRANS_AT5G49770_NRT2P1:
            self.ini_St_B_Trans_AT5G49770_NRT2p1(inpDat, dOState, iTp = iTp)
        elif inpDat.dI['sStIni'] == GC.S_ST_C_INT_NAR2P1_NRT2P1:
            self.ini_St_C_Int_NAR2p1_NRT2p1(inpDat, dOState, iTp = iTp)
        elif inpDat.dI['sStIni'] == GC.S_ST_D_TRANS_NAR2P1_NRT2P1:
            self.ini_St_D_Trans_NAR2p1_NRT2p1(inpDat, dOState, iTp = iTp)
        else:
            self.idO = 'St_Int_Trans'
            self.descO = 'State interaction or transition'
        print('Initiated "State_Int_Trans" object.')
    
    def ini_St_A_Int_AT5G49770_NRT2p1(self, inpDat, dOState, iTp = 90):
        llOI = [[dOState[GC.SPC_KAS_A], dOState[GC.SPC_LPR_A]]]
        lOO = [dOState[GC.SPC_SPR_A], dOState[GC.SPC_KAS_X]]
        super().__init__(inpDat, dOState, llOI, lOO, iTp = iTp)
        self.idO = GC.S_ST_A_INT_AT5G49770_NRT2P1
        self.descO = 'State interaction AT5G49770-NRT2p1'
        dSts = {GC.S_SPS_KAS1_S839: (GC.B_DO_DEPYL, self.lPAs0[0]),
                GC.S_SPS_KAS1_S870: (GC.B_DO_PYL, self.lKAs0[1])}
        self.adaptPSites(inpDat, dOState[GC.SPC_KAS_A], dSites = dSts)
        dSts = {GC.S_SPS_LPR1_S21: (GC.B_DO_PYL, self.lKAs0[2]),
                GC.S_SPS_LPR1_S28: (GC.B_DO_DEPYL, self.lPAs0[3])}
        self.adaptPSites(inpDat, dOState[GC.SPC_LPR_A], dSites = dSts)

    def ini_St_B_Trans_AT5G49770_NRT2p1(self, inpDat, dOState, iTp = 90):
        llOI = [[dOState[GC.SPC_KAS_A], dOState[GC.SPC_LPR_A]],
                [dOState[GC.SPC_KAS_X], dOState[GC.SPC_LPR_A]]]
        lOO = [dOState[GC.SPC_SPR_A]]
        super().__init__(inpDat, dOState, llOI, lOO, iTp = iTp)
        self.idO = GC.S_ST_B_TRANS_AT5G49770_NRT2P1
        self.descO = 'State transition from AT5G49770-NRT2p1'
        dSts = {GC.S_SPS_KAS1_S839: (GC.B_DO_PYL, self.lKAs0[0]),
                GC.S_SPS_KAS1_S870: (GC.B_DO_PYL, self.lKAs0[1])}
        self.adaptPSites(inpDat, dOState[GC.SPC_KAS_A], dSites = dSts)
        dSts = {GC.S_SPS_LPR1_S21: (GC.B_DO_PYL, self.lKAs0[2]),
                GC.S_SPS_LPR1_S28: (GC.B_DO_DEPYL, self.lPAs0[3])}
        self.adaptPSites(inpDat, dOState[GC.SPC_LPR_A], dSites = dSts)

    def ini_St_C_Int_NAR2p1_NRT2p1(self, inpDat, dOState, iTp = 90):
        llOI = [[dOState[GC.SPC_SPR_A], dOState[GC.SPC_LPR_A]]]
        lOO = [dOState[GC.SPC_KAS_A], dOState[GC.SPC_KAS_X]]
        super().__init__(inpDat, dOState, llOI, lOO, iTp = iTp)
        self.idO = GC.S_ST_C_INT_NAR2P1_NRT2P1
        self.descO = 'State interaction NAR2p1-NRT2p1'
        dSts = {GC.S_SPS_KAS1_S839: (GC.B_DO_PYL, self.lKAs0[0]),
                GC.S_SPS_KAS1_S870: (GC.B_DO_DEPYL, self.lPAs0[1])}
        self.adaptPSites(inpDat, dOState[GC.SPC_KAS_A], dSites = dSts)
        dSts = {GC.S_SPS_LPR1_S21: (GC.B_DO_DEPYL, self.lPAs0[2]),
                GC.S_SPS_LPR1_S28: (GC.B_DO_PYL, dOState[GC.SPC_KAS_X])}
        self.adaptPSites(inpDat, dOState[GC.SPC_LPR_A], dSites = dSts)

    def ini_St_D_Trans_NAR2p1_NRT2p1(self, inpDat, dOState, iTp = 90):
        llOI = [[dOState[GC.SPC_SPR_A], dOState[GC.SPC_LPR_A]]]
        lOO = [dOState[GC.SPC_KAS_A], dOState[GC.SPC_KAS_X]]
        super().__init__(inpDat, dOState, llOI, lOO, iTp = iTp)
        self.idO = GC.S_ST_D_TRANS_NAR2P1_NRT2P1
        self.descO = 'State transition from NAR2p1-NRT2p1'
        dSts = {GC.S_SPS_KAS1_S839: (GC.B_DO_PYL, self.lKAs0[0]),
                GC.S_SPS_KAS1_S870: (GC.B_DO_DEPYL, self.lPAs0[1])}
        self.adaptPSites(inpDat, dOState[GC.SPC_KAS_A], dSites = dSts)
        dSts = {GC.S_SPS_LPR1_S21: (GC.B_DO_DEPYL, self.lPAs0[2]),
                GC.S_SPS_LPR1_S28: (GC.B_DO_PYL, dOState[GC.SPC_KAS_X])}
        self.adaptPSites(inpDat, dOState[GC.SPC_LPR_A], dSites = dSts)

    def to_St_A_Int_AT5G49770_NRT2p1(self, inpDat):
        self.idO = GC.S_ST_A_INT_AT5G49770_NRT2P1
        self.descO = 'State interaction AT5G49770-NRT2p1'
        self.lOO[0], self.llOI[0][0] = self.llOI[0][0], self.lOO[0]
        dSts = {GC.S_SPS_KAS1_S839: (GC.B_DO_DEPYL, self.lPAs0[0]),
                GC.S_SPS_KAS1_S870: (GC.B_DO_PYL, self.lKAs0[1])}
        self.adaptPSites(inpDat, self.llOI[0][0], dSites = dSts)
        dSts = {GC.S_SPS_LPR1_S21: (GC.B_DO_PYL, self.lKAs0[2]),
                GC.S_SPS_LPR1_S28: (GC.B_DO_DEPYL, self.lPAs0[3])}
        self.adaptPSites(inpDat, self.llOI[0][1], dSites = dSts)
        print('Changed state to ' + self.idO + ' (' + self.descO + ').')

    def to_St_B_Trans_AT5G49770_NRT2p1(self, inpDat):
        self.idO = GC.S_ST_B_TRANS_AT5G49770_NRT2P1
        self.descO = 'State transition from AT5G49770-NRT2p1'
        self.llOI.append([self.lOO[1], self.llOI[0][1]])
        self.lOO = self.lOO[:1]
        dSts = {GC.S_SPS_KAS1_S839: (GC.B_DO_PYL, self.lKAs0[0])}
        self.adaptPSites(inpDat, self.llOI[0][0], dSites = dSts)
        print('Changed state to ' + self.idO + ' (' + self.descO + ').')

    def to_St_C_Int_NAR2p1_NRT2p1(self, inpDat):
        self.idO = GC.S_ST_C_INT_NAR2P1_NRT2P1
        self.descO = 'State interaction NAR2p1-NRT2p1'
        llOInt = [[self.lOO[0], self.llOI[0][1]]]
        lOOth = [self.llOI[0][0], self.llOI[1][0]]
        self.llOI, self.lOO = llOInt, lOOth
        dSts = {GC.S_SPS_KAS1_S870: (GC.B_DO_DEPYL, self.lPAs0[1])}
        self.adaptPSites(inpDat, self.lOO[0], dSites = dSts)
        dSts = {GC.S_SPS_LPR1_S21: (GC.B_DO_DEPYL, self.lPAs0[2]),
                GC.S_SPS_LPR1_S28: (GC.B_DO_PYL, self.lOO[1])}
        self.adaptPSites(inpDat, self.llOI[0][1], dSites = dSts)
        print('Changed state to ' + self.idO + ' (' + self.descO + ').')

    def to_St_D_Trans_NAR2p1_NRT2p1(self, inpDat):
        self.idO = GC.S_ST_D_TRANS_NAR2P1_NRT2P1
        self.descO = 'State transition from NAR2p1-NRT2p1'
        print('Changed state to ' + self.idO + ' (' + self.descO + ').')
    
###############################################################################
