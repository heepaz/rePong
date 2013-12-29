import os.path
import pygame
from pygame.locals import *
from tecles import *

pygame.init()

class Joc (object):
  WIDTH = 600
  HEIGHT = 400
  screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
  background = pygame.image.load(os.path.join("Imatges","fons.jpg"))

  clock = pygame.time.Clock()
  dt = 0.05

  puntsR = 0
  puntsL = 0

  font = pygame.font.SysFont("Arial", 20)

  quit = False

  palaL = None
  palaR = None
  pilota = None

  pales = pygame.sprite.Group()
  pilotes = pygame.sprite.Group()

  def toggle_quit():
    Joc.quit = not Joc.quit

  def gol():
      for pilota in Joc.pilotes.sprites():
          if pilota.posicio[0] > Joc.WIDTH:
              Joc.puntsR += 1
              print(Joc.puntsL, Joc.puntsR)
              pilota.restart()
          elif pilota.posicio[0] < 0:
              Joc.puntsL += 1
              print(Joc.puntsL, Joc.puntsR)
              pilota.restart()

  def main_loop():
    while not Joc.quit:
      for event in pygame.event.get():
        if event.type == KEYUP or event.type == KEYDOWN:
          handle_keys(event,Joc)
        elif event.type == QUIT:
          Joc.quit = True
      Joc.pales.update()
      Joc.pilotes.update()
      Joc.screen.blit(Joc.background,(0,0))
      Joc.pilotes.draw(Joc.screen)
      Joc.pales.draw(Joc.screen)
      Joc.gol()
      pygame.display.update()
      Joc.dt = Joc.clock.tick() / 10


