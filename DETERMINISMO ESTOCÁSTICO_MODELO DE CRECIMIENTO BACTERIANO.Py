"""
============================================================
DETERMINISMO ESTOCÁSTICO: MODELO DE CRECIMIENTO BACTERIANO
============================================================

Autor: Jetro Ramón López Hernández
Fecha: 14-04-2025

Descripción:
Este script implementa un modelo de determinismo estocástico para simular
el crecimiento de una población bacteriana. Combina una tendencia 
determinista exponencial con perturbaciones aleatorias gaussianas.

Modelo matemático: X(t) = f(t;θ) + ε(t)
Donde:
- f(t;θ) = N₀ * e^(rt) : componente determinista
- ε(t) ~ N(0,σ²) : componente estocástica (ruido)
============================================================
"""

# === IMPORTACIÓN DE BIBLIOTECAS ===
import numpy as np                    # Cálculos numéricos y vectores
import matplotlib.pyplot as plt       # Visualización gráfica
from scipy import stats              # Estadísticas avanzadas
import pandas as pd                  # Manejo de datos tabulares

# === CONFIGURACIÓN INICIAL DEL ENTORNO GRÁFICO ===
plt.style.use('seaborn-v0_8')        # Estilo visual moderno
plt.rcParams['figure.figsize'] = (12, 8)    # Tamaño de figura: 12x8 pulgadas
plt.rcParams['font.size'] = 12              # Tamaño de fuente base

# === PARÁMETROS DEL MODELO ===
# Parámetros biológicos del sistema
N0 = 1000           # Población bacteriana inicial (unidades)
r = 0.5             # Tasa de crecimiento específica (1/hora)
sigma = 10          # Desviación estándar del ruido (sqrt(100))

# === DATOS SIMULADOS DEL EJEMPLO ===
# Datos temporales discretos (0 a 5 horas)
tiempo = np.array([0, 1, 2, 3, 4, 5])

# Valores teóricos deterministas calculados
crecimiento_determinista = np.array([1000, 1649, 2718, 4482, 7389, 12182])

# Perturbaciones aleatorias agregadas (ruido gaussiano)
ruido_aleatorio = np.array([12, -8, 25, -15, 33, -22])

# Observaciones reales resultantes (determinista + ruido)
observacion_real = np.array([1012, 1641, 2743, 4467, 7422, 12160])

# === GENERACIÓN DE DATOS CONTINUOS PARA LA TENDENCIA ===
# Crear vector de tiempo continuo para suavizar la curva
t_continuo = np.linspace(0, 5, 100)  # 100 puntos entre 0 y 5 horas

# Calcular la función determinista continua: f(t) = N₀ * e^(rt)
curva_determinista = N0 * np.exp(r * t_continuo)

# === CÁLCULO DE INTERVALOS DE CONFIANZA ===
# Intervalo de confianza del 95% (±1.96 * desviación estándar)
intervalo_95 = 1.96 * sigma
limite_superior = curva_determinista + intervalo_95  # Límite superior
limite_inferior = curva_determinista - intervalo_95  # Límite inferior

# === CREACIÓN Y CONFIGURACIÓN DE LA FIGURA ===
# Inicializar figura y ejes para el gráfico
fig, ax = plt.subplots(figsize=(12, 8))

# === GRAFICACIÓN DE LA TENDENCIA DETERMINISTA ===
# Línea continua azul que representa la tendencia teórica
ax.plot(t_continuo, curva_determinista, 'b-', linewidth=2, 
        label=f'Tendencia Determinista: f(t) = {N0} * e^({r}t)')

# === GRAFICACIÓN DE BANDAS DE CONFIANZA ===
# Área sombreada que representa el intervalo de confianza del 95%
ax.fill_between(t_continuo, limite_inferior, limite_superior, 
                alpha=0.2, color='blue', 
                label=f'Intervalo de Confianza 95% (+/-{intervalo_95:.0f})')

# === GRAFICACIÓN DE OBSERVACIONES REALES ===
# Puntos rojos que representan las mediciones observadas
ax.scatter(tiempo, observacion_real, color='red', s=100, zorder=5, 
           label='Observaciones Reales', marker='o', edgecolors='black')

# === GRAFICACIÓN DE VALORES TEÓRICOS DETERMINISTAS ===
# Puntos verdes cuadrados que muestran los valores teóricos sin ruido
ax.scatter(tiempo, crecimiento_determinista, color='green', s=80, 
           label='Valores Teóricos Deterministas', marker='s', alpha=0.7)

# === GRAFICACIÓN DE LÍNEAS DE DIFERENCIA (RUIDO) ===
# Líneas punteadas rojas que conectan valores teóricos con observaciones
for i in range(len(tiempo)):
    ax.plot([tiempo[i], tiempo[i]], 
            [crecimiento_determinista[i], observacion_real[i]], 
            'r--', alpha=0.7, linewidth=1.5)

# === PERSONALIZACIÓN DE ETIQUETAS Y TÍTULO ===
# Etiqueta del eje X con formato mejorado
ax.set_xlabel('Tiempo (horas)', fontsize=14, fontweight='bold')

