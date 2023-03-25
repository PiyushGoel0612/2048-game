from tkinter import *
import random as rd

r = Tk()

btns = []
board = [[0 for i in range(4)] for j in range(4)]
indices = [[i,j] for i in range(4) for j in range(4)]
score = 0

def Left():
    global btns,board,indices,score
    sm = 0
    ii = 0
    jj = 0
    tbd = []
    for i in board:
        for j in i:
            sm += j
        if sm != 0:
            tbd.append([i,ii])
        sm = 0
        ii+=1
    for i in tbd:
        rw = i[0]
        rw1 = []
        indx = i[1]
        for j in rw:
            if j != 0:
                rw1.append(j)
        while len(rw1) < 4:
            rw1.append(0)
        m = 0
        while m<3:
            if rw1[m] == rw1[m+1]:
                rw1[m] *= 2
                rw1.pop(m+1)
                rw1.append(0)
                score += rw1[m]
                m+=1
            else:
                m+=1
        board[indx] = rw1
        if rw1 != rw:
            jj+=1
    if jj != 0:
        fake = []
        for i in range(4):
            for j in range(4):
                if board[i][j] == 0:
                    fake.append([i,j])
        xx = rd.choice(fake)
        board[xx[0]][xx[1]] = rd.choice([2,2,2,2,2,2,2,2,2,4])
    for i in btns:
        idx = btns.index(i)
        txt = board[idx//4][idx%4]
        txt1 = board[idx//4][idx%4]
        if txt == 0:
            txt = ' '
        i.config(text=txt,background=col(txt1))
    ll.config(text = "Your Score : "+str(score))

def Right():
    global btns,board,indices,score
    sm = 0
    ii = 0
    jj = 0
    tbd = []
    for i in board:
        for j in i:
            sm += j
        if sm != 0:
            tbd.append([i,ii])
        sm = 0
        ii+=1
    for i in tbd:
        rw = i[0]
        rw1 = []
        indx = i[1]
        for j in rw:
            if j != 0:
                rw1.append(j)
        while len(rw1) < 4:
            rw1.insert(0,0)
        m = 3
        while m>0:
            if rw1[m] == rw1[m-1]:
                rw1[m] *= 2
                rw1.pop(m-1)
                rw1.insert(0,0)
                score += rw1[m]
                m-=1
            else:
                m-=1
        board[indx] = rw1
        if rw1 != rw:
            jj+=1
    if jj != 0:
        fake = []
        for i in range(4):
            for j in range(4):
                if board[i][j] == 0:
                    fake.append([i,j])
        xx = rd.choice(fake)
        board[xx[0]][xx[1]] = rd.choice([2,2,2,2,2,2,2,2,2,4])
    for i in btns:
        idx = btns.index(i)
        txt = board[idx//4][idx%4]
        txt1 = board[idx//4][idx%4]
        if txt == 0:
            txt = ' '
        i.config(text=txt,background=col(txt1))
    ll.config(text = "Your Score : "+str(score))

def Up():
    global btns,board,indices,score
    board_transpose = [[] for j in range(4)]
    x0 = 0
    for i in range(3,-1,-1):
        for j in range(4):
            board_transpose[x0].append(board[j][i])
        x0 += 1
    
    sm = 0
    ii = 0
    jj = 0
    tbd = []
    for i in board_transpose:
        for j in i:
            sm += j
        if sm != 0:
            tbd.append([i,ii])
        sm = 0
        ii+=1
    for i in tbd:
        rw = i[0]
        rw1 = []
        indx = i[1]
        for j in rw:
            if j != 0:
                rw1.append(j)
        while len(rw1) < 4:
            rw1.append(0)
        m = 0
        while m<3:
            if rw1[m] == rw1[m+1]:
                rw1[m] *= 2
                rw1.pop(m+1)
                rw1.append(0)
                score += rw1[m]
                m+=1
            else:
                m+=1
        board_transpose[indx] = rw1
        if rw1 != rw:
            jj+=1
    if jj != 0:
        fake = []
        for i in range(4):
            for j in range(4):
                if board_transpose[i][j] == 0:
                    fake.append([i,j])
        xx = rd.choice(fake)
        board_transpose[xx[0]][xx[1]] = rd.choice([2,2,2,2,2,2,2,2,2,4])
    
    board = [[0 for i in range(4)] for j in range(4)]
    for i in range(4):
        for j in range(4):
            board[j][3-i] = board_transpose[i][j]
    
    for i in btns:
        idx = btns.index(i)
        txt = board[idx//4][idx%4]
        txt1 = board[idx//4][idx%4]
        if txt == 0:
            txt = ' '
        i.config(text=txt,background=col(txt1))
    ll.config(text = "Your Score : "+str(score))

def Down():
    global btns,board,indices,score
    board_transpose = [[] for j in range(4)]
    x0 = 0
    for i in range(3,-1,-1):
        for j in range(4):
            board_transpose[x0].append(board[j][i])
        x0 += 1

    sm = 0
    ii = 0
    jj = 0
    tbd = []
    for i in board_transpose:
        for j in i:
            sm += j
        if sm != 0:
            tbd.append([i,ii])
        sm = 0
        ii+=1
    for i in tbd:
        rw = i[0]
        rw1 = []
        indx = i[1]
        for j in rw:
            if j != 0:
                rw1.append(j)
        while len(rw1) < 4:
            rw1.insert(0,0)
        m = 3
        while m>0:
            if rw1[m] == rw1[m-1]:
                rw1[m] *= 2
                rw1.pop(m-1)
                rw1.insert(0,0)
                score += rw1[m]
                m-=1
            else:
                m-=1
        board_transpose[indx] = rw1
        if rw1 != rw:
            jj+=1
    if jj != 0:
        fake = []
        for i in range(4):
            for j in range(4):
                if board_transpose[i][j] == 0:
                    fake.append([i,j])
        xx = rd.choice(fake)
        board_transpose[xx[0]][xx[1]] = rd.choice([2,2,2,2,2,2,2,2,2,4])
    
    board = [[0 for i in range(4)] for j in range(4)]
    for i in range(4):
        for j in range(4):
            board[j][3-i] = board_transpose[i][j]

    for i in btns:
        idx = btns.index(i)
        txt = board[idx//4][idx%4]
        txt1 = board[idx//4][idx%4]
        if txt == 0:
            txt = ' '
        i.config(text=txt,background=col(txt1))
    ll.config(text = "Your Score : "+str(score))

def move(eff,sid):
    if sid == 'Left':
        Left()
    elif sid == 'Right':
        Right()
    elif sid == 'Up':
        Up()
    elif sid == 'Down':
        Down()

def col(nmbr):
    nn = [0,2,4,8,16,32,64,128,256,512,1024]
    clrs = ['#8B7355','#FFEFDB','#FFF68F','#FFA500','#FF8000','#FF4500','#FF0000','#CDCD00',
            '#CDCD00','#FFFF00','#FFFF00']
    if nmbr in nn:
        return clrs[nn.index(nmbr)]
    else:
        return str('#F8F8FF')

ff = Frame(r)
ff.pack()
ll = Label(ff,text="Your Score : 0",font=('Bold',20))
ll.pack()
for i in range(4):
    f = Frame(r)
    f.config(background='#CDAA7D',padx=5,pady=5)
    f.pack()
    for j in range(4):
        b = Button(f,font='Bold',height='4',width='8',relief='sunken',background='#8B7355')
        b.pack(side='left',padx=5)
        btns.append(b)

def start():
    global btns,board,indices
    x = list()
    x.extend(rd.sample(indices,2))
    numb = rd.choice([2,2,2,2,2,2,2,2,2,4])
    a = btns[(x[0][0])*4+(x[0][1])]
    b = btns[(x[1][0])*4+(x[1][1])]
    a.config(text='2',background=col(2))
    board[x[0][0]][x[0][1]] = 2
    b.config(text=numb,background=col(numb))
    board[x[1][0]][x[1][1]] = numb
start()

r.bind('<Left>',lambda eff,sid='Left': move(eff,sid))
r.bind('<Right>',lambda eff,sid='Right': move(eff,sid))
r.bind('<Up>',lambda eff,sid='Up': move(eff,sid))
r.bind('<Down>',lambda eff,sid='Down': move(eff,sid))

print(board)
r.mainloop()