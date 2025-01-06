class Solution(object):
    def minMovesToSeat(self, seats, students):
        seats.sort()
        studens.sort()
        
        count = 0
        
        for i in range(len(seats)):
            count += abs(seats[i]-studens[i])
    
        return count   