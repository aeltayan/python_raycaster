import pygame
import math

pi = math.pi

class PlayerEntity:
  def __init__(self, game, pos, angle, speed, rot_speed):
    self.game = game
    self.pos = list(pos)
    self.angle = angle
    self.speed = speed * self.game.delta_time
    self.rot_speed = rot_speed
  
  def update(self):

    sin = math.sin(self.angle)
    cos = math.cos(self.angle)

    dx, dy = 0,0

    speed_sin = self.speed * sin # Y movement
    speed_cos = self.speed * cos # X movement

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        dx += speed_cos
        dy += speed_sin

    if keys[pygame.K_s]:
        dx -= speed_cos
        dy -= speed_sin

    if keys[pygame.K_d]:
        dx -= speed_sin
        dy += speed_cos

    if keys[pygame.K_a]:
        dx += speed_sin
        dy -= speed_cos
          
    self.pos[0] += dx
    self.pos[1] += dy

    if keys[pygame.K_LEFT]:
        self.angle -= self.rot_speed * self.game.delta_time
    if keys[pygame.K_RIGHT]:
        self.angle += self.rot_speed * self.game.delta_time 

    self.angle %= 2*pi       


  def render(self, surface):
    pygame.draw.line(surface, "yellow", (self.pos[0], self.pos[1]),
                      (self.pos[0] + self.game.screen.get_height() * math.cos(self.angle),
                       self.pos[1] + self.game.screen.get_width() * math.sin(self.angle) ))
    pygame.draw.circle(surface, 'green', (self.pos[0], self.pos[1]), 2)

