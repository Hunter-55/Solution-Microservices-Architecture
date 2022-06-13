1° creamos un contenedor para la base de datos de mongoDB.

2° creamos un contenedor para visualizar la base de datos con la imagen mongo_express.

3° creamos un contenedor con la imagen de python el cual se encargara de ejecutar el un script que llenara la base de datos.
   - dentro de la carpeta proceso se encuentra un requirement.txt con las librerias requeridas, un Dockerfile con la cofiguración para correr el programa de python.

4° creamos un contenedor con una imagen de python.
   - dentro de una carpeta se encuentra un requirement.txt con los requerimientos o librerias, donde se encuentra un programa de python que se encargara de ejecutar en framwork de flask y el Dockerfile para su funcionamiento con su configuración, este contenedor actuara como una API donde visualmente en una paguina web se vera el contenido de la base de datos.

5° Creamos un archivo llamado docker-compose.yml.
   - este archivo nos ayuda con un simpre comando a levantar o tirar los contenedores.

6° Se crea una base de datos en la cual se le agregara y modifica la informacion siguiente:
 - Email.
 - Referencia (siendo esta clave unica).
 - Fecha.
 - Total.
 - Tipo.
 - Categoria.

7° Despues de eso se creo un script en python el cual ayuda a conectar a la base de datos y editar esta misma.

8° Creamos un script de python FLASK como frameworks para conectar con la api.

9° Se crean Las puebas unitarias.

10° Se hacen las pruebas de integracion.

11° Se dokerizo el proyecto.

# Inicio de Sesión 
![register](/imagenes/1.png)

# Base de datos Completa 
![1](/imagenes/2.png)

# Suma de los inflow y outflow
![register](/imagenes/3.png)

# Muestreo de las Categorías 
![register](/imagenes/4.png)

Brainfuck:

> ++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>++.>+++++++++++.---.-----------.<<++.>>+++++++++++++++.++.---.---------.-.<<.>-.+++++++++++.-----------------.++.++++++.--------.++++++++++++++++++.<+....-.>>+++++++++++.-.+++.<<.>>-------------.++++++++++++++.-------------.+++++++++.+++.++++++++.<++++++++++++++.>--------.<++.++.<.>>++.<----.>------.++++++.-----.<<.>>++++++++++.<<.>>-----.<++++.>------.<.>++++.----.+.++++.<<.>>---.<----.++.++++++.----.>--.<--.>-----.<--.<.>++++.>+++++.<<.>.>.+++++.<.>-----.<----.>++++.----.+.++++.<<.>++++.>.<<.>>++.-------.<<.>---.>+++++++.<+++.>-------.<<.>>++.++.---.<+.-.<.>>++++++++++.<<.>----.++++++++++++.----.--.++++++++.<++++++++++++.------------.>--.>----.<----------.+++++.-------.<.>>--.++.<++++.>---.++.<.<.>--.>-----.-.<<.>>+++++.++.<<.>-.-.>-------.<+++.---.<.>--------------------------------.+++++++++++++++++++..---------------.-----------.<.>+++++++.>.-------.--.+++++++.<<.>>+++++++++++++.<<.>+++.>------------------------.+++++++++++++++++++++.-------------.-----.<<++++++++++++++.<.>>>++++++++++++.-.++++.---------------.---.+++++++++++++++++++.-------------------.<----------.<--------------.>>-----------------.+++++++++++++++++.++++++++++++++++++.--------------.+++++++++.+.++++.<<.>>---.++.---.---------.-.<<.>>----.+++++++++++++++++++..---------------.<.<.>>-.---.++++++++++++.----.--------.+++++++++++++.<<.>>+++++++++++.<<.>>---------.---------------.+.++++++++++.---.+++++++++++.-----.<------------.

