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
    temp=reservation[:]
    temp.append([start,-1])
    temp.append([end,1])
    temp.sort()
    best,count,i=0,0,0
    while i<len(temp):
        count-=temp[i][1]
        if count>best:
            best,beststart,bestend=count,temp[i][0],temp[i+1][0]
    return [best,beststart,bestend]
    
      
    