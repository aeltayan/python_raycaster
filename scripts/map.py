import pygame 

offsets = [(1,1), (1,0), (0,1), (-1,0), (0,-1), (-1,-1), (1,-1), (-1,1)]

map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]


class Map:
  def __init__(self, game, tile_size):
    self.game = game
    self.tile_size = tile_size

  
  def check_collisions(self, pos):

    grid_pos = self.entity_grid_pos(pos)

    if map[grid_pos[1]][grid_pos[0]] != 0:
      return True
    return False
  
    
  def check_collisions_norm(self, pos):

    if map[pos[1]][pos[0]] != 0:
      return True
    return False
  
  def entity_grid_pos(self, pos):

    grid_x = int(pos[0]//self.tile_size)
    grid_y = int(pos[1]//self.tile_size)

    return [grid_x, grid_y]

  def render(self, surface):

    for row_index, row in enumerate(map):
      for column_index, column in enumerate(row):
        if map[row_index][column_index] == 1:
          pygame.draw.rect(surface, "white", pygame.Rect(column_index * self.tile_size, row_index*self.tile_size+1, self.tile_size-1, self.tile_size-1))
        else:
          pygame.draw.rect(surface, "white", pygame.Rect(column_index * self.tile_size, row_index*self.tile_size, self.tile_size, self.tile_size),1)
