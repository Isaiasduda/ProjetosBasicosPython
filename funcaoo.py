def potencia(num1, num2= 2):
    return num1 ** num2


user1=int(input('Digite um numero : '))
user2=input('Digite outro numero (default = 2):')

if user2:
    print(f' o resultado e: {potencia(user1 , int(user2) )}')
else:
    print(f' o resultado e: {potencia(user1)}')