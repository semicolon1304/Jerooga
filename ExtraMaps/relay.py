from Jerooga import Jerooga
from time import sleep

jerooga_obj = Jerooga(.30, "relay.jev")

j1 = jerooga_obj.addJeroo((22,11))
j2 = jerooga_obj.addJeroo((19, 11))
j3 = jerooga_obj.addJeroo((16, 11))
j4 = jerooga_obj.addJeroo((13, 11))

sleep(4)

j1.hop(1)
j1.pick()
j1.turn("r")
j1.turn("r")
j1.hop(3)
j1.give()

j2.turn("l")
j2.turn("l")
j2.hop(2)
j2.give()

j3.turn("r")
j3.turn("r")
j3.hop(2)
j3.give()

j4.turn("l")
j4.turn("l")
j4.hop(2)
j4.turn("l")
j4.hop()
j4.toss()

for i in range(4):
    j4.hop()

jerooga_obj.allDone() 
