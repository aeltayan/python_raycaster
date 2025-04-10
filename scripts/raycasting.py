import math

class Raycaster:

  def __init__(self, pos, angle, fov, screen_width, screen_height):
    
    self.pos = pos
    self.angle = angle
    self.fov = fov
    self.width = screen_width
    self.height = screen_height

  def cast_rays(self):

    dx = math.cos(self.angle)
    dy = math.sin(self.angle)

    plane_x = -dy * self.fov
    plane_y = dx * self.fov

    for x in range(self.width):

      camera_x = ((2*x)/self.width) - 1

      ray_dir_x = dx + plane_x * camera_x
      ray_dir_y = dy + plane_y * camera_x