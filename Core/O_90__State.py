# -*- coding: utf-8 -*-
###############################################################################
# --- O_90__State.py ----------------------------------------------------------
###############################################################################
import Core.C_00__GenConstants as GC
import Core.F_00__GenFunctions as GF
import Core.F_02__PltFunctions as PF
import Core.F_03__OTpFunctions as TF

from Core.O_00__Base import Base
from Core.O_02__Protein import (Kinase_AT5G49770, Kinase_X, Kinase0,
                                Phosphatase0, Protein_NRT2p1, Protein_NAR2p1)
from Core.O_03__Metabolite import SMo_NO3_1m, SMo_H2PO4_1m
from Core.O_80__Interaction import Phosphorylation, Dephosphorylation

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class State(Base):
    def __init__(self, inpDat, dOState, llOInt = [], lOOth = [], iTp = 90):
        super().__init__(inpDat, iTp = iTp)
        for cLOInt in llOInt:
            assert len(cLOInt) >= 2
        self.idO = 'Sta'
        self.descO = 'State'
        if not hasattr(self, 'dOSta'):
            self.dOSta = dOState
        self.llOI = llOInt
        self.lOO = lOOth
        self.complementLO(inpDat, dOState)
        self.prTrans = 0
        self.dCncEvo = {GC.S_TIME: [self.dIG['tStart']],
                        GC.S_CONC_NO3_1M: [self.lSMo[0].cCnc],
                        GC.S_CONC_H2PO4_1M: [self.lSMo[1].cCnc],
                        GC.S_STATE: [self.idO]}
        # print('Initiated "State" object.')
        
    def complementLO(self, inpDat, dOState):
        self.lSMo = dOState[GC.SPC_L_SMO]
        self.dCnc = {cO.idO: [cO.cCnc, cO.dITp['thrLowConc'],
                              cO.dITp['thrHighConc']] for cO in self.lSMo}
        lOSy = GF.lItToUniqueList(self.llOI) + self.lOO + self.lSMo
        lID = TF.complLSpec(inpDat, lOSy, sTp = 'KAs', sD = 'Pyl')
        self.lKAs0 = [Kinase0(inpDat, cID = ID) for ID in lID if ID not in
                      [GC.ID_KAS_X]]        # as Kinase_X is a specific kinase
        lID = TF.complLSpec(inpDat, lOSy, sTp = 'PAs', sD = 'DePyl')
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
    
    def savePlotDCncEvo(self, kSt = 0, llIPlot = None, iSMo = 0):
        assert len(self.lSMo) > iSMo
        sNSt, sKSt = str(self.dIG['nStates']), str(kSt)
        dITpSMo, s0 = self.lSMo[iSMo].dITp, '0'*(len(sNSt) - len(sKSt))
        sF = dITpSMo['sPlt_Conc'] + dITpSMo['sF_SMo'] + '_' + s0 + sKSt
        TF.saveAsPdDfr(self.dIG, self.dCncEvo, dITpSMo['sD_SMo'], sF,
                       overWrite = True)
        if llIPlot is not None:
            lIPlot = llIPlot[iSMo]
            sFPlt = sF + '__' + '_'.join([str(iPlot) for iPlot in lIPlot])
            sP = TF.getPF(self.dIG['sPPlt'], dITpSMo['sD_SMo'], sFPlt,
                          sFExt = GC.S_EXT_PDF)
            PF.plotDCncEvo(dITpSMo[GC.S_D_PLT][dITpSMo['sPlt_Conc']],
                           self.dCncEvo, sP, lIPlot)
    
    def changePSite(self, inpDat, cO):
        if self.cM == GC.M_STOCH:
            pass
        else:
            pass
    
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
        
    def changeConcSMo(self, t, cID = None):
        for cSMo in self.lSMo:
            if cID is None or cSMo.idO == cID:
                cSMo.changeConc(t, self.idO)
                assert cSMo.idO in self.dCnc
                self.dCnc[cSMo.idO][0] = cSMo.cCnc
        lCEl = [t, self.lSMo[0].cCnc, self.lSMo[1].cCnc, self.idO]
        GF.appendToDictL(self.dCncEvo, lCEl)

