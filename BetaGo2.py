#_*_ coding: UTF-8 _*_
#1213清心的五子棋谱库
from random import randint
from time import time
lib=[[['02222',0,10000.001],['20222',1,10000.002],['22022',2,10000.003],['22202',3,10000.004],['22220',4,10000.005]],
     [['01111',0,2000.001],['10111',1,2000.002],['11011',2,2000.003],['11101',3,2000.004],['11110',4,2000.005]],
     [['02220',0,400.001],['02220',4,400.002],['102220',5,0.5],['022201',0,0.5],['02220t',0,0.5],['t02220',5,0.5],\
      ['020220',2,400.003],['022020',3,400.004]],
     [['01110',0,80.001],['01110',4,80.002],['201110',5,0.5],['011102',0,0.5],['01110t',0,0.5],['t01110',5,0.5],\
      ['010110',2,80.003],['011010',3,80.004]],
     [['002221',0,60.001],['002221',1,60.002],['00222t',0,60.003],['00222t',1,60.004],\
      ['122200',5,60.005],['122200',4,60.006],['t22200',5,60.007],['t22200',4,60.008]],
     [['001112',0,50.001],['001112',1,50.002],['00111t',0,50.003],['00111t',1,50.004],\
      ['211100',5,50.005],['211100',4,50.006],['t11100',5,50.007],['t11100',4,50.008]],
     [['00220',0,35.001],['20200',3,35.002],['20020',2,35.003],\
      ['02200',4,35.004],['00202',1,35.005],['02002',2,35.006],\
      ['00220',1,35.007],['02200',3,35.008],['02020',2,35.009]],
     [['00110',0,20.001],['10100',3,20.002],['10010',2,20.003],\
      ['01100',4,20.004],['00101',1,20.004],['01001',2,20.006],\
      ['00110',1,20.007],['01100',3,20.008],['01010',2,20.009]]]
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
                strb+='t'
        if ilib[0]==strb:
            return [lo[0]+v[0]*ilib[1],lo[1]+v[1]*ilib[1]],ilib[2]
        return lo,0
    for i in range(len(qipan)):
        for j in range(len(qipan[i])):
            if qipan[i][j]==0:
                for v in [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]:
                    if -1<i+v[0]<len(qipan) and -1<j+v[1]<len(qipan[0]):
                        if qipan[i+v[0]][j+v[1]]==enemy:
                            ablelist[i][j]+=-0.0001
                        elif qipan[i+v[0]][j+v[1]]==0:
                            ablelist[i][j]+=0.00001 if ablelist[i][j]>0 else -0.00001
                        elif qipan[i+v[0]][j+v[1]]==me:
                            ablelist[i][j]+=0.0001
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
    #print('BetaGo2',time()-t)
    return [maxlo[0],maxlo[1]]
