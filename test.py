

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
        condition=YYZFRA.setPlane(A320)
        self.assertFalse(condition,'def setPlane should return false')



    def testoverBooked(self):

        YYZYOW.setPlane(C172)
        n = YYZYOW.overBooked();
      
        self.assertEqual(n,2,'overbooked')


    def testisInternational(self):
        condition=YYZFRA.isInternational()
        self.assertTrue(condition,'isInternational method should return true')

    

    def testnoPassports(self):
        noPassportsList =  YYZFRA.noPassports()
        self.assertIsInstance(noPassportsList,list,'should be list')



class TestPassenger(unittest.TestCase):
   
    def testcalculatePoints(self):
        # passenger = Passenger("Susan", 111111)
        # points = passenger.calculatePoints()
        # self.assertEqual(points, 7,'should be 7')

        points=passengers[0].calculatePoints()
        self.assertEqual(points, 7,'should be 7')


if __name__ == '__main__':
    unittest.main()