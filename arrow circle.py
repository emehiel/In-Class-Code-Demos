from vpython import *
import math

scene.width = 1200
scene.height = 800

arrows = []

n = 20

for i in range(0, 360, n):
    x = n*math.cos(math.pi/180. * i)
    y = n*math.sin(math.pi/180 * i)
    dx = math.sin(math.pi/180. * i)
    dy = -math.cos(math.pi/180. * i)
    a = arrow(pos=vec(x, y, 0), axis=vec(dx,dy,0), make_trail=True, trail_color = color.blue, retain=200)
    #a.trail_radius = 1
    #a.length = 1
    arrows.append(a)

while 1:
    rate(50)
    for a in arrows:
        p = n*2*math.pi/360
        a.pos = a.pos + a.axis*.5
        a.rotate(angle=1*pi/180, axis=vec(0,0,-1))