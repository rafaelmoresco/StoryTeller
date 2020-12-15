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
quietus = Discipline("Quietus", "The Discipline of silent death, Quietus is practiced by those of Clan Assamite.")
serpentis = Discipline("Serpentis", "Serpentis is believed to be the legacy of Set himself, a gift to his children.")
thaumaturgy = Discipline("Thaumaturgy", "Thaumaturgy encompasses blood magic and other sorcerous arts available to Kindred.")
vicissitude = Discipline("Vicissitude", "Vicissitude is the signature power of the Tzimisce, and is rarely shared outside the Clan.")
lista_disciplinas = [animalism, auspex, celerity, chimerstry, dementation, dominate, fortitude,
 necromancy, obfuscate, obtenebration, potence, presence, protean, quietus, serpentis, thaumaturgy, vicissitude ]

#Clãs
assamite = Clan("Assamite", "Should an Assamite consume the blood of another Kindred, she suffers one automatic level of unsoakable lethal damage per blood point imbibed.", celerity, obfuscate, quietus)
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
lista_clans = [assamite, brujah, settite, gangrel, giovanni, lasombra, malkavian, nosferatu, ravnos, toreador,
tremere, tzimisce, ventrue]
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
#Character
lista_char = []
#Boons
lista_boon = []
####File Loading####
file_path = 'StoryTeller/data.txt'
#se o arquivo estiver vazio
if os.stat(file_path).st_size == 0:
    new = True
#se estiver com informações
else:
    new = False
    f = open('StoryTeller/data.txt', 'r')
    load = json.load(f)
    f.close()
    #lê o vetor de informações
    for i in range(len(load)):
        #se o objeto for do tipo 0 (cidade)
        if load[i][0] == 0:
            city.setName(load[i][1])
        #se o objeto for do tipo 1 (personagem)
        elif load[i][0] == 1:
            char = Character()
            char.setName(load[i][1])
            char.setGen(load[i][2])
            char.setAge(load[i][3])
            char.setInfo(load[i][4])
            char.setSect(load[i][5])
            char.setStatus(load[i][6])
            char.setClan(load[i][7])
            lista_char.append(char)
        #se o objeto for do tipo 2 (divida)
        else:
            boon = Boon(load[i][1], load[i][2], load[i][3])
            lista_boon.append(boon)
    print("Arquivo carregado com sucesso")
####Init do Tkinter####
#Define tela principal
root = Tk()
#windowMenu = Window(root)
#Define frames
frameInit = Frame(root)
frameMain = Frame(root)
frameCharacter = Frame(root)
frameCriar = Frame(root)
frameCriar2 = Frame(root)
frameCity = Frame(root)
frameClans = Frame(root)
frameBoon = Frame(root)
frameDisci = Frame(root)
frameViewC = Frame(root)
frameViewB = Frame(root)
#StringVars
textinput = StringVar()
variable = StringVar()
ec1 = StringVar()
ec2 = StringVar()
ec3 = StringVar()
ec4 = StringVar()
ec5 = StringVar()
ec6 = StringVar()
ec7 = StringVar()
#Test
listIndex = 0
####Funções####
#Muda o frame e faz update
def raise_frame(frame):
    #se for o frame de personagens, atualiza a lista
    if frame == frameCharacter:
        listaChars.delete(0, len(lista_char))
        for i in range(len(lista_char)):
            listaChars.insert(i, lista_char[i].getName())
    #se for o frame de dividas, atualiza a lista
    elif frame == frameBoon:
        listaBoons.delete(0,len(lista_boon))
        for i in range(len(lista_boon)):
            listaBoons.insert(i, lista_boon[i].getOwner())
    #muda o frame
    frame.tkraise()
#Sai do programa
def sair():
    root.destroy()
#Entra o nome da cidade
def entervalueCity():
    city.setName(textinput.get())
    raise_frame(frameMain)
    cityData = [0, textinput.get()]
    temp = [cityData]
    f = open('StoryTeller\data.txt', 'w') #trocar para data.txt depois
    json.dump(temp, f)
    f.close()
#Cria uma nova personagem
def criarC():
    #pega os valores dos campos de texto
    name = e1.get()
    gen = e2.get()
    age = e3.get()
    info = e4.get()
    sect = e5.get()
    status = e6.get()
    clan = e7.get()
    #cria o objeto e define os valores
    char = Character()
    char.setName(name)
    char.setGen(gen)
    char.setAge(age)
    char.setInfo(info)
    char.setSect(sect)
    char.setStatus(status)
    char.setClan(clan)
    #adiciona a lista de personagens
    lista_char.append(char)
    #salva no arquivo
    novochar = [1, name, gen, age, info, sect, status, clan]
    f = open('StoryTeller\data.txt', 'r') #trocar para data.txt depois
    temp = json.load(f)
    f.close
    temp.append(novochar)
    f = open('StoryTeller\data.txt', 'w') #trocar para data.txt depois
    json.dump(temp, f)
    f.close()
