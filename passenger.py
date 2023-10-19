


class Passenger:
    """
    A class to represent passengers  .

    ...

    Attributes
    ----------
    name:str
        name of the passenger 
    passportNumber:int
        passport number of the passenger   
    flights:list 
        list of flights of each passenger to keep track
    Methods
    -------
    __init__(self,name,passportNumber):
        initialize passengers with a name and passport number. 
    addFlight(self, flight): 
        Add a flight to the passenger's list of flights.
    calculatePoints(self):
        Calculate frequent flyer points, by consider the type of flight (domestic or international) 
    
    """

    def __init__(self,name,passportNumber):
        self.name= name
        self.passportNumber= passportNumber
        self.flights=[]
        
    def addFlight(self,flight):
        self.flights.append(flight)

    def calculatePoints(self):
        PassengerPoints=0
        for flight in self.flights:
            if flight.isInternational():
                PassengerPoints+=3
            else:
                PassengerPoints+=1
        return PassengerPoints





   

		