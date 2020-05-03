'''Fibonacci con memorización
'''
#Memoria inicial
memoria = {1:0, 2:1, 3:1}
def fibonacci_memo(numero):
    if numero in memoria: #Si el numero ya se encuentra calculado, se regresa el valor, ya no hace cálculos  
        return memoria[numero]
    memoria[numero] = fibonacci_memo(numero-1) + fibonacci_memo(numero-2)
    return memoria[numero]