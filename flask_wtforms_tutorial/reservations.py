
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
def Admin(username, password):
    textFile = open("/project/passcodes.txt", "r")

    userCode = []
    passCode = []
    for code in textFile:
        line = code.split
        userCode.append(line[0])
        passCode.append(line[1])
        
        

def GenerateChart():
    text = open('/project/reservations.txt', 'r')
    seatingChartRevised = []
    for person in text:
        line = person.split(',')
        seat = int(line[1])
        row = int(line[2])
        seatingChart[seat][row] = "X"
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

def Reservations(row, seat):
    rowActual = int(row) + int(1)
    seatActual = int(seat) + int(1)
    ErrorSeatTaken = "ERROR: row " + str(seatActual) + " seat " + str(rowActual) + " is already taken, please choose another"
    ErrorNameToLong = "ERROR: Your name is to long"
    #check to see if seat already is taken
    seatTaken = open('/project/reservations.txt', 'r')
    for person in seatTaken:
        line = person.split(',')
        seat = int(line[1])
        row = int(line[2])
    seatTaken.close()            
    if seatingChart[seat][row] == "X":
        return ErrorSeatTaken
    else: 
        return None

#This is the function to write to the text file, no error checking here
def ReservationsTest(firstName, row, seat):
    #Noah and Shawn's development with the ticket
    flight = "INFOTC4320"
    ticket = "".join([firstName[i] + flight[i] for i in range(len(firstName))]) + flight[len(firstName):]

    text = open('/project/reservations.txt', 'a')
    new_seat = "\n" + firstName+", "+row+", "+seat + ", "+ticket
    text.write(new_seat)
    text.close()