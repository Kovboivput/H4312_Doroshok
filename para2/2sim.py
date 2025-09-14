from random import randint

class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True


    def to_study(self):
        print ("time to study")
        self.progress += 0.10
        self.gladness -= 3
    def to_sleep(self):
        print ("time to sleep")
        self.gladness += 3
    def to_chill(self):
        print ("rest time")
        self.gladness += 5
        self.progress -= 0.20
    def to_read(self):
        print ("time to read")
        self.gladness -= 4
        self.progress += 0.2

    def is_alive(self):
        if self.progress < - 0.5:
            print ("cast out")
            self.alive = False
        elif self.gladness <= 0:
            print ("depression")
            self.alive = False
        elif self.progress > 5:
            print ("Passed externally")
            self.alive = False
    def end_of_day (self):
        print (f"gladness = {self.gladness}")
        print (f"progress = {round(self.progress, 2)}")
    def live(self, day):
        text_day = f"day{day} of {self.name} live"
        print (f"{text_day:=^40} ")
        cube = randint(1, 4)
        if cube == 1:
            self.to_sleep()
        elif cube == 2:
            self.to_study()
        elif cube == 3:
            self.to_chill()
        else:
            self.to_read()
        self.end_of_day()
        self.is_alive()




Nick = Student(name="Kick")
for day in range(1, 366 ):
    if Nick.alive == False:
        break
    Nick.live(day)
