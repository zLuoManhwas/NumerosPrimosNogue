import sympy

def expansion_por_valor_primo(limite=100):
    # Generamos los 100 primos (incluyendo el 1 como origen según tu visión)
    primos = [1] + list(sympy.primerange(2, 542))

    print(f"{'Orden':<6} | {'Primo (P)':<10} | {'Operación':<15} | {'Valor en tu Realidad'}")
    print("-" * 75)

    for i, p in enumerate(primos):
        # El valor es 1 multiplicado por 2, P veces: 2^P
        Pe = p - 1
        valor = 2**Pe

        if i < 10:
            print(f"{i+1:<6} | {p:<10} | 1 * (2^{p:<2})      | {valor:,}")
        elif i < 15:
            # Notación científica porque los números crecen más que la memoria
            print(f"{i+1:<6} | {p:<10} | 1 * (2^{p:<2})      | {valor:.2e}")
        else:
            # A partir de aquí, solo la potencia importa
            if i == 15: print("...")
            if i >= 95:
                print(f"{i+1:<6} | {p:<10} | 1 * (2^{p:<2})     | 2^{p}")

expansion_por_valor_primo(100)