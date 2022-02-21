function solution(s) {
  let answer = [];
  let whileCount = 0;
  let allZeroCount = 0;

  while (s != '1') {
    // 0빼기
    let zeroCount = 0;
    let oneCount = 0;
    for (i = 0; i < s.length; i++) {
      if (s[i] == '0') {
        zeroCount += 1;
      } else {
        oneCount += 1;
      }
    }
    allZeroCount += zeroCount;
    // s의 길이를 2진수 변환
    let newS = '';
    while (oneCount > 0) {
      let binary = oneCount % 2;
      oneCount = parseInt(oneCount / 2);
      newS = String(binary) + newS;
    }
    s = newS;
    whileCount += 1;
  }
  answer.push(whileCount);
  answer.push(allZeroCount);
  return answer;
}
