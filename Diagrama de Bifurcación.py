# Ejemplo de Diagrama de Bifurcación.
"""
Archivo: Diagrama de Bifurcación.py
Autores: Dennis Zavala & Jetro López.
Fecha: 2025-30-07
Licencia: MIT
Descripción:
Diagrama de Bifurcación.
"""
import numpy as np
import matplotlib.pyplot as plt

def mapa_logistico(x, r):
    return r * x * (1 - x)

def generar_bifurcacion():
    r_vals = np.linspace(2.5, 4.0, 1000)
    x_vals = []
    r_plot = []
    
    for r in r_vals:
        x = 0.5  # Condición inicial
        # Eliminar transitorio
        for _ in range(1000):
            x = mapa_logistico(x, r)
        # Registrar datos
        for _ in range(100):
            x = mapa_logistico(x, r)
            x_vals.append(x)
            r_plot.append(r)
    
    plt.figure(figsize=(12, 6))
    plt.scatter(r_plot, x_vals, s=0.1, alpha=0.8)
    plt.xlabel('Parámetro r')
    plt.ylabel('x')
    plt.title('Diagrama de Bifurcación del Mapa Logístico')
    plt.show()

# Generar diagrama

generar_bifurcacion()
