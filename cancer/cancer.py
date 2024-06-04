#Regresión Logística
import matplotlib.pyplot as plt
import numpy as np

def sigmoid(z):
   return 1/(1+np.exp(-z))

z=np.arange(-7,7,0.1)
phi_z=sigmoid(z)

plt.plot(z,phi_z)
plt.axvline(0.0, color='k')
plt.ylim(-0.1,1.1)
plt.yticks([0.0,0.5,1.0])
plt.xlabel('Z')
plt.ylabel('$\phi (z)$')
ax=plt.gca()
ax.yaxis.grid(True)
plt.show()

#La funcòn sigmoide toma valores de numeros reales como entrada
# y los transforma en valores de rango de [0,1] con un aintercepción de 0.5
