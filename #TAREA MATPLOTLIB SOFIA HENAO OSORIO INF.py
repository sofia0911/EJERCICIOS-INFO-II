#TAREA MATPLOTLIB SOFIA HENAO OSORIO INFORMATICA 2
import numpy as np
import matplotlib.pyplot as plt



vec = np.random.rand(720) #Vector creado de forma aleatoria

mat = vec.reshape(120, 6) #Hacer rechape

mat_T = mat.T   # Crear transpuesta de la matriz inicial

#Crear copias con orden C y F
mat_T_C = np.array(mat_T, order="C")
mat_T_F = np.array(mat_T, order="F")