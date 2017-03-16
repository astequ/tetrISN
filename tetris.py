from tkinter import *
from random import randint

def coord(z): #permet de passer de coordonnées de type grille de jeu (10 de large, 22 de haut) à des coordonnées en pixels pour l'affichage (300 de large, 660 de haut)
    return z*30

def placesquare(x,y): #trace un carré avec tag falling
    main.create_rectangle(coord(x),coord(y),coord(x+1),coord(y+1),tags=("falling"))

def trace(lis): #trace le contenu d'une liste
    main.delete("falling") #suppression de la pièce précédente
    for i in range(2,24): #traçage de la nouvelle pièce
        for j in range(10):
            if lis[i][j] == 1:
                placesquare(j,i-2)

def place(pos,state): #dispose une pièce sur une liste définie
    global shape, flipok
    x,y = pos[0],pos[1]
    lis = []
    for i in range(24): #génération d'une liste temporaire
        lis.append([0,0,0,0,0,0,0,0,0,0])
    try:
        if shape == 1: #génération d'une barre
            if state == 1:
                lis[x][y] = 1
                lis[x][y-1] = 1
                lis[x][y+1] = 1
                lis[x][y+2] = 1
            elif state == 2:
                lis[x][y] = 1
                lis[x-1][y] = 1
                lis[x+1][y] = 1
                lis[x+2][y] = 1
            elif state == 3:
                lis[x][y] = 1
                lis[x][y-1] = 1
                lis[x][y+1] = 1
                lis[x][y+2] = 1
            elif state == 4:
                lis[x][y] = 1
                lis[x-1][y] = 1
                lis[x+1][y] = 1
                lis[x+2][y] = 1
        elif shape == 2: #génération d'un carré
            lis[x][y] = 1
            lis[x][y+1] = 1
            lis[x+1][y+1] = 1
            lis[x+1][y] = 1
        elif shape == 3: #génération d'un T
            if state == 1:
                lis[x][y] = 1
                lis[x][y-1] = 1
                lis[x][y+1] = 1
                lis[x+1][y] = 1
            elif state == 2:
                lis[x][y] = 1
                lis[x-1][y] = 1
                lis[x+1][y] = 1
                lis[x][y-1] = 1
            elif state == 3:
                lis[x][y] = 1
                lis[x][y-1] = 1
                lis[x][y+1] = 1
                lis[x-1][y] = 1
            elif state == 4:
                lis[x][y] = 1
                lis[x-1][y] = 1
                lis[x+1][y] = 1
                lis[x][y+1] = 1
        elif shape == 4: #génération d'un L
            if state == 1:
                lis[x][y] = 1
                lis[x][y-1] = 1
                lis[x+1][y-1] = 1
                lis[x][y+1] = 1
            elif state == 2:
                lis[x][y] = 1
                lis[x-1][y] = 1
                lis[x-1][y-1] = 1
                lis[x+1][y] = 1
            elif state == 3:
                lis[x][y] = 1
                lis[x][y+1] = 1
                lis[x-1][y+1] = 1
                lis[x][y-1] = 1
            elif state == 4:
                lis[x][y] = 1
                lis[x-1][y] = 1
                lis[x+1][y] = 1
                lis[x+1][y+1] = 1
        elif shape == 5: #génération d'un L inversé
            if state == 1:
                lis[x][y] = 1
                lis[x][y+1] = 1
                lis[x+1][y+1] = 1
                lis[x][y-1] = 1
            elif state == 2:
                lis[x][y] = 1
                lis[x+1][y] = 1
                lis[x+1][y-1] = 1
                lis[x-1][y] = 1
            elif state == 3:
                lis[x][y] = 1
                lis[x][y-1] = 1
                lis[x-1][y-1] = 1
                lis[x][y+1] = 1
            elif state == 4:
                lis[x][y] = 1
                lis[x+1][y] = 1
                lis[x-1][y] = 1
                lis[x-1][y+1] = 1
        elif shape == 6: #génération d'un Z
              if state == 1:
                  lis[x][y] = 1
                  lis[x][y-1] = 1
                  lis[x+1][y] = 1
                  lis[x+1][y+1] = 1
              elif state == 2:
                  lis[x][y] = 1
                  lis[x-1][y] = 1
                  lis[x][y-1] = 1
                  lis[x+1][y-1] = 1
              elif state == 3:
                  lis[x][y] = 1
                  lis[x][y-1] = 1
                  lis[x+1][y] = 1
                  lis[x+1][y+1] = 1
              elif state == 4:
                  lis[x][y] = 1
                  lis[x-1][y] = 1
                  lis[x][y-1] = 1
                  lis[x+1][y-1] = 1
        elif shape == 7: #génération d'un Z inversé
              if state == 1:
                  lis[x][y] = 1
                  lis[x][y+1] = 1
                  lis[x+1][y] = 1
                  lis[x+1][y-1] = 1
              elif state == 2:
                  lis[x][y] = 1
                  lis[x][y-1] = 1
                  lis[x-1][y-1] = 1
                  lis[x+1][y] = 1
              elif state == 3:
                  lis[x][y] = 1
                  lis[x][y+1] = 1
                  lis[x+1][y] = 1
                  lis[x+1][y-1] = 1
              elif state == 4:
                  lis[x][y] = 1
                  lis[x][y-1] = 1
                  lis[x-1][y-1] = 1
                  lis[x+1][y] = 1
    except:
        flipok = 0 #utile pour la fonction check(), si un placement est impossible on lui fait savoir en changeant l'état de cette variable globale
    return lis

