#TAREA MATPLOTLIB SOFIA HENAO OSORIO INFORMATICA 2
import numpy as np
import matplotlib.pyplot as plt



vec = np.random.rand(720) #Vector creado de forma aleatoria

mat = vec.reshape(120, 6) #Hacer rechape

mat_T = mat.T   # Crear transpuesta de la matriz inicial

#Crear copias con orden C y F
mat_T_C = np.array(mat_T, order="C")
mat_T_F = np.array(mat_T, order="F")

#Crear el subplot con 6 paneles
plt.figure(figsize=(12, 9))

# Panel 1-Plot
plt.subplot(3, 2, 1)   # (filas, columnas, índice)
x = np.arange(120)
plt.plot(x, mat_T[0], label="fila 0")
plt.title("Plot")
plt.xlabel("índice")
plt.ylabel("valor")
plt.grid(True)
plt.legend()

# Panel 2 - Scatter 
plt.subplot(3, 2, 2)
sc = plt.scatter(x, mat_T[1], c=mat_T[1], cmap="viridis", s=40, alpha=0.4)
plt.colorbar(sc, label="valor")   # añade barra de color
plt.title("Scatter")
plt.xlabel("índice")
plt.ylabel("valor")
plt.grid(True)

# Panel 3 - Errorbar-La guia de la tarea pide una grafica tipo bar pero en clase aprendimos a usar el errorbar
plt.subplot(3, 2, 3)
y = mat_T[2][:30]               # valores de la fila 2 (primeros 30)
x = np.arange(30)               # índices
err = np.random.rand(30) * 0.2  # errores simulados 

plt.errorbar(x, y, yerr=err, fmt='o', color="purple",
            ecolor="black", elinewidth=1, capsize=3, label="fila 2")
plt.title("Errorbar (primeros 30)")
plt.xlabel("índice (0..29)")
plt.ylabel("valor")
plt.grid(True)
plt.legend()

#Panel 4-histograma
plt.subplot(3, 2, 4)
plt.hist(mat_T[3], bins=20,normed=True, histtype="stepfilled", edgecolor="none", color="y", alpha=0.7)
plt.title("Histograma")
plt.xlabel("valor")
plt.ylabel("frecuencia")
plt.grid(True)

