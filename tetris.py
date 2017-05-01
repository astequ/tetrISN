#-*- coding: utf-8 -*-

from tkinter import *
from winsound import *
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
    future = list(piece)
    out = 1
    #les trois premières conditions vérifient que le mouvement voulu ne fait pas sortir la pièce de l'aire de jeu, puis génère une liste contenant la position future de la pièce
    if mov == 1: #vérifie pour un déplacement vers le bas
        if future[-1] == [0,0,0,0,0,0,0,0,0,0]: #vérification que la pièce ne touche pas le sol
            future == future[:-1] #génération de la liste
            future.insert(0,[0,0,0,0,0,0,0,0,0,0])
        else:
            out = 0
    elif mov == 2: #vérifie pour un déplacement vers la droite
        empty = 1
        for i in range(24): #vérification que la pièce n'est pas collée au bord vers lequel elle doit se déplacer
            if future[i][-1] == 1:
                empty = 0
        if empty == 1: #génération de la liste
            for i in range(24):
                element = future[i][-1]
                future[i] = future[i][:-1]
                future[i].insert(0,element)
        else:
            out = 0
    elif mov == 3: #vérifie pour un déplacement vers la gauche
        empty = 1
        for i in range(24): #vérification que la pièce n'est pas collée au bord vers lequel elle doit se déplacer
            if future[i][0] == 1:
                empty = 0
        if empty == 1: #génération de la liste
            for i in range(24):
                element = future[i][0]
                future[i] = future[i][1:]
                future[i].append(element)
        else:
            out = 0
    elif mov == 0: #cas spécial d'une rotation
        future = place(pos,fstate) #on tente de retracer la pièce, si elle dépasse une exception aura lieu et changera l'état de flipok
        if flipok == 0: #cas où la rotation n'est pas valide
            out = 0
            flipok = 1 #on réinitialise flipok (qui est une variable globale) pour le prochain test
        elif pos[0] == 0 or pos[1] == 0: #force à interdire la rotation au premier rang (haut et gauche)
            out = 0
    if out == 1: #si aucune sortie de l'aire de jeu n'a été décelée, on teste les collisions entre pièces
        for i in range(24):
            for j in range(10):
                if fixed[i][j]+future[i][j] == 2: #pour chaque position on aditionne le contenu de la liste anticipant le déplacement générée plus haut avec celui de la liste en charge des pièces déjà posées. Si le résultat vaut 2, alors il y a superposition
                    out = 0
    return out #par défaut à 1 (action possible), la variable out sera mise à 0 (action impossible) à la moindre erreur détectée

def future(direct): #gère les déplacements de la pièce actuelle
    global pos, piece, state, shape, pause, keep
    if pause == 0 and keep == 1: #la pièce n'est déplaçable que si le jeu n'est pas en pause et que la partie est en cours
        temppos = pos
        tstate = state
        if direct == 1: #on vérifie pour les 4 directions si le mouvement est valable en faisant appel à check()
            temppos = (pos[0],pos[1]-1)
            k = check(3,0,pos,piece)
        elif direct == 2:
            temppos = (pos[0],pos[1]+1)
            k = check(2,0,pos,piece)
        elif direct == 3:
            temppos = (pos[0]+1,pos[1])
            k = check(1,0,pos,piece)
        elif direct == 4: #gère les 4 états de rotation
            tstate += 1
            if tstate == 5:
                tstate = 1
            k = check(0,tstate,pos,piece)
        if k == 1: #si le mouvement est accepté, on l'applique et on retrace tout
            pos = temppos
            state = tstate
            piece = place(pos,state)
            trace(piece)
            main.itemconfig("falling",fill=color(shape)) #on applique la couleur à la pièce en mouvement
            ghost() #on met à jour l'aperçu du lieu d'arrivée de la pièce

def death ():
    global fixed, keep
    if fixed[1] != [0,0,0,0,0,0,0,0,0,0]: #la grille fait 24 rangs de haut mais n'en affiche que 22, on détecte la mort en voyant si une pièce est posée en dehors de la zone affichée
        keep = 0 #on arrête le jeu
        #main.create_rectangle(30,210,270,400,fill="black")
        main.create_image(0,0, anchor=NW, image=dedpic) #on affiche l'écran de mort

