import numpy as np
import matplotlib.pyplot as plt

def generar_primordial_zoom_derecho():
    # Rango ajustado de 2.8 a 4.0
    n = 200000  
    r = np.linspace(2.8, 4.0, n) 
    iteraciones = 1000
    ultimo = 200 

    x = 1e-5 * np.ones(n)

    plt.figure(figsize=(16, 9), facecolor='white')
    ax = plt.gca()
    ax.set_facecolor('white')

    for i in range(iteraciones):
        x = r * x * (1 - x) 

        if i >= (iteraciones - ultimo):
            # Graficamos con negro (k) y transparencia sutil
            plt.plot(r, x, ',k', alpha=0.1)

    plt.title("Detalle de Bifurcación: El Límite del Caos (R > 2.8)", 
              color='black', fontsize=18, pad=20)
    plt.xlabel("Complejidad de la Rama (R)", color='black', fontsize=12)
    plt.ylabel("Estado de Equilibrio (X)", color='black', fontsize=12)
    
    # Ajuste de límites visuales
    plt.xlim(2.8, 4.0)
    plt.ylim(0, 1)
    
    for spine in ax.spines.values():
        spine.set_color('#CCCCCC')
    
    ax.tick_params(colors='black', which='both')
    
    plt.tight_layout()
    plt.show()

generar_primordial_zoom_derecho()