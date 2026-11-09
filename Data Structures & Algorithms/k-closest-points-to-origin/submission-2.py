class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        euclidean = lambda x: x[0] ** 2 + x[1] ** 2

        def partition(l, r):
            pivotIndex = r
            pivotDistance = euclidean(points[pivotIndex])
            i = l
            for j in range(l, r):
                if euclidean(points[j]) <= pivotDistance:
                    points[i], points[j] = points[j], points[i]
                    i += 1
            points[i], points[r] = points[r], points[i]
            return i

        left, right = 0, len(points) - 1
        pivot = len(points)

        while pivot != k:
            pivot = partition(left, right)
            if pivot < k:
                left = pivot + 1
            else:
                right = pivot - 1
        
        return points[0:k]
        