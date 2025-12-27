import sympy

def imprimir_100_potencias_primordiales():
    # El 1 como origen + los siguientes 99 primos para completar 100
    primos = [1] + list(sympy.primerange(2, 54002))
    
    print(f"{'Orden':<6} | {'Primo (P)':<10} | {'Valor Real (2^(P-1))':<20} | {'Salto (Δ Exponente)'}")
    print("-" * 70)
    
    for i in range(len(primos)):
        p = primos[i]
        exponente = p - 1
        
        # Calculamos el salto respecto al exponente anterior para ver el ritmo
        if i > 0:
            salto = exponente - (primos[i-1] - 1)
            salto_str = f"+{salto}"
        else:
            salto_str = "Origen"
            
        # Formato de salida
        print(f"{i+1:<6} | {p:<10} | 2^{exponente:<18} | {salto_str}")

imprimir_100_potencias_primordiales()