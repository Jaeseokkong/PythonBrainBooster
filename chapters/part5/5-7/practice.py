# 다음 사양을 만족하는 함수
def get_min(d):
    """d는 문자와 정수를 매핑하는 dict입니다.
       알파벳에 먼저 등장하는 키에 연관된 값을 반환합니다.
       예를 들어 d = {'x': 11, 'b': 12}이면 get_min은 12를 반환합니다"""
    min_key = None
    min_val = None
    for key, val in d.items():
        if min_key == None or min_key > key:
            min_key = key
            min_val = val
    return min_key, min_val

d = {'e': 1, 'b': 3, 'c': 0 }
print(get_min(d))