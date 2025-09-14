from random import randint

class Animal:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.joy = 0
        self.alive = True


    def to_play(self):
        print ("time to play")
        self.joy += 0.12
        self.gladness -= 3
    def to_sleep(self):
        print ("time to sleep")
        self.gladness += 3
    def to_chill(self):
        print ("rest time")
        self.gladness += 5
        self.joy -= 0.1

    def is_alive(self):
        if self.joy < - 0.5:
            print ("happy life")
            self.alive = False
        elif self.gladness <= 0:
            print ("depression")
            self.alive = False
        elif self.gladness > 500:
            print ("Super happy")
            self.alive = False
    def end_of_day (self):
        print (f"gladness = {self.gladness}")
        print (f"joy = {round(self.joy, 2)}")
    def live(self, day):
        text_day = f"day{day} of {self.name} live"
        print (f"{text_day:=^30} ")
        cube = randint(1, 3)
        if cube == 1:
            self.to_sleep()
        elif cube == 2:
            self.to_play()
        else:
            self.to_chill()
        self.end_of_day()
        self.is_alive()



Cat = Animal(name="Cat")
for day in range(365):
    if Cat.alive == False:
        break
    Cat.live(day)