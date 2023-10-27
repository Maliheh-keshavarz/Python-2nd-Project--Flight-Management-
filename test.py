

import unittest
from FlightTester import *
from flight import Flight
from passenger import Passenger
from airport import *
from airplane import *




class TestFlight(unittest.TestCase):


    def test_str(self):

        # flight = Flight('872','YYZ','FRA', 6343.66)
        expectedOutput = 'Flight number 872 from YYZ to FRA with distance 6343.66km.'
        # self.assertEqual(str(flight), expectedOutput,'Failed: Flight __str__ method')
        self.assertEqual(str(YYZFRA), expectedOutput,'Failed: Flight __str__ method')
    
       

    def testaddPassenger(self):
    
        flight =  Flight(446,'Toronto','Ottawa',362.08)
        passenger = Passenger("Susan", 111111)
        flight.addPassenger(passenger)
        self.assertEqual(flight.passengers[0], passenger,"Failed")
       
       

        
    def testsetPlane(self):
       
        self.assertFalse(YYZFRA.setPlane(A320),'def setPlane should return false')
        self.assertTrue(YYZFRA.setPlane(B787),'def setPlane should return true')



    def testoverBooked(self):

        YYZYOW.setPlane(C172)
        n = YYZYOW.overBooked();
      
        self.assertEqual(n,2,'overbooked')


    def testisInternational(self):
        
       
        domesticFlight = YYZYOW.isInternational()
        internationalFlight = YYZFRA.isInternational()
        self.assertFalse(domesticFlight)
        self.assertTrue(internationalFlight)

    

    def testnoPassports(self):
        noPassportsList =  YYZFRA.noPassports()
        expected_names = ["Alice", "Peter"]
        for i in range(len(expected_names)):
            self.assertEqual(noPassportsList[i].name, expected_names[i])
        self.assertEqual(len(noPassportsList), len(expected_names))


        # for i, name in enumerate(expected_names):
        #     self.assertEqual(noPassportsList[i].name, name)
        
        
        

class TestPassenger(unittest.TestCase):
   
    def testcalculatePoints(self):
        # passenger = Passenger("Susan", 111111)
        # points = passenger.calculatePoints()
        # self.assertEqual(points, 7,'should be 7')

        points=passengers[0].calculatePoints()
        self.assertEqual(points, 7,'should be 7')


if __name__ == '__main__':
    unittest.main()