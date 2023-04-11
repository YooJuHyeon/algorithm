def solution(hp):
    
    general_ant = hp // 5
    left_hp = hp % 5
    soldier_ant = left_hp // 3
    ergate = left_hp % 3
    
    return general_ant + soldier_ant + ergate