# Ejemplo de Verificación del TCL.
"""
Archivo: Verificación del TCL.py
Autores: Dennis Zavala & Jetro López.
Fecha: 2025-30-07
Licencia: MIT
UNESR, Valencia, Carabobo, Republica bolivariana de Venezuela.
Descripción:
Verificación del TCL.
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def verificar_tcl(n_muestras=1000, tam_muestra=30):
    """
    Verifica el Teorema Central del Límite
    """
    # Generar muestras de distribución exponencial
    muestras = np.random.exponential(2, (n_muestras, tam_muestra))
    
    # Calcular medias muestrales
    medias = np.mean(muestras, axis=1)
    
    # Teórico
    mu_teorico = 2  # Media de exp(2)
    sigma_teorico = 2 / np.sqrt(tam_muestra)  # Error estándar
    
    # Histograma
    plt.figure(figsize=(10, 6))
    plt.hist(medias, bins=50, density=True, alpha=0.7, color='blue')
    
    # Distribución normal teórica
    x = np.linspace(medias.min(), medias.max(), 100)
    y = stats.norm.pdf(x, mu_teorico, sigma_teorico)
    plt.plot(x, y, 'r-', linewidth=2, label='Normal teórica')
    
    plt.xlabel('Media muestral')
    plt.ylabel('Densidad')
    plt.title('Verificación del Teorema Central del Límite')
    plt.legend()
    plt.show()
    
    # Prueba de normalidad
    shapiro_stat, shapiro_p = stats.shapiro(medias)
    print(f"Estadístico de Shapiro-Wilk: {shapiro_stat:.4f}")
    print(f"p-valor: {shapiro_p:.4f}")
    print(f"¿Normal? {'Sí' if shapiro_p > 0.05 else 'No'}")

# Ejecutar verificación
verificar_tcl()