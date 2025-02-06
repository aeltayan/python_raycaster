import pygame
import sys
from scripts.entity import PlayerEntity
from scripts.map import Map

class Game:

  def __init__(self):
    pygame.init()
    self.clock = pygame.time.Clock()
    self.delta_time = 1
    self.screen = pygame.display.set_mode((1024, 512))
    self.display = pygame.Surface((512, 256))
    self.player = PlayerEntity(self, (200, 150), 0, 1, 0.002)
    self.movement = [False, False, False, False] # N, S, E, W
    self.map = Map(self, tile_size=32)
  
  def run(self):

    while True:

      self.display.fill((0, 0, 0))

      self.map.render(self.display)
      self.player.update()

      print(self.player.pos)
      self.player.render(self.display)

      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()
          
      
      self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0,0))
      self.delta_time = self.clock.tick(60)
      pygame.display.update()
      pygame.display.set_caption(f"Raycaster | FPS: {int(self.clock.get_fps())}")

Game().run()
      