# Etiqueta del eje Y con formato mejorado
ax.set_ylabel('Población Bacteriana', fontsize=14, fontweight='bold')

# Título principal del gráfico con descripción del modelo
ax.set_title('Determinismo Estocástico: Crecimiento de Población Bacteriana\nX(t) = f(t;theta) + epsilon(t)', 
             fontsize=16, fontweight='bold', pad=20)

# === CONFIGURACIÓN DE LA CUADRÍCULA ===
# Activar cuadrícula con transparencia para mejor visualización
ax.grid(True, alpha=0.3)

# === CONFIGURACIÓN DE LA LEYENDA ===
# Leyenda posicionada en el lado derecho inferior con estilo mejorado
ax.legend(fontsize=12,                    # Tamaño de fuente de la leyenda
          loc='lower right',              # Posición: esquina inferior derecha
          frameon=True,                   # Marco alrededor de la leyenda
          fancybox=True,                  # Bordes redondeados
          shadow=True,                    # Sombra para mejor visibilidad
          bbox_to_anchor=(1.02, 0.05),    # Coordenadas específicas de posición
          borderaxespad=0.,               # Espacio entre leyenda y ejes
          title='Componentes del Modelo') # Título de la leyenda

# === CONFIGURACIÓN DE LOS EJES ===
# Establecer límites de visualización para mejor enfoque
ax.set_xlim(-0.2, 5.2)    # Eje X: de -0.2 a 5.2 horas
ax.set_ylim(0, 14000)     # Eje Y: de 0 a 14000 unidades

# === AGREGAR ANOTACIONES NUMÉRICAS ===
# Etiquetas con valores numéricos en cada punto de observación
for i in range(len(tiempo)):
    ax.annotate(f'{observacion_real[i]}', 
                (tiempo[i], observacion_real[i]), 
                xytext=(5, 5),              # Desplazamiento de texto
                textcoords='offset points', # Coordenadas relativas
                fontsize=9,                 # Tamaño de fuente pequeño
                alpha=0.8)                  # Transparencia

# === PANEL DE ESTADÍSTICAS DESCRIPTIVAS ===
# Cuadro de texto con estadísticas clave del modelo
stats_text = f'''Estadísticas del Modelo:
• Población inicial (N0): {N0}
• Tasa crecimiento (r): {r}
• Desv. estándar (σ): {sigma}
• R² observaciones: {np.corrcoef(crecimiento_determinista, observacion_real)[0,1]:.3f}'''

# Posicionar el cuadro de estadísticas en la esquina superior izquierda
ax.text(0.02, 0.98, stats_text, transform=ax.transAxes, 
        verticalalignment='top', 
        bbox=dict(boxstyle='round', facecolor='white', alpha=0.8),
        fontsize=10)

# === AJUSTE FINAL DEL DISEÑO ===
# Optimizar el layout para evitar solapamientos
plt.tight_layout()

# === VISUALIZACIÓN DEL GRÁFICO ===
# Mostrar la figura generada
plt.show()

# === GENERACIÓN DE TABLA DE DATOS ===
print("\n" + "="*60)
print("DATOS DEL MODELO DETERMINISMO ESTOCÁSTICO")
print("="*60)

# Crear estructura de datos tabular
data = {
    'Tiempo (t)': tiempo,
    'Crecimiento Determinista': crecimiento_determinista,
    'Ruido Aleatorio': ruido_aleatorio,
    'Observación Real': observacion_real
}

# Convertir a DataFrame y mostrar tabla formateada
df = pd.DataFrame(data)
print(df.to_string(index=False))

# === ANÁLISIS ESTADÍSTICO COMPLEMENTARIO ===
print("\n" + "="*60)
print("ANÁLISIS ESTADÍSTICO")
print("="*60)

# Calcular y mostrar estadísticas descriptivas
print(f"Media de observaciones: {np.mean(observacion_real):.1f}")
print(f"Desviación estándar observaciones: {np.std(observacion_real):.1f}")
print(f"Error medio absoluto: {np.mean(np.abs(ruido_aleatorio)):.1f}")
print(f"Correlación teórico-observado: {np.corrcoef(crecimiento_determinista, observacion_real)[0,1]:.4f}")

# === CÓDIGO DE EJEMPLO PARA GENERACIÓN DE NUEVOS DATOS ===
print("\n" + "="*60)
print("CÓDIGO PARA GENERAR DATOS SIMILARES")
print("="*60)
print("""
# Para generar nuevos datos con el mismo modelo:
np.random.seed(42)  # Para reproducibilidad
nuevos_ruidos = np.random.normal(0, sigma, len(t_continuo))
nuevas_observaciones = curva_determinista + nuevos_ruidos
""")

"""
============================================================
NOTAS DEL DESARROLLADOR:

Este código implementa el concepto fundamental del determinismo 
estocástico donde:
- Componente sistemático: f(t;θ) = N₀ * e^(rt)
- Componente aleatorio: ε(t) ~ N(0,σ²)
- Observación total: X(t) = f(t;θ) + ε(t)

La visualización permite comprender cómo una tendencia determinista
puede manifestarse con variaciones aleatorias en observaciones reales.

============================================================
"""
