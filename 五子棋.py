import BetaGo,BetaGo2,BetaGo3,FastBetaGo3,ai_go,ai_go2
import pygame,time,sys
from pygame.locals import MOUSEMOTION,MOUSEBUTTONDOWN

pygame.init()
mysize = 15
bg_size = width, height = mysize*30+170, mysize*30+20
screen  = pygame.display.set_mode(bg_size)
pygame.display.set_caption("1213清心的五子棋")

font = pygame.font.SysFont('SimHei',30)
smallfont = pygame.font.SysFont('SimHei',20)
qipan,qizi = [],[]
clockwiseqipan,anticlockwiseqipan=[],[]
thinktime = 0.00001
time1,time2=0,0
numPCVSPC=0
pip,blacknum,whitenum,dognum=100-numPCVSPC,0,0,0
for i in range(mysize):
    qipan.append([])
    for j in range(mysize):
        qipan[i].append(0)
for i in range(mysize*2 - 1):
    clockwiseqipan.append([])
    anticlockwiseqipan.append([])
    for j in range(mysize-abs(mysize-i-1)):
        clockwiseqipan[i].append(0)
        anticlockwiseqipan[i].append(0)
for i in range(mysize**2):
    qizi.append([-100,0])
game,whowin,whoturn,whofirst,whichpc = 0,'none',0,0,['','']

def pk(which,whofirst,me=2-whofirst):
    if which=='BetaGo':
        return BetaGo.next(qipan,qizi,whoturn,me,3-me)
    elif which=='BetaGo2':
        return BetaGo2.next(qipan,qizi,whoturn,me,3-me)
    elif which=='BetaGo3':
        return BetaGo3.next(qipan,qizi,whoturn,me,3-me)
    elif which=='FastBetaGo3':
        return FastBetaGo3.next(list(qipan),clockwiseqipan,anticlockwiseqipan,whoturn,me)
    elif which=='ai_go':
        return ai_go.ai(qipan,me)
    elif which=='ai_go2':
        return ai_go2.ai(qipan,me)
def log(which,whofirst,whowin):
    if 'FastBetaGo3' in which and whowin=='You':
        pygame.image.save(screen,'data/'+'FastBetaGo3'+time.strftime('%m%d_%H%M%S',time.localtime(time.time()))+'.jpg')
        with open('data/'+'FastBetaGo3'+time.strftime('%m%d_%H%M%S',time.localtime(time.time()))+'.txt','w')as f:
            for index in qizi:
                if index[0]!=-100:
                    f.write(hex(index[0])[2]+hex(index[1])[2])
                else:
                    break
        pygame.image.save(screen,'data/last.jpg')
        with open('data/last.txt','w')as f:
            for index in qizi:
                if index[0]!=-100:
                    f.write(hex(index[0])[2]+hex(index[1])[2])
                else:
                    break
    pass
def readlog(logname):
    with open('data/'+logname,'r')as f:
        for i in range(mysize**2):
            try:
                qizi[i][0]=int(f.read(1),16)
                qizi[i][1]=int(f.read(1),16)
                qipan[qizi[i][0]][qizi[i][1]]=2-(i+1)%2
            except:
                qipan[qizi[i-1][0]][qizi[i-1][1]]=0
                qipan[qizi[i-2][0]][qizi[i-2][1]]=0
                qizi[i-1]=[-100,0]
                qizi[i-2]=[-100,0]
                print(i-1)
                return i-2
