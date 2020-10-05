def setup():
    size(500, 300)
    background('#004477')
    stroke('#FFFFFF')
    
    
  
  

  



def polygon(n, x, y, r):
    angle = 360.0 / n
    beginShape()
    for i in range(n):
        vertex(x + r * cos(radians(angle * i)),
          y + r * sin(radians(angle * i)))
    endShape(CLOSE)
    

def draw():
    translate(150, height/2)
    noFill()
    polygon(10, 0, 0, 100)
    polygon(10, 0, 0, 95)
    polygon(10, 0, 0, 60)
    polygon(10, 0, 0, 55)
    polygon(10, 0, 0, 50)
