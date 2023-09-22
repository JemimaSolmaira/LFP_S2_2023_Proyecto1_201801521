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
La siguiente practica consta del  desarrollo de un programa en la consola, utilizando Python,  en donde se puedan realizar procesos de inventario, tales como ingresar datos, y los movimientos (ventas y agregar stock), asi como tambien obtener un informe final.


## Objetivos
* Objetivo General
    * Utilizar las distintas herramientas y metodos de programacion para obtener una solucion al programa que se solicita 
* Objetivos Específicos
    * Conocer las principales funciones de phyton para trabajar en consola
    * Utilizar las funciones de abrir y escribir un archivo en phyton
    * Utilizar distintas extensiones para realizar las acciones correspondientes.

---
## Manual Tecnico
El siguiente codigo es para gestionar un inventario, por lo que partimos de un menu inicial que nos permitira elegir opciones que nos llevaran a realizar las distintas acciones que necesitamos:

![Menu](https://i.ibb.co/LNLJmHb/Menu.jpg)

utilizamos un  bucle while para volver al Menu despues de haber terminado todas las operaciones en un opcion para poder elegir realizar otra accion, para detener el ciclo deberemos elegir la opcion 4 para salir.

Debido a que trabajaremos con productos la mejor manera de gestionar todos los datos es usando una clase llamada productos que contiene la informacion

![ClaseProducto](https://i.ibb.co/7xfqfhT/Objetoproducto.jpg)

Para la lectura de nuestros datos utilizaremos un archivo de texto, con la extension de .inv para agregar el inventario nuevo, y una extension .mov para los movimientos, ambos deberan estar en la carpeta de la practica.

![Extensiones](https://i.ibb.co/wNKk4xq/extensiones.jpg) 

Para la primera opcion , se leera el inventario Inicial, el programa pediria un input para ingresar el nombre del archivo , despues de haber validado la direccion nos llevara a un metodo en donde los datos del archivo .inv seran leidos y trasladados a una lista del objeto Productos

![InventarioInicial](https://i.ibb.co/SRvF53f/leer-Inicial.jpg)

La segunda opcion es para leer los movimientos que se haran en el inventario,  el programa pedira un input para ingresar el nombre del archivo, despues de haber vaidado la direccion nos llevara a un metodo donde los datos del archivo .mov seran leidos

![Movimientos](https://i.ibb.co/z5pjmY5/Movimientos.jpg) 

Para realizar los cambios correspondientes en el invetario primero se validara que el archivo exista, si no existe mostrara el mensaje de error, en caso de que si exista el siguiente paso sera definir si se trata de una venta o de agregar stock:

![ValidacionProducto](https://i.ibb.co/Bn4BPRg/Validacion.jpg) 

El programa nos llevara a dos metodos dependiendo de la accion que se necesite hacer, si es "agregar stock" entonces se validara la ubicacion para luego sumar los productos: 

![AgregarStock](https://i.ibb.co/K23YbT3/Agregar-Stock.jpg)  

Para la venta tambien se validara la ubicacion para luego restar los productos:

![Venta](https://i.ibb.co/3h40jyK/vender.jpg) 

En cada una de las opciones se puede ver un reporte del inventario en la consola con ayuda del metodo de revision de inventario: 

![RevisionInventario](https://i.ibb.co/wJFcn1c/revisar-inventario.jpg)  

Para la opcion 3, es en donde tenemos la funcionalidad de guardar los datos en un txt, con ayuda de la funcion de Imprimir archivo

![ImprimirInventario](https://i.ibb.co/7NHCkBx/Imprimirentxt.jpg)   