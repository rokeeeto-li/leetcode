class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candy = [1]*n
        for i in range(n-1):
            if ratings[i] < ratings[i+1]:  candy[i+1] = candy[i] + 1
        for j in range(n-1, 0, -1):
            if ratings[j] < ratings[j-1]: candy[j-1] = max(candy[j]+1, candy[j-1])
        return sum(candy)
