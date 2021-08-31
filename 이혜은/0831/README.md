# README

[toc]

## collection.counter👨‍👧‍👦

### collection.counter

> 편리하고 빠르게 개수를 세도록 지원하는 계수기 도구가 제공됩니다.

```
# Tally occurrences of words in a list
cnt = Counter()
for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
     cnt[word] += 1
cnt
Counter({'blue': 3, 'red': 2, 'green': 1})

# Find the ten most common words in Hamlet
import re
words = re.findall(r'\w+', open('hamlet.txt').read().lower())
Counter(words).most_common(10)
[('the', 1143), ('and', 966), ('to', 762), ('of', 669), ('i', 631),
 ('you', 554),  ('a', 546), ('my', 514), ('hamlet', 471), ('in', 451)
```



### elements()

> 개수만큼 반복되는 요소에 대한 이터레이터를 반환합니다. 요소는 처음 발견되는 순서대로 반환됩니다. 요소의 개수가 1보다 작으면 `elements()`는 이를 무시합니다

```
c = Counter(a=4, b=2, c=0, d=-2)
sorted(c.elements())
['a', 'a', 'a', 'a', 'b', 'b']
```



### most_commone(n)

> *n* 개의 가장 흔한 요소와 그 개수를 가장 흔한 것부터 가장 적은 것 순으로 나열한 리스트를 반환합니다. *n*이 생략되거나 `None`이면, `most_common()`은 계수기의 *모든* 요소를 반환합니다. 개수가 같은 요소는 처음 발견된 순서를 유지합니다

```
Counter('abracadabra').most_common(3)
[('a', 5), ('b', 2), ('r', 2)]
```



### subtract()

> *이터러블*이나 다른 *매핑* (또는 계수기)으로부터 온 요소들을 뺍니다. `dict.update()`와 비슷하지만 교체하는 대신 개수를 뺍니다. 입력과 출력 모두 0이나 음

```
c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(a=1, b=2, c=3, d=4)
c.subtract(d)
c
Counter({'a': 3, 'b': 0, 'c': -3, 'd': -6})
```



### update()

> 요소는 *이터러블*에서 세거나 다른 *매핑*(또는 계수기)에서 더해집니다. `dict.update()`와 비슷하지만, 교체하는 대신 더합니다. 또한, *이터러블*은 `(key, value)` 쌍의 시퀀스가 아닌, 요소의 시퀀스일 것으로 기대합니다.



### 덧셈 && 뺄셈

> 더하기와 빼기는 해당 요소의 개수를 더 하거나 빼서 계수기를 결합. 각 연산은 부호 있는 개수를 입력으로 받을 수 있지만, 출력은 개수가 0 이하면 결과에서 제외

```
c = Counter(a=3, b=1)
d = Counter(a=1, b=2)

c + d                       # add two counters together:  c[x] + d[x]
Counter({'a': 4, 'b': 3})
c - d                       # subtract (keeping only positive counts)
Counter({'a': 2})
```



### 교집합 && 합집합

> 교집합(intersection)과 합집합(union)은 해당 개수의 최솟값과 최댓값을 반환합니다. 각 연산은 부호 있는 개수를 입력으로 받을 수 있지만, 출력은 개수가 0 이하면 결과

```
c = Counter(a=3, b=1)
d = Counter(a=1, b=2)

c & d                       # intersection:  min(c[x], d[x]) 
Counter({'a': 1, 'b': 1})
c | d                       # union:  max(c[x], d[x])
Counter({'a': 3, 'b': 2})
```



###### 참조

- [`python 공식 문서`](https://docs.python.org/ko/3/library/collections.html )  



## itertools.permutations && itertools.combinations⭐

### itertools.combinations

```
itertools.combinations('ABCD', 2) --> AB AC AD BC BD CD
itertools.combinations(range(4), 3) --> 012 013 023 123
```



### itertools.permutations

```
def combinations(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    for indices in permutations(range(n), r):
        if sorted(indices) == list(indices):
            yield tuple(pool[i] for i in indices)
```





###### 참조

- [`python 공식 문서`](https://docs.python.org/ko/3/library/itertools.html )  