# 팰린드롬 (한 문자열을 거꾸로 읽었을 때 동일한 문자열)
## 팰린드롬 테스트
def is_palindrome(s):
    """s는 문자열이라 가정한다.
        s에 있는 문자가 팰린드롬이면 True, 그렇지 않으면 False를 반환한다.
        알파벳 이외의 문자와 대소문자는 무시한다."""
    
    def to_chars(s):
        s = s.lower()
        letters = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                letters = letters + c
        return letters
    
    def is_pal(s):
        print(s)
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and is_pal(s[1:-1])
    
    return is_pal(to_chars(s))

print(is_palindrome('asdffdsa'))

## 팰린드롬 테스트 시각화 코드
def is_palindrome2(s):
    """s는 문자열이라 가정한다.
        s에 있는 문자가 팰린드롬이면 True, 그렇지 않으면 False를 반환한다.
        알파벳 이외의 문자와 대소문자는 무시한다."""
    
    def to_chars(s):
        s = s.lower()
        letters = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                letters = letters + c
        return letters
    
    def is_pal(s):
        print(' is_pal 호출 :', s)
        if len(s) <= 1:
            print(' True 반환: 베이스 케이스')
            return True
        else:
            # 단락 평가 and 연산자 왼쪽 조건부터 평가하며 False인 경우 오른쪽 조건을 평가하지 않음
            answer = s[0] == s[-1] and is_pal(s[1:-1])
            print('', answer, '반환:', s)
            return answer
    
    return is_pal(to_chars(s))

print(is_palindrome2('assdfcdefdssa'))