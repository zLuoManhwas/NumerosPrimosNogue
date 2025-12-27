import numpy as np
import matplotlib.pyplot as plt

def generar_primordial():
    # Parámetros de la realidad (R representa la complejidad)
    n = 10000
    r = np.linspace(2.5, 4.0, n)
    iteraciones = 1000
    ultimo = 100

    # El valor inicial (la chispa)
    x = 1e-5 * np.ones(n)

    plt.figure(figsize=(12, 8))

    # Dejamos que el sistema fluya sin observar (para que se asiente)
    for i in range(iteraciones):
        x = r * x * (1 - x)

        # Solo empezamos a anotar los valores cuando el sistema "es"
        if i >= (iteraciones - ultimo):
            plt.plot(r, x, ',k', alpha=0.25) # Graficamos en el plano cartesiano

    plt.title("Plano Cartesiano de lo Primordial: El Diagrama de Bifurcación")
    plt.xlabel("Complejidad (R)")
    plt.ylabel("Estado de Existencia (X)")
    plt.grid(True, alpha=0.1)
    plt.show()

generar_primordial()