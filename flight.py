


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

    Methods
    -------
    __init__(self,flightNumber,origin,destination,distance): Initialize each flight with flightNumber,origin,destination,distance.
    
    """

    def __init__(self,flightNumber,origin,destination,distance):
        self.flightNumber= flightNumber
        self.origin= origin
        self.destination= destination
        self.distance= distance
    
   