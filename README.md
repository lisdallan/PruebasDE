# PruebasDE

1. Se entregan 3 dataset en la ruta `/assets/*.csv` compuesto de ventas por tienda, tiendas y otras características, la idea es cargar estos datasets para su posterior análisis. Posterior a su cargue debe ser procesado en Python para responder las siguientes preguntas:

- Cual es la tienda con el mayor valor en ventas totales?
- Entre las 3 tiendas más grandes cuál es la que más ventas totales registra?
- Cual es la tienda con menor ventas ?
- Cual es la tienda que mas vendió en el 2 semestre del año 2012?


2. Dentro de `/assets/` se encuentra una rchivo llamado `anyclass.py`. Se debe responder lo siguiente:

- Qué hace este código?
- Si es posible, refactorizar

Nota:

Esperamos que el ejercicio sea termindo en 24 horas. Debes hacer fork de la rama y subir tus cambios. Toda la documentacion, explicaciones, print screen, debe ir en el Readme.md.
Por favor enviar correo cuando termines a pda_gobierno@avaldigitallabs.com

Respuesta: 

1. Para poder analizar la data y dar las respuestas indicadas se realizó la carga de los CSV mediante la librería pandas, para el archivo historic_sales.csv fue necesario hacer una transformación de datos para no tener inconvenientes al momento de realizar cálculos los cambios realizados son los siguiente:
    - Se eliminan filas que contengan carácter [a-z] en la columna Weekly_Sales
    - Se convierte la columna Data a una Fecha
    - Se Crea una columna nueva donde indicamos mes año para poder hacer los calculos por semestre 

    <img src="/Capturas/carga_datos.png" alt="Transformacion Datos"/>


Las respuestas encontradas para cada pregunta son las siguientes 

Las 3 tiendas con mayor numero de ventas son:
    Store  Weekly_Sales
     20  2.972251e+08
     4  2.959183e+08
     14  2.855328e+08

Las tres tiendas mas grandes son:
[13, 11, 28]

De las mas grandes la que mas ventas tiene es la:
    Store  Weekly_Sales
    13  2.831420e+08

La tienda con menor ventas es la:
    Store  Weekly_Sales
     33   36805439.25

La tienda con mas ventas en el semeste 2 del año 2012 es la:
   Store  Weekly_Sales
      4    36055601.9

Para la respuesta de Cual es la tienda que mas vendió en el 2 semestre del año 2012? Se dejo los datos por parámetros con el fin de poder calcular cualquier año y semestre

2.el código indicado se encarga de analizar una cadena de Json y convertirla en un diccionario de python, esta informacion es guardad en el cahe mediante la clase cached_property() la cual transforma un método en un propiedad, esta se ejecuta una sola vez y como lo indique almacena la informacion en cache. Esto permite que se acelere el acceso a los datos del json y evita la carga nuevamente de este cada que se llama la clase y así reducir tiempos de ejecución. Este proceso es útil si se utiliza código de gran tamaño que aumente los tiempos de ejecución sin embargo sin el Json al leer no es un archivo demasiado pesado no sería eficiente usar la clase cached_property puesto que el proceso no es reutilizable.

Al revisar el scrip evidenciamos que la clase cached_property(object) es declarada de manera total en el código este proceso se puede evitar si importamos la clase que hace parte del módulo functools de la siguiente manera from functools import cached_property 

<img src="/Capturas/import_clase.png" alt="Importar clase"/>

Se la misma manera se evidencia que la funcion  def __init__(self) declara dentro de la clase AnyClass no es necesaria ya que se encarga únicamente de imprimir un dato que se puede imprimir en la funcion def __init__(self, json_stringified)

<img src="/Capturas/def.png" alt="def no necesario"/>

En el archivo se añadió código al final con el fin de realizar una prueba del funcionamiento del código en este caso se incluyó un json pequeño y se llamó la clase para ejecutar el proceso 

<img src="/Capturas/prueba.png" alt="Caso Real"/>