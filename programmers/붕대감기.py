def solution(bandage, health, attacks):
    max_health = health
    current_time = 0
    healing_count = 0
    
    # attacks를 딕셔너리로 변환하여 시간별 데미지를 쉽게 찾을 수 있게 함
    attack_dict = {attack[0]: attack[1] for attack in attacks}
    last_attack_time = attacks[-1][0]
    
    for time in range(last_attack_time + 1):
        if time in attack_dict:  # 공격이 있는 시간
            health -= attack_dict[time]
            healing_count = 0
            if health <= 0:
                return -1
        else:  # 공격이 없는 시간
            health += bandage[1]
            healing_count += 1
            
            if healing_count == bandage[0]:  # 연속 치유 성공
                health += bandage[2]
                healing_count = 0
                
            health = min(health, max_health)  # 최대 체력을 넘지 않도록
            
    return health