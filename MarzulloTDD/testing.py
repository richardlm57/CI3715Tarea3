'''
Created on 27/01/2015

@author:    Richard Lares 11-10508
            Patricia Reinoso 11-10851
'''

import unittest
from marzullo import *

class testMarzullo(unittest.TestCase):
    
    def testMarzulloExists(self):
        marzulloAlg([[600,-1],[700,1]],600,800)
        
    def testAddFirstReservation(self):
        self.assertEqual(marzulloAlg([],900,1000),[1,900,1000])
    
    def testAddSecondReservation(self):
        self.assertEqual(marzulloAlg([[600,-1],[700,1]],900,1000),[1,600,700])
        
    def testOverlapping(self):
        self.assertEqual(marzulloAlg([[700,-1],[1000,1],[900,-1],[1400,1]],800,1100),[3,900,1000])
            
    def testStartEqualsEnd(self):
        self.assertEqual(marzulloAlg([[600,-1],[700,1],[900,-1],[1000,1]],700,800),[1,600,700])
    
    def testNoSpaceInParkingLot(self):
        self.assertEqual(marzulloAlg([[700,-1],[900,1]]*10,800,900),[11,800,900])    
    
    