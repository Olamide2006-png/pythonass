class mover:
    def move(self):
        pass


class car(mover):
    def move(self):
        print("Driving 🚗")
class plane(mover):
    def move(self):
        print("Flying ✈️")
class boat(mover):
    def move(self):
        print("sailing ⛵")
 #Animal classes
class dog(mover):
    def move(self):
        print("Running 🐕")
class bird(mover):
    def move(self):
        print("Flying 🦅")
class fish(mover):
    def move(self):
        print("Swimming 🐟")

movers = [car(), plane(), boat(), dog(), bird(), fish()]
for m in movers:
    m.move()