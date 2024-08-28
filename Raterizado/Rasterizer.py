import pygame
from pygame.locals import *
from gl2 import *
import shaders as s 
from texture import Texture


width = 1024
height = 1024

screen = pygame.display.set_mode((width, height), pygame.SCALED  )
clock = pygame.time.Clock()

# Ejemplo de inicialización correcta
rend = Renderer(width, height)

rend.background = Texture("textures/model.bmp")
rend.glClearBackground()
#Medium
rend.glLookAt(V3(2,5,-3),V3(0,7.9,1))

	
	#rend.glRender()
	#rend.glTriangle(puntoA, puntoB, puntoC
	#cargamos los modelos que vamos a utilizar...
	# Cargamos los modelos que rederizaremos
 
 #imagen1
rend.active_shader = s.rainbow
rend.active_texture = Texture("textures/model.bmp")
rend.glLoadModel("models/model.obj",
                 translate = V3(2,4,-1.5),
                 rotate = V3(-15, -130, 30),
                 scale = V3(0.25, 0.25, 0.25))

#imagen2
rend.active_shader = s.degraded
rend.active_texture = Texture("textures/model.bmp")
rend.glLoadModel("models/model.obj",
                 translate = V3(1.5,4.8,-1),
                 rotate = V3(-15, -130, 30),
                 scale = V3(0.25, 0.25, 0.25))

#imagen3
rend.active_shader = s.zebra
rend.active_texture = Texture("textures/model.bmp")
rend.glLoadModel("models/model.obj",
                  translate = V3(-0.1, 6.3, -0.3),
                  rotate = V3(-20, -25, -10),
                  scale = V3(0.4, 0.4, 0.4))

#imagen4
rend.active_shader = s.zebra
rend.active_texture = Texture("textures/model.bmp")
rend.glLoadModel("models/model.obj",
                 translate = V3(4,2,1),
                 rotate = V3(-15, -130, 30),
                 scale = V3(0.25, 0.25, 0.25))


rend.glFinish("output3.bmp")

pygame.quit()
