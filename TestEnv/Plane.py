import random
# define what an airline will have
class Customer:

    def __init__(self, firstname="blank", lastname="blank"):
        self.name = firstname + " " + lastname
        self.name = " ".join(self.name.strip().split())
        self.firstname = firstname
        self.lastname = lastname
        number = '{:04d}'.format(random.randint(0, 9999))
        self.custID = self.firstname[0:3] + self.lastname[0:3] + number

    # creating a customer
    def create_customer(self):
        number = '{:04d}'.format(random.randint(0, 9999))
        self.custID = self.firstName[0:3] + self.lastName[0:3] + number

    def printName(self):
        print(self.name)


# define what a seat contains, which is a seat number, a reservation for that
# seat, as well as the customer who is in the seat
class Seat:
    def __init__(self, num, reservation):
        self.num = num
        self.reservation = reservation
        self.customer = Customer()

    # updates just the reservation
    def updateRes(self, updReservation):
        self.reservation = updReservation

    # update just the Customer
    def updateCustomer(self, updCustomer):
        self.customer = updCustomer

    # resderve seat
    def updateSeat(self, updCustomer, updReservation):
        self.customer = updCustomer
        self.reservation = updReservation


# define a flight, a flight will contain the time of departure, where it is
# departing from, the time it will arrive, the arrival destination, all flights
# all flights have a name and are able to seat 50 customers
class Flight:
    def __init__(self, AFname):
        self.timeofDep = ""
        self.timeOfArr = ""
        self.depDes = ""
        self.arrDes = ""
        self.AFname = AFname
        self.seats = []

    # initialize seats
    def initialzeSeats(self):
        for x in range(50):
            self.seats.append(Seat(x, 'xxxxxxxx'))

    # update arrival destination, departure time, arrival time,
    # and departing destination
    def changeDest(self, depr, arr, origin, dest):
        self.timeofDep = depr
        self.timeOfArr = arr
        self.depDes = origin
        self.arrDes = dest

    # print destination info
    def printFlightInfo(self):
        print(self.timeofDep + self.timeofArr + self.depDes + self.arrDes)

    # create a reservation and add customer to the specified seat on the flight
    def create_reservation(self, seatNum, customerToAdd=Customer()):
        newReservation = self.depDes[0:2] + self.arrDest[0:2] + customerToAdd.custID[0:4]
        self.seats[seatNum].updateSeat(customerToAdd, newReservation)

    # delete a reservation from a flight
    def del_reservation(self, reservation):
        found = 'FALSE'
        for x in len(self.seats):
            if self.seats[x] == reservation:
                blank = Customer()
                self.seats[x].updateSeat(blank, 'xxxxxxxx')
                found = 'TRUE'
                print("Reservation has been made on flight: " + self.AFname)
                break
        # if reservation could not be found print a statement
        if found == 'FALSE':
            print(reservation + " could not be found on flight: " + self.AFname)

    # search for reservation
    def searchRes(self, reservation):
        found = 'FALSE'
        for x in len(self.seats):
            if self.seats[x] == reservation:
                found = 'TRUE'
                print("Reservation is on flight: " + self.AFname)
                print(reservation + ' is on seat ' + '{:02d}'.format(x))
                self.printFlightInfo()
                break
        # if reservation could not be found print a statement
        if found == 'FALSE':
            print(reservation + " could not be found on flight: " + self.AFname)

    # search for reservation but print once
    def searchResone(self, reservation):
        for x in len(self.seats):
            if self.seats[x] == reservation:
                print("Reservation is on flight: " + self.AFname)
                print(reservation + ' is on seat ' + '{:02d}'.format(x))
                self.printFlightInfo()
    # print seat number along with reservation to the seat
    def printSeats(self):
        for x in range(50):
            print('\t' + '{:02d}'.format(self.seats[x].num) + " " + self.seats[x].reservation)

    # print name of flight and seats
    def printFS(self):
        print(self.AFname)
        self.printSeats()