def check(mov,fstate,pos,piece): #vérifie qu'un mouvement est valide
    global fixed, flipok
    mirai = list(piece)
    out = 1
    #les trois premières conditions vérifient que le mouvement voulu ne fait pas sortir la pièce de l'aire de jeu, puis génère une liste contenant la position future de la pièce
    if mov == 1: #vérifie pour un déplacement vers le bas
        if mirai[-1] == [0,0,0,0,0,0,0,0,0,0]: #vérification que la pièce ne touche pas le sol
            mirai == mirai[:-1] #génération de la liste
            mirai.insert(0,[0,0,0,0,0,0,0,0,0,0])
        else:
            out = 0
    elif mov == 2: #vérifie pour un déplacement vers la droite
        empty = 1
        for i in range(24): #vérification que la pièce n'est pas collée au bord vers lequel elle doit se déplacer
            if mirai[i][-1] == 1:
                empty = 0
        if empty == 1: #génération de la liste
            for i in range(24):
                element = mirai[i][-1]
                mirai[i] = mirai[i][:-1]
                mirai[i].insert(0,element)
        else:
            out = 0
    elif mov == 3: #vérifie pour un déplacement vers la gauche
        empty = 1
        for i in range(24): #vérification que la pièce n'est pas collée au bord vers lequel elle doit se déplacer
            if mirai[i][0] == 1:
                empty = 0
        if empty == 1: #génération de la liste
            for i in range(24):
                element = mirai[i][0]
                mirai[i] = mirai[i][1:]
                mirai[i].append(element)
        else:
            out = 0
    elif mov == 0: #cas spécial d'une rotation
        mirai = place(pos,fstate) #on tente de retracer la pièce, si elle dépasse une exception aura lieu et changera l'état de flipok
        if flipok == 0: #cas où la rotation n'est pas valide
            out = 0
            flipok = 1 #on réinitialise flipok (qui est une variable globale) pour le prochain test
        elif pos[0] == 0 or pos[1] == 0: #force à interdire la rotation au premier rang (haut et gauche)
            out = 0
    if out == 1: #si aucune sortie de l'aire de jeu n'a été décelée, on teste les collisions entre pièces
        for i in range(24):
            for j in range(10):
                if fixed[i][j]+mirai[i][j] == 2: #pour chaque position on aditionne le contenu de la liste anticipant le déplacement générée plus haut avec celui de la liste en charge des pièces déjà posées. Si le résultat vaut 2, alors il y a superposition
                    out = 0
    return out #par défaut à 1 (action possible), la variable out sera mise à 0 (action impossible) à la moindre erreur détectée

def mirai(bisou): #à la base c'tait du test mais c'est la fonction définitive de gestion des déplacements. Faudra changer son nom du coup
    global pos, piece, state, shape
    temppos = pos
    tstate = state
    if bisou == 1:
        temppos = (pos[0],pos[1]-1)
        k = check(3,0,pos,piece)
    elif bisou == 2:
        temppos = (pos[0],pos[1]+1)
        k = check(2,0,pos,piece)
    elif bisou == 3:
        temppos = (pos[0]+1,pos[1])
        k = check(1,0,pos,piece)
    elif bisou == 4: #gère les 4 états de rotation
        tstate += 1
        if tstate == 5:
            tstate = 1
        k = check(0,tstate,pos,piece)
    if k == 1: #si le mouvement est accepté, on l'applique et on retrace tout
        pos = temppos
        state = tstate
        piece = place(pos,state)
        trace(piece)
        main.itemconfig("falling",fill=color(shape))
        ghost()

def death ():
    global fixed, keep
    if fixed[1] != [0,0,0,0,0,0,0,0,0,0]:
        keep = 0
        #main.create_rectangle(30,210,270,400,fill="black")
        main.create_image(0,0, anchor=NW, image=dedpic)

