import sys
import pyglet
import pyglet.gl as gl
from noise import pnoise1
window = pyglet.window.Window(visible=False, resizable=True)

def on_resize(width, height):
	"""Setup 3D viewport"""
 
	gl.glViewport(0, 0, width, height)
	
window.on_resize = on_resize
window.set_visible()

points = 256
span = 5.0
speed = 1.0

if len(sys.argv) > 1:
	octaves = int(sys.argv[1])
else:
	octaves = 1

base = 0
min = max = 0

@window.event
def on_draw():
	global min,max
	window.clear()
	r = range(256)
	gl.glBeginQuery(gl.GL_LINE_STRIP)
	for i in r:
		x = float(i) * span / points - 0.5 * span
		y = pnoise1(x + base, octaves)
		gl.glVertexAttrib3f(x * 2.0 / span, y, 0)
	gl.glEndQuery()

def update(dt):
	global base
	base += dt * speed
pyglet.clock.schedule_interval(update, 1.0/30.0)

pyglet.app.run()