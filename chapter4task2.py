class Airplane:
    def __init__(self, mark, model, year, max_speed):
        self.mark = mark
        self.model = model
        self.year = year
        self.max_speed = max_speed
        self.odometr = 0
        self.is_flying = False
    
    def take_off(self):
        self.is_flying = True
        return f"{self.mark} {self.model} was take off"

    def land(self):
        self.is_flying = False
        return f"{self.mark} {self.model} landed , the odometr {self.odometr}km "

    def fly(self):
        self.is_flying += 100
        return f"{self.mark} {self.model} is flying now {self.odometr}km during the flying {self.max_speed}km"        

plane = Airplane("Airbus", "A380", "2017", 1185)

print(plane.take_off())
print(plane.fly())
print(plane.land())
