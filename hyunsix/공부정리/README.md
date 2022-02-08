## Counter

무시무시한 친구를 알아버렸다. from collections import Counter를 통해 리스트의 요소 갯수를 바로 알아버리는 친구다

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



## 파이썬 람다 함수

람다함수란 ? 일반함수를 굳이 def ~ return으로 선언하지 않고 가볍게 만들 수 있는 연산함수

```python
# 예를 들어
def is_even(x):
    if x % 2 == 0:
        return True
    return False

# 아래처럼 람다함수로 변환 가능
is_even = lambda x : x % 2 == 0

# 사용 법은 둘 다
is_even(1)
is_even(2) ...
```



### lambda & map함수

람다함수는 map함수랑 짝지어서 자주 사용됨 !

map함수는 리스트나, 튜플에 어떠한 처리를 할 때 사용하는 함수로

map(함수, 리스트) 식으로 첫번째 인자에는 함수, 두번째 인자에는 리스트(or튜플)를 받음

```python
# 흔히 공백으로 이루어진 숫자리스트를 인풋 받을 때 아래와 같이 받는데
number_list = list(map(int, input().split()))
# 공백기준으로 나누어 받은 친구들을 int함수로 숫자화 시키고(인풋값은 스트링으로 오기 때문) 그 바깥에서 한 번 더 list화 시킨다는 의미!
```

즉 첫번째 인자인 함수가 두번째 인자로 들어온 리스트나, 튜플에 특정한 처리를 하고 그 처리된 값을 리턴시켜줌

```python
# 만약 모든 값을 *2해주는 함수를 만든다고 치면

# 일반함수
def 곱하기_2(x):
    return x * 2

ans1 = list(map(곱하기_2, [1,2,3,4,5,6,7,8,9,10]))
print(ans1)

# 람다 적용
ans2 = list(map((lambda x: x*2), [1,2,3,4,5,6,7,8,9,10]))
print(ans2)
```



### lambda & sort함수

람다는 sort함수에서 key값으로도 자주 사용됨!

```python
# 요소들의 길이 기준으로 정렬하고 싶을 때
data_list = ['길이', '가', '다릅니다', '맞죠']
data_list.sort(key=lambda x : len(x))
print(data_list)
# ['가', '길이', '맞죠', '다릅니다']

# list안에 2개의 요소가 있을 때 두번째 요소 기준으로 정렬하고 싶을 때
data_list = [[-20, 15], [-14, -5], [-18, -13], [-5, -3]]
data_list.sort(key=lambda x : x[1])
print(data_list)
# [[-18, -13], [-14, -5], [-5, -3], [-20, 15]]

# list안에 2개의 요소가 있을 때 우선 첫 번째 인자를 기준으로 오름차순 정렬하고, 같을 시 두번째 인자 기준으로 내림차순 정렬하고 싶을 때
data_list = [[1,3], [0,1], [1,5], [1,4], [1,3], [2,4]]
data_list.sort(key=lambda x : (x[0], -x[1]))
print(data_list)
# [[0, 1], [1, 5], [1, 4], [1, 3], [1, 3], [2, 4]]
```



### lambda & filter 함수

filter함수는 filter(함수, 리스트)로 이루어지는데 리스트의 요소들을 하나씩 함수에 넣어서 True인 경우만 걸러서 새로운 리턴값을 생성해준다고 생각하면 됨

```python
# 짝수만 거르는 경우

# 일반 함수
def is_even(x):
    return x % 2 == 0

result1 = list(filter(is_even), range(10))


# 람다 함수
result2 = list(filter(lambda x : x % 2 == 0, range(10)))
```



## 다익스트라 알고리즘 (이코테 참조)

1. 출발 노드를 설정한다.
2. 최단 거리 테이블을 초기화한다.
   1. 자기 자신과의 거리는 0
3. 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택한다.
4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신한다.
5. 위 과정의 3번과 4번을 반복한다.

### heap자료구조를 이용하는 이유

1. 단계마다 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택하기 위해 힙(Heap) 자료구조를 이용한다.
2. 다익스크라 알고리즘이 동작하는 기본 원리는 동일하다.
   - 현재 가장 가까운 노드를 저장해 놓기 위해서 힙 자료구졸르 추가적으로 이용한다는 점이 다르다.
   - 현재의 최단 거리가 가장 짧은 노드를 선택해야 하므로 최소 힙을 사용한다.



