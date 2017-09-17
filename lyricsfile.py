# -*- coding: utf-8 -*-
import datetime, time
from pprint import pprint

def capturarLetra(url):
    arquivo = open(url,'r')
    letra={}
    tempo={}
    #musica=[]
    musica={}
    for n,l in enumerate(arquivo.read().splitlines()):
        while l[0] == '[':
            pprint(l)
            tempo[l[1:9]] = n
            l = l[10:]
        letra[n]=l
    arquivo.close()
    keys = tempo.keys()
    keys.sort()
    
    for i in keys:
        musica[i]=letra[tempo[i]]
        #musica.append((i,letra[tempo[i]]))
    return musica
    
def timeTosecond(valor):
    s = int(valor[-2:])
    m = int(valor[3:5])
    h = int(valor[0:2])
    return ((h*3600)+(m*60)+s)*1000