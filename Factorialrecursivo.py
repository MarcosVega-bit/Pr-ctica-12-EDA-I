'''En el siguiente ejemplo se calcula un factorial usando la recursión
'''
def factorial_recursivo(numero):
    if numero < 2: #El caso base es cuando numero < 2 y la función regresa 1 
        return 1
    return numero * factorial_recursivo(numero-1) #La función se llama a sí misma
    