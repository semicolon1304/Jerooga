from Jerooga import Jerooga

jerooga_obj = Jerooga(.75)

bob = jerooga_obj.addJeroo((1,1), 1)
tom = jerooga_obj.addJeroo
for i in range(3):
    bob.hop()
bob.turn('r')
bob.hop(2)
bob.toss()

jerooga_obj.allDone() 
