def morral_ejemplo(morral, pesos, valores, n):

    # Caso base / Evita que se vaya al infinito.
    if n == 0 or morral == 0:
        return 0
    # Termina caso base
   
    # Pregunta si alcanza el objeto en mi mochila mochila
    if pesos[n - 1] > morral:
        return morral_ejemplo(morral, pesos, valores, n - 1)
    # Si es que no le pregunta al siguiente objeto (n-1)
    
    # Le sumo el valor max al morral o no le sumo.
    return max(valores[n - 1] + morral_ejemplo(morral - pesos[n - 1], pesos, valores, n - 1), morral_ejemplo(morral, pesos, valores, n - 1))



if __name__ == "__main__":
    valores = [60, 100, 120]
    pesos = [10, 20, 30]
    morral = 50
    n = len(valores)

    resultado = morral_ejemplo(morral, pesos, valores, n)
    print(resultado)