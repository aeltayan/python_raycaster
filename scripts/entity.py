import pygame

class PlayerEntity:
  def __init__(self, game, pos, size, color):
    self.game = game
    self.pos = list(pos)
    self.size = size
    self.color = color
    self.velocity = [0,0]

  
  def update(self, movement=(0,0)):

    frame_movement = (movement[0] + self.velocity[0], movement[1] + self.velocity[1])
    self.pos[0] += frame_movement[0]
    self.pos[1] += frame_movement[1]

  def render(self, surface):
    pygame.draw.rect(surface, self.color, pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
)
