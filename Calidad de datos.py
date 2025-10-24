# Ejemplo de problema de calidad de datos
"""
Archivo: calidad de datos.py
Autores: Dennis Zavala & Jetro López.
Fecha: 2025-30-07
Licencia: MIT
Descripción:
calidad de datos.
"""
def validar_datos(datos):
    """
    Validación de supuestos estocásticos
    """
    if len(datos) < 30:
        print("Advertencia: Muestra pequeña")
    if stats.shapiro(datos)[1] < 0.05:
        print("Advertencia: No normalidad detectada")

    return True
