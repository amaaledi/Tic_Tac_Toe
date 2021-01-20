import random #importing the random counting module

usrSign = "O" #Declaring the user's sign
progSign = "X" #Declaring the Bot's sign
counter = 0 #This variable is used in DrawMove(board) funtion as a global variable

#The board list is declared here
board = [[ 1 , 2 , 3 ] , [ 4 , 5 , 6 ] , [ 7 , 8 , 9 ]]

#This function will display the board onto the display        
def DisplayBoard(board):
    
    row = 0 
    for i in range(4): # Printing the boardss boarder +--------+---------
        print("+-------" * 3  + "+")
        if i == 3:
            break #will exit the loop when i becomes 3, this will stop printing 
                  #the rest of the code below 
        
        
        for k in range(2): 
            if k == 1: #print the value of each box of the board...ex -: |   3    |
                col = 0
                print("|   " + str(board[row][col]) + "   " , end="")
                col += 1
                print("|   " + str(board[row][col]) + "   " , end="")
                col += 1
                print("|   " + str(board[row][col]) + "   |")
                col += 1
                row += 1

            print("|       " * 3 + "|")          

#This fucntion will go through the board list and store the index values of the 
#board list which does not contain sign of user or bot into a new list
def MakeListOfFreeFields(board):
    freeFields = [] #new list
    for x in range(3):
        for l in range(3):
            if board[x][l] != progSign and board[x][l] != usrSign: #checking whether each value contains signs of user or bot
                pair = x,l #assigning relavant index pairs to a variable
                freeFields.append(pair) #appeniding the pairs to the list as touples
    return freeFields #Returing the new list created


#This function will act as the bot by drawing moves
def DrawMove(board):
    global counter
    
    #This is the first draw by the bot and will only happens once
    if counter == 0:
        board[1][1] = progSign #bot's sign will be drawn in this 
        counter += 1
        VictoryFor(board , progSign) #This will call the game status checking function
        
        
    else: #after above if happened, everytime when this function is invoked, this else will always happen
        found = False # this variable controls the while loop and has an initial state of false
        freeFields1 = MakeListOfFreeFields(board) #the new list of free fileds will be assigned to this list
        

        #untill the random number gets equal with the lists values, the loop will continue
        while found == False:
            randNumb = random.randrange(1,10) #a random number between 1 and 9 will be assigned.
            for x in range(len(freeFields1)):#this will loop through the freeFields1 list
                for i in range(2):
                    if i == 0: #this will skip the 'if' part of the first value in every touple inside the list
                        field1 = freeFields1[x][i]
                        continue
                    
                    field2 = freeFields1[x][i]

                    if board[field1][field2] == randNumb:
                        board[field1][field2] = progSign
                        found = True #if the random number was found this controlling variable will be set to true
                        break #this will exit the inner loop
                        
                    else:
                        found = False
                        
                if found == True:
                    break #this will exit the outer loop
            
        VictoryFor(board , progSign)


#This function is used to get the useres input fot their move
#this fucntion has the same algorithm as DrawMove(board) function
def EnterMove(board):

    freeField = MakeListOfFreeFields(board)
    usrFound = False
    

    while usrFound == False:
        usrMove = int(input("Enter Your Move : ")) #this will get an integer input from the user
        for x in range(len(freeField)):
            for i in range(2):
                if i == 0 :
                    field1 = freeField[x][i]
                    continue
                
                field2 = freeField[x][i]
                if board[field1][field2] == usrMove:
                    board[field1][field2] = usrSign
                    usrFound = True
                    break
                    
                else:
                    usrFound = False
            
            if usrFound == True:
                break
    VictoryFor(board , usrSign)

#This function will decide the status of the game(Won,Tied,Continue)
def VictoryFor(board, sign):
    #will check each elemnt in the board list
    if board[0][0] == sign and board[0][1] == sign and board[0][2] == sign:
        if sign == progSign:
            DisplayBoard(board)
            print("BOT Won!")
        else:
            DisplayBoard(board)
            print("You Won!")

    elif board[1][0] == sign and board[1][1] == sign and board[1][2] == sign:
        if sign == progSign:
            DisplayBoard(board)
            print("BOT Won!")
        else:
            DisplayBoard(board)
            print("You Won!")

    elif board[2][0] == sign and board[2][1] == sign and board[2][2] == sign:
        if sign == progSign:
            DisplayBoard(board)
            print("BOT Won!")
        else:
            DisplayBoard(board)
            print("You Won!")

    elif board[0][0] == sign and board[1][0] == sign and board[2][0] == sign:
        if sign == progSign:
            DisplayBoard(board)
            print("BOT Won!")
        else:
            DisplayBoard(board)
            print("You Won!")

    elif board[0][1] == sign and board[1][1] == sign and board[2][1] == sign:
        if sign == progSign:
            DisplayBoard(board)
            print("BOT Won!")
        else:
            DisplayBoard(board)
            print("You Won!")

    elif board[0][2] == sign and board[1][2] == sign and board[2][2] == sign:
        if sign == progSign:
            DisplayBoard(board)
            print("BOT Won!")
        else:
            DisplayBoard(board)
            print("You Won!")

    elif board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        if sign == progSign:
            DisplayBoard(board)
            print("BOT Won!")
        else:
            DisplayBoard(board)
            print("You Won!")

    elif board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        if sign == progSign:
            DisplayBoard(board)
            print("BOT Won!")
        else:
            DisplayBoard(board)
            print("You Won!")

    elif len(MakeListOfFreeFields(board)) == 0:
        DisplayBoard(board)
        print("Match Tied!")

    else:
        if sign == usrSign:
            DrawMove(board)
            
        else:
            DisplayBoard(board)
            EnterMove(board)
        

#This is the first function that will be invoked in the program
#Starting Function
DrawMove(board)



            
            
