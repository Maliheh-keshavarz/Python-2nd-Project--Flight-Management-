'''
Note: Do not modify this file!

Good Luck!
'''

import airport as apt
import airplane as apn
import flight as fl
import passenger as pg


######################################################


print("(1.1)-------------------------------")
Toronto = apt.Airport("YYZ","CAN")
print(Toronto.code)
print(Toronto.country)
				
Ottawa = apt.Airport("YOW","CAN")
Frankfurt = apt.Airport("FRA","GER")
Vancouver = apt.Airport("YVR","CAN")
HongKong = apt.Airport("HKG","HKG")

######################################################	
	
print("(1.2)-------------------------------")	
CRJ700 = apn.Airplane("Bombardier CRJ700",4660,78)
print(CRJ700.airplanType)
print(CRJ700.airplanRange)
print(CRJ700.seats)
		
B787 = apn.Airplane("Boeing 787",14800,290)
A320 = apn.Airplane("Airbus A320",6150,160)
C172 = apn.Airplane("Cessna 172",1289,3)		
		
######################################################

print("(1.3)-------------------------------")
YYZFRA = fl.Flight(872,Toronto,Frankfurt,6343.66)
print(YYZFRA.flightNumber)
print(YYZFRA.origin.code)	
print(YYZFRA.destination.code)	
print(YYZFRA.distance)
print(YYZFRA)

YYZYOW = fl.Flight(446,Toronto,Ottawa,362.08)
HKGYVR = fl.Flight(8,HongKong,Vancouver,10272.73)

######################################################
		
print("(1.4)-------------------------------")
passengers = [pg.Passenger("Susan",111111),pg.Passenger("Tom",222222),pg.Passenger("Alice",0),pg.Passenger("Mike",333333),pg.Passenger("Peter",0)]
print(passengers[0].name)
print(passengers[0].passportNumber)
print(passengers[4].name)
print(passengers[4].passportNumber)

######################################################		
		
print("(2.1)-------------------------------")
for p in passengers: 
    YYZYOW.addPassenger(p)
				
print("First passenger: " + YYZYOW.passengers[0].name)

######################################################
	
print("(2.2)-------------------------------")
print("Passenger list for flight from Toronto to Ottawa:")
passengerList = YYZYOW.passengers

for p in passengerList:
    print(p.name)
		
######################################################
		
print("(3)-------------------------------")		
print("Passenger " + passengers[0].name + "'s first flight is from " + passengers[0].flights[0].origin.code + " to " + passengers[0].flights[0].destination.code + ".")
	
######################################################
		
print("(4.1)-------------------------------")
if (YYZFRA.setPlane(A320)):
    print("A320 added successfully!")
else:
    print("The A320's range is too small. Use a different plane.")			

#####################################################

print("(4.2)-------------------------------")
if (YYZFRA.setPlane(B787)):
    print("787 added successfully!")
else:
    print("The 787's range is too small. Use a different plane.")			

######################################################

print("(5.1)-------------------------------")
YYZYOW.setPlane(C172);
n = YYZYOW.overBooked();
if (n == 0):
    print("Flight from Toronto to Ottawa has space left.")
else:
    print("Flight from Toronto to Ottawa has " , n , " passengers too many.")

######################################################  
		
print("(5.2)-------------------------------");
for p in passengers:
    YYZFRA.addPassenger(p)
n2 = YYZFRA.overBooked();
if n2 == 0:
    print("Flight from Toronto to Frankfurt has space left.")
else:
    print("Flight from Toronto to Frankfurt has " , n2 , " passengers too many.")

######################################################

print("(6.1)-------------------------------")		
if (YYZYOW.isInternational()):
    print("Flight from Toronto to Ottawa is international.")
else:
    print("Flight from Toronto to Ottawa is domestic.")

######################################################

print("(6.2)-------------------------------")
if (YYZFRA.isInternational()):
    print("Flight from Toronto to Frankfurt is international.")
else:
    print("Flight from Toronto to Frankfurt is domestic.")

######################################################		

print("(7)-------------------------------")	
print("Passengers on flight from Toronto to Frankfurt without passport:")
noPassportsList =  YYZFRA.noPassports()
for p in noPassportsList:
    print(p.name)

######################################################
	
print("(8)-------------------------------")			
HKGYVR.addPassenger(passengers[0])
				
print(passengers[0].name + " has " , passengers[0].calculatePoints() , " frequent flyer points.");
		
