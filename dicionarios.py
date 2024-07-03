cidades={
    'Brasil': 'Brasilia',
    'Argentina': 'Buenos Aires',
    'Chile': 'Santiago',
    'Australia': 'Canberra',
    'Canada': 'Ottawa'
}

usuario = input('Digite o nome do País: ')

if usuario in cidades:
    print(f' A capital de {usuario} é {cidades[usuario]}.')
else:
    print('Desculpe, não temos informações sobre a capital desse país.')
