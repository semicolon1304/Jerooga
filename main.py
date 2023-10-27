from Jerooga import Jerooga
jerooga_obj = Jerooga(file="all.jev")

# for y in range(1,jerooga_obj.blocksHigh-1):
#     for x in range (1,jerooga_obj.blocksWide-1):
#         jerooga_obj.board[y][x].setState("land")



# for i in range(jerooga_obj.blocksWide):
#     jerooga_obj[0][i].setState("water")
#     jerooga_obj[-1][i].setState("water")
# for i in range(jerooga_obj.blocksHigh):
#     jerooga_obj[i][0].setState("water")
#     jerooga_obj[i][-1].setState("water")



bob = jerooga_obj.addJeroo((1,1), 1)
for i in range(3):
    bob.hop()
bob.turn('r')
bob.hop(2)
bob.toss()



jerooga_obj.allDone() 

