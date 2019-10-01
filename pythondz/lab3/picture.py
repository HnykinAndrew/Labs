from graph import *
import math
import numpy as np
windowSize(1000, 1000)
canvasSize(1000, 1000)
global xvostobj
global ptiza1
global ptiza2
global ptiza3
global rib
global i
global krilo1
global krilo2
def elips(x1,y1,x2,y2):
    a=(x2-x1)/2
    b=(y2-y1)/2
    kost=[]
    for fi in range(1,360,1):
        y=int(b*math.sin(fi*math.pi/180)+y1+b)
        x=int(a*math.cos(fi*math.pi/180)+x1+a)
        kost.append((x,y))
    obj=polygon(kost)
    return obj
def neboslices(pos,h0,l):
    c1=1
    c2=1
    c3=254
    delc=int(255/len(h0))
    for h in h0:
        brushColor(c1,c2,c3)
        c1+=delc
        c2+=int(delc/2)
        c3-=delc
        rectangle(pos[0],pos[1],pos[0]+l,pos[1]+h)
        pos[1]+=h
    brushColor(0,0,255)
    rectangle(pos[0],pos[1],pos[0]+l,1000)
def duga(x0,y0,r,fi0,fi1):
    penColor(0,0,0)
    penSize(3)
    kost=[]
    for i in range(fi0,fi1-1,1):
        y=-r*math.sin(i*math.pi/180)+y0
        x=-r*math.cos(i*math.pi/180)+x0
        x1=-r*math.cos((i+1)*math.pi/180)+x0
        y1=-r*math.sin((i+1)*math.pi/180)+y0
        kost.append(line(x,y,x1,y1))
    penSize(1)
    return kost
def bird(x,y,r,fi0,fi1):
    penColor("white")
    return [duga(x-r/2,y,r/2,fi0,fi1),duga(x+r/2,y,r/2,180-fi1,180-fi0)]
def telo(x):
    brushColor('white')
    return elips(319+x,677,526+x,761)
def sheya(x):
    brushColor('white')
    return elips(510+x,683,588+x,723)
def golova(x):
    brushColor('white')
    k = elips(570+x,662,630+x,702)
    brushColor("black")
    y = elips(608+x,669,615+x,676)
    return k,y
def klyuv(x):
    brushColor('yellow')
    return polygon([[627+x, 677], [676+x, 671], [676+x, 671], [689+x, 679], [689+x, 679], [628+x, 683], [628+x, 683], [690+x, 680], [690+x, 680], [674+x, 697], [674+x, 697], [625+x, 688], [627+x, 677]])
def xvost(x):
    brushColor('white')
    return polygon([[344+x, 693], [301+x, 650], [301+x, 650], [268+x, 698], [268+x, 698], [323+x, 720], [344+x, 693]])
def krilozad(x):
    brushColor('white')
    return polygon([[451+x, 683], [442+x, 593], [382+x, 572], [314+x, 528], [338+x, 590], [383+x, 622], [390+x, 672], [451+x, 683]])
def krilopered(x):
    brushColor('white')
    return polygon([[442+x, 687], [406+x, 615], [334+x, 602], [293+x, 579], [312+x, 625], [369+x, 639], [376+x, 683], [442+x, 687]])
def nogazad(x):
    brushColor('white')
    k = elips(420+x,749,455+x,809)
    brushColor('white')
    y = polygon([[450+x, 797], [488+x, 809], [489+x, 809], [512+x, 826], [511+x, 826], [504+x, 835], [504+x, 835], [450+x, 818], [450+x, 818], [438+x, 803], [450+x, 797]])
    brushColor('yellow')
    z = polygon([[511+x, 824], [548+x, 817], [546+x, 816], [523+x, 827], [523+x, 827], [543+x, 832], [543+x, 832], [517+x, 834], [517+x, 834], [532+x, 843], [530+x, 843], [511+x, 838], [511+x, 838], [508+x, 844], [508+x, 844], [503+x, 833], [511+x, 824]])
    return k,y,z
def nogapered(x):
    brushColor('white')
    k = elips(389+x,748,424+x,812)
    brushColor('white')
    y = polygon([[410+x, 806], [457+x, 829], [455+x, 829], [464+x, 846], [464+x, 846], [456+x, 854], [455+x, 854], [406+x, 823], [406+x, 822], [397+x, 803], [410+x, 806]])
    brushColor('yellow')
    z = polygon([[461+x, 847], [503+x, 855], [500+x, 854], [467+x, 855], [468+x, 856], [493+x, 868], [491+x, 868], [466+x, 862], [466+x, 863], [472+x, 880], [473+x, 879], [454+x, 854], [456+x, 858], [454+x, 865], [454+x, 865], [449+x, 850], [461+x, 847]])
    return k,y,z
