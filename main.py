from Jerooga import Jerooga

jerooga_obj = Jerooga(.75)

bob = jerooga_obj.addJeroo((0,0), 1, "E")
tom = jerooga_obj.addJeroo((0,1), 0, "N")

bob.give("r")
tom.give()
print(bob.getFlowers())


# for i in range(2):
#     bob.hop(2)
#     bob.turn('l')

# bob.hop(1)
# bob.toss()

jerooga_obj.allDone() 
