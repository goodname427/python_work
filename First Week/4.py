s = 'abcdefg'
# 反转
print(s[::-1])

print(s[::-2])

try:
    s[0] = '1'
except:
    print('-' * 5)

print(s[:3])
print(s[1:4])
