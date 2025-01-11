function solution(n, m, positions) {
  // 1부터 n까지의 숫자로 배열 만들기
  let queue = Array.from({ length: n }, (_, i) => i + 1);
  let count = 0;

  for (let target of positions) {
    while (true) {
      // 목표가 맨 앞에 있으면 뽑기
      if (queue[0] === target) {
        queue.shift(); // 맨 앞 원소 제거
        break;
      }

      // 목표의 위치 찾기
      let targetIdx = queue.indexOf(target);

      // 왼쪽으로 가는게 더 빠른지 판단
      if (targetIdx <= queue.length / 2) {
        // 왼쪽으로 한 칸 이동
        queue.push(queue.shift());
        count++;
      } else {
        // 오른쪽으로 한 칸 이동
        queue.unshift(queue.pop());
        count++;
      }
    }
  }

  return count;
}

console.log(solution(10, 3, [1, 2, 3])); // 위치에 따른 최소 이동 횟수 출력
