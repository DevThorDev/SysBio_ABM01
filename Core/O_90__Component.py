# -*- coding: utf-8 -*-
###############################################################################
# --- O_90__Component.py ------------------------------------------------------
###############################################################################
import Core.C_00__GenConstants as GC
import Core.F_00__GenFunctions as GF
import Core.F_01__SpcFunctions as SF
import Core.F_02__PltFunctions as PF
import Core.F_03__OTpFunctions as TF

from Core.O_00__Base import Base
from Core.O_02__Protein import (Kinase_HPCAL1, Kinase_X, Kinase0,
                                Phosphatase0, Protein_NRT2p1, Protein_NAR2p1)
from Core.O_03__Metabolite import SMo_NO3_1m, SMo_H2PO4_1m
from Core.O_80__Interaction import Phosphorylation, Dephosphorylation

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class ComponentBase(Base):
    def __init__(self, inpDat, dOComp, llOInt = [], lOOth = [], iTp = 90):
        super().__init__(inpDat, iTp = iTp)
        for cLOInt in llOInt:
            assert len(cLOInt) >= 2
        self.idO = 'CpBase'
        self.descO = 'ComponentBase'
        if not hasattr(self, 'sSt'):
            self.sSt = '____'
        if not hasattr(self, 'dOSta'):
            self.dOSta = dOComp
        self.llOI = llOInt
        self.lOO = lOOth
        self.complementLO(inpDat, dOComp)
        self.prTrans = 0
        self.dCncEvo = {GC.S_TIME: [self.dIG['tStart']],
                        GC.S_CONC_NO3_1M: [self.lSMo[0].cCnc],
                        GC.S_CONC_H2PO4_1M: [self.lSMo[1].cCnc],
                        GC.S_COMP: [self.idO]}
        # print('Initiated "ComponentBase" object.')

    def complementLO(self, inpDat, dOComp):
        self.lSMo = dOComp[GC.SPC_L_SMO]
        self.dCnc = {cO.idO: [cO.cCnc, cO.dITp['thrLowConc'],
                              cO.dITp['thrHighConc']] for cO in self.lSMo}
        lOSy = GF.lItToUniqueList(self.llOI) + self.lOO + self.lSMo
        lID = TF.complLSpec(inpDat, lOSy, sTp = 'KAs', sD = 'Pyl')
        self.lKAs0 = [Kinase0(inpDat, cID = ID) for ID in lID if ID not in
                      [GC.ID_KAS_X]]        # as Kinase_X is a specific kinase
        lID = TF.complLSpec(inpDat, lOSy, sTp = 'PAs', sD = 'DePyl')
        self.lPAs0 = [Phosphatase0(inpDat, cID = ID) for ID in lID]
        self.lKAs = [self.lKAs0[k] for k in range(3)]
        self.lKAs += [self.dOSta[GC.SPC_KAS_X]]
        self.lPAs = [self.lPAs0[k] for k in range(4)]

    def __str__(self):
        sIn = ('++++ Component ' + self.idO + ' (' + self.sSt + ' / ' +
               self.descO + '):')
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
        print('-- Component details:')
        for cO in list(set(GF.lItToUniqueList(self.llOI) + self.lOO +
                           self.lKAs0 + self.lPAs0 + self.lSMo)):
            cO.printMolSpecSites()

    def printComponentDetails(self):
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

    # def savePlotDCncEvo(self, kSt = 0, llIPlot = None, iSMo = 0):
    #     assert len(self.lSMo) > iSMo
    #     sNSt, sKSt = str(self.dIG['nStates']), str(kSt)
    #     dITpSMo, s0 = self.lSMo[iSMo].dITp, '0'*(len(sNSt) - len(sKSt))
    #     sF = dITpSMo['sPlt_Conc'] + dITpSMo['sF_SMo'] + GC.S_USC + s0 + sKSt
    #     TF.saveAsPdDfr(self.dIG, self.dCncEvo, dITpSMo['sD_SMo'], sF,
    #                    overWr = True)
    #     if llIPlot is not None:
    #         lIPlot = llIPlot[iSMo]
    #         sFPlt = sF + '__' + GC.S_USC.join([str(iPlot) for iPlot in lIPlot])
    #         sP = TF.getPF(self.dIG['sPPlt'], dITpSMo['sD_SMo'], sFPlt,
    #                       sFExt = GC.S_EXT_PDF)
    #         PF.plotDCncEvo(dITpSMo[GC.S_D_PLT][dITpSMo['sPlt_Conc']],
    #                        self.dCncEvo, sP, lIPlot)

    def adaptPSites(self, inpDat, cO, sSt):
        for sSpS, dI in GC.DS_SPS[cO.idO].items():
            sPylDPy, cAs = SF.setPylDPy(dI, sSt, self.lKAs, self.lPAs)
            if sPylDPy == GC.B_DO_PYL:
                _ = Phosphorylation(inpDat, cO, cAs, sSpS).doPyl()
                # if Phosphorylation(inpDat, cO, cAs, sSpS).doPyl():
                #     print('Phosphorylation at site', sSpS, 'happened!')
            elif sPylDPy == GC.B_DO_DEPYL:
                _ = Dephosphorylation(inpDat, cO, cAs, sSpS).doDePyl()
                # if Dephosphorylation(inpDat, cO, cAs, sSpS).doDePyl():
                #     print('Dephosphorylation at site', sSpS, 'happened!')

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

