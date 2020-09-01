#_*_ coding: UTF-8 _*_
#1213清心的五子棋谱库
from random import choice
def next(qipan,qizi,whoturn,me,enemy):
    #五子连线
    for i in range(len(qipan)):#横
        for j in range(1,len(qipan[0])-4):
            if qipan[i][j]==qipan[i][j+1]\
                ==qipan[i][j+2]==qipan[i]\
               [j+3]==me:
                if qipan[i][j-1]==0:
                    return (i,j-1)
                if qipan[i][j+4]==0:
                    return (i,j+4)
    for i in range(1,len(qipan)-4):#竖
        for j in range(len(qipan[0])):
            if qipan[i][j]==qipan[i+1][j]\
               ==qipan[i+2][j]==qipan[i+3]\
               [j]==me:
                if qipan[i-1][j]==0:
                    return (i-1,j)
                if qipan[i+4][j]==0:
                    return (i+4,j)
    for i in range(1,len(qipan)-4):#下斜
        for j in range(1,len(qipan[0])-4):
            if qipan[i][j]==qipan[i+1][j+1]\
               ==qipan[i+2][j+2]==qipan[i+3]\
                [j+3]==me:
                if qipan[i-1][j-1]==0:
                    return (i-1,j-1)
                if qipan[i+4][j+4]==0:
                    return (i+4,j+4)
    for i in range(4,len(qipan)-1):#上斜
        for j in range(1,len(qipan[0])-4):
            if qipan[i][j]==qipan[i-1][j+1]\
               ==qipan[i-2][j+2]==qipan[i-3]\
               [j+3]==me:
                if qipan[i+1][j-1]==0:
                    return (i+1,j-1)
                if qipan[i-4][j+4]==0:
                    return (i-4,j+4)
    #变形五子连线
    for i in range(len(qipan)):#横
        for j in range(len(qipan[0])-4):
            if qipan[i][j]==qipan[i][j+4]\
               ==qipan[i][j+2]==qipan[i]\
               [j+3]==me:
                if qipan[i][j+1]==0:
                    return (i,j+1)
            if qipan[i][j]==qipan[i][j+1]\
               ==qipan[i][j+4]==qipan[i]\
               [j+3]==me:
                if qipan[i][j+2]==0:
                    return (i,j+2)
            if qipan[i][j]==qipan[i][j+1]\
               ==qipan[i][j+2]==qipan[i]\
               [j+4]==me:
                if qipan[i][j+3]==0:
                    return (i,j+3)
    for i in range(len(qipan)-4):#竖
        for j in range(len(qipan[0])):
            if qipan[i][j]==qipan[i+4][j]\
               ==qipan[i+2][j]==qipan[i+3]\
               [j]==me:
                if qipan[i+1][j]==0:
                    return (i+1,j)
            if qipan[i][j]==qipan[i+1][j]\
               ==qipan[i+4][j]==qipan[i+3]\
               [j]==me:
                if qipan[i+2][j]==0:
                    return (i+2,j)
            if qipan[i][j]==qipan[i+1][j]\
               ==qipan[i+2][j]==qipan[i+4]\
               [j]==me:
                if qipan[i+3][j]==0:
                    return (i+3,j)
    for i in range(len(qipan)-4):#下斜
        for j in range(len(qipan[0])-4):
            if qipan[i][j]==qipan[i+4][j+4]\
               ==qipan[i+2][j+2]==qipan[i+3]\
               [j+3]==me:
                if qipan[i+1][j+1]==0:
                    return (i+1,j+1)
            if qipan[i][j]==qipan[i+1][j+1]\
               ==qipan[i+4][j+4]==qipan[i+3]\
               [j+3]==me:
                if qipan[i+2][j+2]==0:
                    return (i+2,j+2)
            if qipan[i][j]==qipan[i+1][j+1]\
               ==qipan[i+2][j+2]==qipan[i+4]\
               [j+4]==me:
                if qipan[i+3][j+3]==0:
                    return (i+3,j+3)
    for i in range(4,len(qipan)):#上斜
        for j in range(len(qipan[0])-4):
            if qipan[i][j]==qipan[i-4][j+4]\
               ==qipan[i-2][j+2]==qipan[i-3]\
               [j+3]==me:
                if qipan[i-1][j+1]==0:
                    return (i-1,j+1)
            if qipan[i][j]==qipan[i-1][j+1]\
               ==qipan[i-4][j+4]==qipan[i-3]\
               [j+3]==me:
                if qipan[i-2][j+2]==0:
                    return (i-2,j+2)
            if qipan[i][j]==qipan[i-1][j+1]\
               ==qipan[i-2][j+2]==qipan[i-4]\
               [j+4]==me:
                if qipan[i-3][j+3]==0:
                    return (i-3,j+3)
    #拦截四子连线
    for i in range(len(qipan)):#横
        for j in range(1,len(qipan[0])-4):
            if qipan[i][j]==qipan[i][j+1]\
                ==qipan[i][j+2]==qipan[i]\
               [j+3]==enemy:
                if qipan[i][j-1]==0:
                    return (i,j-1)
                if qipan[i][j+4]==0:
                    return (i,j+4)
    for i in range(1,len(qipan)-4):#竖
        for j in range(len(qipan[0])):
            if qipan[i][j]==qipan[i+1][j]\
               ==qipan[i+2][j]==qipan[i+3]\
               [j]==enemy:
                if qipan[i-1][j]==0:
                    return (i-1,j)
                if qipan[i+4][j]==0:
                    return (i+4,j)
    for i in range(len(qipan)-3):#下斜
        for j in range(len(qipan[0])-3):
            if qipan[i][j]==qipan[i+1][j+1]\
               ==qipan[i+2][j+2]==qipan[i+3]\
                [j+3]==enemy:
                if i!=0 and j!=0 and qipan[i-1][j-1]==0:
                    return (i-1,j-1)
                if i!=len(qipan)-4 and j!=len(qipan[0])-4 and\
                   qipan[i+4][j+4]==0:
                    return (i+4,j+4)
    for i in range(3,len(qipan)-1):#上斜
        for j in range(len(qipan[0])-3):
            if qipan[i][j]==qipan[i-1][j+1]\
               ==qipan[i-2][j+2]==qipan[i-3]\
                [j+3]==enemy:
                if i!=len(qipan)-1 and j!=0\
                   and qipan[i+1][j-1]==0:
                    return (i+1,j-1)
                if i!=3 and j!=len(qipan[0])-4\
                   and qipan[i-4][j+4]==0:
                    return (i-4,j+4)
    #拦截四子连线
    for i in range(len(qipan)):#横
        for j in range(len(qipan[0])-4):
            if qipan[i][j]==qipan[i][j+4]\
               ==qipan[i][j+2]==qipan[i]\
               [j+3]==enemy:
                if qipan[i][j+1]==0:
                    return (i,j+1)
            if qipan[i][j]==qipan[i][j+1]\
               ==qipan[i][j+4]==qipan[i]\
               [j+3]==enemy:
                if qipan[i][j+2]==0:
                    return (i,j+2)
            if qipan[i][j]==qipan[i][j+1]\
               ==qipan[i][j+2]==qipan[i]\
               [j+4]==enemy:
                if qipan[i][j+3]==0:
                    return (i,j+3)
    for i in range(len(qipan)-4):#竖
        for j in range(len(qipan[0])):
            if qipan[i][j]==qipan[i+4][j]\
               ==qipan[i+2][j]==qipan[i+3]\
               [j]==enemy:
                if qipan[i+1][j]==0:
                    return (i+1,j)
            if qipan[i][j]==qipan[i+1][j]\
               ==qipan[i+4][j]==qipan[i+3]\
               [j]==enemy:
                if qipan[i+2][j]==0:
                    return (i+2,j)
            if qipan[i][j]==qipan[i+1][j]\
               ==qipan[i+2][j]==qipan[i+4]\
               [j]==enemy:
                if qipan[i+3][j]==0:
                    return (i+3,j)
    for i in range(len(qipan)-3):#下斜
        for j in range(len(qipan[0])-3):
            if i!=len(qipan)-4 and j!=len(qipan[0])-4\
               and qipan[i][j]==qipan[i+4][j+4]\
                ==qipan[i+2][j+2]==qipan[i+3]\
               [j+3]==enemy:
                if qipan[i+1][j+1]==0:
                    return (i+1,j+1)
            if i!=len(qipan)-4 and j!=len(qipan[0])-4\
               and qipan[i][j]==qipan[i+1][j+1]\
                ==qipan[i+4][j+4]==qipan[i+3]\
               [j+3]==enemy:
                if qipan[i+2][j+2]==0:
                    return (i+2,j+2)
            if i!=len(qipan)-4 and j!=len(qipan[0])-4\
               and qipan[i][j]==qipan[i+1][j+1]\
               ==qipan[i+2][j+2]==qipan[i+4]\
               [j+4]==enemy:
                if qipan[i+3][j+3]==0:
                    return (i+3,j+3)
    for i in range(3,len(qipan)):#上斜
        for j in range(len(qipan[0])-3):
            if i!=3 and j!=len(qipan[0])-4 and\
               qipan[i][j]==qipan[i-4][j+4]\
               ==qipan[i-2][j+2]==qipan[i-3]\
               [j+3]==enemy:
                if qipan[i-1][j+1]==0:
                    return (i-1,j+1)
            if i!=3 and j!=len(qipan[0])-4 and\
               qipan[i][j]==qipan[i-1][j+1]\
               ==qipan[i-4][j+4]==qipan[i-3]\
               [j+3]==enemy and i!=3 and j!=len(qipan[0])-4:
                if qipan[i-2][j+2]==0:
                    return (i-2,j+2)
            if i!=3 and j!=len(qipan[0])-4 and\
               qipan[i][j]==qipan[i-1][j+1]\
               ==qipan[i-2][j+2]==qipan[i-4]\
               [j+4]==enemy and i!=3 and j!=len(qipan[0])-4:
                if qipan[i-3][j+3]==0:
                    return (i-3,j+3)
    #四子连线
    for i in range(len(qipan)):#横
        for j in range(1,len(qipan[0])-3):
            if qipan[i][j]==qipan[i][j+1]\
               ==qipan[i][j+2]==me and\
               qipan[i][j-1]==qipan[i]\
               [j+3]==0:
                return (i,j-1)
    for i in range(1,len(qipan)-3):#竖
        for j in range(len(qipan[0])):
            if qipan[i][j]==qipan[i+1][j]\
               ==qipan[i+2][j]==me and\
                qipan[i-1][j]==qipan[i+3]\
                   [j]==0:
                return (i-1,j)
    for i in range(1,len(qipan)-3):#下斜
        for j in range(1,len(qipan[0])-3):
            if qipan[i][j]==qipan[i+1][j+1]\
               ==qipan[i+2][j+2]==me and\
               qipan[i-1][j-1]==qipan[i+3]\
                [j+3]==0:
                return (i-1,j-1)
    for i in range(3,len(qipan)-1):#上斜
        for j in range(1,len(qipan[0])-3):
            if qipan[i][j]==qipan[i-1][j+1]\
               ==qipan[i-2][j+2]==me and\
               qipan[i+1][j-1]==qipan[i-3]\
               [j+3]==0:
                return (i+1,j-1)
    #拦截三子连线
    for i in range(len(qipan)):#横
        for j in range(1,len(qipan[0])-3):
            if qipan[i][j]==qipan[i][j+1]\
                ==qipan[i][j+2]==enemy and\
               qipan[i][j-1]==qipan[i]\
               [j+3]==0:
                return (i,j-1)
    for i in range(1,len(qipan)-3):#竖
        for j in range(len(qipan[0])):
            if qipan[i][j]==qipan[i+1][j]\
               ==qipan[i+2][j]==enemy and\
               qipan[i-1][j]==qipan[i+3]\
               [j]==0:
                return (i-1,j)
    for i in range(1,len(qipan)-3):#下斜
        for j in range(1,len(qipan[0])-3):
             if qipan[i][j]==qipan[i+1][j+1]\
               ==qipan[i+2][j+2]==enemy and\
               qipan[i-1][j-1]==qipan[i+3]\
               [j+3]==0:
                return (i-1,j-1)
    for i in range(3,len(qipan)-1):#上斜
        for j in range(1,len(qipan[0])-3):
            if qipan[i][j]==qipan[i-1][j+1]\
               ==qipan[i-2][j+2]==enemy and\
               qipan[i+1][j-1]==qipan[i-3]\
               [j+3]==0:
                return (i+1,j-1)
    #拦截变形三子连线
    for i in range(len(qipan)):#横
        for j in range(1,len(qipan[0])-4):
            if qipan[i][j-1]== qipan[i][j+4]\
               ==0 and qipan[i][j]==\
               qipan[i][j+3]==enemy:
                if qipan[i][j+1]==enemy\
                   and qipan[i][j+2]==0:
                    return (i,j+2)
                if qipan[i][j+2]==enemy\
                   and qipan[i][j+1]==0:
                    return (i,j+1)
    for i in range(1,len(qipan)-4):#竖
        for j in range(len(qipan[0])):
            if qipan[i-1][j]==qipan[i+4][j]\
               ==0 and qipan[i][j]==\
               qipan[i+3][j]==enemy:
                if qipan[i+1][j]==enemy\
                   and qipan[i+2][j]==0:
                    return (i+2,j)
                if qipan[i+2][j]==enemy\
                   and qipan[i+1][j]==0:
                    return (i+1,j)
    for i in range(1,len(qipan)-4):#下斜
        for j in range(1,len(qipan[0])-4):
            if qipan[i-1][j-1]== qipan[i+4][j+4]\
               ==0 and qipan[i][j]==\
               qipan[i+3][j+3]==enemy:
                if qipan[i+1][j+1]==enemy\
                   and qipan[i+2][j+2]==0:
                    return (i+2,j+2)
                if qipan[i+2][j+2]==enemy\
                   and qipan[i+1][j+1]==0:
                    return (i+1,j+1)
    for i in range(4,len(qipan)-1):#上斜
        for j in range(1,len(qipan[0])-4):
            if qipan[i+1][j-1]==qipan[i-4][j+4]\
               ==0 and qipan[i][j]==\
               qipan[i-3][j+3]==enemy:
                if qipan[i-1][j+1]==enemy\
                   and qipan[i-2][j+2]==0:
                    return (i-2,j+2)
                if qipan[i-2][j+2]==enemy\
                   and qipan[i-1][j+1]==0:
                    return (i-1,j+1)
    if whoturn!=0:
        x,y=qizi[whoturn-1][0],qizi[whoturn-1][1]
        seed = []
        if x>0 and qipan[x-1][y]==0:
            seed.append((x-1,y))
        if x<len(qipan[0])-1 and qipan[x+1][y]==0:
            seed.append((x+1,y))
        if y>0 and qipan[x][y-1]==0:
            seed.append((x,y-1))
        if y<len(qipan[0])-1 and qipan[x][y+1]==0:
            seed.append((x,y+1))
        if x>0 and y>0 and qipan[x-1][y-1]==0:
            seed.append((x-1,y-1))
        if x>0 and y<len(qipan[0])-1 and\
           qipan[x-1][y+1]==0:
            seed.append((x-1,y+1))
        if x<len(qipan[0])-1 and y>0 and\
           qipan[x+1][y-1]==0:
            seed.append((x+1,y-1))
        if x<len(qipan[0])-1 and y<len(qipan[0])-1\
           and qipan[x+1][y+1]==0:
            seed.append((x+1,y+1))
        if len(seed):
            return choice(seed)
    if whoturn == 0:
        return (int(len(qipan)/2),int(len(qipan)/2))
    blank = []
    for i in range(len(qipan)):
        for j in range(len(qipan[0])):
            if qipan[i][j]==0:
                blank.append((i,j))
    return choice(blank)
