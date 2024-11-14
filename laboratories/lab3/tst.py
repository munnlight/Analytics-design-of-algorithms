class Solution(object):
    def majorityElement(self, nums):
        return self.find_major(nums, 0, len(nums) - 1)

    def find_major(self, nums, l, r):
        if l == r:
            return nums[l]
        
        m = (l + r) // 2

        left = self.find_major(nums, l, m)
        right = self.find_major(nums, m + 1, r)

        if left == right:
            return left
        
        print(left, right)
        
        count_r = 0
        count_l = 0

        for i in range(l, r + 1):
            if nums[i] == right:
                count_r += 1
            if nums[i] == left:
                count_l += 1

        print(f"count %d, %d" %(count_r, count_l))
         
        return left if count_l >= count_r else right

x = Solution()
test = [3, 2, 3]

print(x.majorityElement(test))