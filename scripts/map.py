import pygame 

map = [
  1,1,1,1,1,1,1,1,
  1,0,0,0,0,0,0,1,
  1,0,1,1,0,0,0,1,
  1,0,0,0,0,0,0,1,
  1,0,0,0,1,1,0,1,
  1,0,0,0,1,0,0,1,
  1,0,0,0,0,0,0,1,
  1,1,1,1,1,1,1,1,
]


class Map:
  def __init__(self, game, tile_size):
    self.game = game
    self.tile_size = tile_size


  def render(self, surface):


    for y in range(8):
      for x in range(8):
        if map[y*8 + x] == 1:
          pygame.draw.rect(surface, (255, 255, 255), pygame.Rect(x*self.tile_size, y*self.tile_size , self.tile_size, self.tile_size), 1)