#Deleta uma personagem
def deletarC():
    #pega o item selecionado
    select = listaChars.curselection()
    x = int(select[0])
    #deleta do vetor de objetos
    y = lista_char.pop(x)
    #deleta do listview
    listaChars.delete(x)
    #deleta do arquivo
    f = open('StoryTeller\data.txt', 'r') #trocar para data.txt depois
    temp = json.load(f)
    f.close
    k = 0
    for i in range(len(temp)):
        if temp[i][0] == 1:
            if k == x:
                z = temp.pop(i)
                break
            else:
                k += 1
    f = open('StoryTeller\data.txt', 'w') #trocar para data.txt depois
    json.dump(temp, f)
    f.close()
#Vizualizar uma personagem
def viewC():
    select = listaChars.curselection()
    global listIndex
    listIndex = int(select[0])
    raise_frame(frameViewC)
    ec1.set(lista_char[listIndex].getName())
    ec2.set(lista_char[listIndex].getGen())
    ec3.set(lista_char[listIndex].getAge())
    ec4.set(lista_char[listIndex].getInfo())
    ec5.set(lista_char[listIndex].getSect())
    ec6.set(lista_char[listIndex].getStatus())
    ec7.set(lista_char[listIndex].getClan())
def editC():
    #select = listaChars.curselection()
    #listIndex = int(select[0])
    lista_char[listIndex].setName(e31.get())
    lista_char[listIndex].setGen(e32.get())
    lista_char[listIndex].setAge(e33.get())
    lista_char[listIndex].setInfo(e34.get())
    lista_char[listIndex].setSect(e35.get())
    lista_char[listIndex].setStatus(e36.get())
    lista_char[listIndex].setClan(e37.get())
    f = open('StoryTeller\data.txt', 'r') #trocar para data.txt depois
    temp = json.load(f)
    f.close
    k = 0
    for i in range(len(temp)):
        if temp[i][0] == 1:
            if k == listIndex:
                temp[i][1] = lista_char[listIndex].getName()
                temp[i][2] = lista_char[listIndex].getGen()
                temp[i][3] = lista_char[listIndex].getAge()
                temp[i][4] = lista_char[listIndex].getInfo()
                temp[i][5] = lista_char[listIndex].getSect()
                temp[i][6] = lista_char[listIndex].getStatus()
                temp[i][7] = lista_char[listIndex].getClan()
                break
            else:
                k += 1
    f = open('StoryTeller\data.txt', 'w') #trocar para data.txt depois
    json.dump(temp, f)
    f.close()
#Cria uma nova divida
def criarB():
    #pega os valores dos campos de texto
    btype = e21.get()
    owner = e22.get()
    giver = e23.get()
    #cria o objeto
    boon = Boon(btype, owner, giver)
    #adiciona ao vetor de dividas
    lista_boon.append(boon)
    #salva no arquivo
    novoboon = [2, btype, owner, giver]
    f = open('StoryTeller\data.txt', 'r') #trocar para data.txt depois
    temp = json.load(f)
    f.close
    temp.append(novoboon)
    f = open('StoryTeller\data.txt', 'w') #trocar para data.txt depois
    json.dump(temp, f)
    f.close()
#Deleta uma divida
def deletarB():
    #pega o item selecionado
    select = listaBoons.curselection()
    x = int(select[0])
    #remove do vetor de objetos
    y = lista_boon.pop(x)
    #remove do listview
    listaBoons.delete(x)
    #remove do arquivo
    f = open('StoryTeller\data.txt', 'r') #trocar para data.txt depois
    temp = json.load(f)
    f.close
    k = 0
    for i in range(len(temp)):
        if temp[i][0] == 2:
            if k == x:
                z = temp.pop(i)
                break
            else:
                k += 1
    f = open('StoryTeller\data.txt', 'w') #trocar para data.txt depois
    json.dump(temp, f)
    f.close()
#Vizualizar uma divida
def viewB():
    pass
#Modelagem Telas
for frame in (frameMain, frameCharacter, frameCity, frameClans, frameBoon, frameDisci, frameInit, frameCriar, frameCriar2, frameViewB, frameViewC):
    frame.grid(row=0, column=0, sticky='news')

#Tela frameInit
labelFI = Label(frameInit,text="City Name", font="none 20 bold")
labelFI.pack(pady=15, padx=300, side=TOP)
entryFI = Entry(frameInit,width=20, font='none 18 bold',textvar=textinput)
entryFI.pack(pady=15, padx=300, side=TOP)
buttonFI = Button(frameInit, text='Enter', command=entervalueCity)
buttonFI.pack(pady=15, padx=300, side=TOP)

