class car:
    def __init__(self, year, speed):
        self.year = year
        self.speed = speed
    def getSpeed(self):
        print("maximum speed is: ", self.speed)
    def setSpeed(self, speed):
        self.speed = speed

BMW = car(2018, 155)
FORD = car(2016, 140)

# car.getSpeed(BMW)
# car.getSpeed(FORD)

BMW.getSpeed()
BMW.setSpeed(143)
BMW.getSpeed()
FORD.getSpeed()
