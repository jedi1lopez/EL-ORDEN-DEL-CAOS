# Ejemplo de Optimización de Cartera Adaptativa
"""
Archivo: Optimización de Cartera Adaptativa.py
Autores: Dennis Zavala & Jetro López.
Fecha: 2025-30-07
Licencia: MIT
UNESR, Valencia, Carabobo, Republica bolivariana de Venezuela.
Descripción:
Optimización de Cartera Adaptativa.
"""
import numpy as np
from scipy.optimize import minimize

class CarteraAdaptativa:
    def __init__(self, retornos_historicos, n_generaciones=100):
        self.retornos = retornos_historicos
        self.n_activos = retornos_historicos.shape[1]
        self.n_gen = n_generaciones
        
    def fitness(self, pesos):
        """Función de fitness basada en Sharpe Ratio"""
        port_retorno = np.dot(pesos, np.mean(self.retornos, axis=0))
        port_riesgo = np.sqrt(np.dot(pesos.T, np.dot(np.cov(self.retornos.T), pesos)))
        return port_retorno / port_riesgo if port_riesgo > 0 else 0
    
    def evolucionar_cartera(self):
        """Algoritmo genético para optimización de cartera"""
        poblacion = self.generar_poblacion_inicial(50)
        
        for generacion in range(self.n_gen):
            # Evaluación de fitness
            fitness_scores = [self.fitness(ind) for ind in poblacion]
            
            # Selección
            padres = self.seleccionar_padres(poblacion, fitness_scores)
            
            # Cruzamiento y mutación
            descendencia = self.cruzar_y_mutar(padres)
            
            # Nueva generación
            poblacion = descendencia
            
        mejor_solucion = max(poblacion, key=self.fitness)
        return mejor_solucion, self.fitness(mejor_solucion)
    
    def generar_poblacion_inicial(self, tam):
        """Genera población inicial de carteras"""
        poblacion = []
        for _ in range(tam):
            pesos = np.random.random(self.n_activos)
            pesos = pesos / np.sum(pesos)  # Normalizar
            poblacion.append(pesos)
        return poblacion