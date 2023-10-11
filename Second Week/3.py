class Solution:
    def _is_equal(self, strs, index):
        if index >= len(strs[0]):
            return False

        for i in range(1, len(strs)):
            if index >= len(strs[i]) or strs[i][index] != strs[0][index]:
                return False

        return True

    def longest_common_prefix(self, strs: [str]) -> str:
        if len(strs) == 0:
            return ""

        if len(strs) == 1:
            return strs[0]

        index = 0
        while self._is_equal(strs, index):
            index += 1

        return strs[0][:index]


s = Solution()
print(s.longest_common_prefix(['flower', 'flow', 'flight']))
print(s.longest_common_prefix(['dog', 'racecar', 'car']))
