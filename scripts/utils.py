import os
import pygame
import pygame.image

BASE_IMAGE_PATH = "data/images/"

def load_image(path):

  image = pygame.image.load(BASE_IMAGE_PATH + path).convert()

  return image

def load_images(path):

  images = []

  for img_name in os.listdir(BASE_IMAGE_PATH + path):
    images.append(load_image(path + '/' + img_name))

  return images