def rezero (event):
    global fixed, piece, shade, keep
    if keep == 0:
        main.delete("all")
        fixed = [] #liste contenant les éléments déjà posés
        piece = [] #liste contenant les éléments en mouvement
        shade = []
        for i in range(24): #génération des listes suivant le format expliqué plus haut
            fixed.append([0,0,0,0,0,0,0,0,0,0])
            piece.append([0,0,0,0,0,0,0,0,0,0])
            shade.append([0,0,0,0,0,0,0,0,0,0])
        keep = 1
        cardinal()
    else:
        print("meurs dignement, couard")

def cardinal ():
    global pos, piece, keep
    if check(1,0,pos,piece)==0:
        fixpiece()
        illya()
    else:
        mirai(3)
    death()
    if keep == 1:
        wdw.after(600,cardinal)

def illya():
    global fixed, shade
    for i in range (24):
        if fixed[i] == [1,1,1,1,1,1,1,1,1,1]:
            fixed = fixed[:i] + fixed[i+1:]
            fixed.insert(0,[0,0,0,0,0,0,0,0,0,0])
            shade = shade[:i] + shade[i+1:]
            shade.insert(0,[0,0,0,0,0,0,0,0,0,0])
            main.delete("all")
            for w in range(2,24):
                for j in range(10):
                    if fixed[w][j] == 1:
                        main.create_rectangle(coord(j),coord(w-2),coord(j+1),coord(w-1),fill=color(shade[w][j]))

def ghost():
    main.delete("plop")
    global pos, shape, state, piece
    localpos = pos
    for i in range(24-pos[0]):
        ghostpiece = place(localpos,state)
        if check(1,0,localpos,ghostpiece) == 1:
            localpos = (localpos[0]+1,localpos[1])
    ghostpiece = place(localpos,state)
    for w in range(2,24):
        for j in range(10):
            if ghostpiece[w][j] == 1 and piece[w][j] == 0:
                main.create_rectangle(coord(j),coord(w-2),coord(j+1),coord(w-1),fill="pink",tags="plop")
    return(ghostpiece)

def harddrop(event):
    global piece, shape
    piece = ghost()
    trace(piece)
    main.itemconfig("falling",fill=color(shape))
    fixpiece()
    illya()

def fixpiece(): #fixe la position d'une pièce
    global piece, fixed, shape, shade
    main.dtag("falling") #retire le tag fallind de la pièce afin de la rendre insensible aux effacements de trace()
    for i in range(24):
        for j in range(10):
            fixed[i][j] = piece[i][j]+fixed[i][j] #fusionne la liste contenant la pièce en mouvement avec celle contenant les pièces déjà posées
            if piece[i][j] == 1:
                shade[i][j] = shape
        piece[i] = [0,0,0,0,0,0,0,0,0,0] #réinitialise la liste contenant la pièce en mouvement
    resetpiece()

def resetpiece(): #fait popper une nouvelle pièce, est appelée par fixpiece()
    global shape, state, pos, piece
    shape = randint(1,7)
    state = 1
    pos = (0,4)
    piece = place(pos,state)
    trace(piece)
    main.itemconfig("falling",fill=color(shape))

def color(shape): #donne une couleur en fonction de la pièce
    if shape == 1:
        color = "cyan"
    elif shape == 2:
        color = "gold"
    elif shape == 3:
        color = "purple"
    elif shape == 4:
        color = "orange"
    elif shape == 5:
        color = "blue"
    elif shape == 6:
        color = "red"
    elif shape == 7:
        color = "green"
    return color

wdw = Tk()

#chaque ligne de la grille est représentée par une liste, et la grille est une liste de ces listes, ce qui permet de facilement accéder à un élément précis de la grille en utilisant les indices des listes comme des coordonnées
fixed = [] #liste contenant les éléments déjà posés
piece = [] #liste contenant les éléments en mouvement
shade = []
for i in range(24): #génération des listes suivant le format expliqué plus haut
    fixed.append([0,0,0,0,0,0,0,0,0,0])
    piece.append([0,0,0,0,0,0,0,0,0,0])
    shade.append([0,0,0,0,0,0,0,0,0,0])

flipok = 1
keep = 1
dedpic = PhotoImage(file="ded.png")

main = Canvas(width=300,height=660,bg="white")
main.grid(row=0, column=0)

trace(fixed)
main.dtag("falling")

resetpiece()

cardinal()
wdw.bind("<Up>",lambda e:mirai(4))
wdw.bind("<Down>",lambda e:mirai(3))
wdw.bind("<Left>",lambda e:mirai(1))
wdw.bind("<Right>",lambda e:mirai(2))
wdw.bind("<r>",rezero)
wdw.bind("<Return>",harddrop)

wdw.mainloop()
