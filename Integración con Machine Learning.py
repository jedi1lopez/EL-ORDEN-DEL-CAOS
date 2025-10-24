# Ejemplo de integración con machine learning
"""
Archivo: integración con machine learning.py
Autores: Dennis Zavala & Jetro López.
Fecha: 2025-30-07
Licencia: MIT
Descripción:
integración con machine learning.
"""
from sklearn.ensemble import RandomForestRegressor
import numpy as np

class ModeloHibrido:
    def __init__(self):
        self.modelo_determinista = self.tendencia_base
        self.modelo_residual = RandomForestRegressor()
    
    def tendencia_base(self, t):
        return 100 * np.exp(0.05 * t)  # Crecimiento exponencial
    
    def fit(self, X, y):
        tendencia = [self.tendencia_base(t) for t in X]
        residuales = y - tendencia
        self.modelo_residual.fit(X.reshape(-1,1), residuales)
    
    def predict(self, X):
        tendencia = [self.tendencia_base(t) for t in X]
        residuales = self.modelo_residual.predict(X.reshape(-1,1))

        return np.array(tendencia) + residuales
