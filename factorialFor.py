'''En el siguiente ejemplo se calcula un factorial con ciclo for
'''
def factorial_no_recursivo(numero):
    fact=1
    #Se genera una lista que va de n a 1, el -1 indica que cada iteración se resta 1 al índice
    for i in range(numero, 1, -1):
        fact = fact * i
    return fact    
