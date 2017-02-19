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

def placesquare(x,y): #trace un carré avec tag falling
    main.create_rectangle(coord(x),coord(y),coord(x+1),coord(y+1),tags=("falling"))

def trace(lis): #trace le contenu d'une liste
    main.delete("falling")
    for i in range(22):
        for j in range(10):
            if lis[i][j] == 1:
                placesquare(j,i)

def place(pos,state): #dispose une pièce sur une liste définie
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
            lis[x+1][y+1] = 1
            lis[x+1][y] = 1
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
        flipok = 0
    return lis

def check(mov,fstate): #vérifie qu'un mouvement est valide
    global fixed, piece, pos, flipok
    mirai = list(piece)
    out = 1
    if mov == 1:
        if mirai[-1] == [0,0,0,0,0,0,0,0,0,0]:
            mirai == mirai[:-1]
            mirai.insert(0,[0,0,0,0,0,0,0,0,0,0])

        else:
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
            out = 0
    elif mov == 3:
        empty = 1
        for i in range(22):
            if mirai[i][0] == 1:
                empty = 0
        if empty == 1:
            for i in range(22):
                element = mirai[i][0]
                mirai[i] = mirai[i][1:]
                mirai[i].append(element)
        else:
            out = 0
    elif mov == 0:
        mirai = place(pos,fstate)
        if flipok == 0:
            out = 0
            flipok = 1
    if out == 1:
        1+1
        for i in range(22):
            for j in range(10):
                if fixed[i][j]+mirai[i][j] == 2:
                    out = 0
    return out

def mirai(bisou): #à la base c'tait du test mais c'est la fonction définitive de gestion des déplacements. Faudra changer son nom du coup
    global pos, piece, state
    temppos = pos
    tstate = state
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
        if tstate == 5:
            tstate = 1
        k = check(0,tstate)
    if k == 1:
        pos = temppos
        state = tstate
        piece = place(pos,state)
        trace(piece)
        color()

def fixpiece(): #fixe la position d'une pièce
    global piece, fixed
    main.dtag("falling")
    for i in range(22):
        for j in range(10):
            fixed[i][j] = piece[i][j]+fixed[i][j]
        piece[i] = [0,0,0,0,0,0,0,0,0,0]
        print(piece[i]," | ",fixed[i])
    resetpiece()

def resetpiece(): #fait popper une nouvelle pièce, est appelée par fixpiece()
    global shape, state, pos
    shape = randint(1,7)
    state = 1
    pos = (0,4)
    trace(place(pos,state))
    color()

def color(): #colore la pièce en mouvement, à appeler à chaque retraçage
    global shape
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
    main.itemconfig("falling",fill=color)



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

flipok = 1

main = Canvas(width=300,height=660,bg="white")
main.pack(side = LEFT)

trace(fixed)
main.dtag("falling")

resetpiece()

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
fix = Button(test,text="Fix", command=fixpiece)
fix.pack()
test.pack(side = RIGHT)

wdw.bind("<Up>",lambda e:mirai(4))
wdw.bind("<Down>",lambda e:mirai(3))
wdw.bind("<Left>",lambda e:mirai(1))
wdw.bind("<Right>",lambda e:mirai(2))

wdw.mainloop()
