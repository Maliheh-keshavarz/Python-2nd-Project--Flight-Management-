
import passenger as pg

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
    __init__(self,flightNumber,origin,destination,distance): Initialize each flight with flightNumber,origin,destination,distance.
    addPassenger:Method of the Flight class, which allows you to add passengers to a flight 
    """

    def __init__(self,flightNumber,origin,destination,distance):
        self.flightNumber= flightNumber
        self.origin= origin
        self.destination= destination
        self.distance= distance
        self.passengers=[]
       
        

    def addPassenger(self,passenger):
        self.passengers.append(passenger)
        passenger.addFlight(self)
        
