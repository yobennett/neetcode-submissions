class Solution:
    # Two Heaps
    # maximize profit
    # minimize capital
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        maxProfit = [] # max heap, values are multiplied by -1
        minCapital = [(c, p) for c, p in zip(capital, profits)] # min heap
        heapq.heapify(minCapital)

        # repeat up to k projects
        for _ in range(k):
            # iterate through projects (capital and profit)
            # until capital exceeds available capital (initially w)
            # gives the project with max profits that can be afforded 
            # with no more than w capital
            while minCapital and minCapital[0][0] <= w:
                capital, profit = heapq.heappop(minCapital)
                heapq.heappush(maxProfit, -profit)

            # break if no affordable projects given w capital
            if not maxProfit:
                break

            # add profit from the project
            w += -heapq.heappop(maxProfit)

        return w