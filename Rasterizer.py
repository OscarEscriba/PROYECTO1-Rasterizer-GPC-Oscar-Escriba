import pygame
from pygame.locals import *
from gl2 import *
import shaders as s 
from texture import Texture


width = 1000
height = 600

screen = pygame.display.set_mode((width, height), pygame.SCALED  )
clock = pygame.time.Clock()

# Ejemplo de inicialización correcta
rend = Renderer(width, height)

rend.background = Texture("textures/Fondo.bmp")
rend.glClearBackground()
#Medium
rend.glLookAt(V3(2,5,-3),V3(0,7.9,1))

	
	#rend.glRender()
	#rend.glTriangle(puntoA, puntoB, puntoC
	#cargamos los modelos que vamos a utilizar...
	# Cargamos los modelos que rederizaremos
 
 #imagen1 sillon dorado
rend.active_shader = s.flat
rend.active_texture = Texture("textures/gold.bmp")
rend.glLoadModel("models/Couch.obj",
                 translate = V3(4.5,0.5,-2),
                 rotate = V3(-20, -25, -10),
                 scale = V3(2, 2, 2))

#imagen2 planta que adorna.
rend.active_shader = s.degraded
rend.active_texture = Texture("textures/TexturaPlanta.bmp")
rend.glLoadModel("models/planta.obj",
                 translate = V3(-1,4.6,-1),
                 rotate = V3(-15, -130, 30),
                 scale = V3(0.25, 0.25, 0.25))

#imagen3 lampara.
rend.active_shader = s.rainbow
rend.active_texture = Texture("textures/gold.bmp")
rend.glLoadModel("models/globes.obj",
                 translate = V3(0.3,7.4,0.2),
                 rotate = V3(-20, 25, -10),
                 scale = V3(0.4, 0.4, 0.4))

#imagen4 la planta.
rend.active_shader = s.zebra
rend.active_texture = Texture("textures/model.bmp")
rend.glLoadModel("models/Chair.obj",
                  translate = V3(1, 5, -0.3),
                  rotate = V3(-15, 180, 30),
                  scale = V3(0.4, 0.4, 0.4))


rend.glFinish("output.bmp")

pygame.quit()