class Component(ComponentBase):
    def __init__(self, inpDat, sComp, iTp = 90):
        self.sSt = sComp
        self.createdOComp(inpDat)
        if sComp in inpDat.dI['dS_St'][GC.S_ST_A_KIN_INT]:
            self.ini_St_A_Kin_Int(inpDat, sComp, iTp = iTp)
        elif sComp in inpDat.dI['dS_St'][GC.S_ST_B_KIN_TRA]:
            self.ini_St_B_Kin_Tra(inpDat, sComp, iTp = iTp)
        elif sComp in inpDat.dI['dS_St'][GC.S_ST_C_SPR_INT]:
            self.ini_St_C_SPr_Int(inpDat, sComp, iTp = iTp)
        elif sComp in inpDat.dI['dS_St'][GC.S_ST_D_SPR_TRA]:
            self.ini_St_D_SPr_Tra(inpDat, sComp, iTp = iTp)
        else:
            self.idO = 'Cp'
            self.descO = 'Component'
        # print('Initiated "Component" object ' + sComp + '.')

    def createdOComp(self, inpDat, ddVOvwr = {}, iV = 0):
        # Kinases KAsHPCAL1, KAsX ---------------------------------------------
        KAsHPCAL1 = Kinase_HPCAL1(inpDat)
        KAsX = Kinase_X(inpDat)
        # Large protein NRT2.1 ------------------------------------------------
        NRT2p1 = Protein_NRT2p1(inpDat)
        # Small protein NAR2.1 ------------------------------------------------
        NAR2p1 = Protein_NAR2p1(inpDat)
        # Small molecules NO3- and H2PO4- -------------------------------------
        NO3_1m = SMo_NO3_1m(inpDat)
        H2PO4_1m = SMo_H2PO4_1m(inpDat)
        # overwrite type dict. input of small molecules with values of ddVOvwr
        NO3_1m.overwInpV(ddVOvwr, iV)
        H2PO4_1m.overwInpV(ddVOvwr, iV)
        # Create initial component --------------------------------------------
        self.dOSta = {GC.SPC_KAS_A: KAsHPCAL1,
                      GC.SPC_KAS_X: KAsX,
                      GC.SPC_LPR_A: NRT2p1,
                      GC.SPC_SPR_A: NAR2p1,
                      GC.SPC_L_SMO: [NO3_1m, H2PO4_1m]}

    def ini_St_A_Kin_Int(self, inpDat, sSt, iTp = 90):
        llOI = [[self.dOSta[GC.SPC_KAS_A], self.dOSta[GC.SPC_LPR_A]]]
        lOO = [self.dOSta[GC.SPC_SPR_A], self.dOSta[GC.SPC_KAS_X]]
        super().__init__(inpDat, self.dOSta, llOI, lOO, iTp = iTp)
        self.idO = GC.S_ST_A_KIN_INT
        self.descO = 'State interaction HPCAL1-NRT2p1'
        self.adaptPSites(inpDat, self.dOSta[GC.SPC_KAS_A], sSt)
        self.adaptPSites(inpDat, self.dOSta[GC.SPC_LPR_A], sSt)

    def ini_St_B_Kin_Tra(self, inpDat, sSt, iTp = 90):
        llOI = [[self.dOSta[GC.SPC_KAS_A], self.dOSta[GC.SPC_LPR_A]],
                [self.dOSta[GC.SPC_KAS_X], self.dOSta[GC.SPC_LPR_A]]]
        lOO = [self.dOSta[GC.SPC_SPR_A]]
        super().__init__(inpDat, self.dOSta, llOI, lOO, iTp = iTp)
        self.idO = GC.S_ST_B_KIN_TRA
        self.descO = 'State transition from HPCAL1-NRT2p1'
        self.adaptPSites(inpDat, self.dOSta[GC.SPC_KAS_A], sSt)
        self.adaptPSites(inpDat, self.dOSta[GC.SPC_LPR_A], sSt)

    def ini_St_C_SPr_Int(self, inpDat, sSt, iTp = 90):
        llOI = [[self.dOSta[GC.SPC_SPR_A], self.dOSta[GC.SPC_LPR_A]]]
        lOO = [self.dOSta[GC.SPC_KAS_A], self.dOSta[GC.SPC_KAS_X]]
        super().__init__(inpDat, self.dOSta, llOI, lOO, iTp = iTp)
        self.idO = GC.S_ST_C_SPR_INT
        self.descO = 'State interaction NAR2p1-NRT2p1'
        self.adaptPSites(inpDat, self.dOSta[GC.SPC_KAS_A], sSt)
        self.adaptPSites(inpDat, self.dOSta[GC.SPC_LPR_A], sSt)

    def ini_St_D_SPr_Tra(self, inpDat, sSt, iTp = 90):
        llOI = [[self.dOSta[GC.SPC_SPR_A], self.dOSta[GC.SPC_LPR_A]]]
        lOO = [self.dOSta[GC.SPC_KAS_A], self.dOSta[GC.SPC_KAS_X]]
        super().__init__(inpDat, self.dOSta, llOI, lOO, iTp = iTp)
        self.idO = GC.S_ST_D_SPR_TRA
        self.descO = 'State transition from NAR2p1-NRT2p1'
        self.adaptPSites(inpDat, self.dOSta[GC.SPC_KAS_A], sSt)
        self.adaptPSites(inpDat, self.dOSta[GC.SPC_LPR_A], sSt)

    # def to_other_St(self, inpDat, sStN):
    #     pass

    # def to_St_A_Kin_Int(self, inpDat, sStN):
    #     self.idO = GC.S_ST_A_KIN_INT
    #     self.descO = 'State interaction HPCAL1-NRT2p1'
    #     self.lOO[0], self.llOI[0][0] = self.llOI[0][0], self.lOO[0]
    #     dSts = {GC.S_SPS_KAS1_S839: (GC.B_DO_DEPYL, self.lPAs0[0]),
    #             GC.S_SPS_KAS1_S870: (GC.B_DO_PYL, self.lKAs0[1])}
    #     self.adaptPSites(inpDat, self.llOI[0][0]
    #     dSts = {GC.S_SPS_LPR1_S21: (GC.B_DO_PYL, self.lKAs0[2]),
    #             GC.S_SPS_LPR1_S28: (GC.B_DO_DEPYL, self.lPAs0[3])}
    #     self.adaptPSites(inpDat, self.llOI[0][1]
    #     print('Changed state to ' + self.idO + ' (' + self.descO + ').')

    # def to_St_B_Kin_Tra(self, inpDat, sStN):
    #     self.idO = GC.S_ST_B_KIN_TRA
    #     self.descO = 'State transition from HPCAL1-NRT2p1'
    #     self.llOI.append([self.lOO[1], self.llOI[0][1]])
    #     self.lOO = self.lOO[:1]
    #     dSts = {GC.S_SPS_KAS1_S839: (GC.B_DO_PYL, self.lKAs0[0])}
    #     self.adaptPSites(inpDat, self.llOI[0][0]
    #     print('Changed state to ' + self.idO + ' (' + self.descO + ').')

    # def to_St_C_SPr_Int(self, inpDat, sStN):
    #     self.idO = GC.S_ST_C_SPR_INT
    #     self.descO = 'State interaction NAR2p1-NRT2p1'
    #     llOInt = [[self.lOO[0], self.llOI[0][1]]]
    #     lOOth = [self.llOI[0][0], self.llOI[1][0]]
    #     self.llOI, self.lOO = llOInt, lOOth
    #     dSts = {GC.S_SPS_KAS1_S870: (GC.B_DO_DEPYL, self.lPAs0[1])}
    #     self.adaptPSites(inpDat, self.lOO[0]
    #     dSts = {GC.S_SPS_LPR1_S21: (GC.B_DO_DEPYL, self.lPAs0[2]),
    #             GC.S_SPS_LPR1_S28: (GC.B_DO_PYL, self.lOO[1])}
    #     self.adaptPSites(inpDat, self.llOI[0][1]
    #     print('Changed state to ' + self.idO + ' (' + self.descO + ').')

    # def to_St_D_SPr_Tra(self, inpDat, sStN):
    #     self.idO = GC.S_ST_D_SPR_TRA
    #     self.descO = 'State transition from NAR2p1-NRT2p1'
    #     print('Changed state to ' + self.idO + ' (' + self.descO + ').')

###############################################################################