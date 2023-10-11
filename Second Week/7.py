class Solution:
    def isomorphic_string(self, s: str, t: str) -> bool:
        s_dic = {}
        t_dic = {}

        for i in range(len(s)):
            if s[i] not in s_dic:
                s_dic[s[i]] = len(s_dic)
            if t[i] not in t_dic:
                t_dic[t[i]] = len(t_dic)

            if s_dic[s[i]] != t_dic[t[i]]:
                return False

        return True


solution = Solution()
print(solution.isomorphic_string("egg", 'add'))
print(solution.isomorphic_string("foo", 'bar'))
print(solution.isomorphic_string("paper", 'title'))
print(solution.isomorphic_string("asd", 'sdr'))
print(solution.isomorphic_string("sorry", 'sally'))
print(solution.isomorphic_string("sorry", 'badly'))
