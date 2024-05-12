import random

num_aleatorios = [random.randint(1, 100) for i in range(15)]
print ("Lista Original", num_aleatorios)

num_invertidos = num_aleatorios [::-1]
print("Lista Invertida", num_invertidos)
