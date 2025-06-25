
class Solution(object):
    def canVisitAllRooms(self, rooms):
        visit = set()
        stack = [0]
        while stack:
            room = stack.pop()
            if room not in visit:
                visit.add(room)
                for key in rooms[room]:
                            if key not in visit:
                                stack.append(key)
                return len(visit) == len(rooms)
            

