# s에 sub가 등장하지 않으면 s.find(sub)이 무엇을 반환하나?
s = 'ttt'
sub = 'ccc'
print(s.find(sub)) # -1 반환

# find를 사용하여 다음 사양을 만족하는 함수를 구현
def find_last(s, sub):
    """s와 sub는 빈 문자열이 아니다.
        s에서 sub가 마지막으로 등장하는 인덱스를 반환한다.
        s에서 sub가 등장하지 않으면 None을 반환한다."""
    if s.find(sub) < 0:
        return None
    else:
        return len(s) - s[::-1].find(sub[::-1]) + len(sub)


print(find_last('abcdefdefdefeedefaadee', 'def'))