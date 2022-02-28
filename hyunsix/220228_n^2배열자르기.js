function solution(n, left, right) {
  let answer = [];

  for (i = left; i < right + 1; i++) {
    let row = parseInt(i / n);
    let col = i % n;
    answer.push(Math.max(row, col) + 1);
  }

  return answer;
}
