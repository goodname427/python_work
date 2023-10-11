class Solution:
    def last_word_len(self, s: str) -> int:
        cur_len = 0
        is_space = True
        for c in s:
            if c != ' ':
                if is_space:
                    cur_len = 1
                    is_space = False
                else:
                    cur_len += 1
            else:
                is_space = True

        return cur_len


solution = Solution()
print(solution.last_word_len("Hello World"))
print(solution.last_word_len("  fly me    to   the  moon"))
print(solution.last_word_len("luffy is still joyboy"))