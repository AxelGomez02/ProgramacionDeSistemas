# ProgramacionDeSistemas
Aquí subiré mi documentación relacionada a la Experiencia Educativa de Programación de sistemas 
## Ensamblador
Adjunto captura de mi hola mundo.    
![ensamblador](https://github.com/AxelGomez02/ProgramacionDeSistemas/blob/main/Imagenes/ensamblador.png?raw=true)    
### historia 
El lenguaje ensamblador es un lenguaje de bajo nivel, a mi parecer el de mas bajo nivel.<br> 
Consiste en un conjunto de nemonicos (palabra que sustituye a un codigo de operacion) que representan instrucciones basicas para los computadores, microprocesadores, microcontroladores y otros circuitos integrados programados.<br>
Implementa una representacion simbolica de los codigos de maquina binarios y otras constantes necesarias. Constituye la representacion mas directa del __codigo maquina__ especifico para cada arquitectura legible por un programador     
### Sintaxis
Debido a que el lenguaje ensamblador depende de las ___instruciones del codigo maquina___,cada lengiaje ensamblador esta diseñado para exactamente una arquitectura de computadora especifica    
Como ya mencione ensamblador usa un nemonico para representar cada instruccion de maquina de bajo nivel o codigo de operacion, tipicamente cada registro, bandera, etc.   
Muchas operaciones requieren uno o mas ___operandos___ para formar una instruccion completa.     
La mayoria de los ensambladores permiten constantes,registros y etiquetas con nombre para ubicaciones de programa y memoria, y pueden calcular expreciones para operandos.    
Por lo tanto, los programadores se liberan de tediosos calculos repetitivos y los programas en ensamblador son mucho mas legibles que el codigo maquina    
Muhchos ensambladores ofrecen  mecanismos adicionales para facilitar el desarrollo de programas,
controlar el proceso de ensamblaje y ayudar a la depuracion    
## Bibliotecas Estaticas
Una biblioteca estatica es un archivo informatico que contiene un grupo de archivos relacionados para facilitar la vinculacion a los programas. El contenido de esta biblioteca suele ser archivos de codigo maquina normalmente se genera **apartir de la compilacion de codigo o un proceso similar**.       
La biblioteca estatica es mas fexible que una biblioteca dinamica por que su ruta exacta es irrelevante para el ejecutable que usa. Las bibliotecas estaticas se vinculan a un archivo ejecutable y luego se pueden eliminar si es necesario por que su contenido se incluido en el programa final.    
![biblioteca estatica](https://www.embarcados.com.br/wp-content/uploads/2021/01/image-4.png)     
La vinculacion estatica permite mover o reutilizar una biblioteca sin preocuparse por las rutas de  ubicacion absolutas, a diferencia de una biblioteca dinamica, la biblioteca estatica no suele ser ejecutable por si sola.    
Construir una biblioteca estatica es mucho mas simple que construir una biblioteca dinamica. Los contenidos de las bibliotecas estaticas no estan vinculados entre si 
por que no se espera que se ejecuten por si mismos, por lo que un simple archivador suele ser suficiente para crearlos.   
## Bibliotecas Dinamicas
![Biblioteca dinamica](https://ainotes298786558.files.wordpress.com/2021/06/dynamic-1.jpeg?w=430)    
Una biblioteca dinamica es aquella que **se carga a la hora de arrancar un programa**, a diferencia de las bibliotecas estaticas estas utilizan recursos independientes al ejecutable que las llama.   
***Una biblioteca dinamica no es copiada al programa durante el proceso de compilacion***    
Durante la ejecucion de nuestro programa, en el momento que se necesiten los recursos, este los buscara en las bibliotecas. En el supuesto de borrar la biblioteca el programa daria un error al no encontrala.   
### Diferencias entre las bibliotecas
- Como al compilar un programa con una biblioteca estatica esta copiada en el codigo, el tamaño del ejecutable sera mayor que si utilizan bibliotecas dinamicas    
- Una vez la biblioteca estatica se ha enlazado al programa durante el proceso de compilacion, esta puede ser borrada y el programa seguira funcionando. En el caso de una dinamica obtendremos un error.   
- Utilizando una biblioteca estatica el ejecutable no tiene que buscar en ningun otro archivo externo,por lo que su ejecucion sera mas rapida que al utilizar dinamicas       
- Un cambio en una biblioteca estatica no afecta al programa. Un cambio en una biblioteca dinamica si afecta al programa     
![image](https://user-images.githubusercontent.com/113264761/190874760-a014040d-f78c-4988-b514-5bec7695b593.png)   
### Adjunto evidencia de la practica que hicimos 
![imagen ensamblador](https://github.com/AxelGomez02/ProgramacionDeSistemas/blob/main/Imagenes/bibliotecas.png)
