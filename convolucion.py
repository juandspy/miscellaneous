import numpy as np
import matplotlib.pyplot as plt

# Triangulo moviéndose:
#base_triangulo = np.linspace(-10, 10, 101)
#triangulo_y = 10 - abs(base_triangulo)
base_triangulo = np.linspace(0, 20, 201)
triangulo_y  = (20 - base_triangulo)/2
triangulo_y[0] = 0	

base_triangulo = base_triangulo - 40
# Cuadrado fijo:

base_cuadrado = np.linspace(-10, 10, 101)
cuadrado_y = np.ones(len(base_cuadrado))*10
cuadrado_y[0] = 0
cuadrado_y[-1] = 0

xmin = -50
xmax = 50
x0t  = 0
dx   = 0.2
ymin = 0
ymax = 15
ymin2 = 0
ymax2 = 80
x = np.linspace(xmin, xmax, 1000)

fig, (ax1, ax2) = plt.subplots(2, 1)

ax1.set_xlim([xmin, xmax])
ax2.set_xlim([xmin, xmax])
ax1.set_ylim([ymin, ymax])
ax2.set_ylim([ymin2, ymax2])

ax1.axhline(0, color='grey')
ax1.axvline(0, color='grey')

ax2.axhline(0, color='grey')
ax2.axvline(0, color='grey')

g1,  = ax1.plot(base_triangulo, triangulo_y)
g1b, = ax1.plot(base_cuadrado, cuadrado_y, 'r')
g2,  = ax2.plot(0, 0)
indice = 349
areas = np.zeros(len(x))

for i in range(2000):
	base_triangulo += dx
	indice += 1
	g1.set_data(base_triangulo, triangulo_y)
	plt.pause(0.01)

	#calculo area encerrado
	area = 0
	for k, e in enumerate(base_triangulo):
		for j in base_cuadrado:
			if abs(e - j) < 0.5:
				area += triangulo_y[k]/100
	areas[indice] = area
	g2.set_data(x, areas)

plt.show()