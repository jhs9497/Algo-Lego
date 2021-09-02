## Counter

무시무시한 친구를 알아버렸다. from collections import Counter를 통해 리스트의 요소 갯수를 바로 알아버리는 친구다.

```python
from collections import Counter

a = [1,1,1,2,3,4,5,5,5,6,7,8,8,8,8]
c = Counter(a)
print(c)

# Counter({8: 4, 1: 3, 5: 3, 2: 1, 3: 1, 4: 1, 6: 1, 7: 1})


for i in c:
    print('중복없이', i)
    print('------')
# 마치 set함수에 넣은 듯한 느낌으로 중복없이 출력 할수도 있다.    
# 중복없이 1
# ------
# 중복없이 2
# ------
# 중복없이 3
# ------
# 중복없이 4
# ------
# 중복없이 5
# ------
# 중복없이 6
# ------
# 중복없이 7
# ------
# 중복없이 8
# ------


# 딕셔너리처럼 key, value, items다 가능
print(c.keys())
# dict_keys([1, 2, 3, 4, 5, 6, 7, 8])
print(c.values())
# dict_values([3, 1, 1, 1, 3, 1, 1, 4])
print(c.items())
# dict_items([(1, 3), (2, 1), (3, 1), (4, 1), (5, 3), (6, 1), (7, 1), (8, 4)])


# 문자열도 매우 가능이다!

s = 'hello, world'
sc = Counter(s)
print(sc)
# Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ',': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})

# 더하기도 가능 bammmm
sc.update('hello')
print('update', sc)
# plus Counter({'l': 5, 'o': 3, 'h': 2, 'e': 2, ',': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})


# 물론 빼기도 가능!!
sc.subtract('hello')
print('빼자', sc)
# 빼자 Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ',': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
```



## defaultdict란 ?

A라는 딕셔너리를 선언하고 key값으로 접근했을 때 만약 A[key]가 처음 접근된 친구면 **KeyError**를 일으킨다! 그래서 특히 dict에 value값으로 리스트를 삼을때 리스트가 처음 추가되는지 아닌지 if / else로 분기처리를 해준다. defaultdict는 그러한 수고로움을 덜어준다. 처음 접근되는 key일지라도 기본적으로 제공되는 기본값이 존재하기 때문! 

- defaultdict(list)
  - 기본 값으로 빈 리스트 []를 제공 -> 처음 접근하는 key값이어도 A[key].append('블라블라') 가능!
- defaultdict(int)
  - 기본 값으로 숫자 0 제공
- defaultdict(set)
  - 기본 값으로 빈 set 제공