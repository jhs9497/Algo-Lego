function check(skill, interaction) {
  let num = 0;
  let can_skill = [skill[0]];
  for (let i = 0; i < interaction.length; i++) {
    let now_skill = interaction[i];
    if (can_skill.includes(now_skill)) {
      num += 1;
      if (num < skill.length) {
        can_skill.push(skill[num]);
      }
    } else {
      return 0;
    }
  }
  return 1;
}

function solution(skill, skill_trees) {
  var answer = 0;
  skill = skill.split('');
  for (let i = 0; i < skill_trees.length; i++) {
    let skill_tree = skill_trees[i].split('');
    let interaction = skill_tree.filter((x) => skill.includes(x));
    console.log(interaction);
    let flag = check(skill, interaction);
    answer += flag;
  }
  return answer;
}
