from joc import Joc
import pygame
import os.path
import random

class Element(pygame.sprite.Sprite):
  def __init__(self, pos=(0,0)):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load(os.path.join("Imatges","Default.png"))
    self.rect = self.image.get_rect()
    self.rect.center = list(pos)
    self.posicio = (0,0)
    self.velocitat = (0,0)

  def top(self):
    return self.posicio[1] - self.rect[3]/2

  def bottom(self):
    return self.posicio[1] + self.rect[3]/2

  def left(self):
    return self.posicio[0] - self.rect[2]/2

  def right(self):
    return self.posicio[0] + self.rect[2]/2

  def __str__(self):
    return "<Pos" + str(self.posicio) +" Top" +str(self.top())+ "Bot" +str(self.bottom())+ str(self.rect) + ">"

class Pala(Element):
  def __init__(self, pos=(0,0)):
    Element.__init__(self, pos)
    self.image = pygame.image.load(os.path.join("Imatges","pad.jpg"))
    self.rect = self.image.get_rect()
    self.amunt = False
    self.avall = False
    self.posicio = list(pos)
    self.rect.center = pos
    Joc.pales.add(self)

  def mou_amunt(self):
    self.amunt = True
  def atura_amunt(self):
    self.amunt = False

  def mou_avall(self):
    self.avall = True
  def atura_avall(self):
    self.avall = False

  def update(self):
    x = self.posicio[0]
    y = self.posicio[1]
    vx = self.velocitat[0]
    vy = self.velocitat[1]

    if self.top() < 0:
      y = self.rect[3]/2
    elif self.bottom() > Joc.HEIGHT:
      y = Joc.HEIGHT-self.rect[3]/2
    self.rect.center = (x,y)

    if self.amunt and self.avall:
      self.velocitat = [0,0]
    elif not self.amunt and not self.avall:
      self.velocitat = [0,0]
    elif self.amunt:
      self.velocitat = [0,-2]
    elif self.avall:
      self.velocitat = [0,2]
    self.posicio = [x+vx*Joc.dt,y+vy*Joc.dt]
    self.rect.center = (x,y)

class Pilota(Element):
  def __init__(self, pos=(0,0)):
    Element.__init__(self, pos)
    self.image = pygame.image.load(os.path.join("Imatges","ball.png"))
    self.rect = self.image.get_rect()
    self.posicio = list(pos)
    self.rect.center = pos
    self.velocitat = self.rand_vel()
    Joc.pilotes.add(self)
    self.boing = pygame.mixer.Sound(os.path.join("Sons","boing.wav"))
    self.pala = pygame.mixer.Sound(os.path.join("Sons","pala.wav"))

  def rand_vel(self):
    signe = [-1,1]
    vx = random.uniform(1,3)
    vy = random.uniform(1,3)
    random.shuffle(signe)
    vx *= signe[0]
    random.shuffle(signe)
    vy *= signe[0]
    return [vx,vy]

  def restart(self):
    self.posicio = [Joc.WIDTH/2,Joc.HEIGHT/2]
    self.rect.center = tuple(self.posicio)
    self.velocitat = self.rand_vel()

  def update(self):
    x = self.posicio[0]
    y = self.posicio[1]
    vx = self.velocitat[0]
    vy = self.velocitat[1]

    if Joc.palaL.right() <x<Joc.palaR.left() and pygame.sprite.spritecollideany(self,Joc.pales):

      if x > Joc.WIDTH/2:
        x = Joc.palaR.left() - self.rect[2]/2
        dist = y - Joc.palaR.posicio[1]
        vy = (vy+dist)/Joc.palaR.rect[3]*3
      else:
        x = Joc.palaL.right() + self.rect[2]/2
        dist = y - Joc.palaL.posicio[1]
        vy = (vy+dist)/Joc.palaL.rect[3]*3
      self.pala.play()
      vx *= -1.1
      self.rect.center = (x,y)
    else:
      if self.top() < 0:
        y = self.rect[3]/2
        vy *= -1
        self.boing.play()
      elif self.bottom() > Joc.HEIGHT:
        y = Joc.HEIGHT - self.rect[3]/2
        vy *= -1
        self.boing.play()
    self.posicio = [x+vx*Joc.dt,y+vy*Joc.dt]
    self.velocitat = [vx,vy]
    self.rect.center = (self.posicio[0], self.posicio[1])
