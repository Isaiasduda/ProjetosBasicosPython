lista = [1, 2, 3, 4, 5]
quadrado = lambda x: x **2

resultados = []

for i in lista:
    resultados.append(quadrado(i))
    
print(f' O quadrado dos numeros {lista} sao {resultados}!')