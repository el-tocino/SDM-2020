#!/usr/bin/python3
""" show the distance to an object, and a relevant background color. """

from time import sleep
import pygame
from gpiozero import DistanceSensor

# Initialize ultrasonic sensor
sensor = DistanceSensor(trigger=24, echo=23)

# Init pygame
pygame.init()
#pi 5" display
screentraits = pygame.display.Info()
wres = screentraits.current_w
hres = screentraits.current_h
screen = pygame.display.set_mode([wres, hres])
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


def add_distance(dist, text_color):
    """ add distanceto display. """
    font = pygame.font.SysFont(None, 60)
    text = font.render(str(dist)[:6], True, text_color)
    text_rect = text.get_rect(center=(int(wres / 2), int(hres / 2 + 100 )))
    screen.blit(text, text_rect)
    pygame.display.update()

def add_text(text_string, text_color, fontsize):
    """ write the text to display. """
    font = pygame.font.Font(None, fontsize)
    text = font.render(text_string, True, text_color)
    text_rect = text.get_rect(center=((wres / 2), (hres / 2) - 100))
    screen.blit(text, text_rect)
    pygame.display.update()

def show_distance(distance):
    """ set the bg color, then print the distance if it's under 2 meters. """
    distnc = float(distance)
    if distnc < .4:
        new_text = "Won't you back that ass up?"
        set_bgcolor(red)
        tcolor = yellow 
        fsize = 64
        # Juvenile
    elif distnc < 1.0:
        new_text = "GET BACK, MOTHER FUCKER YOU DON'T KNOW ME LIKE THAT!"
        set_bgcolor(yellow)
        tcolor = blue 
        fsize = 52
        # Ludacris
    elif distnc < 2:
        new_text = "Don't stand so close to me!"
        set_bgcolor(black)
        tcolor = white 
        fsize = 70
        # The Police
    else:
        set_bgcolor(blue)
        new_text = "No proximity faults detected."
        tcolor = white
        fsize = 30
    add_text(new_text, tcolor, fsize)
    add_distance(distnc, tcolor)

def main():
    while True:
        sleep(2)
        getdist = sensor.distance
        print (getdist)
        show_distance(getdist)


if __name__ == '__main__':
    main()
