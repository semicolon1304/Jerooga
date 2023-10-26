from Jerooga import Jerooga
jerooga_obj = Jerooga()

for y in range(1,jerooga_obj.blocksHigh-1):
    for x in range (1,jerooga_obj.blocksWide-1):
        jerooga_obj.board[y][x].setState("land")

jerooga_obj

jerooga_obj.updateWindow()
input("Enter To continue")
