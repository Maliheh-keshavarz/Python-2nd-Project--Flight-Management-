
class Airport:
    """
    A class to sets up the airports and initializes them with their codes and countries  .

    ...

    Attributes
    ----------
    Name: of the airport
    List of flights departing from the airport
    List of airplanes available at the airport

    Methods
    -------
    __init__(self, name): Initialize the airport with a name.
    add_flight(self, flight): Add a flight to the list of flights.
    remove_flight(self, flight): Remove a flight from the list of flights.
    add_airplane(self, airplane): Add an airplane to the list of airplanes.
    remove_airplane(self, airplane): Remove an airplane from the list of airplanes.
    get_flights(self): Return the list of flights.
    get_airplanes(self): Return the list of airplanes.
    """

    def __init__(self,code,country):
        self.code= code
        self.country= country

 


