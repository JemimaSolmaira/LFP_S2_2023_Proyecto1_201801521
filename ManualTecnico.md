# Laboratorio de lenguajes Formales y de programacion
## Proyecto1
### Segundo Semestre 2023
```js
Universidad San Carlos de Guatemala
Programador: Jemima Solmaira Chavajay Quieju
Carne: 201801521
Correo: jemimasolmaira2425@gmail.com
```
---
## Descripción del Proyecto
El siguiente proyecto consta del  desarrollo de un programa utilizando Python, su funcion principal es realizar calculos matematicos y ser presentados en forma de grafos, sin embargo los datos que ingresen al programa son analizados previamente, el programa incluye una herramienta diseñada para analizar y dividir un flujo de caracteres de entrada en unidades léxicas significativas, conocidas como tokens según las reglas gramaticales y las expresiones regulares definidas 


## Objetivos
* Objetivo General
    * Realizar operaciones matematicas , utilizando el formato Json para obtener los resultados en forma de grafos 
* Objetivos Específicos
    * Implementar un analizador lexico para la lectura de datos de un archivo Json
    * Implementar un AFD para el proceso de deteccion de tokens correctos e incorrectos
    * Hacer uso de grafos para visualizar los resultados de las operaciones matematicas 

---
## Manual Tecnico

El archivo interfaz.py contiene todo el desarrollo de la interfaz grafica , el cual es realizada en con la libreria tkinder consta de 3 botones y un menu desplegable con las funciones para manejar el archivo.

![Tkinder](https://i.ibb.co/GnBqJLy/ventana.jpg)

en la interfaz grafica  tenemos las funciones que se usan para las opciones de abrir archivo, guardar el archivo asi tambien para guardar una copia del archivo, el archivo debe ser de formato .json

![MenuDesplegable](https://i.ibb.co/4267w2L/Menu-desplegable.jpg)

las 3 funciones principales de nuestro programa son:  Analizador, Errores, y Reportes

![Funciones Principales](https://i.ibb.co/C09b9DN/Funciones-principales.jpg)

El analizador es la herramienta que nos permite procesar el archivo json, y evaluar sus errores antes de realizar todas las operaciones matematicas

Para el analisis del archivo, se utiliza un AFD que nos permite clasificar los tokens encontrados dentro del texto analizar los tokens para buscar erroes, y clasificar las palabras correctas en una tabla de tokens y las incorrectas en una tabla de errores , para abordar el proceso empezamos viendo la gramatica permitida: 

* Gramatica

La gramatica permitida es la que se presenta en el siguiente cuadro: 

![Gramatica](https://i.ibb.co/xFhz6LS/Gramatica.jpg)

* AFD

Para realizar este proceso se utiliza la clase Scanner, en donde encontramos todas las funciones que nos permiten dividir los tokens dependiendo de sus patrones de texto, cual token que no se incluya dentro de nuestra gramatica sera considerado un error e incluido en la tabla de errores

![Tokens](https://i.ibb.co/RvHw3V3/Analisis-de-tokens.jpg) 

El analisis se realiza letra por letra , las palabras se comparan con los patrones permitidos, en caso de encontrar alguna letra que no sea permitida se eliminara del formato inicial, y se incluira en la tabla de errores, al finalizar se creara un nuevo archivo json libre de errores.
![Analisis](https://i.ibb.co/GkHQkFF/Busqueda-de-errores.jpg)


Al finalizar el analisis la tabla de errores se podra visualizar por medio de un formato .json 

![Errores](https://i.ibb.co/MVTxsyL/Errores-en-archivo-Json.jpg)

Cuando el archivo .json se encuentre libre de cualquier error se podra procesar cada dato dentro de nuestra tabla e tokens para crear una tabla de resultados con todas las operaciones matematicas correspondientes
![TablaResultados](https://i.ibb.co/2k3vWzX/Tabla-de-resultados.jpg)

Toda la informacion obtenida se procesara en una clase Math que incluye todas las operaciones que necesitamos procesar
![Matematica](https://i.ibb.co/gjKXsqT/Operar.jpg) 

Para poder obtener un reporte visual de los resultados se hace uso de los grafos por medio de la herramienta graphiz, para ello se usan dos nodos para representar el valor1 y el valor2, las configuraciones del grafo seran descritas en el archivo json 
![Grafica](https://i.ibb.co/zrBrHvp/class-grafica.jpg) 

