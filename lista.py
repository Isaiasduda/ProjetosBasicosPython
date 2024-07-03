carros = ['bmw x6', 'bmw x7', 'bmw x8']
cliente = input('Insira o carro desejado: ')

if cliente.lower() in carros:
    print('Carro Disponivel!')
else:
    print('Carro Indisponivel!')#