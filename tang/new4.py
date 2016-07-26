ttt = [0 for i in range(9)]
lines = [[0, 1, 2],[3, 4, 5],[6, 7, 8],[0, 3, 6],[1, 4, 7],[2, 5, 8],[0, 4, 8],[2, 4, 6]]
lineValues = [0 for i in range(8)]
userChar = {1: "O", -1: "X", 0: "_"}
turn = -1 # defalut to user move first

#*****************************************************
def main():
    global userChar, turn
    if input("Do you want me to start first? (Y/N)").lower()=="y":
        userChar = {1:"X",-1:"O",0:"_"}
        turn = 1
    display()
    while not hasWinner():
        if 0 in ttt:
            nextMove(turn)
            turn *= -1
            display()
        else:
            print("It's a tie!")
            break


turn = "X"
map = [[" "," "," "],
       [" "," "," "],
       [" "," "," "]]
done = False


def check_done():
    pass


while done != True:
    print_board()

    print turn, "'s turn"
    print

    moved = False
    while moved != True:
        print "Please select position by typing in a number between 1 and 9, see below for which number that is which position..."
        print "7|8|9"
        print "4|5|6"
        print "1|2|3"

try:
    pos = input("Select: ")
    if pos <= 9 and pos >= 1:
        Y = pos / 3
        X = pos % 3
        if X != 0:
            X -= 1






