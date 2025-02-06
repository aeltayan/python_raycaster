import pygame
import sys
from scripts.entity import PlayerEntity
from scripts.map import Map

class Game:

  def __init__(self):
    pygame.init()
    self.clock = pygame.time.Clock()
    self.screen = pygame.display.set_mode((1024, 512))
    self.display = pygame.Surface((512, 256))
    self.player = PlayerEntity(self, (200, 150), (5, 5), (255, 0, 0))
    self.movement = [False, False, False, False] # N, S, E, W
    self.map = Map(self, tile_size=32)
  
  def run(self):

    while True:

      self.display.fill((0, 0, 0))

      self.map.render(self.display)
      self.player.update((self.movement[2] - self.movement[3], self.movement[1] - self.movement[0]))
      self.player.render(self.display)


      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()
      
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_w:
            self.movement[0] = True
          if event.key == pygame.K_s:
            self.movement[1] = True
          if event.key == pygame.K_d:
            self.movement[2] = True
          if event.key == pygame.K_a:
            self.movement[3] = True
        
            
        if event.type == pygame.KEYUP:
          if event.key == pygame.K_w:
            self.movement[0] = False
          if event.key == pygame.K_s:
            self.movement[1] = False
          if event.key == pygame.K_d:
            self.movement[2] = False
          if event.key == pygame.K_a:
            self.movement[3] = False
      
      self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0,0))
      self.clock.tick(60)
      pygame.display.update()
      pygame.display.set_caption(f"Raycaster | FPS: {int(self.clock.get_fps())}")

Game().run()
      