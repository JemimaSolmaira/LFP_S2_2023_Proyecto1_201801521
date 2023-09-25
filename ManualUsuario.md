# Laboratorio de lenguajes Formales y de programacion
## Practica1
### Segundo Semestre 2023
```js
Universidad San Carlos de Guatemala
Programador: Jemima Solmaira Chavajay Quieju
Carne: 201801521
Correo: jemimasolmaira2425@gmail.com
```
---
## Descripción del Proyecto
El silguiente programa desarrollado en pyton es un programa que realiza operaciones matematicas desde un formato .json, sin embargo antes de realizar el proceso matematico se debera analizar el archivo, con la funcion del analizador , para encontrar posibles errores, al finalizar todo el proceso matematico se podran visualizar los resultados en un grafo con la ayuda de graphiz


## Objetivos
* Objetivo General
    * Realizar operaciones matematicas desde un archivo .jason
* Objetivos Específicos
    * Revisar archivos .json y los posibles errores de texto  
    * Visualizar los posibles errores del archivo, en un formato .json
    * Visualizar los resultados en grafos.

---
## Manual de Usuario

En el programa se debera ingresar un archivo .json

![Ejemplojson](https://i.ibb.co/QMzDtTg/ejemplo-en-jason.jpg)  

El cual como en la imagen puede incluir algunos errores los cuales el programa podra analizarlos mas adelante

La interfaz principal del programa se muestra de la siguiente manera:

![InterfazPrincipal](https://i.ibb.co/DY1wcn9/Interfaz-principal.jpg) 

Contamos un menu desplegable el cual mostrara las opciones para manejar el archivo .json, podremos abrir el archivo, guardar los cambios, o incluso guardar una copia del archivo

![MenuDesplegable](https://i.ibb.co/pvWp99w/Menu-desplegable.jpg) 

Al abrir el archivo .json podremos visualizar el contenido en el editor de texto del programa, antes de realizar las operaciones matematicas se debera analizar el archivo para buscar los posibles errores

![Archivoabierto](https://i.ibb.co/PYLpsWP/archivo-abierto.jpg)

Al presionar el boton de analizar se analizara cada letra del texto en busqueda de errores y al finalizar mostrara el nuevo archivo sin errores en el editor de texto

![Analisis](https://i.ibb.co/QdnTZjy/Analisis-Realizado.jpg)  

Para visualizar los errores del archivo, presionamos el boton de errores

![Errores](https://i.ibb.co/pQ9QZxX/Errores-Exito.jpg)

El resultado sera un archivo .json con la descripcion de todos los errores encontrados
![ErroresJson](https://i.ibb.co/Mgy9qf5/errores-en-json.jpg) 

y por ultimo se realizan todas las operaciones matematicas presionando el boton reportes, el resultado sera un archivo.svg donde se podran visualizar todos los resultados en un grafo

![Reportes](https://i.ibb.co/WywPhPq/Reportes.jpg)

En el grafo podremos observar todos los resultados de todas las operaciones realizadas, la configuracion del grafo, se encontrara en el archivo .json, en el cual se describira la fuente, la forma, y el color de los nodos.
![Graphiz](https://i.ibb.co/0q1qbWm/Resultado-graphiz.jpg)