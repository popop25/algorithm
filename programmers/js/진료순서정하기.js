function solution(emergency) {
  // 원본 배열 복사해두기 (참조를 끊기 위해 spread 연산자 사용)
  const sorted = [...emergency].sort((a, b) => b - a); // 내림차순 정렬

  // 순위로 변환
  return emergency.map((v) => sorted.indexOf(v) + 1);
}

console.log(solution([3, 76, 24])); // [3, 1, 2]
console.log(solution([1, 2, 3, 4, 5, 6, 7])); // [7, 6, 5, 4, 3, 2, 1]
