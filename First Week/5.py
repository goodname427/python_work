l = [1, 'v', 3, 4, 5, 6, 7]
# 反转
print(l[::-1])

print(l[::-2])

try:
    l[0] = '1'
except:
    print('-' * 5)

print(l[:3])
print(l[1:4])
