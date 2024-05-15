#lista= []
# lista.pop()

#n=int(input())
#lista= []
#for _ in range(n):
#lista.sort(reverse=True)

#for indice in range(n):
# grupo = lista[indice-2:indice+1]
  #  grupo.remove(min(grupo))
 #   soma += sum(grupo)
  #  for num in grupo:
  #  grupo.remove(min(grupo))
  #  soma += sum                                                    
#print("soma")


soma = int(input())
a= int(input())
b = int(input())
resposta = 0
for numero in range(a, b+1):
    numero = str(numero)
    somaAlgarismos = 0
    for algarismo in numero:
        somaAlgarismos += int(algarismo)
    if somaAlgarismos == soma:
        resposta +=1
print(resposta)