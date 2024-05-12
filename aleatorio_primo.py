import random

def primo (num):
    if num <= 1: #num 1 não é considerado primo
        return False
    if num <= 3: #num 3 é o primeiro num primo
        return True
    if num % 2 == 0 or num % 3 == 0: # num pares não são primos (exceto o 2) e num divisiveis por 3, como 21 / 3 = 7
        return False
    
    i = 5 # segundo num primo dos inteiros
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True
    
num_aleatorio = random.randint (1, 100)

print("Número aleatorio: ", num_aleatorio)
if primo(num_aleatorio):
    print("É primo. ")
else:
    print("Não é primo. ")
