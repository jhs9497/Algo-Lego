function solution(dirs) {
  let nowX = 0;
  let nowY = 0;

  const dirDict = {
    U: [0, 1],
    D: [0, -1],
    R: [1, 0],
    L: [-1, 0],
  };

  let answerArr = [];
  let answer = 0;

  for (dir of dirs) {
    const newX = nowX + dirDict[dir][0];
    const newY = nowY + dirDict[dir][1];
    if (newX >= -5 && newX < 6 && newY >= -5 && newY < 6) {
      const road1 = String(nowX) + String(nowY) + String(newX) + String(newY);
      const road2 = String(newX) + String(newY) + String(nowX) + String(nowY);
      if (
        answerArr.includes(road1) === false &&
        answerArr.includes(road2) === false
      ) {
        answer += 1;
      }
      answerArr.push(road1);
      answerArr.push(road2);
      nowX = newX;
      nowY = newY;
    }
  }

  return answer;
}
