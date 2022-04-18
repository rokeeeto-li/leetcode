class TwoSum(object):

    def __init__(self):
        self.nums = []
        self.is_sorted = False
        

    def add(self, number):
        self.nums.append(number)
        self.is_sorted = False
        """
        :type number: int
        :rtype: None
        """
        

    def find(self, value):
        if self.is_sorted == False:
            self.nums.sort()
            self.is_sorted = True
        start = 0
        end = len(self.nums) - 1
        while start < end:
            if self.nums[start] + self.nums[end] == value: return [start+1, end+1]
            elif self.nums[start] + self.nums[end] < value: start += 1
            else: end -= 1
        """
        :type value: int
        :rtype: bool
        """
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
