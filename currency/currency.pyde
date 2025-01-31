from pattern import *

username = 0
balance = 83200
transfer = 12345


def setup():
    size(500, 300)
    background('#2b2b2b')
    font = loadFont("TwCenMT40.vlw")
    textFont(font)
    

def polygon(n, x, y, r):
    angle = 360.0 / n
    beginShape()
    for i in range(n):
        vertex(x + r * cos(radians(angle * i)), y + r * sin(radians(angle * i)))
    endShape(CLOSE)

x = 0
bal = balance
pay = False


def draw():
    global x, balance, bal, select
    
    if pay == False:
        x += 10
        if bal < 0:
            balance = 0
            bal = 0
        elif balance < bal:
            bal -= 200
        
        
        #line effect
        fill(0x662b2b2b)
        rect(0, 0, width, height)
        stroke('#ff9717')
        line(x, 10, x-100, 10)
        line(x, 290, x-100, 290)
        stroke(0x55ff9717)
        line(0, 10, width, 10)
        line(0, 290, width, 290)
        
        if x > 550 :
            x = 0
        
        thetaL = TAU/100000 * bal
        if bal > 99999:
            thetaS = TAU
            thetaL = TAU
        elif bal < 100000:
                thetaS = TAU/10000 * (bal%10000)
        
        #charge balance
        pushMatrix()
        translate(150, 130)
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
        
        fill(230)
        textAlign(CENTER, CENTER)
        textSize(30)
        text(str(balance) + "mAh", 150, 250)
    
    
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
        
        fill('#2b2b2b')
        textSize(30)
        text('PAY', 320, 125)
        textSize(20)
        text('TRANSFER', 400, 175)
        
        
    elif pay == True:
        renderPolygon()
        strokeWeight(0)
        stroke(150)
        #rect(10, 10, 50, 30)
        strokeWeight(5)
        line(25, 25, 45, 15)
        line(25, 25, 45, 35)
        noLoop()

    
def mousePressed():
    global balance, transfer, pay

    disX1 = 320 - mouseX
    disY1 = 125 - mouseY
    if sqrt(sq(disX1) + sq(disY1)) < 40 and pay == False:
        pay = True

    disX2 = 400 - mouseX
    disY2 = 175 - mouseY
    if sqrt(sq(disX2) + sq(disY2)) < 40 and pay == False:
        balance = balance - transfer
        print(balance)

    if mouseX>10 and mouseX<60 and mouseY>10 and mouseY<40 and pay == True:
        global pay, x
        pay = False
        loop()
        x = 0
        
        
        

    
