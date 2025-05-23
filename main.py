import pygame
import sys
from scripts.entity import PlayerEntity
from scripts.map import Map
from scripts.raycasting import Raycaster
from scripts.lighting import Lighting
from settings import *

class Game:

  def __init__(self):
    pygame.init()
    self.clock = pygame.time.Clock()
    self.delta_time = 1
    self.screen = pygame.display.set_mode((screen_width, screen_height))
    self.display = pygame.Surface((screen_width, screen_height))
    self.player = PlayerEntity(self, (200, 150), 0, 2, 0.003, 10, 0, 10)
    self.movement = [False, False, False, False] # N, S, E, W
    self.assets = {}
    self.map = Map(self, tile_size=64)
    self.raycaster = Raycaster(self, 0.66, screen_width, screen_height, tile_size=64)
    self.lighting = Lighting(self,0.4, 0.8, 2)
  
  def run(self):
    while True:

      self.display.fill((0, 0, 0))
      self.player.update()
      self.raycaster.cast_rays(self.display, self.player.pos, self.player.angle, self.player.head_tilt)
      self.lighting.toggle_flashlight(self.player.flashlight)

      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()

        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_f:
            self.player.flashlight = not self.player.flashlight
    
          
      
      self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0,0))
      self.delta_time = self.clock.tick(60)
      pygame.display.update()
      pygame.display.set_caption(f"Raycaster | FPS: {int(self.clock.get_fps())}")

Game().run()
      