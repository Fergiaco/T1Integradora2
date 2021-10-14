import os
import time

#############################
#nomes e respectivo hash
arquivo='443KB'  #QmW5zTdPXnp8KsVhcxPsxTytUWj8ZZfCLm8FhXzaDLFfxE
arquivo='55MB'  #QmVL277PN2Hma58Abxtw6w81QWEQaunL5o8teY2QMLutwR
arquivo='350MB' #QmQNhjBA3qidmZwSh47hcvYKoiPDFC1a8oCSFmhTvLSbKH

f = open(arquivo, "w")

temposAdd=[]
temposPin=[]

for x in range(50):
    tIni=time.time()
    os.system('ipfs add C:\\Users\\ferna\\Downloads\\'+arquivo)
    temposAdd.append(time.time()-tIni)
    
    tIni=time.time()
    os.system('ipfs pin add QmQNhjBA3qidmZwSh47hcvYKoiPDFC1a8oCSFmhTvLSbKH')
    temposPin.append(time.time()-tIni)
    f.write(str(temposAdd[x])+', '+str(temposPin[x])+'\n')

f.close()
