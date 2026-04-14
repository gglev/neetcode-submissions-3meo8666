class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_eat(k):
            total_hours = 0
            for pile in piles:
                total_hours += (pile + k - 1) // k
            
            return total_hours <= h

        left = 1
        right = max(piles)

        while left < right:
            mid = (left + right) // 2
            if can_eat(mid):
                right = mid
            else:
                left = mid + 1
            
        return left