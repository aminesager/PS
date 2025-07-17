def distance(x1,x2,y1,y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2)**0.5


def countPoints(self, points, queries):
        """
        :type points: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        result = []
        for query in queries:
            i=0 
            for point in points:
                if distance(point[0], query[0], point[1], query[1]) <= query[2]:
                    i+= 1
            result.append(i)
                
        return result
    
points = [[1,3],[3,3],[5,3],[2,2]]
queries = [[2,3,1],[4,3,1],[1,1,2]]

print(countPoints(None, points, queries))  
                