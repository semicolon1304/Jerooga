from Jerooga import Jerooga

jerooga_obj = Jerooga(.10, "maze2.jev")

bob = jerooga_obj.addJeroo((0,0))
bob.turn("right")

while not bob.isFlower():
    if bob.isClear("ahead") or bob.isFlower("ahead"):
        bob.hop()
    elif bob.isClear("left"):
        bob.turn("left")
    elif bob.isClear("right"):
        bob.turn("right")
    else:
        bob.turn("right")
        bob.turn("right")

jerooga_obj.allDone() 
