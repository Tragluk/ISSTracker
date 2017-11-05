#!/bin/python3

import json
from requests import get as geturl
import turtle
from time import sleep
import pygame, sys

class Station:
  def __init__(self,lat,long):
    self.lat = lat
    self.long = long
    self.heading = 90
    self.shape = 'iss.gif'
    
  def getLocation(self):
    # updates the location
    url = 'http://api.open-notify.org/iss-now.json'
    response = geturl(url)
    result = json.loads(response.text)

    location = result['iss_position']
    self.lat = location['latitude']
    self.long = location['longitude']
    print("Long: " + self.long + " Lat: " + self.lat)
  
  
pygame.init()
screen = turtle.Screen()
screen.setup(720, 360)
screen.setworldcoordinates(-180, -90, 180, 90)
screen.bgpic('map.gif')

iss = Station(0,0)
screen.register_shape(iss.shape)

turtleiss = turtle.Turtle()
turtleiss.shape(iss.shape)
turtleiss.setheading(iss.heading)

turtleiss.penup()
iss.getLocation()
turtleiss.goto(float(iss.long), float(iss.lat))


turtleiss.pendown()
turtleiss.pencolor("White")

clock = pygame.time.Clock()
checktime = 0

while True:
  clock.tick(50)
  
  for event in pygame.event.get():
      if event.type == pygame.QUIT: sys.exit()

  
  checktime += 1
  if checktime > 600:
    iss.getLocation()
    turtleiss.goto(float(iss.long), float(iss.lat))
    checktime = 0
