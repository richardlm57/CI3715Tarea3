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
        
    def testOneInterval(self):
        self.assertEqual(marzulloAlg([[600,-1],[700,1]],600,800),[1,600,700])
        
    
    