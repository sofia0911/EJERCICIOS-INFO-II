#TAREA MATPLOTLIB SOFIA HENAO OSORIO INFORMATICA 2
import numpy as np
import matplotlib.pyplot as plt



vec = np.random.rand(720) #Vector creado de forma aleatoria

mat = vec.reshape(120, 6) #Hacer rechape

mat_T = mat.T   # Crear transpuesta de la matriz inicial

#Crear copias con orden C y F
mat_T_C = np.array(mat_T, order="C")
mat_T_F = np.array(mat_T, order="F")

print("Shape de mat_T:", mat_T.shape)
print("C_CONTIGUOUS:", mat_T_C.flags['C_CONTIGUOUS'])
print("F_CONTIGUOUS:", mat_T_F.flags['F_CONTIGUOUS'])


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

# Panel 2-scatter
plt.subplot(3, 2, 2)
plt.scatter(x, mat_T[1], c="r", s=15, label="fila 1")
plt.title("Scatter")
plt.xlabel("índice")
plt.grid(True)
plt.legend()

# Panel 3-bar
plt.subplot(3, 2, 3)
plt.bar(x[:30], mat_T[2][:30])  
plt.title("Bar")
plt.xlabel("índice (0..29)")
plt.ylabel("valor")
plt.grid(True)

# Panel 4-histograma
plt.subplot(3, 2, 4)
plt.hist(mat_T[3], bins=15, color="g", alpha=0.7)
plt.title("Histograma")
plt.xlabel("valor")
plt.ylabel("frecuencia")
plt.grid(True)

# Panel 5- pie
plt.subplot(3, 2, 5)
groups = mat_T[4].reshape(6, -1).sum(axis=1)
labels = [f"G{i}" for i in range(6)]
plt.pie(groups, labels=labels, autopct="%1.1f%%", startangle=90)
plt.title("Pie (fila 4)")

# Panel 6-boxplot
plt.subplot(3, 2, 6)
plt.boxplot(mat_T[5])
plt.title("Boxplot")
plt.grid(True)


plt.suptitle("6 paneles con diferentes gráficos", fontsize=16, y=1.02)
plt.tight_layout()
plt.show()

