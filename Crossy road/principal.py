import sys, pygame, util
from pygame.locals import *
from heroe import *
from villano import *
from hoguera import *
from maiz import *


SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
ICON_SIZE = 32

def game():
      pygame.init()
      pygame.mixer.init()
      screen = pygame.display.set_mode( (SCREEN_WIDTH,SCREEN_HEIGHT) )
      jugando = True
      pygame.display.set_caption( "Crossy road" )
      fuente = pygame.font.Font(None, 30)
      background_image = util.cargar_imagen('Imagenes/4.jpg');
      pierde_vida = util.cargar_sonido('Sonidos/el-pollo_1.mp3')
      gana_punt = util.cargar_sonido('Sonidos/misc108.mp3')
      pygame.mouse.set_visible( False )
      temporizador = pygame.time.Clock()
      heroe = Heroe()
      villano = [Villano((0,450),6),Villano((0,0),6),Villano((50,100),4),Villano((100,200),10),Villano((150,300),8),Villano((200,370),20),Villano((200,50),20)]
      hoguera = [Hoguera((100,20),0),Hoguera((125,90),0),Hoguera((310,320),0),Hoguera((100,170),0),Hoguera((400,370),0),Hoguera((170,170),0),Hoguera((250,170),0),Hoguera((200,320),0),Hoguera((350,400),0)]
      maiz = [Maiz((310,450),0),Maiz((310,0),0)]
      while jugando:
          heroe.update()
          if heroe.vida <= 0:

              jugando = False
          texto_vida = fuente.render("Vida: " + str(heroe.vida), 1, (250, 250, 250))
          for n in villano:
              n.update()
          heroe.image = heroe.imagenes[0]
          for n in villano:
              if heroe.rect.colliderect(n.rect):
                  heroe.image = heroe.imagenes[1]
                  pierde_vida.play()
                  heroe.vida -= 1
          for n in hoguera:
                
              n.update()
          heroe.image = heroe.imagenes[0]
          for n in hoguera:
              if heroe.rect.colliderect(n.rect):
                  heroe.image = heroe.imagenes[1]
                  pierde_vida.play()
                  heroe.vida -= 1
                  
          for n in maiz:
              if heroe.rect.colliderect(n.rect):
                  gana_punt.play()
                  heroe.punt += 0.5
              
          for event in pygame.event.get():
              if event.type == pygame.QUIT:
                  sys.exit()
          screen.blit(background_image, (0,0))
          screen.blit(heroe.image, heroe.rect)
          for n in villano:
              screen.blit(n.image, n.rect)
          screen.blit(texto_vida, (20, 10))
          pygame.display.update()
          pygame.time.delay(10)
          for n in hoguera:
              screen.blit(n.image, n.rect)
          for n in maiz:         
                 screen.blit(n.image, n.rect)
          screen.blit(texto_vida, (20, 10))
          pygame.display.update()
          pygame.time.delay(10)
          texto_vida = fuente.render("Puntaje: " + str(heroe.punt), 1, (250, 250, 250))
          screen.blit(texto_vida, (400, 10))
          pygame.display.update()
          pygame.time.delay(10)
        
                
         
   
if __name__ == '__main__':
      game()