#Tela frameMain
bCharPage = Button(frameMain, text='Chars', command=lambda: raise_frame(frameCharacter))
bCharPage.pack(pady=15, padx=15, side=LEFT)
bClanPage = Button(frameMain, text='Clans', command=lambda: raise_frame(frameClans))
bClanPage.pack(pady=15, padx=15, side=LEFT)
bBoonPage = Button(frameMain, text = 'Boon', command = lambda: raise_frame(frameBoon))
bBoonPage.pack(pady = 15, padx = 15, side = LEFT)
bDisciPage = Button(frameMain, text='Disci', command=lambda: raise_frame(frameDisci))
bDisciPage.pack(pady=15, padx=15, side=LEFT)

#tela frameCharacter
listaChars = Listbox(frameCharacter)
listaChars.pack(fill = X, expand = YES)
bCriar = Button(frameCharacter, text = 'Criar', command = lambda: raise_frame(frameCriar))
bCriar.pack(pady = 15, padx = 15, side = LEFT)
bEditar = Button(frameCharacter, text = 'Vizualizar', command = viewC)
bEditar.pack(pady = 15, padx = 15, side = LEFT)
bDeletar = Button(frameCharacter, text = 'Deletar', command = deletarC)
bDeletar.pack(pady = 15, padx = 15, side = LEFT)
bVoltar = Button(frameCharacter, text = 'Voltar', command = lambda: raise_frame(frameMain))
bVoltar.pack(pady = 15, padx = 15, side = LEFT)

#tela frameCriar
l1 = Label(frameCriar, text = "Name:").grid(row = 0, column = 0, sticky = W, pady = 2) 
l2 = Label(frameCriar, text = "Generation:").grid(row = 1, column = 0, sticky = W, pady = 2) 
l3 = Label(frameCriar, text = "Age:").grid(row = 2, column = 0, sticky = W, pady = 2) 
l4 = Label(frameCriar, text = "Info:").grid(row = 3, column = 0, sticky = W, pady = 2) 
l5 = Label(frameCriar, text = "Sect:").grid(row = 4, column = 0, sticky = W, pady = 2) 
l6 = Label(frameCriar, text = "Status:").grid(row = 5, column = 0, sticky = W, pady = 2) 
l7 = Label(frameCriar, text = "Clan:").grid(row = 6, column = 0, sticky = W, pady = 2) 

e1 = Entry(frameCriar)
e1.grid(row = 0, column = 1, pady = 2)
e2 = Entry(frameCriar)
e2.grid(row = 1, column = 1, pady = 2)
e3 = Entry(frameCriar)
e3.grid(row = 2, column = 1, pady = 2)
e4 = Entry(frameCriar)
e4.grid(row = 3, column = 1, pady = 2)
e5 = Entry(frameCriar)
e5.grid(row = 4, column = 1, pady = 2)
e6 = Entry(frameCriar)
e6.grid(row = 5, column = 1, pady = 2)
e7 = Entry(frameCriar)
e7.grid(row = 6, column = 1, pady = 2)

bVoltar2 = Button(frameCriar, text = 'Voltar', command = lambda: raise_frame(frameCharacter))
bVoltar2.grid(row = 7, column = 1, sticky = W, pady = 2)
bCriar2 = Button(frameCriar, text = 'Criar', command = criarC)
bCriar2.grid(row = 7, column = 0, sticky = W, pady = 2)

#tela frameViewC
l31 = Label(frameViewC, text = "Name:").grid(row = 0, column = 0, sticky = W, pady = 2) 
l32 = Label(frameViewC, text = "Generation:").grid(row = 1, column = 0, sticky = W, pady = 2) 
l33 = Label(frameViewC, text = "Age:").grid(row = 2, column = 0, sticky = W, pady = 2) 
l34 = Label(frameViewC, text = "Info:").grid(row = 3, column = 0, sticky = W, pady = 2) 
l35 = Label(frameViewC, text = "Sect:").grid(row = 4, column = 0, sticky = W, pady = 2) 
l36 = Label(frameViewC, text = "Status:").grid(row = 5, column = 0, sticky = W, pady = 2) 
l37 = Label(frameViewC, text = "Clan:").grid(row = 6, column = 0, sticky = W, pady = 2) 

