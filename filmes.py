filmes=[]
nome=[]
n = 5
for i in range(n):
    nome.append(input('Qual seu nome? '))
    filmes.append(int(input('Qual seu filme favorito?\n[1]Batman\n[2]Homem-Aranha')))
    
for i in range(n):
    if filmes[i]==1:
        print(nome[i],', seu filme favorito é Batman!')
        
    elif filmes[i]==2:
        print(nome[i],', seu filme favorito é Homem-Aranha!')
