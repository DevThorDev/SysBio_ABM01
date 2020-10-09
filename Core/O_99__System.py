# -*- coding: utf-8 -*-
###############################################################################
# --- O_99__System.py ---------------------------------------------------------
###############################################################################
from operator import itemgetter

import Core.C_00__GenConstants as GC
import Core.F_00__GenFunctions as GF
import Core.F_03__OTpFunctions as TF

from Core.O_00__Base import Base
from Core.O_90__State import State_Int_Trans

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class System(Base):
    def __init__(self, inpDat, lStObj = [], iTp = 99):
        super().__init__(inpDat, iTp)
        self.idO = 'Sys'
        self.descO = 'System'
        self.lStO = lStObj
        self.dCncSMo = TF.createDCnc(self.dITp)
        self.addStObj(inpDat)
        self.getDictsStObj()
        print('Initiated "System" object.')
    
    def addStObj(self, inpDat):
        for sSt, nSt in self.dITp['dNStaObj'].items():
            for cSt in range(nSt):
                self.lStO.append(State_Int_Trans(inpDat, sSt))
    
    def getDictsStObj(self):
        self.dIDStO, self.dStO = {}, {}
        for cStO in self.lStO:
            GF.addToDictCt(self.dIDStO, cStO.idO)
            GF.addToDictL(self.dStO, cStO.idO, cStO)
    
    def printCncSMo(self):
        print('--- Concentrations of small molecules in system', self.idO)
        for s, cCnc in self.dCncSMo:
            print(s + ':\t' + str(cCnc))
    
    def printSystemIDs(self):
        print('*'*16, 'Counts of state objects contained in System:', '*'*18)
        for sSt, ctSt in self.dIDStO.items():
            print(sSt + ':', ctSt)
        print('*'*80)
    
    def printSystemObj(self):
        print('*'*16, 'Details of state objects contained in System:', '*'*17)
        for sSt, lSt in self.dStO.items():
            print('~'*20, 'States with ID', sSt, '~'*20)
            for cSt in lSt:
                cSt.printStateDetails()
        print('*'*80)
    
    def changeConcSMo(self, dO, cID = None):
        dCncCh = self.dITp['dConcChg']
        for sSMo in self.dCncSMo:
            cncCh = 0.
            for s in self.dIDStO:
                assert s in dCncCh[sSMo]
                cncCh += dCncCh[sSMo][s]*self.dIDStO[s]
            self.dCncSMo[sSMo] += cncCh*self.dITp['concChgScale']

    def reCalcReactHazardsCS(self, dITp, dO):
        dRRC, dH = dITp['dRRC'], dO['dH']
        # recalculate dH, which contains the h_i (i = 1,... len(dH))
        dH['A_B'] = dRRC['A_B']*dO['dN'][GC.S_ST_A_INT_AT5G49770_NRT2P1]
        dH['B_C'] = dRRC['B_C']*dO['dN'][GC.S_ST_B_TRANS_AT5G49770_NRT2P1]
        dH['C_D'] = dRRC['C_D']*dO['dN'][GC.S_ST_C_INT_NAR2P1_NRT2P1]
        dH['D_A'] = dRRC['D_A']*dO['dN'][GC.S_ST_D_TRANS_NAR2P1_NRT2P1]
        # h, the sum of the h_i, is the overall reaction hazard
        dO['h'] = sum(dH.values())
        # sort dH in ascending order for numerical stability
        dO['dH'] = {cK: cV/dO['h'] for cK, cV in
                    sorted(dH.items(), key = itemgetter(1))}
    
    def evolveOverTime(self):
        t, T, cTSt = self.dIG['tStart'], self.dIG['tMax'], 0
        dO = TF.iniDictOut(self.dITp, self.dCncSMo, t)
        while t < T:
            # change the concentrations of the small molecules
            self.changeConcSMo(dO)
            # for s, lOCSt in self.dStO.items():
            #     for oCSt in lOCSt:
            #         oCSt.changeConcSMo(t)
            # adapt the re-calc reaction hazards function to current system
            self.reCalcReactHazardsCS(self.dITp, dO)
            # do next event and update time with tToNext
            t += TF.nextEvent(self.dITp, dO, T, cTSt)
            # update the data storage matrix
            if t < T:
                TF.updateDictOut(self.dITp, dO, self.dCncSMo, t)
            cTSt += 1
        # self.dResEvo = TF.Gillespie_StateMod(self.dIG, self.dITp)
        self.dResEvo = dO['dRes']
        dR, sD, sF = self.dResEvo, self.dITp['sD_Sys'], self.dITp['sF_SysEvo']
        self.pFResEvo = TF.saveAsPdDfr(self.dIG, dR, sD, sF, overWrite = True)

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
        
#     def setToState(self, inpDat, lOIntSt, lPAsSt = []):
#         pass

###############################################################################
