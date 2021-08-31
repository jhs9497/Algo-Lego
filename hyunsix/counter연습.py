from collections import Counter

a = [1,1,1,2,3,4,5,5,5,6,7,8,8,8,8]
c = Counter(a)
print(c)

for i in c:
    print('중복없이', i)
    print('------')

print(c.keys())
print(c.values())
print(c.items())

# 문자열도 됨!
s = 'hello, world'
sc = Counter(s)
print(sc)

# 더하기도 가능 bammmmm
sc.update('hello')
print('plus', sc)

# 뺴고시풔 ?
sc.subtract('hello')
print('빼자', sc)