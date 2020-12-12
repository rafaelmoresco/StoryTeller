from classes import *
from tkinter import *
import os
import json

####Criação das Classes Fixas####
#Disciplinas
animalism = Discipline("Animalism", "Animalism allows the vampire to amplify his intensely primordial nature.")
auspex = Discipline("Auspex", "Auspex gives the vampire uncanny sensory abilities.")
celerity = Discipline("Celerity", "Celerity allows Assamites, Brujah, and Toreadors to move with astonishing swiftness, becoming practically a blur.")
chimerstry = Discipline("Chimerstry", "The Discipline is, fundamentally, an art of conjuration that converts the vampire’s will into phantoms that confound the senses and technology alike.")
dementation = Discipline("Dementation", "Dementation is the Discipline that allows a vampire to focus and channel madness into the minds of those around him.")
dominate = Discipline("Dominate", "Dominate is one of the most dreaded of Disciplines. It is a vampire’s ability to inﬂuence another person’s thoughts and actions through her own force of will.")
fortitude = Discipline("Fortitude", "Vampires with this Discipline can shrug off agonizing trauma and make the most bone-shattering impact look like a ﬂesh wound.")
necromancy = Discipline("Necromancy", "Necromancy is both a Discipline and a school of blood magic devoted to the command of the souls of the dead.")
obfuscate = Discipline("Obfuscate", "Obfuscate is the uncanny ability for Kindred to conceal themselves from sight, sometimes even in full view of a crowd.")
obtenebration = Discipline("Obtenebration", "The signature power of the Lasombra, Obtenebration grants the vampire power over darkness itself.")
potence = Discipline("Potence", "Kindred endowed with Potence possess unnatural strength.")
presence = Discipline("Presence", "Presence is the Discipline of emotional manipulation.")
protean = Discipline("Protean", "Protean allows the Kindred the mystical ability to manipulate his physical form.")
quietus = Discipline("Quietus", "he Discipline of silent death, Quietus is practiced by those of Clan Assamite.")
serpentis = Discipline("Serpentis", "Serpentis is believed to be the legacy of Set himself, a gift to his children.")
thaumaturgy = Discipline("Thaumaturgy", "Thaumaturgy encompasses blood magic and other sorcerous arts available to Kindred.")
vicissitude = Discipline("Vicissitude", "Vicissitude is the signature power of the Tzimisce, and is rarely shared outside the Clan.")
#Clãs
assaamite = Clan("Assamite", "Should an Assamite consume the blood of another Kindred, she suffers one automatic level of unsoakable lethal damage per blood point imbibed.", celerity, obfuscate, quietus)
brujah = Clan("Brujah", "The diffculties of rolls to resist or guide frenzy (p. 298) are two higher than normal.", celerity, potence, presence)
settite = Clan("Followers of Set", "Add two health levels to damage caused by exposure to sunlight. Setites also lose one die from dice pools for actions taken in bright light.", obfuscate, presence, serpentis)
gangrel = Clan("Gangrel", "Every time a Gangrel frenzies, she acquires a temporary animal characteristic.", animalism, fortitude, protean)
giovanni = Clan("Giovanni", "The Kiss of a Giovanni vampire causes excruciating pain in mortal vessels who receive it.", dominate, necromancy, potence)
lasombra = Clan("Lasombra", "Lasombra vampires cast no reﬂections.", dominate, obtenebration, potence)
malkavian = Clan("Malkavian", "All members of Clan Malkavian suffer from a permanent, incurable derangement.", auspex, dementation, obfuscate)
nosferatu = Clan("Nosferatu", "All Nosferatu have an Appearance score of zero, and they may never improve it.", animalism, obfuscate, potence)
ravnos = Clan("Ravnos", "Each Ravnos has a penchant for some sort of vice — lying, cruelty, or theft, for example.", animalism, chimerstry, fortitude)
toreador = Clan("Toreador", "When a Toreador experiences something truly remarkable the player must make a Self-Control or Instincts roll (diffculty 6).", auspex, celerity, presence)
tremere = Clan("Tremere", "It takes only two draughts of another vampire’s blood for a Tremere to become blood bound instead of the normal three.", auspex, dominate, thaumaturgy)
tzimisce = Clan("Tzimisce", "The Tzimisce are inextricably tied to their domains of origin, and must rest in the proximity of at least two handfuls of native soil", animalism, auspex, vicissitude)
ventrue = Clan("Ventrue", "The Ventrue have rarifed tastes, and they fnd only one specifc type of mortal blood palatable and vital for them.", dominate, fortitude, presence)
#Sect
camarilla = Sect("Camarilla", "Sabbat, Anarchs")
sabbat = Sect("Sabbat", "Camarilla, Anarchs")
anarchs = Sect("Anarchs", "Camarilla, Sabbat")
independents = Sect("Independents", "Varies")
#Status - Camarilla
prince = Status("Prince", "Ruling a city", "Highest position of power in a Camarilla city.")
seneschal = Status("Seneschal", "Prince right hand", "Prince right hand and usually replacement when the Prince is unavalliable")
primogen = Status("Primogen", "Represents a Clan", "Clan representative in a Camarilla city.")
sheriff = Status("Sheriff", "Police the Kindred", "Enforcer of the Traditions and the will of the Prince.")
hound = Status("Hound", "Sheriff assistant", "The Sheriff subordinates.")
scourge = Status("Scourge", "Remove the undesirables", "Like the Sheriff, but his objective is to purge the city of undesirables.")
harpy = Status("Harpy", "Social administrators", "The official recorders of debts owed, status gained and can serve as diplomats or envoys to other domains in the Camarilla.")
keeper = Status("Keeper of the Elysium", "Take care of an Elysium", "The one responsible for keeping the peace in one of the Camarilla's official Elysiums.")
regent = Status("Tremere Regent", "Take care of a Chantry", "The one responsible for administrating one of the Tremere's Chantry")
#Status - Sabbat
archbishop = Status("Archbishop", "Ruling a city", "Highest position of power in a Sabbat city")
bishop = Status("Bishop", "Advise an Archibishop", "Direct servents of an Archibishop. some times a group of Bishops can rule a city toghether")
priest = Status("Priest", "Ritual leader of a pack", "Responsible for the rituals and the vitae of a pack, usually second to the Ductus")
ductus = Status("Ductus", "Leader of a Pack", "Leader of one individual Sabbat Pack")
priscus = Status("Priscus", "Honorary Advisor", "Honorary advisor of any high ranking Sabbat official")
#Status - Anarch
baron = Status("Baron", "Ruling a city", "Ruler of an Anarch territory")
#City
city = City("Genericville")
####File Loading####
file_path = 'StoryTeller/data.txt'
if os.stat(file_path).st_size == 0:
    new = True
