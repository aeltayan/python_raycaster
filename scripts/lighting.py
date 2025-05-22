import math

class Lighting:

  def __init__(self, game, ambience, diffuse, max_distance):

    self.game = game
    self.ambience = ambience
    self.diffuse = diffuse
    self.max_distance = max_distance
    self.flashlight_power = True
    self.flashlight_cone_angle = 30
  

  def compute_light_intensity(self, ray_length):

    if self.flashlight_power:
      max_dist_mult = 2

    else:
      max_dist_mult = 1

    intensity = self.ambience * self.flashlight_power + self.diffuse * (1-(ray_length/(self.max_distance*max_dist_mult)))

    intensity = max(0,min(1, intensity))

    return intensity


  def toggle_flashlight(self, flashlight_on):

    if flashlight_on:

      self.flashlight_power = True
    
    else:

      self.flashlight_power = False


  def shade_color(self, color, intensity):

    r,g,b = color

    return (r*intensity, g*intensity, b*intensity)