e31 = Entry(frameViewC, textvar = ec1)
e31.grid(row = 0, column = 1, pady = 2)
e32 = Entry(frameViewC, textvar = ec2)
e32.grid(row = 1, column = 1, pady = 2)
e33 = Entry(frameViewC, textvar = ec3)
e33.grid(row = 2, column = 1, pady = 2)
e34 = Entry(frameViewC, textvar = ec4)
e34.grid(row = 3, column = 1, pady = 2)
e35 = Entry(frameViewC, textvar = ec5)
e35.grid(row = 4, column = 1, pady = 2)
e36 = Entry(frameViewC, textvar = ec6)
e36.grid(row = 5, column = 1, pady = 2)
e37 = Entry(frameViewC, textvar = ec7)
e37.grid(row = 6, column = 1, pady = 2)

bEditar2 = Button(frameViewC, text = 'Editar', command = editC)
bEditar2.grid(row = 7, column = 1, sticky = W, pady = 2)
bVoltar3 = Button(frameViewC, text = 'Voltar', command = lambda: raise_frame(frameCharacter))
bVoltar3.grid(row = 7, column = 0, sticky = W, pady = 2)

#tela frameClan
s = Scrollbar(frameClans)
s.pack(side = RIGHT, fill = Y)
lClans = Text(frameClans)
lClans.pack(side = TOP, fill = Y)
for i in range(len(lista_clans)):
    lista_clans[i].getCName()
    lista_clans[i].getCWeakness()
    lista_clans[i].getCDisciplines()
    lClans.insert(END, lista_clans[i]._cName)
    lClans.insert(END, ' - ')
    lClans.insert(END, "Weakness: "+str(lista_clans[i]._cWeakness))
    lClans.insert(END, ' - ')
    lClans.insert(END, "Clan Disciplines: "+str(lista_clans[i].getCDisciplines()))
    lClans.insert(END, '\n\n')
s.config(command = lClans.yview)
bVoltar = Button(frameClans, text = 'Voltar', command = lambda: raise_frame(frameMain))
bVoltar.pack(pady = 15, padx = 15, side = BOTTOM)

#tela frameBoon
listaBoons = Listbox(frameBoon)
listaBoons.pack(fill = X, expand = YES)
bCriarB = Button(frameBoon, text = 'Criar', command = lambda: raise_frame(frameCriar2))
bCriarB.pack(pady = 15, padx = 15, side = LEFT)
bEditarB = Button(frameBoon, text = 'Vizualizar')
bEditarB.pack(pady = 15, padx = 15, side = LEFT)
bDeletarB = Button(frameBoon, text = 'Deletar', command = deletarB)
bDeletarB.pack(pady = 15, padx = 15, side = LEFT)
bVoltar = Button(frameBoon, text = 'Voltar', command = lambda: raise_frame(frameMain))
bVoltar.pack(pady = 15, padx = 15, side = LEFT)

#tela frameCriar2
l21 = Label(frameCriar2, text = "Type:").grid(row = 0, column = 0, sticky = W, pady = 2) 
l22 = Label(frameCriar2, text = "Owner:").grid(row = 1, column = 0, sticky = W, pady = 2) 
l23 = Label(frameCriar2, text = "Giver:").grid(row = 2, column = 0, sticky = W, pady = 2) 

e21 = Entry(frameCriar2)
e21.grid(row = 0, column = 1, pady = 2)
e22 = Entry(frameCriar2)
e22.grid(row = 1, column = 1, pady = 2)
e23 = Entry(frameCriar2)
e23.grid(row = 2, column = 1, pady = 2)

bVoltar3 = Button(frameCriar2, text = 'Voltar', command = lambda: raise_frame(frameCharacter))
bVoltar3.grid(row = 3, column = 1, sticky = W, pady = 2)
bCriar3 = Button(frameCriar2, text = 'Criar', command = criarB)
bCriar3.grid(row = 3, column = 0, sticky = W, pady = 2)

#tela frameDisci
s = Scrollbar(frameDisci)
s.pack(side = RIGHT, fill = Y)
lDisci = Text(frameDisci)
lDisci.pack(side = TOP, fill = Y)
for i in range(len(lista_disciplinas)):
    lista_disciplinas[i].getDName()
    lista_disciplinas[i].getDesc()
    lDisci.insert(END, lista_disciplinas[i].dName)
    lDisci.insert(END, ' - ')
    lDisci.insert(END, lista_disciplinas[i].desc)
    lDisci.insert(END, '\n\n')
s.config(command = lDisci.yview)
bVoltar = Button(frameDisci, text = 'Voltar', command = lambda: raise_frame(frameMain))
bVoltar.pack(pady = 15, padx = 15, side = BOTTOM)

#define qual o frame inicial
if new:
    raise_frame(frameInit)
else:
    raise_frame(frameMain)

#inicia a tela
root.wm_title("StoryTeller")
root.geometry("865x445")
root.resizable(False, False)
root.config(background="white")
root.mainloop()
