from tkinter import *

class Vampire():
    def __init__(self):
        self._vWeakness = "Burns in the sun."
        self._rName = "Vampire"
        self._special = "Immortal creature, lives on the blood of its prey."
    _vWeakness = "Burns in the sun."
    _rName = "Vampire"
    _special = "Immortal creature, lives on the blood of its prey."
    
    def getRName(self):
        return self.rName
    def getSpecial(self):
        return self.special
    def getRWeakness(self):
        return self.rWeakness

class Clan(Vampire):
    def __init__(self, name, weakness, dis1, dis2, dis3):
        super().__init__()
        self._cName = name
        self._cWeakness = weakness
        self._dis1 = dis1
        self._dis2 = dis2
        self._dis3 = dis3

    def getCName(self):
        return self._cName
    def getCWeakness(self):
        return self._cWeakness
    def getCDisciplines(self):
        x = []
        x.append(self._dis1.getDName())
        x.append(self._dis2.getDName())
        x.append(self._dis3.getDName())
        return x

class Discipline():
    def __init__(self, name, desc):
        self.dName = name
        #self.level = level
        self.desc = desc
    
    def getDName(self):
        return self.dName
    #def getLevel(self):
        #return self.level
    def getDesc(self):
        return self.desc

class Sect():
    def __init__(self, name, rivals):
        self.sName = name
        self.rivals = rivals
    def getSName(self):
        return self.sName
    def getRivals(self):
        return self.rivals

class Coterie():
    def __init__(self, name, sect):
        self.name = name
        self.sect = sect
        self.members = []
    def setMember(self, member):
        self.members.append(member)
    def getMembers(self):
        return self.members

class Status():
    def __init__(self, name, duties, desc):
        self.pName = name
        self.duties = duties
        self.desc = desc
    def getPName(self):
        return self.pName
    def getDuties(self):
        return self.duties
    def getDesc(self):
        return self.desc

class City():
    def __init__(self, name):
        self.name = name
        self.admin = []
    def setAdmin(self, admin):
        self.admin.append(admin)
    def setName(self,name):
        self.name = name
    def getName(self):
        return self.name
    def getAdmin(self):
        return self.admin

class AdminS():
    def __init__(self, sector, owner, control):
        self.sector = sector
        self.owner = owner
        self.control = control

class Specialist():
    def __init__(self, name, function):
        self.name = name
        self.function = function

class Boon():
    def __init__(self, btype, owner, giver):
        self.btype = btype
        self.owner = owner
        self.giver = giver
    def setType(self, btype):
        self.btype = btype
    def setOwner(self, owner):
        self.owner = owner
    def setGiver(self, giver):
        self.giver = giver
    def getOwner(self):
        return self.owner
    def getGiver(self):
        return self.giver
    def getType(self):
        return self.btype

class Character():
    def __init__(self):
        super().__init__()
        self.name = "name"
        self.gen = 13
        self.age = 30
        self.info = "info"
        self.sect = None
        self.status = None
        self.clan = None

    def setName(self, name):
        self.name = name
    def setGen(self, gen):
        self.gen = gen
    def setAge(self, age):
        self.age = age
    def setInfo(self, info):
        self.info = info
    def setSect(self, sect):
        self.sect = sect
    def setStatus(self, status):
        self.status = status
    def setClan(self, clan):
        self.clan = clan
    def getName(self):
        return self.name
    def getGen(self):
        return self.gen
    def getAge(self):
        return self.age
    def getInfo(self):
        return self.info
    def getStatus(self):
        return self.status
    def getSect(self):
        return self.sect
    def getClan(self):
        return self.clan