def reset (event): #recommence la partie
    global fixed, piece, shade, keep, lines, score, level
    if keep == 0: #on ne peut recommencer que si la partie est perdue
        main.delete("all")
        fixed = []
        piece = []
        shade = []
        lines = 0
        score = 0
        level = 0
        for i in range(24): #génération des listes suivant le format expliqué plus haut
            fixed.append([0,0,0,0,0,0,0,0,0,0])
            piece.append([0,0,0,0,0,0,0,0,0,0])
            shade.append([0,0,0,0,0,0,0,0,0,0])
        keep = 1
        master() #on réinitialise les pièces affichées, les variables et on relance le jeu
    else:
        print("meurs dignement, couard") #faut bien motiver le joueur :3

def master (): #coordonne les autres fonctions, gère le rythme du jeu
    global pos, piece, keep, level
    if check(1,0,pos,piece)==0: #pose la pièce si un déplacement vers le bas est impossible
        fixpiece()
        findline()
    else: #effectue un déplacement vers le bas dans le cas inverse
        future(3)
    death() #vérifie que la partie n'est pas perdue
    if keep == 1 and pause == 0: #se relance d'elle-même si la partie n'est pas perdue et le jeu n'est pas en pause
        if level < 30:
            speed = int(round(-18*level+600,0))
        else:
            speed = int(round(-18*29+600,0))
        wdw.after(speed,master)

def findline(): #détecte une ligne complétée
    global fixed, shade
    combo = 0
    for i in range (24): #parcourt toutes les lignes une à une
        if fixed[i] == [1,1,1,1,1,1,1,1,1,1]: #si la ligne est pleine
            fixed = fixed[:i] + fixed[i+1:] #on supprime la ligne
            fixed.insert(0,[0,0,0,0,0,0,0,0,0,0]) #on remet une ligne vide au rang le plus haut
            shade = shade[:i] + shade[i+1:] #on effectue les mêmes opérations pour la liste en charge des couleurs
            shade.insert(0,[0,0,0,0,0,0,0,0,0,0])
            main.delete("all") #on supprime puis on retrace tout
            combo += 1
            for w in range(2,24):
                for j in range(10):
                    if fixed[w][j] == 1:
                        main.create_rectangle(coord(j),coord(w-2),coord(j+1),coord(w-1),fill=color(shade[w][j]))
    scoring(combo)

def scoring(combo):
    global lines, score, level
    lines += combo
    if combo == 1:
        score += 40*(level+1)
    elif combo == 2:
        score += 100*(level+1)
    elif combo == 3:
        score += 300*(level+1)
    elif combo == 4:
        score += 1200*(level+1)
    if lines >= (level+1)*10:
        level += 1
    if combo != 0:
        aside.itemconfig(scorelabel,text=str(score))
        aside.itemconfig(levellabel,text=str(level))
        aside.itemconfig(lineslabel,text=str(lines))

def ghost(): #aperçu du lieu de chute de la pièce
    main.delete("plop") #supprime l'ancien aperçu
    global pos, shape, state, piece
    localpos = pos #position de l'aperçu
    for i in range(24-pos[0]): #on part de la position de la pièce actuelle avant de vérifier pour tous les rangs inférieurs
        ghostpiece = place(localpos,state) #génère une liste contenant l'emplacement de l'aperçu
        if check(1,0,localpos,ghostpiece) == 1: #si un déplacement vers le bas est possible, on l'effectue
            localpos = (localpos[0]+1,localpos[1])
    ghostpiece = place(localpos,state) #on met à jour la liste avant la suite du traitement
    for w in range(2,24): #on trace l'aperçu en parcourant chaque case de la grille
        for j in range(10):
            if ghostpiece[w][j] == 1 and piece[w][j] == 0: #si la pièce en mouvement ne se superpose pas à son aperçu, on trace l'aperçu
                main.create_rectangle(coord(j),coord(w-2),coord(j+1),coord(w-1),fill="dim gray",tags="plop")
    return(ghostpiece) #retourne la position de la pièce, utile pour le hard drop

