#Name: Ayush Chanda
#My game: Tic-Tac-Toe
#This game is tic-tac-toe, a game of two players with one player marking 'x' as a character on spaces of a square grid and another player making 'o'.
#The objective of this game is to be the first player to place three marks of 'x's or 'o's in a horizontal, vertical, or a diagonl way. 

#The print statement below displays the insturctions for playing Tic-Tac-Toe. 
print("""Instructions for Tic-Tac-Toe: 
1) Decide which player goes first. The player that goes first plays with the character "x". 
The player that goes second plays with the character "o".

2) In each turn, a player gives the x-coordinate and y-coordinate of the space the player wants to occupy. 
For example if player want to put his or her "x" on the top right corner in that player's turn, 
the player needs to type 0 when asked for the x-value and 2 for the y-value.
This is because the coordinate of where the player wants to occupy the space is (0,2).

3) If a player doesn't know the coordinate of space he or she wants to occupy, the coordinates can be referenced down in the grid below.

4) The first player to connect 3 same characters of "x" or "o" horizontally, vertically, or diagonally, wins the game of Tic-Tac-Toe. 
['(0,0)' , '(0,1)' , '(0,2)']
['(1,0)' , '(1,1)' , '(1,2)']
['(2,0)' , '(2,1)' , '(2,2)']
""")


#The variable 'rows, cols' stores the number of rows and the number of columns to use to make a 2-dimentional list. 
rows, cols = (3, 3)

#The code right below this comment is an an empty list.
arr=[]

# The code below generates a tic-tac-toe baord by making a 2-dimentional list. 
for i in range(rows):
    #For each row out of the total range of rows, a column gets generated.
    col = []
    for j in range(cols):
    #Then there is a for-loop inside the first for-loop. 
    #That second for-loop inside the first one, appends empty space for each column added. 
        col.append(" ")
    print(col)
    arr.append(col)


#This function named processInput below takes the input location of the user to locate on a square where the user wants on the square grid.
#This also checks whether the input locations of the user is valid or invalid.
#In the 'processInput' function, there is a parameter called 'player' that is being passed 
#That parameter called 'player' stores the character 1 or 0 

def processInput(player):
#The location input requires a x-value and a y-value for a user's character to located on the square grid. 
#The location input is proccessed as a coordinate value. 

#This try block tries to convert inputs into integers. 
#If inputs cannot be conveted into integers, an exception is thrown to show that the inputs cannot be taken as integers. 
    try:
        x=int(input("x:"))
        y=int(input("y:"))
    except ValueError:
        print("Input is not a number.")
        return "false"
    
#The user location inputs of x and y are invalid based on those conditions.
#This is because the square grid consists of coordinates ranging from (0,0) to (2,2).
    if (x > 2 or y > 2 or x < 0 or y <0):
        print("Inavlid input. The input is outside of boundary.")
        return "false"
#This function also checks the validity of the inputs by checking if the location input is occupied by a character from previous turns.
    elif  arr[x][y] == 'x' or arr[x][y] == 'o': 
        print("Place already occupied.")
        return "false"
#If the location inputs are not considered invalid, then they must be valid.
#This function locates the user's character on the location where the user wants on the tic-tac-toe grid. 
    else:
        arr[x][y] = player
#The function returns "true" if the input is valid for each turn. 
        return "true"



#Winner Function
#This function determines the winner of this game. 
#The 'winner' function returns 'true' if a player out of the two players or users has won the game of tic-tac-toe. 
def  winner(player):
    #Horizontal 
#This is a for loop of checking whether a player won in a horizontal way of connecting 3 characters in a row. 
    for r in range(len(arr)):
#This works by inspecting each row and checks whether all the sqaure-column characters are marked by the same and one user character.
#The variable 'count' is intialized as zero and counts the number of horizontal characters in a row for each row.
        count = 0
        for c in range(len(arr[r])):
#For the presence of the same user character marked in each column of a row, the count adds up by 1. 
            if arr[r][c] == player:
                count = count + 1
#If the variable 'count' equals to 3, that means the horizontal count of characters in a row is 3 meaning that player won the game by connecting three chcaracters in a row first. 
            if count == 3:
                print("Player "+ str(player)+" has won the game")
                return "true"
    
    #Vertical
#This is a for loop of checking whether a player won in a vertical way of connecting 3 characters in a row in each column. 
    for c in range(len(arr)):
#The variable 'count' is intialized as zero and counts the number of horizontal characters in a row for each column.
        count = 0
        for r in range(len(arr)):
#For the presence of the same user character marked in each square of a column, the count adds up by 1. 
            if arr[r][c] == player:
                count = count + 1
#If b equals to 3, that means the horizontal count of characters in a row is 3 meaning that player won the game by connecting three chcaracters in a row first. 
            if count == 3:
                print(count)
                print("Player "+ str(player)+" has won the game") 
                return "true"
        
    #Diagonal 
#This is a for loop of checking whether a player won in diagonal way of connecting 3 characters in a row. 
    diagonalCount = 0
    r = 0 
    c = 0
# Variables r and c are initialized as 0, and r and c respectively represent the x and y coordintates of the grid. 
#This for-loop starts at 
    for r in range(len(arr)):
        if arr[r][c] == player:
            diagonalCount = diagonalCount + 1
            r = r + 1
            c = c + 1
        if diagonalCount == 3:
            print(diagonalCount)
            print("Player "+ str(player)+" has won the game")
            return "true"
    #AntiDiagonal 
#This is a for loop of checking whether a player won in diagonal way of connecting 3 characters in a row. 
    antiDiagonal = 0
    r = 0 
    c = 2
    for r in range(len(arr)):
        if arr[r][c] == player:
            antiDiagonal = antiDiagonal + 1
            r = r + 1
            c = c - 1
        if antiDiagonal == 3:
            print("Player "+ str(player)+" has won the game")
            return "true"
    #Draw   
    indexOccupied = 0 
    for r in range(len(arr)):
        for c in range(len(arr[r])):
            if arr[r][c] != ' ':
                indexOccupied = indexOccupied+1
    if indexOccupied == 9:
        print("Match ended in a draw")
        return "true"            

print("Lets start the game")



#The variable 'game_over' is initialized as "false".
game_over = "false" 



#This is a while-loop that keeps running until the game is over. 
#When 'game-over' variable equates to 'true', the game stops with a tic-tac-toe winner.
while game_over != "true":
#There are separate if-statement processes for each player. 
#If game_over is not true, two functions processInput(player) and winner(player) run and get called with a different value of the parameter.
    if game_over != "true":
        print("Player x goes. Where do you want to put your 'x'?")
        playerInput1 = processInput("x")
        
        while "false" == playerInput1:
            playerInput1 = processInput("x")
            
        game_over = winner("x")
#Winner("x") returns true when the player with the character "x" won or drew the game. 
#This makes game_over set to true making the game stop.
    print(arr[0])
    print(arr[1])
    print(arr[2])
    
    if game_over != "true":
        print("Player o goes now. Where do you want to put your 'o'?")
        playerInput2 = processInput('o')
    
        while "false" == playerInput2:
            playerInput2 = processInput('o')
            
        game_over = winner('o')
#Winner("o") returns true when the player with the character "o" won or drew the game.
#This makes game_over set to true making the game stop.
    print("")
    print(arr[0])
    print(arr[1])
    print(arr[2])











