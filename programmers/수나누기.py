number = int(input()) # 2134 입력
answer = 0

while number > 0:  # number가 0보다 클 때까지 반복
    answer += number % 100  # 100으로 나눈 나머지를 더함
    number //= 100  # 100으로 나눈 몫을 다시 number에 저장

print(answer)