else:
    new = False
    f = open('StoryTeller/data.txt', 'r')
    load = json.load(f)
    f.close()
    print("Arquivo carregado com sucesso")
####Init do Tkinter####
#Define tela principal
root = Tk()
#windowMenu = Window(root)
#Define frames
frameInit = Frame(root)
frameMain = Frame(root)
frameCharacter = Frame(root)
frameCity = Frame(root)
frameClans = Frame(root)
frameDisci = Frame(root)
frameBoon = Frame(root)
frameCharacterC = Frame(root)
frameCityC = Frame(root)
frameBoonC = Frame(root)
#StringVars
textinput=StringVar()
#Funções
def raise_frame(frame):
    frame.tkraise()
def sair():
    root.destroy()
def entervalue():
    city.setName(textinput.get())
    raise_frame(frameMain)
#Modelagem Telas

for frame in (frameMain, frameCharacter, frameCity, frameClans, frameDisci, frameInit, frameBoon, frameCharacterC, frameCityC, frameBoonC):
    frame.grid(row=0, column=0, sticky='news')

#Tela frameInit
labelFI = Label(frameInit,text="City Name", font="none 20 bold")
labelFI.pack(pady=15, padx=300, side=TOP)
entryFI = Entry(frameInit,width=20, font='none 18 bold',textvar=textinput)
entryFI.pack(pady=15, padx=300, side=TOP)
buttonFI = Button(frameInit, text='Enter', command=entervalue)
buttonFI.pack(pady=15, padx=300, side=TOP)

#Tela frameMain
bCharPage = Button(frameMain, text='Chars', command=lambda: raise_frame(frameCharacter))
bCharPage.pack(pady=15, padx=15, side=LEFT)
bClanPage = Button(frameMain, text='Clans', command=lambda: raise_frame(frameClans))
bClanPage.pack(pady=15, padx=15, side=LEFT)
bDisciPage = Button(frameMain, text='Disci', command=lambda: raise_frame(frameDisci))
bDisciPage.pack(pady=15, padx=15, side=LEFT)
bBoonPage = Button(frameMain, text='Boons', command=lambda: raise_frame(frameBoon))
bBoonPage.pack(pady=15, padx=15, side=LEFT)

#Tela frameCharacter
bVoltar1 = Button(frameCharacter, text='Back', command=lambda: raise_frame(frameMain))
bVoltar1.pack(pady=15, padx=15, side=BOTTOM)
bCriar1 = Button(frameCharacter, text='Create', command=lambda: raise_frame(frameCharacterC))
bCriar1.pack(pady=15, padx=15, side=BOTTOM)

#Tela frameCharacterC
bVoltar5 = Button(frameCharacterC, text='Back', command=lambda: raise_frame(frameCharacter))
bVoltar5.pack(pady=15, padx=15, side=BOTTOM)

#Tela frameClans
bVoltar2 = Button(frameClans, text='Back', command=lambda: raise_frame(frameMain))
bVoltar2.pack(pady=15, padx=15, side=BOTTOM)

#Tela frameDisci
bVoltar3 = Button(frameDisci, text='Back', command=lambda: raise_frame(frameMain))
bVoltar3.pack(pady=15, padx=15, side=BOTTOM)

#Tela frameBoon
bVoltar4 = Button(frameBoon, text='Back', command=lambda: raise_frame(frameMain))
bVoltar4.pack(pady=15, padx=15, side=BOTTOM)
bCriar2 = Button(frameBoon, text='Create', command=lambda: raise_frame(frameCharacterC))
bCriar2.pack(pady=15, padx=15, side=BOTTOM)

#Tela frameBoonC
bVoltar6 = Button(frameBoonC, text='Back', command=lambda: raise_frame(frameBoon))
bVoltar6.pack(pady=15, padx=15, side=BOTTOM)

if new:
    raise_frame(frameInit)
else:
    raise_frame(frameMain)

root.wm_title("StoryTeller")
root.geometry("900x600")
root.resizable(False, False)
root.config(background="white")
root.mainloop()


print(city.name)