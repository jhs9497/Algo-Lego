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

```python
from collections import defaultdict
```

- defaultdict(list)
  - 기본 값으로 빈 리스트 []를 제공 -> 처음 접근하는 key값이어도 A[key].append('블라블라') 가능!
- defaultdict(int)
  - 기본 값으로 숫자 0 제공
- defaultdict(set)
  - 기본 값으로 빈 set 제공





## 플로이드-워셜 알고리즘

- 모든 최단 경로를 구하는 알고리즘
- 노드 간의 최단 경로를 입려겨한 2차원 행렬을 구성한다.
- 경유지를 설정하고. 각 시행마다 새로운 경유지로 교체해가며, **기존의 출발->도착 경로**와 **출발->new경유지->도착의 경로**를 비교하여 더 짧은 경로를 선택한다.

```python
n = 6
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]

# n : 노드의 수 
# fares : 출발, 도착, 요금의 정보가 주어진다고 했을 때

INF = 1e10   # 충분히 큰 수

# dist -> x에서 y로 가는 운임 나타내는 2차원 요금지도
dist = [[INF for _ in range(n)] for _ in range(n)]

# 나 자신 -> 나 자신으로 가는 경우 0으로 설정
for i in range(n):
    dist[i][i] = 0
    
# fares로 받은 운임 적용해주기
for info in fares:
    # 우린 인덱스를 0부터 쓰니깐 -1해주자
    dist[info[0]-1][info[1]-1] = info[2]
    # 양방향으로 적용
    dist[info[1]-1][info[0]-1] = info[2]
```

##### 여기까지 적용하면 아래와 같은 2차원 요금지도 확인 가능

![캡처1](%EC%BA%A1%EC%B2%982.PNG)

```python
# 플로이드-워셜 알고리즘 적용
def floyd(dist, n):
    # i->j로 가는 최단거리를 저장하려고 하는거임
    # k라는 경유지를 두고 i에서 j로 갈때 i->k->j가 빠른지 현재의 i->j가 빠른지 비교
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][k] + dist[k][j], dist[i][j])

floyd(dist, n)
```

##### 그럼 아래와 같은 모든 경로의 최단거리 알 수 있는 요금지도 완성

![캡처1](%EC%BA%A1%EC%B2%981-1630680830324.PNG)





## deque

- 데크(deque)는 양방향 큐이다.
- 양쪽 방향에서 요소를 추가하거나 제거할 수 있다.
- 즉 일반적인 리스트의 경우 pop()보다 pop(0)을 할 경우 메모리 사용량이 늘어난다. 그 이유는 pop(0)의 경우 pop(0)을 하고 리스트를 맨 끝부터 앞으로 한 칸 씩 이동시키는 작업을 하기 때문이다.
  - 그런데 deque는 양방향 큐니깐 pop(0)이나 pop()이나 똑같다는 뜻!
- 즉 deque를 쓸 경우 확률상 양 끝 엘리먼트의 append와 pop이 압도적으로 빠르다.
- 심지어 사용법도 쉬움.. 앞으로 deque에 익숙해지도록 하자

```python
from collections import deque

deq = deque()

# 리스트 맨 앞에 요소 추가
deq.appendleft('요소')

# 리스트 뒤에 요소 추가 (일반적인 append)
deq.append('요소')

# 리스트 맨 앞에 요소 제거 (일반적인 pop(0))
deq.popleft()

# 리스트 맨 뒤에 요소 제거 
deq.pop()
```



## 소수 구할 때 제곱근까지만 구해도 되는 이유



> N의 약수는 무조건 sqrt(N)의 범위에 존재한다.

만약 N이 12라 할때, 12의 제곱근은 약 3.46이다.
12의 약수는 1, 2, 3, 4, 6, 12 이다.
여기서 1과 12를 제외했을 때 이는 2 * 6, 3 * 4, 4 * 3, 6 * 2의 결과이다.

이들의 관계는 몫이 커지면 나누는 값이 작아지거나 나누는 값이 커지만 몫이 작아지는 반비례 관계이다. 결국 N의 절반(제곱근)까지 향하게 되면 이후 몫과 나누는 값이 반대로 바뀌게만 되는 상황이다.

따라서 N의 제곱근까지 나누어 떨어지는지 여부를 조사하면 더 빠르게 소수판별을 할 수 있다.

