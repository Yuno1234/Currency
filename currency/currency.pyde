from pattern import *

username = 0
balance = 100000
transfer = 13000


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
bal = balance

def draw():
    global x, balance, bal
    
    x += 10
    if bal < 0:
        balance = 0
        bal = 0
    elif balance < bal:
        bal -= 200
    
    #line effect
    fill(0x032b2b2b)
    rect(0, 0, width, height)
    stroke('#ff9717')
    line(x, 10, x-100, 10)
    line(x, 290, x-100, 290)
    if x > 550:
        x = 0
    
    thetaL = TAU/100000 * bal
    if bal == 100000:
        thetaS = TAU
    elif bal < 100000:
            thetaS = TAU/10000 * (bal%10000)
    
    #charge balance
    pushMatrix()
    translate(150, height/2)
    rotate(-PI/2)
    noStroke()
    fill('#2b2b2b')
    arc(0, 0, 194, 194, 0, 2*PI, PIE)
    fill('#ffaf4d')
    arc(0, 0, 194, 194, 0, thetaL, PIE)
    fill('#2b2b2b')
    arc(0, 0, 114, 114, 0, 2*PI, PIE)
    fill('#ffaf4d')
    arc(0, 0, 114, 114, 0, thetaS, PIE)
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
    
    
    renderPolygon()
    

    #buttons
    fill('#ffaf4d')
    stroke('#2b2b2b')
    strokeWeight(8)
    polygon(6, 320, 125, 50)
    polygon(6, 400, 175, 50)
    noFill()
    stroke('#FFFFFF')
    strokeWeight(2)
    polygon(6, 320, 125, 50)
    polygon(6, 400, 175, 50)

    
def mousePressed():
    global balance, transfer
    balance = balance - transfer
    print(balance)
    