# An airline contains the name of the airline along with a number of flights
# in the airline. The default of the number flights in a airline is 10
class Airline:

    def __init__(self, name):
        self.name = name
        self.flights = []

    # initialize flights
    def initializeFlights(self):
        for x in range(10):
            self.flights.append(Flight(self.name[0:2]+'{:02d}'.format(x)))
            self.flights[x].initialzeSeats()

    # add a new flight to the airline and initilize the seats all follow the same
    # naming convention for simplicity sake
    def createNewFlight(self):
        newFlight = Flight(self.name[0:2]+'{:02d}'.format(len(self.flights)+1))
        self.flights.append(newFlight)
        self.flights[len(self.flights)].initializeSeats()

    # search flights by arriving destination
    def searchDest(self, destination):
        found = 'FALSE'
        for x in range(len(self.flights)):
            if destination == self.flights[x].arrDes:
                self.flights[x].printFlightInfo
                found = 'TRUE'
        if found == 'FALSE':
            print("There are no flights going to " + destination)

    # search flights by departing city
    def searchDept(self, departing):
        found = 'FALSE'
        for x in range(len(self.flights)):
            if departing == self.flights[x].depDes:
                self.flights[x].printFlightInfo
                found = 'TRUE'
        if found == 'FALSE':
            print("There are no flights leaving " + departing)

    # search reservation with error print satements
    def searchRes(self, reservation):
        for x in range(len(self.flights)):
            self.flights[x].searchRes(reservation)

    # search reservation with only found print statement
    def searchResone(self, reservation):
        for x in range(len(self.flights)):
            self.flights[x].searchResone(reservation)

    # search for a flight and return the index of that flight
    def searchForFlight(self, flightName):
        for x in range(len(self.flights)):
            if flightName == self.flights[x].AFname:
                return x
        print("INVALID NAME FLIGHT COULD NOT BE FOUND")

    # adding a customer to the first available seat on a specific flight
    def add_to_flightAuto(self, customer, flightNum):
        # check to see for availability
        seatAvail = 'TRUE'
        seatNum = 0
        for x in range(self.flights[flightNum].seats):
            if self.flights[flightNum].seat[x] != 'xxxxxxxx':
                seatNum = x
                break
            else:
                seatAvail = 'FALSE'
        if seatAvail == 'TRUE':
            self.flights[flightNum].create_reservation(seatNum, customer)
        elif seatAvail == 'FALSE':
            print("There is no availability for flight " + self.flights[flightNum].AFname)
        else:
            print("ERROR: SOMETHING WENT WRONG")

    # print available seats
    def checkAvail(self, flightNum):
        for x in range(self.flights[flightNum].seats):
            if self.flights[flightNum].seat[x] == 'xxxxxxxx':
                print(self.flights[flightNum].seat[x].num)

    # add customer to a specific seat on a specific flight
    def addToSeat(self, flightNum, seatNum, customer=Customer()):
        self.flights[flightNum].create_reservation(seatNum, customer)

    # print the name of all the flights on a airline
    def printAllFlights(self):
        for x in range(len(self.flights)):
            print(self.flights[x].AFname)

    # print all flight names and the seats along with the reservation on each
    # flight in a airline
    def printAllFS(self):
        for x in range(len(self.flights)):
            self.flights[x].printFS()


class Airport:

    # create initial flights to airport and initialze seats in flights
    def initializeAirport(self):
        self.airlines = [Airline("BLUE"), Airline("RED"), Airline("YELLOW"), Airline("GREEN"), Airline("PURPLE")]
        for x in range(len(self.airlines)):
            self.airlines[x].initializeFlights()

    # adding a new airline to the airport
    def addNewAL(self, nameOfAL):
        self.airlines.append(Airline(nameOfAL))
        self.airlines[len(self.airlines)].initializeFlights()

    # search for airline and return index of airline
    def searchAL(self, name):
        for x in range(len(self.airlines)):
            if self.airlines[x].name == name:
                return x
        print("Airline " + name + " does not exist")

    # search for reservation with just resvation
    def searchRes(self, reservation):
        for x in range(len(self.airlines)):
            self.airlines[x].searchResone(reservation)

    # add Customer to seat
    def addCustToSeat(self, ALName, flightName, seatnum, customer):
        alNum = self.searchAL(ALName)
        if isinstance(alNum, int):
            flightnum = self.airlines[alNum].searchForFlight(flightName)
            if isinstance(flightnum, int):
                self.airlines[alNum].flights[flightnum].create_reservation(seatnum, customer)

    # print specific flight print info
    def printFlightInfo(self, name):
        flightIndex = 'FALSE'
        for x in range(len(self.airlines)):
            flightIndex = self.airlines[x].searchForFlight(name)
            if isinstance(flightIndex, int):
                self.airlines[x].flights[flightIndex].printFlightInfo()
                break

    # print all flights in airport
    def printFlights(self):
        for x in range(len(self.airlines)):
            self.airlines[x].printAllFlights()

    # print all flights in airport along with seats info
    def printAll(self):
        for x in range(len(self.airlines)):
            self.airlines[x].printAllFS()


SkyAir = Airport()
SkyAir.initializeAirport()
