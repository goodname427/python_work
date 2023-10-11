class Solution:
    def sum_of_two_num(self, nums: [int], target: int) -> tuple[int, int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return i, j

        return -1, -1


s = Solution()
print(s.sum_of_two_num([2, 7, 11, 15], 9))
print(s.sum_of_two_num([3, 2, 4], 6))
print(s.sum_of_two_num([3, 3], 6))