def ptiza(x):
    global krilo1,krilo2
    nogazad1,nogazad2,nogazad3=nogazad(x)
    sheya1=sheya(x)
    golova1,golova2=golova(x)
    klyuv1=klyuv(x)
    telo1=telo(x)
    xvost1=xvost(x)
    krilo1=krilozad(x)
    krilo2=krilopered(x)
    nogapered1,nogapered2,nogapered3=nogapered(x)
def telo_rib():
    brushColor('gray')
    return elips(681,896,787,942)
def xvost_rib():
    brushColor('red')
    return polygon([[684, 915], [641, 894], [646, 931], [683, 923], [684, 915]])
def uppl_rib():
    brushColor('red')
    return polygon([[722, 902], [704, 880], [762, 879], [756, 901], [722, 902]])
def glaz_rib1():
    brushColor('blue')
    return elips(763,912,776,926)
def glaz_rib2():
    brushColor('black')
    return elips(771,921,770,922)
def glaz_rib3():
    brushColor('white')
    return elips(766,915,771,921)
def leftpl_rib():
    brushColor('red')
    return polygon([[703, 935], [693, 952], [693, 952], [714, 956], [714, 956], [720, 939], [703, 935]])
def rightpl_rib():
    brushColor('red')
    return polygon([[749, 940], [750, 956], [773, 947], [759, 933], [749, 940]])
def riba():
    global rib
    rib=[rightpl_rib(),
    leftpl_rib(),
    uppl_rib(),
    xvost_rib(),
    telo_rib(),
    glaz_rib1(),
    glaz_rib2(),
    glaz_rib3()
    ]
h=[100,50,100,200,200]
neboslices([0,0],h,1000)
ptiza1=bird(200,70,50,90,200)
ptiza2=bird(700,200,50,90,200)
ptiza3=bird(500,400,50,90,200)
x=-300
nogazad1,nogazad2,nogazad3=0,0,0
sheya1=0
golova1,golova2=0,0
klyuv1=0
telo1=0
xvost1=0
krilo1=0
krilo2=0
nogapered1,nogapered2,nogapered3=0,0,0
riba()
v_x=50
i=-1
def update():
    global i,x
    global ptiza1,ptiza2,ptiza3
    global krilo1,krilo2
    global nogazad1,nogazad2,nogazad3,sheya1,golova1,golova2,klyuv1,telo1,xvost1,krilo1,krilo2,nogapered1,nogapered2,nogapered3
    x=x+v_x
    for t in ptiza1[0]:
        deleteObject(t)
    for t in ptiza1[1]:
        deleteObject(t)
    ptiza1=bird(200+i*20,70+i*30,50,70+i*20,180+i*20)
    for t in ptiza2[0]:
        deleteObject(t)
    for t in ptiza2[1]:
        deleteObject(t)
    ptiza2=bird(700+i*20,200+i*30,50,70+i*20,180+i*20)
    for t in ptiza3[0]:
        deleteObject(t)
    for t in ptiza3[1]:
        deleteObject(t)
    ptiza3=bird(500+i*20,400+i*30,50,70+i*20,180+i*20)
    for t in rib:
        moveObjectBy(t,i*20,i*20)
    deleteObject(krilo1)
    if (i==1):
        brushColor("white")
        deleteObject(krilo1) 
        deleteObject(krilo2)
    else:
        brushColor("white")
        deleteObject(krilo1)
        krilo1=krilozad(x)
        deleteObject(krilo2)
        krilo2=krilopered(x)
    deleteObject(nogapered1)
    deleteObject(nogapered2)
    deleteObject(nogapered3)
    nogapered1,nogapered2,nogapered3=nogapered(x)
    deleteObject(sheya1)
    sheya1=sheya(x)
    deleteObject(golova1)
    deleteObject(golova2)
    golova1,golova2=golova(x)
    deleteObject(klyuv1)
    klyuv1=klyuv(x)
    deleteObject(telo1)
    telo1=telo(x)
    deleteObject(xvost1)
    xvost1=xvost(x)
    deleteObject(nogazad1)
    deleteObject(nogazad2)
    deleteObject(nogazad3)
    nogazad1,nogazad2,nogazad3=nogazad(x)
    i=-i
onTimer(update,1000)
run()
def func():
	return x,y
x,y = func(dfg)
