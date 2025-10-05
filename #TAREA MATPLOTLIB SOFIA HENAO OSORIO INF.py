#TAREA MATPLOTLIB SOFIA HENAO OSORIO INFORMATICA 2
import numpy as np
import matplotlib.pyplot as plt



vec = np.random.rand(720) #1-Vector creado de forma aleatoria

mat = vec.reshape(120, 6) #2-Hacer rechape

#3-Crear transpuesta de la matriz inicial y copias de esta en orden C y F
mat_T = mat.T   

mat_T_C = np.array(mat_T, order="C")
mat_T_F = np.array(mat_T, order="F")

#4-Crear el subplot con 6 paneles
plt.figure(figsize=(12, 9))

#5- Creación de graficos en cada panel 
#6-Titulos y etiquetas

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

# Panel 3 - Errorbar-aprendido en clase
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
plt.hist(mat_T[3], bins=20,density=True, histtype="stepfilled", edgecolor="none", color="y", alpha=0.7)
plt.title("Histograma")
plt.xlabel("valor")
plt.ylabel("frecuencia")
plt.grid(True)

# Panel 5- pie
plt.subplot(3, 2, 5)
sizes = mat_T[4].reshape(6, -1).sum(axis=1)
labels = [f"G{i}" for i in range(6)]
colors=['#ff9999','#66b3ff','#99ff99','#ffcc99', '#c2c2f0', '#ffb3e6']
plt.pie(sizes, labels=labels, colors=colors, autopct="%1.1f%%")
plt.title("Pie (fila 4)")

# Panel 6 - Bar 
plt.subplot(3, 2, 6)
sums = mat_T.sum(axis=1)  # suma de cada fila
x = np.arange(6)

plt.bar(x, sums, color="teal")#6 barras, cada una representa la suma de los 120 valores de cada fila de mat_T
plt.title("Bar (suma por fila)")
plt.xlabel("Fila")
plt.ylabel("Suma")
plt.grid(True)

plt.suptitle("6 paneles con diferentes gráficos", fontsize=16, y=1.02)
plt.tight_layout()
plt.subplots_adjust(hspace=0.6, wspace=0.4)

plt.show()


