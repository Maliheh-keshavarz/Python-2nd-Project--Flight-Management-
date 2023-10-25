

import unittest
from flight import Flight
from passenger import Passenger




class TestFlight(unittest.TestCase):


    def teststr(self):

        flight = Flight('872','YYZ','FRA', 6343.66)
        expectedOutput = 'Flight number 872 from YYZ to FRA with distance 6343.66km.'
        self.assertEqual(str(flight), expectedOutput,'failed step')
       

    def testaddPassenger(self):
        pass
        
    def testsetPlane(self):
        pass



    def testoverBooked(self):
        pass


    def testisInternational(self):
        pass

    def testnoPassports(self):
        pass



class TestPassenger(unittest.TestCase):
    def testaddFlight(self):
        pass


    def testcalculatePoints(self):
        pass




if __name__ == '__main__':
    unittest.main()