while True:
    screen.fill((204,204,204))
    #绘制棋盘
    for i in range(1,mysize-1):
        pygame.draw.line(screen,(0,0,0),(i*30+30,30),(i*30+30,mysize*30),1)
        pygame.draw.line(screen,(0,0,0),(30,i*30+30),(mysize*30,i*30+30),1)
        screen.blit(smallfont.render(str(i+1),True,(0,0,0)),(25+i*30,5))
        screen.blit(smallfont.render(chr(i+65),True,(0,0,0)),(5,25+i*30))
    for i in [0,mysize-1]:
        pygame.draw.line(screen,(0,0,0),(i*30+30,30),(i*30+30,mysize*30),3)
        pygame.draw.line(screen,(0,0,0),(30,i*30+30),(mysize*30,i*30+30),3)
        screen.blit(smallfont.render(str(i+1),True,(0,0,0)),(25+i*30,5))
        screen.blit(smallfont.render(chr(i+65),True,(0,0,0)),(5,25+i*30))
    for i in [[120,120],[360,120],[120,360],[360,360],[240,240]]:
        pygame.draw.ellipse(screen,(0,0,0),(i[0]-5,i[1]-5,10,10),0)
    #绘制棋子
    for i in range(mysize**2):
        if i%2==1:
            pygame.draw.ellipse(screen,(255,255,255),\
            (qizi[i][1]*30-10+30, qizi[i][0]*30-10+30,20,20),0)
        if i%2==0:
            pygame.draw.ellipse(screen,(0,0,0),\
            (qizi[i][1]*30-10+30,qizi[i][0]*30-10+30,20,20),0)
        screen.blit(smallfont.render(str(i+1),True,(0,255,0)),(qizi[i][1]*30-10+30,qizi[i][0]*30-10+30))
    if game == 200:
        text1 = font.render("BetaGo",True,(0,0,0))
        text2 = font.render("BetaGo2",True,(0,0,0))
        text3 = font.render("BetaGo3",True,(0,0,0))
        text4 = font.render("FastBetaGo3",True,(0,0,0))
        text5 = font.render("ai_go",True,(0,0,0))
        text6 = font.render("ai_go2",True,(0,0,0))
        text7 = font.render("VS Who?",True,(255,0,0))
        text8 = font.render("BetaGo来自1213清心",True,(0,0,255))
        text9 = font.render("ai_go来自云星宇",True,(0,0,255))
        pygame.draw.rect(screen,(0,0,0),(width-150,50,150,40),1)
        pygame.draw.rect(screen,(0,0,0),(width-150,100,150,40),1)
        pygame.draw.rect(screen,(0,0,0),(width-150,150,150,40),1)
        pygame.draw.rect(screen,(0,0,0),(width-150,200,150,40),1)
        pygame.draw.rect(screen,(0,0,0),(width-150,250,150,40),1)
        pygame.draw.rect(screen,(0,0,0),(width-150,300,150,40),1)
        screen.blit(text1,(width-150,50))
        screen.blit(text2,(width-150,100))
        screen.blit(text3,(width-150,150))
        screen.blit(text4,(width-150,200))
        screen.blit(text5,(width-150,250))
        screen.blit(text6,(width-150,300))
        screen.blit(text7,(width/2-200,height/2-80))
        screen.blit(text8,(width/2-200,height/2))
        screen.blit(text9,(width/2-200,height/2+80))
    if game == 20:
        text1 = font.render("People",True,(0,0,0))
        text2 = font.render("PC",True,(0,0,0))
        text5 = font.render("Who First?",True,(0,0,0))
        pygame.draw.rect(screen,(0,0,0),(width-150,50,150,40),1)
        pygame.draw.rect(screen,(0,0,0),(width-150,150,150,40),1)
        screen.blit(text1,(width-150,50))
        screen.blit(text2,(width-150,150))
        screen.blit(text5,(width/2,height/2))
    #绘制游戏开局,选择模式
    if game == 0:
        text1 = font.render("VS friend",True,(0,0,0))
        text2 = font.render("VS PC",True,(0,0,0))
        text3 = font.render("PC VS PC",True,(0,0,0))
        text4 = font.render("PC test",True,(0,0,0))
        pygame.draw.rect(screen,(0,0,0),(width-150,50,150,40),1)
        pygame.draw.rect(screen,(0,0,0),(width-150,150,150,40),1)
        pygame.draw.rect(screen,(0,0,0),(width-150,250,150,40),1)
        pygame.draw.rect(screen,(0,0,0),(width-150,350,150,40),1)
        screen.blit(text1,(width-150,50))
        screen.blit(text2,(width-150,150))
        screen.blit(text3,(width-150,250))
        screen.blit(text4,(width-150,350))
        if whowin == whichpc[0]:
            blacknum+=1
        elif whowin == whichpc[1]:
            whitenum+=1
        elif whowin == 'Dogfall':
            dognum+=1
        screen.blit(font.render(whowin+str(' Win' if whowin and whowin!='Dogfall'else ''),\
                                True,(255,0,0)),(width/2-150,height/2))

        #time.sleep(0.5)
        if pip<100:
            print(blacknum,dognum,whitenum,pip,whoturn,whowin+' win')
            for i in range(mysize):
                for j in range(mysize):
                    qipan[i][j] = 0
                    clockwiseqipan[i+j][j if i+j<mysize else mysize-1-i] = 0
                    anticlockwiseqipan[mysize-1-j+i][min(i,j)] = 0
            for i in range(mysize**2):
                qizi[i][0],qizi[i][1]=-100,0
            whowin,whoturn = '',0
            game=3
        pip+=1
    if game==1 or game==2 or game==4:
        text1 = font.render("Return",True,(0,0,0))
        pygame.draw.rect(screen,(0,0,0),(width-150,50,150,40),1)
        screen.blit(text1,(width-150,50))
    if game:
        #判断赢家是哪一方
        for i in range(mysize):#竖
            for j in range(mysize-4):
                if qipan[i][j]==qipan[i][j+1]==qipan[i][j+2]==\
                    qipan[i][j+3]==qipan[i][j+4]==1:#黑
                    whowin,game = whichpc[0],0
                    log(whichpc,whofirst,whowin)
                if qipan[i][j]==qipan[i][j+1]==qipan[i][j+2]==\
                    qipan[i][j+3]==qipan[i][j+4]==2:#白
                    whowin,game = whichpc[1],0
                    log(whichpc,whofirst,whowin)
        for i in range(mysize-4):#横
            for j in range(mysize):
                if qipan[i][j]==qipan[i+1][j]==qipan[i+2][j]==\
                    qipan[i+3][j]==qipan[i+4][j]==1:#黑
                    whowin,game = whichpc[0],0
                    log(whichpc,whofirst,whowin)
                if qipan[i][j]==qipan[i+1][j]==qipan[i+2][j]==\
                    qipan[i+3][j]==qipan[i+4][j]==2:#白
                    whowin,game = whichpc[1],0
                    log(whichpc,whofirst,whowin)
        for i in range(mysize-4):#下斜
            for j in range(mysize-4):
                if qipan[i][j]==qipan[i+1][j+1]==qipan[i+2][j+2]==\
                    qipan[i+3][j+3]==qipan[i+4][j+4]==1:#黑
                    whowin,game = whichpc[0],0
                    log(whichpc,whofirst,whowin)
                if qipan[i][j]==qipan[i+1][j+1]==qipan[i+2][j+2]==\
                    qipan[i+3][j+3]==qipan[i+4][j+4]==2:#白
                    whowin,game = whichpc[1],0
                    log(whichpc,whofirst,whowin)
        for i in range(4,mysize):#上斜
            for j in range(mysize-4):
                if qipan[i][j]==qipan[i-1][j+1]==qipan[i-2][j+2]==\
                    qipan[i-3][j+3]==qipan[i-4][j+4]==1:#黑
                    whowin,game = whichpc[0],0
                    log(whichpc,whofirst,whowin)
                if qipan[i][j]==qipan[i-1][j+1]==qipan[i-2][j+2]==\
                    qipan[i-3][j+3]==qipan[i-4][j+4]==2:#白
                    whowin,game = whichpc[1],0
                    log(whichpc,whofirst,whowin)
        if qizi[mysize**2-1] !=[-100,0]:#平局
            whowin,game = 'Dogfall',0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEMOTION:
            pos = pygame.mouse.get_pos()
        elif event.type == MOUSEBUTTONDOWN:
            pressed_array = pygame.mouse.get_pressed()
            if pressed_array[0]:
                if game == 0:
                    if width-150<pos[0]<width-150+150 and 50<pos[1]<50+40:
                        game = 1
                        for i in range(mysize):
                            for j in range(mysize):
                                qipan[i][j] = 0
                                clockwiseqipan[i+j][j if i+j<mysize else mysize-1-i] = 0
                                anticlockwiseqipan[mysize-1-j+i][min(i,j)] = 0
                        for i in range(mysize**2):
                            qizi[i][0],qizi[i][1]=-100,0
                        whowin,whoturn = '',0
                    if width-150<pos[0]<width-150+150 and 150<pos[1]<150+40:
                        game = 200
                        for i in range(mysize):
                            for j in range(mysize):
                                qipan[i][j] = 0
                                clockwiseqipan[i+j][j if i+j<mysize else mysize-1-i] = 0
                                anticlockwiseqipan[mysize-1-j+i][min(i,j)] = 0
                        for i in range(mysize**2):
                            qizi[i][0],qizi[i][1]=-100,0
                        whowin,whoturn = '',0
                    if width-150<pos[0]<width-150+150 and 250<pos[1]<250+40:
                        game = 3
                        for i in range(mysize):
                            for j in range(mysize):
                                qipan[i][j] = 0
                                clockwiseqipan[i+j][j if i+j<mysize else mysize-1-i] = 0
                                anticlockwiseqipan[mysize-1-j+i][min(i,j)] = 0
                        for i in range(mysize**2):
                            qizi[i][0],qizi[i][1]=-100,0
                        whowin,whoturn = '',0
                    if width-150<pos[0]<width-150+150 and 350<pos[1]<350+40:
                        game = 4
                        for i in range(mysize):
                            for j in range(mysize):
                                qipan[i][j] = 0
                                clockwiseqipan[i+j][j if i+j<mysize else mysize-1-i] = 0
                                anticlockwiseqipan[mysize-1-j+i][min(i,j)] = 0
                        for i in range(mysize**2):
                            qizi[i][0],qizi[i][1]=-100,0
                        whowin,whoturn = '',0
                elif game==200:
                    if width-150<pos[0]<width-150+150 and 50<pos[1]<50+40:
                        whichpc[0],game='BetaGo',20
                    if width-150<pos[0]<width-150+150 and 100<pos[1]<100+40:
                        whichpc[0],game='BetaGo2',20
                    if width-150<pos[0]<width-150+150 and 150<pos[1]<150+40:
                        whichpc[0],game='BetaGo3',20
                    if width-150<pos[0]<width-150+150 and 200<pos[1]<200+40:
                        whichpc[0],game='FastBetaGo3',20
                    if width-150<pos[0]<width-150+150 and 250<pos[1]<250+40:
                        whichpc[0],game='ai_go',20
                    if width-150<pos[0]<width-150+150 and 300<pos[1]<300+40:
                        whichpc[0],game='ai_go2',20
                elif game==20:
                    if width-150<pos[0]<width-150+150 and 50<pos[1]<50+40:
                        whichpc.pop()
                        whichpc=['You']+whichpc
                        whofirst,game=0,2#人先
                        #whoturn = readlog('last.txt')
                    if width-150<pos[0]<width-150+150 and 150<pos[1]<150+40:
                        whichpc[1]='You'
                        whofirst,game=1,2#PC先
                        #whoturn = readlog('last.txt')
                if game==1 or game==2 or game==4:
                    if width-150<pos[0]<width-150+150 and 50<pos[1]<50+40 and whoturn>1:
                        qipan[qizi[whoturn-1][0]][qizi[whoturn-1][1]]=0
                        qipan[qizi[whoturn-2][0]][qizi[whoturn-2][1]]=0
                        clockwiseqipan[sum(qizi[whoturn-1])][qizi[whoturn-1][1] if sum(qizi[whoturn-1])<mysize else mysize-1-qizi[whoturn-1][0]] = 0
                        anticlockwiseqipan[mysize-1-qizi[whoturn-1][1]+qizi[whoturn-1][0]][min(qizi[whoturn-1])] = 0
                        clockwiseqipan[sum(qizi[whoturn-2])][qizi[whoturn-2][1] if sum(qizi[whoturn-2])<mysize else mysize-1-qizi[whoturn-2][0]] = 0
                        anticlockwiseqipan[mysize-1-qizi[whoturn-2][1]+qizi[whoturn-2][0]][min(qizi[whoturn-2])] = 0
                        qizi[whoturn-1],qizi[whoturn-2]=[-100,0],[-100,0]
                        whoturn-=2
                #双人模式
                if game == 1:
                    if whoturn%2==0:
                        for i in range(mysize):
                            for j in range(mysize):
                                if qipan[i][j] == 0:
                                    if i*30+15<pos[1]<i*30+45 and j*30+15<\
                                        pos[0]<j*30+45 :
                                            qizi[whoturn]=[i,j]
                                            whoturn,qipan[i][j] = whoturn+1,1
                                            clockwiseqipan[i+j][j if i+j<mysize else mysize-1-i] = 1
                                            anticlockwiseqipan[mysize-1-j+i][min(i,j)] = 1
                    if whoturn%2==1:
                        for i in range(mysize):
                            for j in range(mysize):
                                if qipan[i][j] == 0:
                                    if i*30+15<pos[1]<i*30+45 and j*30+15<\
                                        pos[0]<j*30+45 :
                                            qizi[whoturn]=[i,j]
                                            whoturn,qipan[i][j] = whoturn+1,2
                                            clockwiseqipan[i+j][j if i+j<mysize else mysize-1-i] = 2
                                            anticlockwiseqipan[mysize-1-j+i][min(i,j)] = 2
                #人机模式
                if game == 2:
                    if whoturn%2==whofirst:
                        for i in range(mysize):
                            for j in range(mysize):
                                if qipan[i][j] == 0:
                                    if i*30+15<pos[1]<i*30+45 and j*30+15<\
                                        pos[0]<j*30+45 :
                                            qizi[whoturn]=[i,j]
                                            time1=time.time()
                                            whoturn,qipan[i][j] = whoturn+1,1+whofirst
                                            clockwiseqipan[i+j][j if i+j<mysize else mysize-1-i] = 1+whofirst
                                            anticlockwiseqipan[mysize-1-j+i][min(i,j)] = 1+whofirst
                #test模式                            
                if game == 4:
                    whichpc=['ai_go2','FastBetaGo3']
                    if whoturn%2==0:
                        result=pk(whichpc[0],1,1)
                        qizi[whoturn]=[result[0],result[1]]
                        whoturn,qipan[result[0]][result[1]] = whoturn+1,1
                        clockwiseqipan[sum(result)][result[1] if sum(result)<mysize else mysize-1-result[0]] = 1
                        anticlockwiseqipan[mysize-1-result[1]+result[0]][min(result)] = 1
                    elif whoturn%2==1:
                        result=pk(whichpc[1],0,2)
                        result=BetaGo2.next(qipan,qizi,whoturn,2,1)
                        qizi[whoturn]=[result[0],result[1]]
                        whoturn,qipan[result[0]][result[1]] = whoturn+1,2
                        clockwiseqipan[sum(result)][result[1] if sum(result)<mysize else mysize-1-result[0]] = 2
                        anticlockwiseqipan[mysize-1-result[1]+result[0]][min(result)] = 2
                        #print(whoturn,(result[0]+1,result[1]+1))
    if game == 2:
        if time.time()-time1>thinktime:
            if whoturn%2==1-whofirst:
                result=pk(whichpc[1-whofirst],whofirst)
                qizi[whoturn]=[result[0],result[1]]
                whoturn,qipan[result[0]][result[1]] = whoturn+1,2-whofirst
                clockwiseqipan[sum(result)][result[1] if sum(result)<mysize else mysize-1-result[0]] = 2-whofirst
                anticlockwiseqipan[mysize-1-result[1]+result[0]][min(result)] = 2-whofirst
                #print(whoturn,(result[0]+1,result[1]+1))
    #机机模式
    if game == 3:
        whichpc=['BetaGo3','FastBetaGo3']
        if time.time()-time2>thinktime:
            if whoturn%2==0:
                result=pk(whichpc[0],1,1)
                if qipan[result[0]][result[1]]!=0:
                    print('xxxxxxxxxxxxx')#检验机器代码
                    #time.sleep(1)
                qizi[whoturn]=[result[0],result[1]]
                time1=time.time()
                whoturn,qipan[result[0]][result[1]] = whoturn+1,1
                clockwiseqipan[sum(result)][result[1] if sum(result)<mysize else mysize-1-result[0]] = 1
                anticlockwiseqipan[mysize-1-result[1]+result[0]][min(result)] = 1
                #print(whoturn,(result[0]+1,result[1]+1))
        if time.time()-time1>thinktime:
            if whoturn%2==1:
                result=pk(whichpc[1],0,2)
                if qipan[result[0]][result[1]]!=0:
                    print('xxxxxxxxxxxxx')#检验机器代码
                    #time.sleep(1)
                qizi[whoturn]=[result[0],result[1]]
                time2=time.time()
                whoturn,qipan[result[0]][result[1]] = whoturn+1,2
                clockwiseqipan[sum(result)][result[1] if sum(result)<mysize else mysize-1-result[0]] = 2
                anticlockwiseqipan[mysize-1-result[1]+result[0]][min(result)] = 2
                #print(whoturn,(result[0]+1,result[1]+1))
    pygame.display.flip()

