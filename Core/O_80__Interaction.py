# -*- coding: utf-8 -*-
###############################################################################
# --- O_80__Interaction.py ----------------------------------------------------
###############################################################################
import Core.F_03__OTpFunctions as TF

from Core.O_00__Base import Base

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
    
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class Phosphorylation(Interaction):
    def __init__(self, inpDat, cOB, cAse, sSpSite, iTp = 80):
        super().__init__(inpDat, [cOB, cAse], iTp = iTp)    # order in list!
        self.idO = 'Pyl'
        self.descO = 'Phosphorylation'
        self.sSpS = sSpSite
        self.idAse = self.lOI[1].idO                        # 2nd obj. of list
        print('Initiated "Phosphorylation" object.')
        
    def doPyl(self):
        # check if first interaction partner has site to be phosphorylated
        return TF.doSiteChange(self.lOI[0], self.sSpS, self.idAse)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class Dephosphorylation(Interaction):
    def __init__(self, inpDat, cOB, cAse, sSpSite, iTp = 80):
        super().__init__(inpDat, [cOB, cAse], iTp = iTp)    # order in list!
        self.idO = 'DePyl'
        self.descO = 'Dephosphorylation'
        self.sSpS = sSpSite
        self.idAse = self.lOI[1].idO                        # 2nd obj. of list
        print('Initiated "Dephosphorylation" object.')
        
    def doDePyl(self):
        # check if first interaction partner has site to be dephosphorylated
        return TF.doSiteChange(self.lOI[0], self.sSpS, self.idAse,
                               doDePyl = True)

###############################################################################
