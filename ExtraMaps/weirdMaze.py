from Jerooga import Jerooga
from time import sleep

jerooga_obj = Jerooga(.2, "maze1.jev")


bob = jerooga_obj.addJeroo((0,0))
sleep(5)
bob.turn("right")

while not (bob.isNet("left") and bob.isNet("right")):
    if bob.isClear("ahead"):
        bob.hop()
    elif bob.isFlower("ahead"):
        bob.hop()
        bob.pick()
    elif bob.isNet("ahead"):
        bob.toss()
        bob.hop()
        bob.pick()
    elif not bob.isWater("left"):
        bob.turn("left")
    elif not bob.isWater("right"):
        bob.turn("right")

jerooga_obj.allDone() 
