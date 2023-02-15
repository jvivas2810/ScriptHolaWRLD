import pygame
import random
import sys

# Inicializamos la biblioteca Pygame
pygame.init()

# Creamos una ventana de 800x600 pixels
ventana = pygame.display.set_mode((800, 600))

# Creamos un objeto fuente de texto
fuente = pygame.font.Font("C:/Windows/Fonts/arial.ttf", 36)

# Generamos un número aleatorio entre 1 y 6 (inclusive)
resultado = random.randint(1, 6)

# Creamos una imagen a partir del texto que representa el número
imagen = fuente.render(str(resultado), True, (0, 0, 0))

# Obtenemos el rectángulo que contiene la imagen
rectangulo = imagen.get_rect()

# Establecemos la posición de la imagen en la ventana
rectangulo.center = (400, 300)

# Dibujamos la imagen en la ventana
ventana.blit(imagen, rectangulo)

# Actualizamos la ventana
pygame.display.update()

# Bucle principal del juego
while True:
    # Procesamos los eventos de Pygame
    for event in pygame.event.get():
        # Si se recibe el evento de cierre de ventana, terminamos el juego
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Generamos un número aleatorio entre 1 y 6 (inclusive)
    resultado = random.randint(1, 6)

    # Creamos una imagen a partir del texto que representa el número
    imagen = fuente.render(str(resultado), True, (0, 0, 0))

    # Obtenemos el rectángulo que contiene la imagen
    rectangulo = imagen.get_rect()

    # Establecemos la posición de la imagen en la ventana
    rectangulo.center = (400, 300)

    # Dibujamos la imagen en la ventana
    ventana.blit(imagen, rectangulo)

    # Actualizamos la ventana
    pygame.display.update()

