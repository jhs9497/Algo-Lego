## JS 메서드 정리

```javascript
// n진수의 x값을 10진수의 숫자로 변환해준것
parseInt(x값, n진수)
parseInt('100', 10) -> 100
parseInt('100', 16)  -> 256
parseInt('100', 8)   -> 64
parseInt('100', 2)   -> 4
// 굳이 슬라이싱 안해도됨 숫자스러운 애들만 빼줌
parseint('100asdfawe', 10) -> 100

// 유사품 : parseFloat()
```

```javascript
// 형변환
Boolean()
Number()
String()
Array()
Object()
RegExp()
Map()
Set()
```

```javascript
// array 관련 메소드
let arr = [10, 2, 3, 22, 33, 100, 11]
let arr2 = [12, 13]

// 이어붙이고 return 해주기
arr.concat(arr2)
[10, 2, 3, 22, 33, 100, 11, 12, 13]

// pop, push
arr.pop()
[10, 2, 3, 22, 33, 100]
return값 : 11
arr.push(1000)
[10, 2, 3, 22, 33, 100, 1000]
return값 : 7(arr의 길이)

// shift
arr.shift()
pop느낌이지만 앞에서 꺼냄

// unshift
arr.unshift()
push 느낌이지만 앞에서 넣음

----------------------------------------
arr[10, 20, 30, 40, 50]
arr.length // arr길이 
arr.fill(100) // arr을 모두 100으로 채워주기
arr.filter(x => x > 30) // 30초과인 요소만
[40, 50]

----------------------------------------
arr = [1, 2, 3, [1, 2, 3, [10, 20]]]
arr.flat(2) // 2는 몇 꺼풀 벗겨낼지 ㅇㅇ
[1, 2, 3, 1, 2, 3, 10, 20]

arr.inclues(값) // 값을 포함하고 있는지
arr.join()     // 리스트 스트링화 1231231020
arr.join('!')  // 사이에 ! 껴서 스트링화 1!2!3!1!2!3!10!20
```

```javascript
// map
['1', '2', '3'].map(x => parseInt(x))
[1, 2, 3]

// sort
arr.sort(function(a,b){return b-a})

// splice 요소를 삭제 or 교체
// slice 요소를 인덱스 기준으로 잘라낸다.
```

```javascript
// set
let arr = [1,1,1,1,2,2,3,3,4,4,5]
let s = new Set(arr)
{1,2,3,4,5}

s.size // 길이구하기
s.has(1) // 1 갖고 있는지
```

```javascript
// String
let str = 'abc abc de de abcde defg'
// \n \t \v \' \" \\
str.concat() 문자 합치기
str.inclues(값) 값 포함여부
split(값) 값 기준으로 나누기
str.replace('abc', '!') 맨 처음 만나는 'abc'만 '!'로 변환
str.replace(/abc/g, '!') 모든 'abc' '!'로 변환
str.replace(/ /g, '!') 모든 띄어쓰기 '!'로 변환
slice(3, 6)  3(start), 6(end)값 잘라내기
indexOf('abce') abce를 만나는 첫 인덱스 반환
```



