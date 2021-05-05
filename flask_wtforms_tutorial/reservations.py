
#list[row][collumn]
seatingChart = [["O","O","O","O"],
                ["O","O","O","O"],
                ["O","O","O","O"],
                ["O","O","O","O"],
                ["O","O","O","O"],
                ["O","O","O","O"],
                ["O","O","O","O"],
                ["O","O","O","O"],
                ["O","O","O","O"],
                ["O","O","O","O"],
                ["O","O","O","O"],
                ["O","O","O","O"]
                ]

#to insert a X into the correct seat we will use this 
# seatingChart.insert([R][C],"X")
def get_cost_matrix():
    cost_matrix = [[100, 75, 50, 100] for row in range(12)]
    return cost_matrix
    

def get_total():
    costChart = get_cost_matrix()
    reservations = open("/project/reservations.txt", "r")
    totalSales = 0
    for cash in reservations:
        line = cash.split(",")
        seat = int(line[2])
        row = int(line[1])
        seatingChart[row][seat] = "X"
               
        if seatingChart[row][seat] == "X":
            sale = costChart[row][seat]
            totalSales += sale
    reservations.close() 
    
    return totalSales
    

def Admin(username, password):
    textFile = open("/project/passcodes.txt", "r")
   
    error = "ERROR: The username/password was incorrect!"
    
    userCode = []
    passCode = []
    for code in textFile:
        line = code.split(',')
        userCode.append(str(line[0]))
        passCode.append(str(line[1]).replace("\n",""))
   

    if username in userCode and password in passCode:
        return None
    else:
        return error
        

def GenerateChart():
    text = open('/project/reservations.txt', 'r')
    seatingChartRevised = []
    for person in text:
        line = person.split(',')
        seat = int(line[2])
        row = int(line[1])
        seatingChart[row][seat] = "X"
    with open('/project/chart.txt', 'w') as writeFile:
        for x in seatingChart:
            writeFile.write(' '.join([str(a) for a in x]) + '\n')
    text.close()
    writeFile.close()

def imageChart():
    chart = open("/project/chart.txt", "r")
    content = chart.read()
    content_split = content.splitlines()
    return content_split

def Reservations(row, seat, rowActual, seatActual):
    ErrorSeatTaken = "Row " + str(rowActual) + " seat " + str(seatActual) + " is already taken, please choose another"
    ErrorNameToLong = "ERROR: Your name is too long."
    #check to see if seat already is taken
    seatTaken = open('/project/reservations.txt', 'r')
    for person in seatTaken:
        line = person.split(',')
        seatz = int(line[2])
        rowz = int(line[1])
        seatingChart[rowz][seatz] = "X"
    seatTaken.close()            
    if seatingChart[int(row)][int(seat)] == "X":
        return ErrorSeatTaken
    else: 
        return None

#This is the function to write to the text file, no error checking here
def ReservationsWrite(firstName, row, seat):
    #Noah and Shawn's development with the ticket
    flight = "INFOTC4320"
    ticket = "".join([firstName[i] + flight[i] for i in range(len(firstName))]) + flight[len(firstName):]

    text = open('/project/reservations.txt', 'a')
    new_seat = "\n" + firstName+", "+row+", "+seat + ", "+ticket
    text.write(new_seat)
    text.close()

def Successful(rowActual, seatActual, firstName):
    flight = "INFOTC4320"
    ticket = "".join([firstName[i] + flight[i] for i in range(len(firstName))]) + flight[len(firstName):]
    success = "Congratulations " + firstName + "! Row " + str(rowActual) + " Seat " + str(seatActual) + " is now reserved for you! Enjoy the Trip! Your e-ticket number is " + ticket
    return success