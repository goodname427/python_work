class Solution:
    def valid_parentheses(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '[' or c == '{' or c == '(':
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False

                top = stack[-1]
                stack.pop()
                if (c == ')' and top != '(') or (c == ']' and top != '[') or (c == '}' and top != '{'):
                    return False

        return len(stack) == 0


solution = Solution()
print(solution.valid_parentheses('()'))
print(solution.valid_parentheses('()[]{}'))
print(solution.valid_parentheses('(]'))
