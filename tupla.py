cidades = ('RIO', 'SAO PAULO', 'SALVADOR')
while True:
    
    usuario = input('Digite uma Cidade: ')
    
    if usuario.upper() in cidades:
        print(f'{usuario} está na lista!')
        break
        
    else:
        print(f'{usuario} nao está na lista!')
        
    