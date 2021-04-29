
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
    for x in seatingChart:
        seatingChartRevised = x
    text.close()
    return seatingChart


def Reservations(firstName, row, seat):
    ErrorSeatTaken = "ERROR: This seat is already taken choose another"
    ErrorNameToLong = "ERROR: Your name is to long"
    text = open('/project/reservations.txt', 'a')
    name = firstName
    flight = "INFOTC4320"
    #check to see if seat already is taken
    seatTaken = open('/project/reservations.txt', 'r')
    for person in seatTaken:
        line = person.split(',')
        seat = int(line[1])
        row = int(line[2])
        seatingChart[seat][row] = "X"
    seatTaken.close()
    if seatingChart[seat][row] != "X":
    #if not append the name to the file and generate ticket and re-gen the chart
        if len(name) >= len(flight):
            return ErrorNameToLong
        else:
            ticket = "".join([name[i] + flight[i] for i in range(len(name))]) + flight[len(name):]
            #new_seat = firstName+", "+row+", "+seat+", "+ticket
            #text.write(new_seat)
            GenerateChart()
            
    else:
        return ErrorSeatTaken

    text.write(firstName + ", " + str(seat) + ", " + str(row) + ", " + ticket)
    text.close()
    return None