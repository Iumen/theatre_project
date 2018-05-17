# Function Definitions

def displayMenu():
    print('\n')
    print("- (D)isplay a seating chart")
    print("- (S)ell one or more tickets")
    print("- (P)resent statistics")
    print("- (R)eset program")

def displaySeatingChart(rows, columns, theatre = []):

    #print top line
    print("       ", end = "")
    print("0", end = "")
    for a in range(1,columns):
        if (a + 1) % 10 == 0:
            num = (a + 1) / 10
            num = int(num)
            print(num, end = "")
        else:
            print(" ", end = "")

    #print second to top line
    print('') #newline
    i = 1
    tempColumns = columns
    print("       ", end = "")
    while tempColumns > 0:
        print(i, end = "")
        if i == 9:
            i = 0
            tempColumns -= 1
            continue
        i += 1
        tempColumns -= 1

    #print seats
    print('') #newline
    for row in range(0,rows):
        tempString = ""
        for col in range(0,columns):
            tempString += theatre[row][col]
        print("Row",row," ",end = "")
        print(tempString)

def sellTickets(theatre = [], rowPrices = []):
    seats = input("How many seats are being sold: ")
    seats = int(seats)
    cost = 0
    for seat in range(0,seats): 
        print("Enter row and column of seat being sold: ")
        row = input("Row #")
        col = input("Column #")
        row = int(row) - 1
        col = int(col) - 1
        if theatre[row][col] == 'O':
            print("Seats already taken. Please enter tickets again.")
            break
        theatre[row][col] = 'O'
        cost += rowPrices[row]
    print("Total cost is $",cost)
    return theatre

def presentStats(theatre = [], rowPrices = []):
    ticketsSold = 0
    ticketsLeft = 0
    ticketRevenue = 0
    
    for i in range(0,rows):
        for j in range(0,columns):
            if theatre[i][j] == 'O':
                ticketsSold += 1
                ticketRevenue += rowPrices[i]
    ticketsLeft = (rows * columns) - ticketsSold
    print(ticketsSold, "tickets sold")
    print(ticketsLeft, "tickets left")
    print("$", ticketRevenue, "in revenue")
    
##################################################################
# Main Program

menuFlag = True
resetFlag = True
falseInput = True
MAX_LIST_SIZE = 100



while resetFlag == True:
    menuFlag = True
    falseInput = True
    answer = input("Would you like to you use the old layout? (y or n): ")
    if answer == 'y':
        with open("theatre.txt", "r") as f:
            rows = f.readline()
            columns = f.readline(2)
    if answer == 'n':
        while falseInput == True:
            rows = input("How many rows: ")
            columns = input("How many columns: ")
            if int(rows) > MAX_LIST_SIZE or int(columns) > MAX_LIST_SIZE:
                print("Input is too large. Rows and columns must be under", MAX_LIST_SIZE)
                continue
            else:
                f = open("theatre.txt", "w")
                f.write(rows)
                f.write('\n')
                f.write(columns)
                f.close()
                falseInput = False
    rows = int(rows)
    columns = int(columns)
            
    rowPrices = []
    for row in range(0,rows):
        print("Input price of row",row + 1,":")
        rowPrices.append(input("$"))
    for i in range(0,rows):
        rowPrices[i] = int(rowPrices[i])

    theatre = []
    theatreRow = []
    for row in range(0,columns):
        theatreRow.append('X')
    for seats in range(0,rows):
        theatre.append(theatreRow[:])

    while menuFlag == True:    
        displayMenu()
        userInput = input("What would you like to do: ")

        if userInput == 'D':
            displaySeatingChart(rows, columns, theatre)
        elif userInput == 'S':
            theatre = sellTickets(theatre, rowPrices)
        elif userInput == 'P':
            presentStats(theatre, rowPrices)
        elif userInput == 'R':
            menuFlag = False
        else:
            print("Invalid input")
    
