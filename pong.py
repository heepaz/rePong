#! /usr/bin/env python3
from joc import Joc
from objectes import Pala, Pilota
import pygame

def main():
  pygame.init()
  Joc.palaL = Pala((5,Joc.HEIGHT/2))
  Joc.palaR = Pala((Joc.WIDTH-5,Joc.HEIGHT/2))
  Joc.pilota = Pilota((Joc.WIDTH/2, Joc.HEIGHT/2))
  Joc.main_loop()
  

if __name__ == "__main__":
  main()
