#_*_ coding: UTF-8 _*_
#1213清心的五子棋谱库
from random import randint
from time import time
lib=[[['02222',0,100000],['20222',1,100000],['22022',2,100000]],
     [['01111',0,2000],['10111',1,2000],['11011',2,2000]],
     [['02220',0,600],['02220',4,600],['022201',0,0.1],['022209',0,0.1],['020220',2,600.1]],
     [['01110',0,86],['01110',4,86],['011102',0,0.1],['011109',0,0.1],['010110',2,86],['201110',1,-0.1],['011109',1,-0.1]],
     [['020221',0,60],['020221',2,60],['020229',0,60],['020229',2,60],\
      ['022021',0,60],['022021',3,60],['022029',0,60],['022029',3,60],\
      ['200221',1,60],['200221',2,60],['200229',1,60],['200229',2,60],\
      ['202021',1,60],['202021',3,60],['202029',1,60],['202029',3,60],\
      ['002221',0,60],['002221',1,60],['002229',0,60],['002229',1,60]],
     [['010112',0,50],['010112',2,50],['010119',0,50],['010119',2,50],\
      ['011012',0,50],['011012',3,50],['011019',0,50],['011019',3,50],\
      ['100112',1,50],['100112',2,50],['100119',1,50],['100119',2,50],\
      ['101012',1,50],['101012',3,50],['101019',1,50],['101019',3,50],\
      ['001112',0,50],['001112',1,50],['001119',0,50],['001119',1,50]],
     [['00220',0,35],['20200',3,35],['020020',2,35],['020020',3,35],['00220',1,35.1],['02020',2,35.1],\
      ['002202',0,-35],['220200',3,-35],['220020',1,-35],['220020',2,-35],['002202',1,-35.1],['202020',2,-35.1]],
     [['00110',0,27],['10100',3,27],['10010',1,27],['10010',2,27],['00110',1,27.1],['01010',2,27.1],\
      ['001101',0,-27],['110100',3,-27],['110010',1,-27],['110010',2,-27],['001101',1,-27.1],['101010',2,-27.1]]]
for i in range(len(lib)):
    for j in range(len(lib[i])):
        if lib[i][j][0]!=lib[i][j][0][::-1]:
            lib[i].append([lib[i][j][0][::-1],len(lib[i][j][0])-1-lib[i][j][1],lib[i][j][2]])

with open('ttt.txt','w')as f:
    [f.write(str([[i[1],i[2]]+[int(j) for j in i[0]]for i in ilib])+',\n')for ilib in lib]
def next(qipan,qizi,whoturn,me,enemy):
    ablelist,maxlo=[],[0,0]
    t=time()
    for i in range(len(qipan)):
        ablelist.append([])
        for j in range(len(qipan[i])):
            ablelist[i].append(0)
    def ddd(ilib,lo,v):
        strb=''
        for i in range(len(ilib[0])):
            if -1<lo[0]+v[0]*i<len(qipan) and -1<lo[1]+v[1]*i<len(qipan[0]):
                s=str(qipan[lo[0]+v[0]*i][lo[1]+v[1]*i])
                if me==1:
                    strb+='1' if s=='2' else '2' if s=='1' else '0'
                elif me==2:
                    strb+=s
            else:
                strb+='9'
        if ilib[0] == strb:
            #print(strb,[lo[1]+1,chr(lo[0]+65)],[lo[1]+v[1]*ilib[1]+1,chr(lo[0]+v[0]*ilib[1]+65)],ilib[2])
            return [lo[0]+v[0]*ilib[1],lo[1]+v[1]*ilib[1]],ilib[2]+randint(-1,1)/1000
        return lo,0
    for i in range(len(qipan)):
        for j in range(len(qipan[i])):
            if qipan[i][j]==0:
                for v in [[0,1],[1,0],[1,1],[1,-1],[0,-1],[-1,0],[-1,-1],[-1,1]]:
                    if -1<i+v[0]<len(qipan) and -1<j+v[1]<len(qipan[0]):
                        if qipan[i+v[0]][j+v[1]]==enemy:
                            ablelist[i][j]+=-0.005
                        elif qipan[i+v[0]][j+v[1]]==0:
                            ablelist[i][j]+=0.0001 if ablelist[i][j]>0 else -0.0001
                        elif qipan[i+v[0]][j+v[1]]==me:
                            ablelist[i][j]+=0.005
                ablelist[i][j]=abs(ablelist[i][j])+randint(-1,1)/100000
            for tlib in lib:
                for ilib in tlib:
                    for v in [[0,1],[1,0],[1,1],[-1,1]]:
                        result,able=ddd(ilib,[i,j],v)
                        ablelist[result[0]][result[1]]+=able
    if whoturn == 0:
        ablelist[int(len(qipan)/2)][int(len(qipan)/2)]+=0.1
    for i in range(len(ablelist)):
        for j in range(len(ablelist[i])):
            if ablelist[i][j]>ablelist[maxlo[0]][maxlo[1]]:
                maxlo=[i,j]
    #print([maxlo[1]+1,chr(65+maxlo[0])],ablelist[maxlo[0]][maxlo[1]])
    #print('BetaGo3',time()-t)
    return [maxlo[0],maxlo[1]]
