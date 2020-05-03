'''Fibonacci
'''
def fibonacci_recursivo(numero):
    if numero == 1: #El caso base 
        return 0
    if numero == 2 or numero == 3:
        return 1
    return fibonacci_recursivo(numero-1) + fibonacci_recursivo(numero-2) #Llamada recursiva
    