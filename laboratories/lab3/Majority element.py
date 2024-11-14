class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        table = {}

        for i in nums:
            if i in table:
                table[i] += 1
            else:
                table[i] = 1

        maximum = max(table.values())
        print(maximum)
        print(table)
        for key, value in table.items():
            print(key, value)
            if maximum == value:
                return key
    
test = Solution()

print(test.majorityElement([3,3,4]))