"""
find the k closest to origin points in a list
leetcode url: https://leetcode.com/problems/k-closest-points-to-origin/
"""

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def _calculate_distance(point: List[int]) -> int:
            return math.sqrt((point[0]) ** 2 + (point[1]) ** 2)
        
        distances = []
        distance_to_index = {}
        
        for i, item in enumerate(points):
            distance = _calculate_distance(item)
            distances.append(distance)
            if distance not in distance_to_index:
                distance_to_index[distance] = [i]
            else:
                distance_to_index[distance].append(i)
        
        heapq.heapify(distances)
        
        result = []
        
        for i in range(k):
            val = heapq.heappop(distances)
            index = distance_to_index[val]
            result.append(points[index[0]])
            if len(index) > 1:
                distance_to_index[val].remove(index[0])
        
        return result