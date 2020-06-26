# Tarea 3: Variables Aleatorias Múltiples
Modelos Probabilísticos de señales y sistemas.

Thamara Montero Montoya. B64577.

Asignaciones de la tarea 3.


# Curva de ajuste para las funciones de densidad marginales de X y Y.
En las imágenes que se muestran a continuación es posible observar las funciones de densidad marginales tanto de X como de Y. Estas imágenes se obtuvieron gracias a las herramientas para analizar datos de Python.



![](ajustex.png) ![](ajustey.png)




Considerando el comportamiento de ambas curvas observable en la sección 4. las cuales tienen tendencia a tener simetría en el origen se busca ajustar la curva a una distribución normal, la cual se puede definir mediante la siguiente ecuación matemática:



<p align="center">
  <img src="https://render.githubusercontent.com/render/math?math={ f }_{ x }\left( x \right) =\frac { 1 }{ \sqrt { 2\pi { \sigma  }_{ x }^{ 2 } }  } { e }^{ \left\lfloor \frac { -{ \left( x-{ \mu  }_{ x } \right)  }^{ 2 } }{ 2{ \sigma  }_{ x }^{ 2 } }  \right\rfloor  }">  
</p>



Para el caso de x, y para el caso de y la siguiente:



<p align="center">
  <img src="https://render.githubusercontent.com/render/math?math={ f }_{ y }\left( y \right) =\frac { 1 }{ \sqrt { 2\pi { \sigma  }_{ y }^{ 2 } }  } { e }^{ \left\lfloor \frac { -{ \left( y-{ \mu  }_{ y } \right)  }^{ 2 } }{ 2{ \sigma  }_{ y }^{ 2 } }  \right\rfloor  }">  
</p>

Ecuaciones que se introdujeron en el código junto con la herramienta de *curve_fit* y los datos de mu=9.904843810018251 y sigma=3.2994428643069567 para X y mu=15.079460901835715 y sigma=6.026937742803979 para Y obtenidos del mismo.


# Expresión de la función de densidad conjunta que modela los datos.

Al asumir X y Y como dos variables independientes la función de densidad conjunta está dada por la multiplicación de las funciones de densidad marginals de cada una de las variables, por lo que, teniendo en cuenta las ecuaciones mencionadas anteriormente y los valores de sigma y mu para ambas variables, matemáticamente se podría ver en la siguiente ecuación la expresión de la función de densidad conjunta:

<p align="center">
  <img src="https://render.githubusercontent.com/render/math?math={ f }_{ x, y }\left( x, y \right) =\left( \frac { 1 }{ \sqrt { 2\pi { \cdot 3.2994 }^{ 2 } }  } { e }^{ \left\lfloor \frac { -{ \left( x-9.9048 \right)  }^{ 2 } }{ 2\cdot { 3.2994 }^{ 2 } }  \right\rfloor  } \right) \cdot \left( \frac { 1 }{ \sqrt { 2\pi { \cdot 6.0269 }^{ 2 } }  } { e }^{ \left\lfloor \frac { -{ \left( x-15.0796 \right)  }^{ 2 } }{ 2{ \cdot 6.0269 }^{ 2 } }  \right\rfloor  } \right) ">  
</p>


# Valores de correlación, covarianza y coeficiente de correlación (Pearson) para los datos y su significado.

* Correlación = 149.54281000000012

* Covarianza = 0.18310502804041562

* Coeficiente de correlación = 0.0023019875014526135


# Funciones de densidad marginales (2D), la función de densidad conjunta (3D).
A continuación se pueden observar las funciones de densidad marginales de x y y mencionadas en secciones anteriores.
## Funciones marginales:
![](marginalx.png) ![](marginaly.png)

Finalmente, la función de densidad conjunta corresponde a 
## Función de densidad conjunta:
![](densidad_conjunta.png)
