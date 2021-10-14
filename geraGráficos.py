import matplotlib.pyplot as plt
import numpy as np

temposDaemon=[]
total=0
cont=0

#############################
#Arquivo Log do Daemon
file=open('LOG1')

#Arquivo tempos Pin e Add
arq='443KB'

for linha in file:
    if 'db@open done' in linha:
        cont+=1
        l=linha.split('TÂ·')[1].replace('\n','')
        valor=float(l.replace('ms',''))
        valor=valor/1000
        total+=valor
        temposDaemon.append(valor)

i=[]
da=[]
c=0
for t in range(len(temposDaemon)):
    if t%2==0:
        c+=1
        i.append(c)
        da.append(temposDaemon[t])   

file=open(arq)
c=0
add=[]
pin=[]
for linha in file:
    l=linha.replace('\n','')
    l=l.split(', ')
    add.append(float(l[0]))
    pin.append(float(l[1]))
fig, ax = plt.subplots()

a=np.array(add)
p=np.array(pin)
d=np.array(da)

ax.set(xlabel='Número de testes', ylabel='Tempo(s)')
ax.axis([0,50,0,2])
ax.plot(i,d,"-b",label='Daemon')
ax.plot(i,a,"-k",label='Add')
ax.plot(i,p,"-r",label='Pin')
leg=ax.legend()

fig.savefig("g"+arq+".png")
plt.show()