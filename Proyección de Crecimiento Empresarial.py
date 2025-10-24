# Ejemplo de Proyección de Crecimiento Empresarial
"""
Archivo: Proyección de Crecimiento Empresarial.py
Autores: Dennis Zavala & Jetro López.
Fecha: 2025-30-07
Licencia: MIT
Descripción:
Proyección de Crecimiento Empresarial.
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Datos históricos de crecimiento
tiempo = np.array([0, 1, 2, 3, 4, 5])  # años
ventas = np.array([100, 105, 112, 118, 125, 132])  # millones

# Ajuste determinista (regresión lineal)
coeficientes = np.polyfit(tiempo, np.log(ventas), 1)
r = coeficientes[0]  # tasa de crecimiento
P0 = np.exp(coeficientes[1])  # valor inicial

print(f"Tasa de crecimiento: {r:.4f} ({r*100:.2f}%)")
print(f"Valor inicial: {P0:.2f} millones")

# Modelo determinista
def modelo_determinista(t):
    return P0 * np.exp(r * t)

# Análisis de residuales para componente estocástica
ventas_predichas = modelo_determinista(tiempo)
residuales = ventas - ventas_predichas
sigma = np.std(residuales)

print(f"Desviación estándar de residuales: {sigma:.2f}")

# Proyección futura con intervalos de confianza
tiempo_futuro = np.linspace(0, 10, 100)
proyeccion_media = modelo_determinista(tiempo_futuro)
intervalo_superior = proyeccion_media + 1.96 * sigma
intervalo_inferior = proyeccion_media - 1.96 * sigma

# Visualización
plt.figure(figsize=(10, 6))
plt.plot(tiempo, ventas, 'ro', label='Datos históricos', markersize=8)
plt.plot(tiempo_futuro, proyeccion_media, 'b-', label='Tendencia determinista')
plt.fill_between(tiempo_futuro, intervalo_inferior, intervalo_superior, 
                 alpha=0.3, color='blue', label='Intervalo de confianza 95%')
plt.xlabel('Tiempo (años)')
plt.ylabel('Ventas (millones)')
plt.title('Modelo de Determinismo Estocástico: Proyección de Ventas')
plt.legend()
plt.grid(True, alpha=0.3)

plt.show()
