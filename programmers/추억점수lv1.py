def solution(name, yearning, photo):
    answer = []
    for picture in photo:
        count = 0  # 각 사진마다 count 초기화
        for person in picture:
            if person in name:
                # name 리스트에서 person의 인덱스를 찾아서 해당하는 yearning 값을 더함
                idx = name.index(person)
                count += yearning[idx]
        answer.append(count)  # 한 사진의 총점을 answer에 추가
    return answer