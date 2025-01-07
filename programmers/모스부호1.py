def solution(letter):
    answer = ''
    morse = { 
        '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
        '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
        '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
        '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
        '-.--':'y','--..':'z'
    }
    
    # 공백을 기준으로 모스 부호를 분리
    morse_codes = letter.split()
    
    # 각 모스 부호를 알파벳으로 변환하여 answer에 추가
    for code in morse_codes:
        answer += morse[code]
        
    return answer