```python
import heapq

INF = 1e9

# 노드의 개수, 간선의 개수 입력받기
n, m = map(int, input().split())
# 시작 노드 번호 입력받기
start = int(input())
# 노드 연결 리스트 만들기
graph = [[] for _ in range(n+1)]
# 최단 거리 테이블 모두 무한으로 초기화해서 만들기
distance = [INF] * (n+1)

# 모든 간선 정보 graph에 반영하기
for _ in range(m):
    a, b, c, = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c다.
    graph[a].append((b,c))
    
    
# 다익스트라 알고리즘
def dijkstra(start):
    q = []
    # start 노드로 가기 위한 거리는 0으로 설정(자기 자신에게 가는 거리임, 우선순위 큐에 삽입)
    heapq.heappush(q, (0, start))
    distanch[start] = 0
    # q가 비어있기 전 까지 진행
    while q:
        # 현재 가장 짧은 거리의 노드정보 꺼내기
        dist, node = heapq.heappop(q)
        # 현재 노드의 거리가 방금 꺼낸 dist보다 작다는건 탐색할 필요가 없다는 뜻이므로 continue로 무시
        if distance[now] < dist:
            continue
           
        # 현재 노드와 연결된 다른 인접한 노드들 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우 
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(cost, i[0])

# 다익스트라 수행                
dijkstra(start)

# distance안에 start노드 기준 모든 노드로 가는 최단거리 들어있음 
    
```



### 프로그래머스 가장 먼 노드 풀이

```python
import heapq

def solution(n, edge):
    INF = 1e9
    graph = [[] for _ in range(n+1)]
    distance = [INF] * (n+1)
    for start, end in edge:
        graph[start].append((end, 1))
        graph[end].append((start, 1))
        
    def dijkstra(start):
        q = []
        distance[start] = 0
        heapq.heappush(q, (0, start))
        while q:
            dist, now_node = heapq.heappop(q)
            if distance[now_node] < dist:
                continue
            
            for i in graph[now_node]:
                cost = dist + i[1]
                if distance[i[0]] > cost:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))
                    
    dijkstra(1)
    
    distance.pop(0)
    
    max_d = max(distance)
    answer = 0
    for d in distance:
        if max_d == d:
            answer += 1
    
    return answer
```

```python
{'*': 0, '+': 1, '-': 2}
['100', '200', '*', '300', '500', '+', '20', '-']
{'*': 0, '-': 1, '+': 2}
['100', '200', '*', '300', '500', '-', '20', '+']
{'+': 0, '*': 1, '-': 2}
['100', '200', '*', '300', '500', '+', '20', '-']
{'+': 0, '-': 1, '*': 2}
['100', '200', '-', '300', '-', '500', '+', '20', '*']
{'-': 0, '*': 1, '+': 2}
['100', '200', '-', '300', '-', '500', '*', '20', '+']
{'-': 0, '+': 1, '*': 2}
['100', '200', '-', '300', '-', '500', '+', '20', '*']
```

```python
from itertools import permutations

def calculate(num2, num1, operator): 
    if operator == '*': return num1*num2 
    elif operator == '+': return num1+num2 
    else: return num1-num2




def solution(expression):
    expr_list = []
    N = ""
    for e in expression:
        if e.isdigit():
            N += e
        else:
            expr_list.append(N)
            N = ""
            expr_list.append(e)
    expr_list.append(N)  
            
    operations = ["*", "+", "-"]
    operation_list = list(permutations(operations, 3))
    for operation in operation_list:
        
        # 6가지 우선순위 만들기
        operation_dict = {}
        for i in range(len(operation)):
            operation_dict[operation[i]] = i
        postfix = []
        stack = []
        
        # 후위표기식으로 전환
        for expr in expr_list:
            if expr.isdigit():
                postfix.append(expr)
            else:
                if len(stack) == 0:
                    stack.append(expr)
                else:
                    if operation_dict[expr] < operation_dict[stack[-1]]:
                        postfix.append(expr)
                    elif operation_dict[expr] > operation_dict[stack[-1]]:
                        priorN = stack.pop()
                        postfix.append(priorN)
                        stack.append(expr)
        
        while stack:
            lastN = stack.pop()
            postfix.append(lastN)
        
        print(operation_dict)
        print(postfix)
        
        # 후위표기식 계산
        # stack = []
        # for x in postfix:
        #     if type(x) == int:
        #         stack.append(x)
        #     else:
        #         stack.append(calculate(stack.pop(), stack.pop(), x))
        # print(stack[0])
        
    answer = 0
    return answer
```

```python
from itertools import permutations 

def calculate(num2, num1, operator): 
    if operator == '*': return num1*num2 
    elif operator == '+': return num1+num2 
    else: return num1-num2 
    
def solution(expression): answer = 0 temp = ['*', '+', '-']
    for operator in permutations(temp):
        postfix = [] stack = [] num = '' 
        for s in expression: 
            if s.isnumeric(): num += s else: 
                    postfix.append(int(num)) num = '' 
                    if stack:
                        if operator.index(stack[-1]) > operator.index(s): 									stack.append(s)
                        else: 
                            while stack and operator.index(stack[-1]) <= operator.index(s): 												postfix.append(stack.pop()) stack.append(s) 
                    else: stack.append(s) 
                        
        postfix.append(int(num))
        
        while stack: 
            postfix.append(stack.pop()) 
        stack = [] 
        for x in postfix: 
            if type(x) == int: 
                stack.append(x) 
            else: stack.append(calculate(stack.pop(), stack.pop(), x)) 
                
        answer = max(answer, abs(stack[0])) 
    return answer

```

