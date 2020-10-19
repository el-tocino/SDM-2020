""" show the distance to an object, and a relevant background color. """

from time import sleep
import pygame
from gpiozero import DistanceSensor

# Initialize ultrasonic sensor
sensor = DistanceSensor(trigger=18, echo=24)

# Init pygame
pygame.init()
#pi 5" display
screen = pygame.display.set_mode([800, 480])
# testing screen
##screen = pygame.display.set_mode([1920, 1080])
white = [255, 255, 255]
red = [255, 0, 0]
blue = [0, 0, 255]
green = [0, 255, 0]
yellow = [255, 250, 25]
black = [0, 0, 0]

def set_bgcolor(bgcolor):
    """ fill the screen with a color. """
    pygame.display.flip()
    screen.fill(bgcolor)
    pygame.display.update()

def add_text(text_string, text_color):
    """ write the text to display. """
    font = pygame.font.Font(None, 80)
    text = font.render(text_string, True, text_color)
    text_rect = text.get_rect(center=(960, 540))
    screen.blit(text, text_rect)
    pygame.display.update()

def show_distance(distance):
    """ set the bg color, then print the distance if it's under 2 meters. """
    distnc = float(distance)
    if distnc < .9:
        new_text = "GET BACK, MOTHER FUCKER YOU DON'T KNOW ME LIKE THAT!"
        set_bgcolor(black)
        tcolor = white
        # Ludacris
    elif distnc < 1.5:
        new_text = "Won't you back that ass up?"
        set_bgcolor(red)
        tcolor = yellow
        # Juvenile
    elif distnc < 2.1:
        new_text = "Don't stand so close to me!"
        set_bgcolor(yellow)
        tcolor = blue
        # The Police
    else:
        set_bgcolor(blue)
    add_text(new_text, tcolor)

while True:
    sleep(4)
    getdist = sensor.distance
    show_distance(getdist)
