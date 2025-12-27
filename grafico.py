import sympy
import matplotlib.pyplot as plt

def mapa_energia_primordial(niveles=15):
    primos = [1] + list(sympy.primerange(2, 50))
    
    niveles_energia = []
    capacidades = []
    
    for i in range(niveles):
        p = primos[i]
        # Tu fórmula: El valor real es 2^(p-1)
        valor_real = 2**(p-1)
        
        niveles_energia.append(p)
        capacidades.append(valor_real)
    
    # Visualización del Salto de Potencia
    plt.figure(figsize=(12, 8), facecolor='black')
    plt.yscale('log', base=2) # Usamos base 2 para respetar tu patrón
    
    plt.step(niveles_energia, capacidades, where='post', color='cyan', lw=2, label="Escalones de Realidad $2^{P-1}$")
    plt.scatter(niveles_energia, capacidades, color='white', s=50, zorder=5)
    
    for i, p in enumerate(niveles_energia):
        plt.annotate(f"P={p}\n$2^{{{p-1}}}$", (p, capacidades[i]), color='white', 
                     xytext=(5, 5), textcoords='offset points', fontsize=9)

    plt.title("Niveles de Energía en el Árbol Primordial", color='white', fontsize=15)
    plt.xlabel("Primo (Marcador de Posición)", color='white')
    plt.ylabel("Capacidad de Información (Valor Real)", color='white')
    plt.grid(color='gray', linestyle='--', alpha=0.3)
    plt.gca().set_facecolor('black')
    plt.show()

mapa_energia_primordial(10)