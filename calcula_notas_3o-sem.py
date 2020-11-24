from numpy import mean, arange
from heapq import nlargest

def get_key(val, my_dict): 
    for key, value in my_dict.items(): 
         if val == value: 
             return key 

########################################## FISMOV ##########################################


a1=[6.45,0.15]
a2=[3.7,0.25]
a3=[3.1,0.20]
pf=[0,0.3]
aps=[mean(nlargest(3, [9.5, 9, 5.25, 5.3, 7.5])), 0.1]

def calcula_nota():
    nota=((a1[0]*a1[1])+(a2[0]*a2[1])+(a3[0]*a3[1])+(pf[0]*pf[1])+(aps[0]*aps[1]))
    return nota
    
nota=calcula_nota()

while nota<5:
    pf[0]+=0.01
    nota=calcula_nota()
    

print("Preciso tirar {0} ({1} sem o bônus) na PF para ficar com média {2} em FisMov".format(round((pf[0]-1),1), round((pf[0]),1), round(nota,1)))

########################################## MATVAR ##########################################

a1=[3.6,0.15]
a2=[3,0.2]
a3=[4.15,0.25]
a4=[6.7,0.2]
a5=[0,0.2]
af=[0,0.4]

def calcula_nota():
    nota=(((a1[0]*a1[1])+(a2[0]*a2[1])+(a3[0]*a3[1])+(a4[0]*a4[1])+(a5[0]*a5[1]))*0.6)+((af[0]*af[1]))
    return nota
    

nota=calcula_nota()
nota_semPF=mean([a1[0],a2[0],a3[0],a4[0]])

if nota_semPF>=5:
    while mean([nota_semPF,a5[0]])<6.5:
        a5[0]+=0.01
    print("Você precisa tirar {0} na AI5 para não ter que fazer a PF.".format(round(a5[0],1)))
    
else:
    while nota<5:
        a5[0]+=0.01
        af[0]+=0.01
        nota=calcula_nota()
    
    print("Preciso tirar {0} na AI5 e {1} na PF para ficar com média de provas {2} em MatVar".format(round(a5[0],1), round(af[0],1), round(nota,1)))

########################################## MATMULT ##########################################

a1=[2.25,0.25]
a2=[4.5,0.25]
a3=[0,0.25]
af=[0,0.25]

def calcula_nota():
    nota=((a1[0]*a1[1])+(a2[0]*a2[1])+(a3[0]*a3[1])+(af[0]*af[1]))
    return nota
    
nota=calcula_nota()

while nota<5:
    a3[0]+=0.1
    af[0]+=0.1
    nota=calcula_nota()
    

print("Preciso tirar {0} na AI3 e {1} na PF para ficar com média de provas {2} em MatMult".format(round(a3[0],1), round(af[0],1), round(nota,1)))

########################################## DESMAT ##########################################

LB1=6.93
AI1=4.6
AT2=4.7
QZ3=0

OBJ1=[[LB1,0.4],[AI1,0.4],[AT2,0.15],[QZ3,0.05]]

LB2=0
AI2C=0

OBJ2=[[LB2,0.44],[AI2C,0.56]]

LB3=0
AI2P=0

OBJ3=[[LB3,0.44],[AI2P,0.56]]

AT1=0
AT4=0

OBJ4=[[AT1,0.2],[AT4,0.8]]

def calcula_nota():
    nota_OBJ1=0
    nota_OBJ2=0
    nota_OBJ3=0
    nota_OBJ4=0
    
    for i in OBJ1:
        nota_OBJ1+=i[0]*i[1]
        
    for i in OBJ2:
        nota_OBJ2+=i[0]*i[1]
        
    for i in OBJ3:
        nota_OBJ3+=i[0]*i[1]
        
    for i in OBJ4:
        nota_OBJ4+=i[0]*i[1]
    
    notas={'A':list(arange(9,10,0.01)),'B':list(arange(7,8,0.01)),'C':list(arange(5,6,0.01)),'D':list(arange(4,5,0.01)), 'F':list(arange(0,4,0.01))}
    for v, d in notas.items():
        for r in d:
            lv=d.index(r)
            notas[v][lv]=round(r,2)
    
    results={}
    for n in notas.values():
        if round(nota_OBJ1,2) in n:
            results['OBJ1']=get_key(n, notas)
            
        if round(nota_OBJ2,2) in n:
            results['OBJ2']=get_key(n, notas)
            
        if round(nota_OBJ3,2) in n:
            results['OBJ3']=get_key(n, notas)
            
        if round(nota_OBJ4,2) in n:
            results['OBJ4']=get_key(n, notas)
    
    return results

print("Conceitos em DesMat: ",calcula_nota())