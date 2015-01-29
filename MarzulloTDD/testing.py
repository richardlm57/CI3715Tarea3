'''
Created on 27/01/2015

@author:    Richard Lares 11-10508
            Patricia Reinoso 11-10851
'''

import unittest
from marzullo import *

class testMarzullo(unittest.TestCase):
    
    def testMarzulloExists(self):
        parkinglot = ParkingLot([[600,-1],[700,1]]) 
        parkinglot.marzulloAlg(600,800)
        
    def testAddFirstReservation(self):
        parkinglot = ParkingLot([]) 
        self.assertEqual(parkinglot.marzulloAlg(900,1000),[1,900,1000])
    
    def testAddSecondReservation(self):
        parkinglot = ParkingLot([[600,-1],[700,1]]) 
        self.assertEqual(parkinglot.marzulloAlg(900,1000),[1,600,700])
        
    def testOverlapping(self):
        parkinglot = ParkingLot([[700,-1],[1000,1],[900,-1],[1400,1]]) 
        self.assertEqual(parkinglot.marzulloAlg(800,1100),[3,900,1000])
            
    def testStartEqualsEnd(self):
        parkinglot = ParkingLot([[600,-1],[700,1],[900,-1],[1000,1]]) 
        self.assertEqual(parkinglot.marzulloAlg(700,800),[1,600,700])
        
    def testNewReservationInAFullInterval(self):
        parkinglot = ParkingLot([[700,-1],[900,1]]*10) 
        self.assertEqual(parkinglot.marzulloAlg(800,900),[11,800,900]) 
        
    def testNewReservationBetweenTwoFullIntervals(self):
        parkinglot = ParkingLot([[1300,-1],[1500,1],[1700,-1],[1800,1]]*10) 
        self.assertEqual(parkinglot.marzulloAlg(1400,1600),[11,1400,1500]) 
        
    def testNewReservationOutOfAFullInterval(self):
        parkinglot = ParkingLot([[700,-1],[900,1]]*10) 
        self.assertEqual(parkinglot.marzulloAlg(1100,1600),[10,700,900]) 

    
        