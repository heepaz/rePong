from pygame.locals import *


def key_down(event,Joc):
  key_down_opts = {
      K_q : Joc.toggle_quit,
      K_ESCAPE : Joc.toggle_quit,
      K_w : Joc.palaL.mou_amunt,
      K_s : Joc.palaL.mou_avall,
      K_UP : Joc.palaR.mou_amunt,
      K_DOWN : Joc.palaR.mou_avall
      }
  if event.key in key_down_opts.keys():
    key_down_opts[event.key]()

def key_up(event,Joc):
  key_up_opts = {
      K_q : Joc.toggle_quit,
      K_ESCAPE : Joc.toggle_quit,
      K_w : Joc.palaL.atura_amunt,
      K_s : Joc.palaL.atura_avall,
      K_UP : Joc.palaR.atura_amunt,
      K_DOWN : Joc.palaR.atura_avall
      }
  if event.key in key_up_opts.keys():
    key_up_opts[event.key]()

def handle_keys(event,Joc):
  if event.type == KEYDOWN:
    key_down(event,Joc)
  elif event.type == KEYUP:
    key_up(event,Joc)
