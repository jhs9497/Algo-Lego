function calTime(front, back) {
  let frontTime = front.split(':');
  let frontH = frontTime[0];
  let frontM = frontTime[1];
  let totalFrontTime = parseInt(frontH) * 60 + parseInt(frontM);

  let backTime = back.split(':');
  let backH = backTime[0];
  let backM = backTime[1];
  let totalBackTime = parseInt(backH) * 60 + parseInt(backM);

  return totalBackTime - totalFrontTime;
}

function solution(fees, records) {
  const defaultTime = parseInt(fees[0]);
  const defaultFee = parseInt(fees[1]);
  const unitTime = parseInt(fees[2]);
  const unitFee = parseInt(fees[3]);

  let allCarTime = {};

  let allCarPlusTime = {};

  let answer = [];

  for (let i = 0; i < records.length; i++) {
    let part = records[i].split(' ');
    let time = part[0];
    let num = part[1];
    let flag = part[2];

    if (flag == 'IN') {
      allCarTime[num] = time;
    } else {
      let INTime = allCarTime[num];
      let carCalTime = calTime(INTime, time);
      allCarTime[num] = '';
      if (allCarPlusTime[num]) {
        allCarPlusTime[num] = allCarPlusTime[num] + carCalTime;
      } else {
        allCarPlusTime[num] = carCalTime;
      }
    }
  }

  for (keys in allCarTime) {
    if (allCarTime[keys]) {
      let carCalTime = calTime(allCarTime[keys], '23:59');
      if (allCarPlusTime[keys]) {
        allCarPlusTime[keys] = allCarPlusTime[keys] + carCalTime;
      } else {
        allCarPlusTime[keys] = carCalTime;
      }
    }
  }

  allCarFees = {};
  for (keys in allCarPlusTime) {
    let totalFee;
    let totalTime = parseInt(allCarPlusTime[keys]);

    if (totalTime - defaultTime > 0) {
      totalFee =
        defaultFee + Math.ceil((totalTime - defaultTime) / unitTime) * unitFee;
    } else {
      totalFee = defaultFee;
    }
    allCarFees[keys] = totalFee;
  }

  let sortobj = [];
  for (let car in allCarFees) {
    sortobj.push([car, allCarFees[car]]);
  }
  console.log(sortobj);
  sortobj.sort(function (a, b) {
    return a[0] - b[0];
  });

  for (let keys in sortobj) {
    answer.push(sortobj[keys][1]);
  }

  return answer;
}
