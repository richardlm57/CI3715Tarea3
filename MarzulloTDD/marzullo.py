'''
Created on 27/01/2015

@author: Richard Lares. Carnet: 11-10508
         Patricia Reinoso. Carnet: 11-10851
'''

def marzulloAlg(reservation, start, end):
    
    assert(start < end)
    assert (start >= 600 and start < 1800)
    assert (end > 600 and end <= 1800)
    assert (start % 100 == 0 and end % 100 == 0)
    n = len(reservation)/2
    return [n, reservation[0][0],reservation[1][0]]
    
      
    