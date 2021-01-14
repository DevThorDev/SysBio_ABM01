# -*- coding: utf-8 -*-
###############################################################################
# --- O_80__Interaction.py ----------------------------------------------------
###############################################################################
import Core.C_00__GenConstants as GC
import Core.F_03__OTpFunctions as TF

from Core.O_00__Base import Base

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class Interaction(Base):
    def __init__(self, inpDat, cOInt, lSCpAs, iTp = 80):
        super().__init__(inpDat, iTp)
        self.idO = GC.ID_INT
        self.descO = 'Interaction'
        self.cOI = cOInt
        self.lSCpA = lSCpAs
        # print('Initiated "Interaction" object.')

    def printObjInt(self):
        idO, descO = self.cOI.yieldIDDesc()
        t = (idO, descO, self.cOI.dITp['strNSpec'], self.cOI.dITp['strCS'])
        print(GC.S_DASH*8, 'Object in interaction:', GC.S_DASH*8)
        print([GC.S_DASH*2 + ' ' + str(s) + ' ' + GC.S_DASH*2 for s in t])

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class Phosphorylation(Interaction):
    def __init__(self, inpDat, cOInt, lSCpAs, sSpSite, iTp = 80):
        super().__init__(inpDat, cOInt, lSCpAs, iTp = iTp)
        self.idO = GC.ID_PYL
        self.descO = 'Phosphorylation'
        self.sSpS = sSpSite
        # print('Initiated "Phosphorylation" object.')

    def doPyl(self):
        # check if first interaction partner has site to be phosphorylated
        return TF.doSiteChange(self.cOI, self.sSpS, self.lSCpA, doPyl = True)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class Dephosphorylation(Interaction):
    def __init__(self, inpDat, cOInt, lSCpAs, sSpSite, iTp = 80):
        super().__init__(inpDat, cOInt, lSCpAs, iTp = iTp)
        self.idO = GC.ID_DPY
        self.descO = 'Dephosphorylation'
        self.sSpS = sSpSite
        # print('Initiated "Dephosphorylation" object.')

    def doDePyl(self):
        # check if first interaction partner has site to be dephosphorylated
        return TF.doSiteChange(self.cOI, self.sSpS, self.lSCpA, doPyl = False)

###############################################################################
