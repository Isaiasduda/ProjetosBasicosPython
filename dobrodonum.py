def dobro(n):
   return n * 2
def quadrado(y):
    return dobro(y) **2 
    
usuario = int(input('Digite um numero: '))

print(f'O dobro do numero {usuario} é {dobro(usuario)}')
print(f'O quadrado do numero {usuario} é {quadrado(usuario)}')