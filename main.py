from colorama import init, Fore, Back, Style
import random
import time

import time
#Informacion sobre mi trivia : Tema
print(
    Fore.WHITE + Back.YELLOW +
    "Bienvenido a mi trivia sobre la historia del Perú \n Pondremos a prueba que tanto sabes de nuestro pais tu puedes, suerte..!!! "
    + Back.RESET)

#COLORES DEL TEXTO
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

nombre = input(GREEN + "Ingresa tu nombre: " + RESET)

print("Espere un momento mientras se carga las preguntas, gracias..........")
time.sleep(1.5)
#Instrucciones
print()
print(
    MAGENTA + "Hola " + nombre,
    "responde las siguientes preguntas escribiendo la letra de la alternativa y presiona 'Enter' para enviar tu respuesta:\n"
    + RESET)
time.sleep(1.5)

puntaje = random.randint(0, 10)
print(CYAN + "Empiezas con ", puntaje, "puntos \n" + RESET)

#Pregunta 1
print(
    YELLOW +
    "\t :::::::Pregunta 1::::::: \n ¿Cual fue el primer presidente del Perú? \n  "
    + RESET)

print(YELLOW + "a. Miguel Grau" + RESET)
print(YELLOW + "b. Jose de la Riva Agüero" + RESET)
print(YELLOW + "c. Cristobal Colón" + RESET)
print(YELLOW + "d. Pedro Castillo" + RESET)

respuesta_1 = input(BLUE + " \nElige una respuesta: " + RESET)

while respuesta_1 not in ("a", "b", "c", "d"):
    respuesta_1 = input(RED + "Respuesta no valida, intentalo de nuevo: " +
                        RESET)

#Verficacion pregunta 1
if respuesta_1 == "a":
    print(RED + "Incorrecto", nombre + RESET)
elif respuesta_1 == "c":
    print(RED + "Incorrecto", nombre + RESET)
elif respuesta_1 == "d":
    print(RED + "Incorrecto", nombre + RESET)
else:
    puntaje += 10
    print(GREEN + "Muy bien", nombre, "!!!" + RESET)
print("\n", nombre, "llevas", puntaje, "puntos")

print("\t ⧖⧖⧖⧖⧖⧖⧖⧖⧖⧖⧖⧖⧖⧖⧖")
time.sleep(1)
#Pregunta 2
print(
    YELLOW +
    "\n \t :::::::Pregunta 2::::::: \n ¿En que año fue la independencia del Perú? \n"
    + RESET)
print(YELLOW + "a. 1500" + RESET)
print(YELLOW + "b. 2000" + RESET)
print(YELLOW + "c. 1902" + RESET)
print(YELLOW + "d. 1821" + RESET)

respuesta_2 = input(BLUE + " \nElige una respuesta: " + RESET)

while respuesta_2 not in ("a", "b", "c", "d"):
    respuesta_2 = input(RED + "Respuesta no valida, intentalo de nuevo: " +
                        RESET)

#Verficacion pregunta 2
if respuesta_2 == "a":
    print(RED + "Incorrecto", nombre + RESET)
elif respuesta_2 == "b":
    print("Incorrecto", nombre)
elif respuesta_2 == "c":
    print("Incorrecto", nombre + RESET)
else:
    puntaje += 10
    print(GREEN + "Muy bien", nombre, "!!!" + RESET)

print("\n", nombre, "llevas", puntaje, "puntos")
print("\t ⧖⧖⧖⧖⧖⧖⧖⧖⧖⧖⧖⧖⧖⧖⧖")
time.sleep(1)

# Pregunta 3

print(
    YELLOW +
    "\n \t :::::::Pregunta 3::::::: \n ¿Cual es el actual presidente del Perú? \n"
    + RESET)
print(YELLOW + "a. Pedro castillo" + RESET)
print(YELLOW + "b. Bad bunny" + RESET)
print(YELLOW + "c. Pedro Pablo Kuczynski" + RESET)
print(YELLOW + "d. Obama" + RESET)

respuesta_3 = input(BLUE + " \nElige una respuesta: " + RESET)

while respuesta_3 not in ("a", "b", "c", "d"):
    respuesta_3 = input(
        RED +
        "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: " +
        RESET)

#PREGUNTAS CON OPERADORES MATEMATICOS
if respuesta_3 == "b":
    print(RED + "Totalmente incorrecto! ..." + RESET)
    puntaje = puntaje / 2
elif respuesta_3 == "d":
    print(RED + "Casi aciertas" + RESET)
    puntaje = puntaje + 5
elif respuesta_3 == "c":
    print(RED + "Incorrecto! ..." + RESET)
    puntaje = puntaje - 5
else:
    print(GREEN + "Correcto! ..." + RESET)
    puntaje = puntaje * 2
print("\n", nombre, "llevas", puntaje, "puntos")

print("\t ⧖⧖⧖⧖⧖⧖⧖⧖⧖⧖⧖⧖⧖⧖⧖")
time.sleep(2)
print(MAGENTA + "Gracias", nombre, "por jugar mi trivia, alcanzaste", puntaje,
      "puntos" + RESET)

#Pregunta 4

#Pregunta 5
