# 사양을 만족하는 함수 (try-except 사용)
def sum_digits(s):
    """s는 문자열이라고 가정한다.
        s에 있는 숫자의 합을 반환한다.
        예를 들어 s가 'a2b3c'라면 5를 반환한다.""" 
    sum = 0
    for c in s:
        try:
            sum += int(c)
        except (ValueError):
            continue
    return sum


print(sum_digits('a2b3c'))