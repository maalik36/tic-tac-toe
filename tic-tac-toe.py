#print("X O X")
#print("O X O")
#print("X X O")
string = "_________"
player = "X"
game = True
grid = [["1 1", string[0]], ["1 2", string[1]], ["1 3", string[2]], ["2 1", string[3]], ["2 2", string[4]], ["2 3", string[5]], ["3 1", string[6]], ["3 2", string[7]], ["3 3", string[8]]]
list = [grid[0][1] + grid[1][1] + grid[2][1], grid[3][1] + grid[4][1] + grid[5][1], grid[6][1] + grid[7][1] + grid[8][1], grid[0][1] + grid[3][1] + grid[6][1], grid[1][1] + grid[4][1] + grid[7][1], grid[2][1] + grid[5][1] + grid[8][1], grid[0][1] + grid[4][1] + grid[8][1], grid[2][1] + grid[4][1] + grid[6][1]]

print("---------")
print("| " + string[0], string[1], string[2] + " |")
print("| " + string[3], string[4], string[5] + " |")
print("| " + string[6], string[7], string[8] + " |")
print("---------")
while game == True:    
    correct = False
    while correct == False:
        count = 0
        coordinates = input()
        if coordinates.isdigit() == True:
            print("You should enter numbers!")
            continue
        numbers = coordinates.split(" ")
        if int(numbers[0]) >= 4 or int(numbers[1]) >= 4:
            print("Coordinates should be from 1 to 3!")
            continue
        for item in grid:
            if coordinates == grid[count][0]:
                break
            count += 1
        if grid[count][1] == "X" or grid[count][1] == "O":
            print("This cell is occupied! Choose another one!")
            continue
        correct = True
    space = 0
    for item in grid:
        if coordinates == grid[space][0]:
            grid[space][1] = player
            if player == "X":
                player = "O"
            elif player == "O":
                player = "X"
            break
        space += 1
    print("---------")
    print("| " + grid[0][1], grid[1][1], grid[2][1] + " |")
    print("| " + grid[3][1], grid[4][1], grid[5][1] + " |")
    print("| " + grid[6][1], grid[7][1], grid[8][1] + " |")
    print("---------")
    print(list[7])
    string = string.replace("_", "A", 1)
    print(string)
    list = [grid[0][1] + grid[1][1] + grid[2][1], grid[3][1] + grid[4][1] + grid[5][1], grid[6][1] + grid[7][1] + grid[8][1], grid[0][1] + grid[3][1] + grid[6][1], grid[1][1] + grid[4][1] + grid[7][1], grid[2][1] + grid[5][1] + grid[8][1], grid[0][1] + grid[4][1] + grid[8][1], grid[2][1] + grid[4][1] + grid[6][1]] 
#if "XXX" in list and "OOO" in list or abs(string.count("X") - string.count("O")) >= 2:
#    print("Impossible")
#elif '_' in string and "XXX" not in list and "OOO" not in list:
#    print("Game not finished")
    if "XXX" not in list and "OOO" not in list and "_" not in string:
        print("Draw")
        break
    elif "XXX" in list and "OOO" not in list:
        print("X wins")
        break
    elif "XXX" not in list and "OOO" in list:
        print("O wins")
        break