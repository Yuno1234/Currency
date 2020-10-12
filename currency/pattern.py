def polygon(n, x, y, r):
    angle = 360.0 / n
    beginShape()
    for i in range(6):
        vertex(x + r * cos(radians(angle * i)), y + r * sin(radians(angle * i)))
    endShape(CLOSE)

def renderPolygon():
    pushMatrix()
    fill('#2b2b2b')
    rect(0, 0, width, height)
    translate(width/2, height/2)
    strokeWeight(8)
    stroke('#2b2b2b')
    fill('#ffaf4d')
    polygon(6, 0, 0, 130)
    
    noFill()
    for i in range(1, 10):
        pushMatrix()
        c = random(0,100)
        stroke(c, c, c)
        polygon(6, 0, 0, 12*i)
        rotate(random(0, 2*PI))
        c = random(0,100)
        stroke(c, c, c)
        polygon(6, 0, 0, 12*i)
        popMatrix()
    popMatrix()
