import pygame
import sys
from scripts.entity import PlayerEntity

class Game:

  def __init__(self):
    pygame.init()
    self.clock = pygame.time.Clock()
    self.screen = pygame.display.set_mode((800, 600))
    self.display = pygame.Surface((400, 300))
    self.player = PlayerEntity(self, (200, 150), (10, 10), (255, 0, 0))
  
  def run(self):

    while True:

      self.display.fill((0, 0, 0))

      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()
      

      self.player.render(self.display)

      self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0,0))
      pygame.display.update()
      self.clock.tick(60)
      pygame.display.set_caption(f"Raycaster | FPS: {int(self.clock.get_fps())}")

Game().run()
      