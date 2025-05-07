import math
import pygame
from settings import *
from scripts.map import map

class Raycaster:

  def __init__(self ,game, fov, screen_width, screen_height, tile_size):
    
    self.game = game
    self.fov = fov
    self.width = screen_width
    self.height = screen_height
    self.tile_size = tile_size

  def cast_rays(self, surface, pos, angle):

    dx = math.cos(angle)
    dy = math.sin(angle)
    
    plane_x = -dy * self.fov
    plane_y = dx * self.fov

    for x in range(self.width):

      player_x = pos[0] / self.tile_size
      player_y = pos[1] / self.tile_size

      map_x = int(player_x)
      map_y = int(player_y)

      camera_x = ((2*x)/self.width) - 1

      ray_dx = dx + plane_x * camera_x
      ray_dy = dy + plane_y * camera_x

      #Length of ray if we are to move one unit on either axis

      if ray_dx != 0:
        delta_ray_x = math.sqrt(1 + math.pow(ray_dy/ray_dx, 2))
      
      else:
        delta_ray_x = float("inf")
      
      if ray_dy != 0:
        delta_ray_y= math.sqrt(1 + math.pow(ray_dx/ray_dy, 2))
      
      else:
        delta_ray_y = float("inf")

      step_x = 0
      step_y = 0

      # scales up/down delta ray distances by a normalized value based on player pos when ray start position is not alligned with grid lines 

      if ray_dx < 0:      
        step_x = -1
        ray_length_x = (player_x - map_x) * delta_ray_x
      
      else:
        step_x = 1
        ray_length_x = ((map_x + 1.0) - player_x) * delta_ray_x
      
      if ray_dy < 0:
        step_y = -1
        ray_length_y = (player_y - map_y) * delta_ray_y

      else:
        step_y = 1
        ray_length_y = ((map_y + 1.0) - player_y) * delta_ray_y
      

      hit = False
      hit_side = False

      while hit is False:
        
        if ray_length_x < ray_length_y:
          map_x += step_x
          ray_length_x += delta_ray_x
          hit_side = False
        
        else:
          map_y += step_y 
          ray_length_y += delta_ray_y
          hit_side = True
        

        if self.game.map.check_collisions_norm((map_x,map_y)):
          hit = True
      
      

      #fix fisheye effect
      if hit_side == False:
          final_distance = (map_x - player_x + (1 - step_x) / 2) / ray_dx
          
      else:
          final_distance = (map_y - player_y + (1 - step_y) / 2) / ray_dy

      
      wall_height = (screen_height) / final_distance

      max_view_distance = math.sqrt(unit_width*unit_width + unit_height*unit_height)
      
      falloff = 1 - (final_distance/max_view_distance)

      falloff = max(0,min(falloff,1))
      
      self.render_wall(surface, x, wall_height, falloff)


  def render_wall(self, surface, x_pos, wall_height,alpha):

      wall_end = max(0 , (screen_height // 2) - (wall_height // 2))
      wall_start = min(screen_height, (screen_height // 2) + (wall_height // 2))

      wall_rgb = (128*alpha, 128*alpha, 128*alpha)
      floor_rgb = (128*alpha, 128*alpha, 128*alpha)
      ceiling_rgb = (128*alpha,128*alpha,128*alpha)

      pygame.draw.line(surface, wall_rgb, (x_pos, wall_start), (x_pos, wall_end))
      pygame.draw.line(surface, "black",  (x_pos, wall_start), (x_pos, screen_height))
      pygame.draw.line(surface, "black",  (x_pos, wall_end), (x_pos, 0))



      
        
      



