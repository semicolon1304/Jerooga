from Jerooga import Jerooga
jerooga_obj = Jerooga()

for y in range(1,jerooga_obj.blocksHigh-1):
    for x in range (1,jerooga_obj.blocksWide-1):
        jerooga_obj.board[y][x].setState("land")


bob = jerooga_obj.addJeroo((1,1))
for i in range(3):
    bob.hop()



jerooga_obj.allDone() 

