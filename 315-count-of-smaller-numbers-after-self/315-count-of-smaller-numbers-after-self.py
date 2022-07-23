class Solution:
    def countSmaller(self, nums):
        counts = []
        done = []
        for num in nums[::-1]:
            counts.insert(0, bisect.bisect_left(done, num))
            bisect.insort(done, num)
        return counts
        