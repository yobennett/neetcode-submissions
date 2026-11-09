# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.helper(pairs, 0, len(pairs) - 1)
        return pairs
    
    def helper(self, arr: List[pairs], s: int, e :int) -> None:
        # base case
        if e - s + 1 <= 1:
            return

        pivot = arr[e] # last
        left = s #insertion pointer start from left

        for i in range(s, e):
            if arr[i].key < pivot.key:
                tmp = arr[left]
                arr[left] = arr[i]
                arr[i] = tmp
                left += 1
        
        # move pivot in btwn left and right
        arr[e] = arr[left]
        arr[left] = pivot

        # recurse left and right
        self.helper(arr, s, left - 1)
        self.helper(arr, left + 1, e)
