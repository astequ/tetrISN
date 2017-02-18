from tkinter import *
from random import randint

def coord(z):
    return z*30

def randum(): #TEST
    global shape, state, pos, piece
    main.delete("falling")
    pos = (int(ex.get()),int(ey.get()))
    state = int(es.get())
    shape = int(et.get())
    piece = place(pos,state)
    trace(piece)

def placesquare(x,y):
    main.create_rectangle(coord(x),coord(y),coord(x+1),coord(y+1),tags=("falling"))

def trace(lis):
    main.delete("falling")
    for i in range(22):
        for j in range(10):
            if lis[i][j] == 1:
                placesquare(j,i)

def place(pos,state):
    global shape, flipok
    x,y = pos[0],pos[1]
    lis = [[0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0]]
    try:
        if shape == 1:
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
        elif shape == 2:
            lis[x][y] = 1
            lis[x][y+1] = 1
            lis[x-1][y+1] = 1
            lis[x-1][y] = 1
        elif shape == 3:
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
        elif shape == 4:
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
        elif shape == 5:
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
        elif shape == 6:
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
        elif shape == 7:
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
        flipok == 0
    return lis

def check(mov,fstate): #pour le moment il ne fait que vérifier si ça sort pas de la zone de jeu, c'est du gros wip
    #mov est dans le cas d'un mouvement, mettre à 0 pour une rotation
    #fstate (futurestate c'trop long) est dans le cas d'une rotation, donne l'état voulu de la pièce (pas l'actuel), mettre à 0 pour un déplacement
    global fixed, piece, pos, flipok
    mirai = list(piece)
    out = 1
    if mov == 1:
        if mirai[-1] == [0,0,0,0,0,0,0,0,0,0]:
            mirai = mirai[-1]+mirai[:-1]
        else:
            print("on est au plus bas")
            out = 0
    elif mov == 2:
        empty = 1
        for i in range(22):
            if mirai[i][-1] == 1:
                empty = 0
        if empty == 1:
            for i in range(22):
                element = mirai[i][-1]
                mirai[i] = mirai[i][:-1]
                mirai[i].insert(0,element)
        else:
            print("on est à fond à droite")
            out = 0
    elif mov == 3:
        empty = 1
        for i in range(22):
            if mirai[i][0] == 1:
                empty = 0
        if empty == 1:
            for i in range(22):
                element = mirai[i][0]
                mirai[i] = mirai[i][0:]
                mirai[i].append(element)
        else:
            print("on est à fond à gauche")
            out = 0
    elif mov == 0:
        mirai = place(pos,fstate)
        if flipok == 0:
            print("on peut pas tourner")
            out = 0
            flipok == 1
    return out

def mirai(bisou): #TEST
    global pos, piece, state, tstate
    temppos = pos
    if bisou == 1:
        temppos = (pos[0],pos[1]-1)
        k = check(3,0)
    elif bisou == 2:
        temppos = (pos[0],pos[1]+1)
        k = check(2,0)
    elif bisou == 3:
        temppos = (pos[0]+1,pos[1])
        k = check(1,0)
    elif bisou == 4:
        tstate += 1
        if tstate ==5:
            tstate = 1
        k = check(0,tstate)
    if k == 1:
        pos = temppos
        state = tstate
        piece = place(pos,state)
        trace(piece)

wdw = Tk()

fixed = [[0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]]

piece = [[0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]]

#shape = randint(1,7)
shape = 1
state = 1
pos = (0,4)
tstate = 1
flipok = 1

main = Canvas(width=300,height=660,bg="white")
main.pack()

trace(place(pos,state))

test = Frame(wdw)
Label(test,text="x").pack()
ex = Entry(test)
ex.pack()
Label(test,text="y").pack()
ey = Entry(test)
ey.pack()
Label(test,text="type").pack()
et = Entry(test)
et.pack()
Label(test,text="state").pack()
es = Entry(test)
es.pack()
ok = Button(test,text="go", command=randum)
ok.pack()
ch = Button(test,text="Gauche", command=lambda:mirai(1))
ch.pack()
ch1 = Button(test,text="Droite", command=lambda:mirai(2))
ch1.pack()
ch2 = Button(test,text="Bas", command=lambda:mirai(3))
ch2.pack()
ch3 = Button(test,text="Ori", command=lambda:mirai(4))
ch3.pack()

test.pack()
wdw.mainloop()
