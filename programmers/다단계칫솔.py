def solution(enroll, referral, seller, amount):
    # 1. 추천인 관계를 딕셔너리로 만들기
    parent = {}  # 자신의 추천인을 저장
    for i in range(len(enroll)):
        parent[enroll[i]] = referral[i]
    
    # 2. 수익 저장할 딕셔너리
    profit = {name: 0 for name in enroll}
    
    # 3. 수익 분배 함수
    def distribute(name, money):
        if name == "-" or money < 1:  # 추천인 없거나 분배할 돈이 1원 미만이면
            return
            
        give = money // 10  # 10% 계산
        mine = money - give  # 자신이 가질 돈
        
        profit[name] += mine  # 자신의 돈 저장
        
        # 추천인에게 10% 전달 (재귀)
        if parent[name] != "-":
            distribute(parent[name], give)
    
    # 4. 판매 정보를 순회하며 수익 분배
    for i in range(len(seller)):
        distribute(seller[i], amount[i] * 100)
    
    # 5. 최종 수익 반환
    return [profit[name] for name in enroll]