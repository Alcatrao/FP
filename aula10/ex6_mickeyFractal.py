import sys
from ezgraphics import GraphicsWindow

def circle(canvas, x, y, r):
   """Draw a filled circle with center (x, y) and radius r."""
   canvas.drawOval(x-r, y-r, 2*r, 2*r)

# Draw a Mickey fractal with n levels.
# n=1 produces a circle, n=2 produces a familiar face.
def mickeyFractal(canvas, x, y, r, n):
   # The largest circle has center (x, y) and radius r.
   circle(canvas, x, y, r)
   #...
   if n<=1:
      return
   
   #linhaAbcissas=r*math.cos(60)
   linhaAbcissas=r      #"cantos do quadrado que o circunscreve" refere-se ao quadrado centrado no centro da circunferência e lado igual ao raio
   #mickeyFractal(canvas, x-linhaAbcissas, y*math.sin(math.pi/6), r/2, n-1)      #certo também, mas com x+x*sin(math.pi/6), o crescimento é exponencial e não linear (ao contrário de x-x*sinsin(math.pi/6))
   #mickeyFractal(canvas, x-y*math.sin(math.pi/6), y*math.sin(math.pi/6), r/2, n-1)
   #mickeyFractal(canvas, x+y*math.sin(math.pi/6), y*math.sin(math.pi/6), r/2, n-1)
   #mickeyFractal(canvas, x-linhaAbcissas, y-r, r/2, n-1)
   mickeyFractal(canvas, x-r, y-r, r/2, n-1)
   mickeyFractal(canvas, x+r, y-r, r/2, n-1)
   
   

def main():
   UNIT = 32

   win = GraphicsWindow(4*UNIT, 4+3*UNIT)
   canvas = win.canvas()
   canvas.setColor("cyan")
   canvas.setOutline("black")

   n = 4
   mickeyFractal(canvas, 2*UNIT, 2*UNIT, UNIT, n)
 
   win.wait()

main()
