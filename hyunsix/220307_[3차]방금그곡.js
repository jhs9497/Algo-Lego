function solution(m, musicinfos) {
  m = m.replace(/C#/g, 'ㄱ');
  m = m.replace(/D#/g, 'ㄴ');
  m = m.replace(/F#/g, 'ㄷ');
  m = m.replace(/G#/g, 'ㄹ');
  m = m.replace(/A#/g, 'ㅁ');

  let answer = '(None)';
  let time = 0;

  for (let info of musicinfos) {
    const musicInfo = info.split(',');
    const startTime =
      parseInt(musicInfo[0].slice(0, 2)) * 60 +
      parseInt(musicInfo[0].slice(3, 5));
    const endTime =
      parseInt(musicInfo[1].slice(0, 2)) * 60 +
      parseInt(musicInfo[1].slice(3, 5));
    const runningTime = endTime - startTime;

    const musicName = musicInfo[2];
    let musicScroe = musicInfo[3];

    musicScroe = musicScroe.replace(/C#/g, 'ㄱ');
    musicScroe = musicScroe.replace(/D#/g, 'ㄴ');
    musicScroe = musicScroe.replace(/F#/g, 'ㄷ');
    musicScroe = musicScroe.replace(/G#/g, 'ㄹ');
    musicScroe = musicScroe.replace(/A#/g, 'ㅁ');

    let allMusicScore = '';
    let r = runningTime;
    let idx = 0;
    while (r > 0) {
      allMusicScore += musicScroe[idx];
      idx = idx + 1;
      r = r - 1;
      if (idx >= musicScroe.length) {
        idx = 0;
      }
    }

    if (allMusicScore.indexOf(m) >= 0) {
      if (time < runningTime) {
        time = runningTime;
        answer = musicName;
      }
    }
  }

  return answer;
}
