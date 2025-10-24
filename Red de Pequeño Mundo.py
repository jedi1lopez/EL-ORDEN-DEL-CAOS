# Ejemplo de Red de Pequeño Mundo
"""
Archivo: Red de Pequeño Mundo.py
Autores: Dennis Zavala & Jetro López.
Fecha: 2025-30-07
Licencia: MIT
Descripción:
Red de Pequeño Mundo.
"""
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

def crear_red_pequeno_mundo(n, k, p):
    """
    Crea una red de pequeño mundo tipo Watts-Strogatz
    """
    # Crear red regular
    G = nx.watts_strogatz_graph(n, k, p)
    
    # Calcular métricas
    avg_path_length = nx.average_shortest_path_length(G)
    clustering_coeff = nx.average_clustering(G)
    
    return G, avg_path_length, clustering_coeff

# Ejemplo
G, L, C = crear_red_pequeno_mundo(100, 4, 0.1)
print(f"Longitud de camino promedio: {L:.3f}")

print(f"Coeficiente de clustering: {C:.3f}")
