class Solution:
    def move_zero(self, nums: [int]) -> [int]:
        zero_count = 0
        res = []
        for num in nums:
            if num != 0:
                res.append(num)
            else:
                zero_count += 1

        for i in range(zero_count):
            res.append(0)

        for i in range(len(res)):
            nums[i] = res[i]

        return nums


solution = Solution()
print(solution.move_zero([0, 1, 0, 3, 12]))
print(solution.move_zero([0]))
