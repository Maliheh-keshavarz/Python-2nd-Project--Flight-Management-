OOP programming; Flight Management:


1) You need to develop a flight management system for an airline. Each flight is characterized by its flight number, origin airport, destination airport, and distance. Airports are characterized by their three-letter airport code and country code. Airplanes have a type name, range in km, and number of seats. Passengers have a name and integer passport number.
2) Each flight stores a list of passengers.
3) Passengers store a list of flights they are taking. When a passenger is added to a flight, this flight also needs to be added to the list of flights stored by the passenger.
4) Each flight has an airplane type. Before a plane is added, the method needs to check whether the plane’s range is sufficiently large for the flight distance. If successful, the method needs to return true. If unsuccessful, it needs to return false.
5) A method is needed to determine whether the flight is overbooked i.e. it checks whether there are more passengers on the flight than seats on the plane. If the number of passengers is larger than the number of seats, the method needs to return by how many passengers the flight is overbooked. If not, the method needs to return zero