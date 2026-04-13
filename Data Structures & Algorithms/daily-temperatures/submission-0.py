class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for i,temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                idx = stack[-1][0]
                result[idx] = i - idx
                stack.pop()
            stack.append((i,temp))
        return result