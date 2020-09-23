# -*- coding: utf-8 -*-
###############################################################################
# --- O_80__Interaction.py ----------------------------------------------------
###############################################################################
# import Core.C_00__GenConstants as GC
# import Core.F_00__GenFunctions as GF
import Core.F_03__OTpFunctions as TF

from Core.O_00__Base import Base
from Core.O_02__Protein import Kinase, LargeProtein, SmallProtein

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class Interaction(Base):
    def __init__(self, inpDat, lOInt = [], iTp = 80):
        super().__init__(inpDat, iTp)
        assert len(lOInt) >= 2
        self.idO = 'Int'
        self.descO = 'Interaction'
        self.lOI = lOInt
        print('Initiated "Interaction" object.')

    def printObjInt(self):
        lTIP = []
        for cO in self.lOI:
            idO, descO = cO.yieldIDDesc()
            (strNSpec, strCS) = (cO.dITp['strNSpec'], cO.dITp['strCS'])
            lTIP.append((idO, descO, strNSpec, strCS))
        print('Interaction partners:')
        for cT in lTIP:
            print('\t' + str(cT))

    def startInter(self):
        pass
        # interDone = False
        # dSpS = self.lOI[0].dITp['dInfSpS'][self.sSpS]
        # if dSpS['Stat'] == GC.B_NOT_PYL and self.sPylAse in dSpS['Pyl']:
        #     dSpS['Stat'] = GC.B_IS_PYL
        #     self.lOI[0].dSpS[self.sSpS].sSPTM = dSpS['Stat']
        #     interDone = True
        # return interDone
    
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class Phosphorylation(Interaction):
    def __init__(self, inpDat, cOB, cPAs, sSpSite, iTp = 80):
        super().__init__(inpDat, [cOB, cPAs], iTp = iTp)    # order in list!
        self.idO = 'Pyl'
        self.descO = 'Phosphorylation'
        self.sSpS = sSpSite
        self.sPylAse = self.lOI[1].dITp['strCS']        # 2nd obj. of list
        print('Initiated "Phosphorylation" object.')
        
    def doPyl(self):
        # check if first interaction partner has site to be phosphorylated
        return TF.doSiteChange(self.lOI[0], self.sSpS, self.sPylAse)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class Dephosphorylation(Interaction):
    def __init__(self, inpDat, cOB, cPAs, sSpSite, iTp = 80):
        super().__init__(inpDat, [cOB, cPAs], iTp = iTp)    # order in list!
        self.idO = 'DePyl'
        self.descO = 'Dephosphorylation'
        self.sSpS = sSpSite
        self.sDePylAse = self.lOI[1].dITp['strCS']      # 2nd obj. of list
        print('Initiated "Dephosphorylation" object.')
        
    def doDePyl(self):
        # check if first interaction partner has site to be dephosphorylated
        return TF.doSiteChange(self.lOI[0], self.sSpS, self.sDePylAse,
                               doDePyl = True)

###############################################################################
