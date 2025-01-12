function solution(players, callings) {
  let idx;
  let name1;
  let name2;
  const idxList = {};

  players.forEach((name, index) => (idxList[name] = index));
  for (let call of callings) {
    idx = idxList[call]; // 호명된 선수의 현재 위치 찾기
    name1 = players[idx]; // 호명된 선수 (추월하는 선수)
    name2 = players[idx - 1]; // 앞에 있는 선수 (추월당하는 선수)
    idxList[call] -= 1; // 호명된 선수의 인덱스 1 감소
    idxList[name2] += 1; // 추월당한 선수의 인덱스 1 증가
    players[idx] = name2; // players 배열에서 실제 위치 교환
    players[idx - 1] = name1;
  }

  return players;
}