class State_Int_Trans(State):
    def __init__(self, inpDat, sState, iTp = 90):
        self.createDOState(inpDat)
        if sState == GC.S_ST_A_KIN_INT:
            self.ini_St_A_Int_AT5G49770_NRT2p1(inpDat, iTp = iTp)
        elif sState == GC.S_ST_B_KIN_TRA:
            self.ini_St_B_Trans_AT5G49770_NRT2p1(inpDat, iTp = iTp)
        elif sState == GC.S_ST_C_SPR_INT:
            self.ini_St_C_Int_NAR2p1_NRT2p1(inpDat, iTp = iTp)
        elif sState == GC.S_ST_D_SPR_TRA:
            self.ini_St_D_Trans_NAR2p1_NRT2p1(inpDat, iTp = iTp)
        else:
            self.idO = 'St_Int_Trans'
            self.descO = 'State interaction or transition'
        # print('Initiated "State_Int_Trans" object.')
    
    def createDOState(self, inpDat, ddVOvwr = {}, iV = 0):
        # Kinases KAsAT5G49770, KAsX ------------------------------------------
        KAsAT5G49770 = Kinase_AT5G49770(inpDat)
        KAsX = Kinase_X(inpDat)
        # Large protein NRT2.1 -----------------------------------------------
        NRT2p1 = Protein_NRT2p1(inpDat)
        # Small protein NAR2.1 ------------------------------------------------
        NAR2p1 = Protein_NAR2p1(inpDat)
        # Small molecules NO3- and H2PO4- -------------------------------------
        NO3_1m = SMo_NO3_1m(inpDat)
        H2PO4_1m = SMo_H2PO4_1m(inpDat)
        # overwrite type dict. input of small molecules with values of ddVOvwr 
        NO3_1m.overwInpV(ddVOvwr, iV)
        H2PO4_1m.overwInpV(ddVOvwr, iV)
        # Create initial state ------------------------------------------------
        self.dOSta = {GC.SPC_KAS_A: KAsAT5G49770,
                      GC.SPC_KAS_X: KAsX,
                      GC.SPC_LPR_A: NRT2p1,
                      GC.SPC_SPR_A: NAR2p1,
                      GC.SPC_L_SMO: [NO3_1m, H2PO4_1m]}

    def ini_St_A_Int_AT5G49770_NRT2p1(self, inpDat, iTp = 90):
        llOI = [[self.dOSta[GC.SPC_KAS_A], self.dOSta[GC.SPC_LPR_A]]]
        lOO = [self.dOSta[GC.SPC_SPR_A], self.dOSta[GC.SPC_KAS_X]]
        super().__init__(inpDat, self.dOSta, llOI, lOO, iTp = iTp)
        self.idO = GC.S_ST_A_KIN_INT
        self.descO = 'State interaction AT5G49770-NRT2p1'
        dSts = {GC.S_SPS_KAS1_S839: (GC.B_DO_DEPYL, self.lPAs0[0]),
                GC.S_SPS_KAS1_S870: (GC.B_DO_PYL, self.lKAs0[1])}
        self.adaptPSites(inpDat, self.dOSta[GC.SPC_KAS_A], dSites = dSts)
        dSts = {GC.S_SPS_LPR1_S21: (GC.B_DO_PYL, self.lKAs0[2]),
                GC.S_SPS_LPR1_S28: (GC.B_DO_DEPYL, self.lPAs0[3])}
        self.adaptPSites(inpDat, self.dOSta[GC.SPC_LPR_A], dSites = dSts)

    def ini_St_B_Trans_AT5G49770_NRT2p1(self, inpDat, iTp = 90):
        llOI = [[self.dOSta[GC.SPC_KAS_A], self.dOSta[GC.SPC_LPR_A]],
                [self.dOSta[GC.SPC_KAS_X], self.dOSta[GC.SPC_LPR_A]]]
        lOO = [self.dOSta[GC.SPC_SPR_A]]
        super().__init__(inpDat, self.dOSta, llOI, lOO, iTp = iTp)
        self.idO = GC.S_ST_B_KIN_TRA
        self.descO = 'State transition from AT5G49770-NRT2p1'
        dSts = {GC.S_SPS_KAS1_S839: (GC.B_DO_PYL, self.lKAs0[0]),
                GC.S_SPS_KAS1_S870: (GC.B_DO_PYL, self.lKAs0[1])}
        self.adaptPSites(inpDat, self.dOSta[GC.SPC_KAS_A], dSites = dSts)
        dSts = {GC.S_SPS_LPR1_S21: (GC.B_DO_PYL, self.lKAs0[2]),
                GC.S_SPS_LPR1_S28: (GC.B_DO_DEPYL, self.lPAs0[3])}
        self.adaptPSites(inpDat, self.dOSta[GC.SPC_LPR_A], dSites = dSts)

    def ini_St_C_Int_NAR2p1_NRT2p1(self, inpDat, iTp = 90):
        llOI = [[self.dOSta[GC.SPC_SPR_A], self.dOSta[GC.SPC_LPR_A]]]
        lOO = [self.dOSta[GC.SPC_KAS_A], self.dOSta[GC.SPC_KAS_X]]
        super().__init__(inpDat, self.dOSta, llOI, lOO, iTp = iTp)
        self.idO = GC.S_ST_C_SPR_INT
        self.descO = 'State interaction NAR2p1-NRT2p1'
        dSts = {GC.S_SPS_KAS1_S839: (GC.B_DO_PYL, self.lKAs0[0]),
                GC.S_SPS_KAS1_S870: (GC.B_DO_DEPYL, self.lPAs0[1])}
        self.adaptPSites(inpDat, self.dOSta[GC.SPC_KAS_A], dSites = dSts)
        dSts = {GC.S_SPS_LPR1_S21: (GC.B_DO_DEPYL, self.lPAs0[2]),
                GC.S_SPS_LPR1_S28: (GC.B_DO_PYL, self.dOSta[GC.SPC_KAS_X])}
        self.adaptPSites(inpDat, self.dOSta[GC.SPC_LPR_A], dSites = dSts)

    def ini_St_D_Trans_NAR2p1_NRT2p1(self, inpDat, iTp = 90):
        llOI = [[self.dOSta[GC.SPC_SPR_A], self.dOSta[GC.SPC_LPR_A]]]
        lOO = [self.dOSta[GC.SPC_KAS_A], self.dOSta[GC.SPC_KAS_X]]
        super().__init__(inpDat, self.dOSta, llOI, lOO, iTp = iTp)
        self.idO = GC.S_ST_D_SPR_TRA
        self.descO = 'State transition from NAR2p1-NRT2p1'
        dSts = {GC.S_SPS_KAS1_S839: (GC.B_DO_PYL, self.lKAs0[0]),
                GC.S_SPS_KAS1_S870: (GC.B_DO_DEPYL, self.lPAs0[1])}
        self.adaptPSites(inpDat, self.dOSta[GC.SPC_KAS_A], dSites = dSts)
        dSts = {GC.S_SPS_LPR1_S21: (GC.B_DO_DEPYL, self.lPAs0[2]),
                GC.S_SPS_LPR1_S28: (GC.B_DO_PYL, self.dOSta[GC.SPC_KAS_X])}
        self.adaptPSites(inpDat, self.dOSta[GC.SPC_LPR_A], dSites = dSts)

    def to_St_A_Int_AT5G49770_NRT2p1(self, inpDat):
        self.idO = GC.S_ST_A_KIN_INT
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
        self.idO = GC.S_ST_B_KIN_TRA
        self.descO = 'State transition from AT5G49770-NRT2p1'
        self.llOI.append([self.lOO[1], self.llOI[0][1]])
        self.lOO = self.lOO[:1]
        dSts = {GC.S_SPS_KAS1_S839: (GC.B_DO_PYL, self.lKAs0[0])}
        self.adaptPSites(inpDat, self.llOI[0][0], dSites = dSts)
        print('Changed state to ' + self.idO + ' (' + self.descO + ').')

    def to_St_C_Int_NAR2p1_NRT2p1(self, inpDat):
        self.idO = GC.S_ST_C_SPR_INT
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
        self.idO = GC.S_ST_D_SPR_TRA
        self.descO = 'State transition from NAR2p1-NRT2p1'
        print('Changed state to ' + self.idO + ' (' + self.descO + ').')
    
###############################################################################
