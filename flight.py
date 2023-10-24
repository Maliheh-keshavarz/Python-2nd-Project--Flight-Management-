

class Flight:
    """
    A class to to represent different flights.

    ...

    Attributes
    ----------
    flightNumber:int
        A unique identifier for the flight.
    origin:str
        The departure airport 
    destination:str
        The destination airport
    distance:float
        The distance between the origin and destination airports in miles.
    passengers:list
        Each flight stores a list of passengers.

    Methods
    -------
    __init__(self,flightNumber,origin,destination,distance): 
        Initialize each flight with flightNumber,origin,destination,distance.
    addPassenger(self,passenger):
        Method which allows you to add passengers to a flight and call addFlight from Passenger class to update flights list in same time
    setPlane(self,airplane):
        Set a plane to a flight and checking its range before adding it to a flight 
    overBooked(self):
        Allow to calculate overbooking based on the number of passengers 
    isInternational(self):
        Check whether a flight is domestic or international 
    noPassports(self):
        Identify list of passengers without passports
    """

    def __init__(self,flightNumber,origin,destination,distance):
        self.flightNumber= flightNumber
        self.origin= origin
        self.destination= destination
        self.distance= distance
        self.passengers=[]
       
        
    def __str__(self) -> str:
        return (f'flightNumber{self.flightNumber} from {self.origin.code} to {self.destination.code} with distance {self.distance} km.')
    
    def addPassenger(self,passenger):
        self.passengers.append(passenger)
        passenger.addFlight(self)

    def setPlane(self,airplane):
        if airplane.airplanRange >= self.distance:
            self.airplane=airplane
            return True
        else:
            return False
        
    def overBooked(self):
       
        if len(self.passengers)>self.airplane.seats:
            return len(self.passengers) - self.airplane.seats
        else:
            return 0


    def isInternational(self):
        if self.origin.country == self.destination.country:
            return False
        else:
            return True
        

    def noPassports(self):   
        noPassportsList=[]
        for passenger in self.passengers:
            if passenger.passportNumber==0:
                noPassportsList.append(passenger)
        return noPassportsList

        
