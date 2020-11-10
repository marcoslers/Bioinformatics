import numpy as np
import matplotlib.pyplot as plt

# En cada momento tendremos un vector de la distribución de la población
# (sanos, sintomas leves, sintomas graves, recuperados, fallecidos)

# Población inicial
x_0=(100000,0,0,0,0)

# Definimos las probabilidades de transición

S_L = 0.30
L_G = 0.10
L_R = 0.20
G_R = 0.10
G_F = 0.10

# Definimos la matriz A
A=np.array([[1-S_L,0,0,0,0],
            [S_L,1-L_G-L_R,0,0,0],
            [0,L_G,1-G_R-G_F,0,0],
            [0,L_R,G_R,1,0],
            [0,0,G_F,0,1]])

# Encontramos la evolución de la epidemia los primeros 60 días

evolution=[x_0] # Día 0

#print(evolution[-1])
#print(evolution[0])


for j in range(60):
    evolution.append(np.matmul(A,evolution[-1]))

# Mostramos lo que pasa los primeros 3 días

for j in range(1,60):
    print(evolution[j])

# Hacemos gráfica para mostrar la evolución de todo el tiempo
plt.plot([j[0] for j in evolution], label="Sanos")
plt.plot([j[1] for j in evolution], label="Síntomas leves")
plt.plot([j[2] for j in evolution], label="Síntomas graves")
plt.plot([j[3] for j in evolution], label="Recuperados")
plt.plot([j[4] for j in evolution], label="Fallecidos")
plt.title("Evolución de la población, contagio=0.30")
plt.legend()
plt.show()
