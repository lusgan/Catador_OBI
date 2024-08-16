# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 16:06:04 2024

@author: balbi
"""

#lendo as informacoes
qtd_baldes, n_operacoes = map(int, input().split())
conchas = list(map(int, input().split()))
indices = list(map(int, input().split()))

#ajustar as conchas com seus respectivos baldes comecando a partir do 1
#para isso vou inserir um valor 0 na primeira posicao
conchas.insert(0, 0)
print(conchas)


#para cada indice i, contar a quantidade de conchas no balde i
for indice_i in indices:
    qtd_conchas_C = conchas[indice_i]  
    
    
    #retirar uma concha de cada balde j no qual |j-i| <= C
    for j in range(1,len(conchas)): #percorrer cada balde j, lembrando de comecar do 1
        
        if abs(j - indice_i) <= qtd_conchas_C: #se |j-i| <= C
            
            if(conchas[j]!=0):#Lembrar que so podemos retirar uma concha, caso tenhamos conchas no balde
                conchas[j] = conchas[j] - 1 # retirar uma concha de j
            
    
    print(conchas)


#contar quantas conchas restaram no total
qtd = 0
for conjunto_conchas in conchas:
    qtd+=conjunto_conchas
print(f"\n\nqtd = {qtd}")
