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
    piece = place(pos)
    trace(place(pos))

def placesquare(x,y):
    main.create_rectangle(coord(x),coord(y),coord(x+1),coord(y+1),tags=("falling"))

def trace(lis):
    main.delete("falling")
    for i in range(22):
        for j in range(10):
            if lis[i][j] == 1:
                placesquare(j,i)

def place(pos,state):
    global shape
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
            lis[x][y-2] = 1
            lis[x][y+1] = 1
        elif state == 4:
            lis[x][y] = 1
            lis[x-1][y] = 1
            lis[x-2][y] = 1
            lis[x+1][y] = 1
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
    return lis

def check(mov,fstate): #pour le moment il ne fait que vérifier si ça sort pas de la zone de jeu, c'est du gros wip
    #mov est dans le cas d'un mouvement, mettre à 0 pour une rotation
    #fstate (futurestate c'trop long) est dans le cas d'une rotation, donne l'état voulu de la pièce (pas l'actuel), mettre à 0 pour un déplacement
    global fixed, piece, pos
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
    return out

def mirai(): #TEST
    global pos, piece, state
    pos = (pos[0],pos[1]-1)
    k = check(3,0)
    if k == 1:
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
ch = Button(test,text="check", command=mirai)
ch.pack()
test.pack()

wdw.mainloop()
