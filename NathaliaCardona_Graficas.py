import numpy as np
import matplotlib.pyplot as plt
#se lee la informacion de los datos de python y de c++
data_python= np.loadtxt("times_python.csv")
data_cpp= np.loadtxt("times_cpp.csv")

#se grafican los resultados anteriores en una misma grafica
#se grafica el N en funcion del tiempo para los dos casos y se asignan label para diferenciar ambas curvas
plt.plot(data_python[:,1],data_python[:,0],label="python",c="red")
plt.scatter(data_cpp[:,1],data_cpp[:,0],label="cpp")
plt.legend()
plt.title("Cpp vs python")
plt.xlabel("Tiempo (s)")
plt.ylabel("N-esimo termino de fibonacci")
#se guardan las curvas en una imagen .png
plt.savefig("cpp_vs_python.png")
plt.close()
