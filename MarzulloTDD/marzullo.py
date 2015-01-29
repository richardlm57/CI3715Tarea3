'''
Created on 27/01/2015

@author: Richard Lares. Carnet: 11-10508
         Patricia Reinoso. Carnet: 11-10851
'''
from operator import itemgetter

class ParkingLot():
    
    def __init__(self,reservation):
        self._reservation = reservation
        self._maxspots = 10

    def marzulloAlg(self, start, end):    
        
        assert(start < end)
        assert (start >= 600 and start < 1800)
        assert (end > 600 and end <= 1800)
        assert (start % 100 == 0 and end % 100 == 0)
        
        temp= self._reservation[:]
        temp.append([start,-1])
        temp.append([end,1])
        temp = sorted(temp, key = itemgetter(1), reverse = True)
        temp = sorted(temp, key = itemgetter(0))
        best,count,i=0,0,0
        
        while i<len(temp):
            count-=temp[i][1]
            if count>best:
                best,beststart,bestend=count,temp[i][0],temp[i+1][0]
            i+=1
    
        return [best,beststart,bestend]   
    