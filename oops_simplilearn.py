class car:

    def __init__(self, year, speed):
        self.year = year
        self.speed = speed

    def getSpeed(self):
        print("Maximum speed is: ", self.speed)
    def setSpeed(self, speed):
        self.speed = speed

bmw = car(2018, 155)
ford = car(2016, 140)

class Sedan(car):   #Child class
    def accelerate(self):
        print('137')
    def openTrunk(self):
        print('trunk has been opened')
class SUV(car): #child class
    def accelerate(self):
        print('127')

honda = Sedan(2018,150)
bmw.getSpeed()
honda.getSpeed()
honda.openTrunk()
#bmw.openTrunk()

#bmw.setSpeed(143)
#bmw.getSpeed()
#ford.getSpeed()



#car.getSpeed(BMW)
#car.getSpeed(FORD)
#BMW.getSpeed()
#FORD.getSpeed()