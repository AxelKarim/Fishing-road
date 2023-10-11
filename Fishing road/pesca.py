#Funcion import usada para añadir librerias al código
import pygame, sys
from pygame.locals import*

#Funcion usada para dar inicio a la libreria pygame
pygame.init()

#Ventana del juego
Ancho, Alto = 900, 680
pantalla = pygame.display.set_mode((Ancho, Alto))

#Icono y título
pygame.display.set_caption('Fishing Road')
icono = pygame.image.load("imagenes/iconopesca.png")
pygame.display.set_icon(icono)

#Fondo de juego
fondo = pygame.image.load('imagenes/fondo.png')
fondo = pygame.transform.scale(fondo, (900,680))
pantalla.blit(fondo, (0,0))

#Esta funcion defiene la fuente de la letra
fuente = pygame.font.SysFont("arialblack", 60)

#Paleta de colores en formato RGB
BLANCO = (255, 255, 255)
NEGRO = (0,0,0)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    pantalla.blit(img, (x, y))

#Imagenes de los botones
boton_de_inicio = pygame.image.load("imagenes/botondejugar.png").convert_alpha()
pantalla.blit(boton_de_inicio, (160, 160))
boton_de_configuracion = pygame.image.load("imagenes/botondeconfiguracion.png").convert_alpha()
pantalla.blit(boton_de_configuracion, (200, 390))
boton_de_creditos = pygame.image.load("imagenes/botondecreditos.png").convert_alpha()
pantalla.blit(boton_de_creditos, (289, 400))
#musica
pygame.mixer.music.load('imagenes/sonidodemenu.mp3')
pygame.mixer.music.play(-1)

pygame.draw.rect(pantalla, NEGRO, (100, 120, 450, 100))
draw_text('Fishing Road', fuente, BLANCO, 110, 130)

#Bucle del juego
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #Función para actualizar los cambios en la pantalla    
    pygame.display.update()