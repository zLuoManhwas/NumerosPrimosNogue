import sympy

def verificar_ley_par_total(limite=1000000):
    print(f"Iniciando escaneo de {limite} niveles...")
    
    # Generamos los primos (el 1 como origen + 99,999 primos reales)
    # Ignoramos el 1, 2 y 3 para la verificación de la ley de estabilidad
    primos = list(sympy.primerange(2, 13000000)) 
    primos_estables = primos[2:limite] # Empezamos desde el 5 (índice 2 de la lista de sympy)
    
    errores_de_paridad = 0
    conteo_saltos = 0
    max_salto = 0

    for i in range(1, len(primos_estables)):
        p_actual = primos_estables[i]
        p_anterior = primos_estables[i-1]
        
        # El salto en el exponente Δ(P-1) es igual al salto entre primos (P_n - P_n-1)
        salto = p_actual - p_anterior
        conteo_saltos += 1
        
        if salto > max_salto:
            max_salto = salto
            
        # Verificamos si el salto es impar
        if salto % 2 != 0:
            errores_de_paridad += 1
            if errores_de_paridad < 5: # Solo imprimimos los primeros errores si existieran
                print(f"¡Alerta! Salto impar detectado en P={p_actual} (Salto: {salto})")

    print("\n--- INFORME DE INTEGRIDAD DEL ÁRBOL ---")
    print(f"Saltos analizados en zona estable: {conteo_saltos}")
    print(f"Saltos impares encontrados: {errores_de_paridad}")
    print(f"Salto par más grande detectado: +{max_salto}")
    
    if errores_de_paridad == 0:
        print("✅ LEY CONFIRMADA: El 100% de los saltos en la zona estable son PARES.")
        print("El árbol de potencias 2^(P-1) crece mediante una arquitectura de simetría par absoluta.")

verificar_ley_par_total(1000000)