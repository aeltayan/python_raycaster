class Lighting:

  def __init__(self, game, ambience, diffuse, max_distance):

    self.game = game
    self.ambience = ambience
    self.diffuse = diffuse
    self.max_distance = max_distance
  

  def compute_light_intensity(self, ray_length):

    intensity = self.ambience + self.diffuse * (1-(ray_length/self.max_distance))

    intensity = max(0,min(1, intensity))

    return intensity


  def shade_color(self, color, intensity):

    r,g,b = color

    return (r*intensity, g*intensity, b*intensity)