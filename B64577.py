# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 18:06:58 2020

@author: Thamara
"""
import numpy as np 
import scipy
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit
from scipy.stats import norm
from mpl_toolkits.mplot3d import Axes3D


#Lectura de los archivos
datos_xy = pd.read_csv('xy.csv')
datos_xyp = pd.read_csv('xyp.csv', header= 0)
xy = datos_xy.drop(['Unnamed: 0'], axis = 1)
xy_num = xy.to_numpy()

#1. Curva de mejor ajuste (modelo probabilístico)
# para las funciones de densidad marginales de X y Y.
fX = np.sum(xy_num, axis = 1)
fY = np.sum(xy_num, axis = 0)


#Para X
#Eje x: 
eje_X = np.linspace(5,15,len(fX))


#Se define la función de distribución normal
def normal(x,mu,sigma):
  return 1/(np.sqrt(2*np.pi*sigma**2)) * np.exp(-(x-mu)**2/(2*sigma**2))
param_X, _ = curve_fit(normal,eje_X,fX) #parámetros de la función
print(param_X)

curva_X = norm.pdf(eje_X, param_X[0], param_X[1]) # param [0]=mu y param[1]=sigma
plt.plot(eje_X,curva_X)
plt.show()
plt.close()

print ("mu_x = ", param_X[0])
print ("sigma_x = ", param_X[1])

#Para Y
#Eje y:
eje_Y = np.linspace(5,25, len(fY))

param_Y, _ = curve_fit(normal,eje_Y,fY)
curva_Y = norm.pdf(eje_Y, param_Y[0], param_Y[1])
plt.plot(eje_Y,curva_Y)
plt.show()
plt.close()

print ("mu_y = ", param_Y[0])
print ("sigma_y = ", param_Y[1])

#2. Expresión de la función de densidad conjunta:


#3. Valores de correlación, covarianza y coeficiente de correlación (Pearson), y su significado
X1 = datos_xyp["x"] 
Y1 = datos_xyp["y"] 
P1 = datos_xyp["p"]

#Correlación
correlacion = 0 
for i in range(len(datos_xyp)):
    correlacion = correlacion + X1[i]*Y1[i]*P1[i]; 
print( "La correlacion es :" , correlacion)


# Varianza 
covarianza = correlacion - (param_X[0]*param_Y[0])
print( "La varianza es :" , covarianza)


# Coeficiente de varianza
coef_var = covarianza/ (param_X[1]*param_Y[1])
print( "El coeficiente de varianza es :" , coef_var)

#4. Funciones de densidad marginales (2D), la función de densidad conjunta (3D).

#Funcion marginal de x
plt.xlabel('x')
plt.ylabel('fX')
plt.title('Funcion marginal de x')
plt.plot(eje_X,fX)
plt.show()

#Función marginal de y
plt.xlabel('y')
plt.ylabel('fY')
plt.title('Funcion marginal de y')
plt.plot(eje_Y, fY)
plt.show()

a = plt.axes(projection = '3d')
X_1 = X1
Y_1 = Y1 
Z_1 = P1

a.plot_trisurf(X_1, Y_1, Z_1, cmap = 'twilight_shifted')
plt.title('Funcion de densidad conjunta')



















