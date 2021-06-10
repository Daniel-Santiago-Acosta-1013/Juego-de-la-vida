import pygame
import numpy as np 

pygame.init()

# Ancho y alto de la pantalla 
width, height = 600, 600
# Creacion de la pantalla 
screen = pygame.display.set_mode((height, width))

#color del fondo = casi negro, casi oscuro.
bg = 25, 25, 25
# Color del fondo con el color elegido
screen.fill(bg)

nxC, nyC = 25,25

dimCW = width  / nxC
dimCH = height / nyC


#bucle de ejecucion
while True:
    
    for y in range(0, nxC):
        for x in range(0, nxC):

            poly = [((x)   * dimCW, y * dimCH),
                    ((x+1) * dimCW, y * dimCH),
                    ((x+1) * dimCW, (y+1) * dimCH),
                    ((x)   * dimCW, (y+1) * dimCH)]

            pygame.draw.polygon(screen, (128, 128, 128), poly, 1)
    
    pygame.display.flip()