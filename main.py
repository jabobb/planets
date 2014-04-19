# -*- coding: utf-8 -*-
#!/usr/bin/python
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint
from math import sqrt,pi,copysign

class CelestialObject(Widget):
    velocity_y = NumericProperty(0)
    velocity_x = NumericProperty(0)

    dx = NumericProperty(0)
    dy = NumericProperty(0)

    #volume = NumericProperty(0)
        
    velocity = ReferenceListProperty(velocity_x, velocity_y)  
    
    def move(self):
        vx,vy = self.velocity 
        diff_x = self.center_x - other.center_x
        diff_y = self.center_y - other.center_y

        r2 = sqrt((diff_x)**2 +\
                (diff_y)**2)

        m1 = pi*((self.width)/2)**2   
        m2 = pi*((other.width)/2)**2   
        self.velocity_y = self.G*m1*m2/r2
        self.velocity_x = self.G*m1*m2/r2
        #volume = NumericProperty(0)
        self.velocity = vx + self.velocity_x, vy + self.velocity_y
   
        
        self.pos = Vector(*self.velocity) + self.pos


class GravGame(Widget):

    sun1 = ObjectProperty(None)
    sun2 = ObjectProperty(None)

    G = 10**-6
    def prepare_move(self,first,second):
        diff_x = self.center_x - other.center_x
        diff_y = self.center_y - other.center_y

        r2 = sqrt((diff_x)**2 +\
                (diff_y)**2)

        m1 = pi*((self.width)/2)**2   
        m2 = pi*((other.width)/2)**2   
        self.velocity_y = self.G*m1*m2/r2
        self.velocity_x = self.G*m1*m2/r2
        #volume = NumericProperty(0)
        self.velocity = vx + self.velocity_x, vy + self.velocity_y
   
        
        self.pos = Vector(*self.velocity) + self.pos
    def serve_planets(self):
        self.sun1.velocity = Vector(0,-1)
        self.sun2.velocity = Vector(0,1)

    def update(self, dt):
        
       
        
        
        self.sun1.prepare_move(self.sun2)
        self.sun2.prepare_move(self.sun1)
        self.sun1.move()
        self.sun2.move()
    def on_touch_move(self,touch):
        self.serve_planets()
class GravApp(App):
    def build(self):
        game = GravGame()
        game.serve_planets()
        Clock.schedule_interval(game.update, 1.0/60.0)
        return game
    
if __name__ == '__main__':
    GravApp().run()
