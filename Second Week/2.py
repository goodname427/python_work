class Solution:
    def is_palindromic_number(self, num: int) -> bool:
        num_str = num.__str__()
        for i in range(int(len(num_str) / 2)):
            if num_str[i] != num_str[len(num_str) - i - 1]:
                return False

        return True


s = Solution()
print(s.is_palindromic_number(121))
print(s.is_palindromic_number(-121))
print(s.is_palindromic_number(10))
