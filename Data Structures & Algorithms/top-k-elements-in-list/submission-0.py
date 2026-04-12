class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i,ch in enumerate(nums):
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1
        
        heap = []
        for w, count in freq.items():
            heapq.heappush(heap,(-count,w))
        
        result = []
        for i in range(k):
            result.append(heapq.heappop(heap)[1])
        
        return result