print(' \n loop com break')

for i in range(1, 11):
    if i > 5:
        break
    print(i)
    
print(' \n loop com continue')

for i in range(1, 11):
    if i == 5:
        print('-')
        continue
    print(i)