def harddrop(event): #effectue un hard drop (pose la pièce instantanément au plus bas possible)
    global piece, shape, pause, keep
    if pause == 0 and keep == 1: #si la partie n'est pas perdue et le jeu n'est pas en pause
        piece = ghost() #on met la pièce à l'emplacement de son aperçu
        trace(piece) #on retrace la pièce
        main.itemconfig("falling",fill=color(shape)) #on applique sa couleur à la pièce
        fixpiece() #on pose la pièce
        findline() #on vérifie si une ligne n'est pas complétée

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

def resetpiece(): #fait popper une nouvelle pièce et prévoit la suivante, est appelée par fixpiece()
    global shape, state, pos, piece, nshape
    shape = nshape
    nshape = randint(1,7)
    preview() #trace l'aperçu
    state = 1 #initialise toutes les variables caractérisant la nouvelle pièce
    pos = (0,4)
    piece = place(pos,state) #génère la liste de la pièce
    trace(piece) #trace la pièce
    main.itemconfig("falling",fill=color(shape)) #applique sa couleur à la pièce

def preview(): #affiche la pièce à venir
    global shape, nshape
    aside.delete("preview")
    temp = shape
    shape = nshape
    prev = place((1,1),1)
    for i in range(4):
        for j in range(4):
            if prev[i][j] == 1:
                aside.create_rectangle(coord(j)+10,coord(i),coord(j+1)+10,coord(i+1),tags="preview",fill=color(shape))
    shape = temp

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

def ohwait(plz): #met le jeu en pause
    global pause, keep
    if keep == 1: #si la partie n'est pas perdue
        if pause == 0: #si le jeu n'est pas en pause
            pause = 1 #on met le jeu en pause
            main.create_image(1,1, anchor=NW, image=pausepic, tags="pause") #on affiche l'écran de pause
        else: #si le jeu est en pause
            pause = 0 #on annule la pause
            main.delete("pause") #on supprime l'écran de pause
            master() #on relance la fonction principale

wdw = Tk()
wdw.title("TetrISN")
wdw.resizable(width=False, height=False)

#chaque ligne de la grille est représentée par une liste, et la grille est une liste de ces listes, ce qui permet de facilement accéder à un élément précis de la grille en utilisant les indices des listes comme des coordonnées
fixed = [] #liste contenant les éléments déjà posés
piece = [] #liste contenant les éléments en mouvement
shade = [] #liste contenant les couleurs des éléments déjà posés
for i in range(24): #génération des listes suivant le format expliqué plus haut
    fixed.append([0,0,0,0,0,0,0,0,0,0])
    piece.append([0,0,0,0,0,0,0,0,0,0])
    shade.append([0,0,0,0,0,0,0,0,0,0])

flipok = 1
keep = 1
pause = 0
nshape = randint(1,7)
dedpic = PhotoImage(file="resources/ded.png")
pausepic = PhotoImage(file="resources/pause.png")
lines = 0
score = 0
level = 0

PlaySound("resources/theme.wav",SND_ASYNC | SND_LOOP)

main = Canvas(width=300,height=660,bg="black",highlightthickness=0)
main.grid(row=0, column=0)

aside = Canvas(width=140,height=660,bg="white",highlightthickness=0)
aside.grid(row=0, column=1)

aside.create_text(70,180,text="SCORE",font=("",22))
aside.create_text(70,290,text="NIVEAU",font=("",22))
aside.create_text(70,400,text="LIGNES",font=("",22))

scorelabel = aside.create_text(70,230,text=str(score),font=("",22))
levellabel = aside.create_text(70,340,text=str(level),font=("",22))
lineslabel = aside.create_text(70,450,text=str(lines),font=("",22))

trace(fixed)
main.dtag("falling")

resetpiece()
master()

wdw.bind("<Up>",lambda e:future(4))
wdw.bind("<Down>",lambda e:future(3))
wdw.bind("<Left>",lambda e:future(1))
wdw.bind("<Right>",lambda e:future(2))
wdw.bind("<r>",reset)
wdw.bind("<p>",ohwait)
wdw.bind("<Return>",harddrop)

wdw.mainloop()
