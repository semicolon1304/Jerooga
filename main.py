from Jerooga import Jerooga

jerooga_obj = Jerooga(.75)

bob = jerooga_obj.addJeroo((1,1), 1)
tom = jerooga_obj.addJeroo

for i in range(2):
    bob.turn('l')

bob.hop(1)
bob.toss()

jerooga_obj.allDone() 
