def setup():
    size(500, 300)
    background('#2b2b2b')
    

def polygon(n, x, y, r):
    angle = 360.0 / n
    beginShape()
    for i in range(n):
        vertex(x + r * cos(radians(angle * i)), y + r * sin(radians(angle * i)))
    endShape(CLOSE)
    

x = 0

def draw():
    global x
    x += 10
    
    fill(0x032b2b2b)
    rect(0, 0, width, height)
    stroke('#ff9717')
    line(x, 10, x-100, 10)
    line(x, 290, x-100, 290)
    if x > 550:
        x = 0
    
    pushMatrix()
    translate(150, height/2)
    rotate(-PI/2)
    fill('#ffaf4d')
    arc(0, 0, 195, 195, 0, PI, PIE)
    arc(0, 0, 115, 115, 0, PI+PI/2, PIE)
    noFill()
    stroke('#2b2b2b')
    strokeWeight(8)
    polygon(10, 0, 0, 100)
    polygon(10, 0, 0, 60)
    fill('#2b2b2b')
    polygon(10, 0, 0, 20)
    stroke('#FFFFFF')
    strokeWeight(2)
    noFill()
    polygon(10, 0, 0, 100)
    polygon(10, 0, 0, 60)
    polygon(10, 0, 0, 20)
    popMatrix()
