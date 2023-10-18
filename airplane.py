
class Airplane:
    """
    A class to represent different types of airplanes.

    ...

    Attributes
    ----------
    airplanType:str
        The type or model of the airplane.
    airplanRange:int
        The maximum range of the airplane in miles.
    seats:int
        The maximum passenger capacity of the airplane.
            

    Methods
    -------
    __init__(self,airplanType,airplanRange,seats): Initialize the airplane with airplanType,airplanRange and seats.
    
    """

    def __init__(self,airplanType,airplanRange,seats):
        self.airplanType= airplanType
        self.airplanRange= airplanRange
        self.seats= seats

		
