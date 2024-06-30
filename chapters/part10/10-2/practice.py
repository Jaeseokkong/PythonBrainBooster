class Person(object):

    def __init__(self, name):
        """name은 문자열이라고 가정한다. Person 객체를 만든다."""
        self._name = name
        try:
            last_blank = name.rindex(' ')
            self._last_name = name[last_blank + 1:]
        except:
            self._last_name = name
        self.birthday = None
    
    def get_name(self):
        """self의 전체 이름을 반환한다."""
        return self._name
    
    def get_last_name (self):
        """self의 성을 반환한다."""
        return self._last_name
    
    def set_birthday(self, birthdate):
        """birthdate는 datetime.data 타입이라고 가정한다.
            self의 생일을 birthdate로 설정한다."""
        self._birthday = birthdate
    
    def get_age(self):
        """self의 현재 나이를 날짜 단위로 반환한다."""
        if self._birthday == None:
            raise ValueError
        return (datetime.date.today() - self._birthday).days
    
    # < 연산자을 오버로드한 메서드
    def __lt__(self, other):
        """other는 Person 객체라고 가정한다.
            self가 알파벳 순서로 other보다 앞에 있으면 True, 그렇지 않으면 False를 반환한다.
            성을 기준으로 비교하되 성이 같다면 전체 이름을 비교한다."""
        if self._last_name == other._last_name:
            return self._name < other._name
        return self._last_name < other._last_name
    
    def __str__(self):
        """self의 이름을 반환한다."""
        return self._name
    
# 다음 사양을 만족한는 Person의 서브 클래스 구현
class Politician(Person):
    """Politician은 한 정당에 소속될 수 있는 Person이다."""
    def __init__(self, name, party = None):
        """name과 party는 문자열이다."""
        super().__init__(name)
        self._party = party
    
    def get_party(self):
        """self가 소속된 정당을 반환한다."""
        return self._party
    
    def might_agree(self, other):
        """self와 other가 같은 정당에 속하거나 둘 중 하나가 정당에 소속되지 않으면 True,
            그렇지 않으면 False를 반환한다."""
        if self._party == other._party or self._party == None or other._party == None:
            return True
        return False
        

po1 = Politician('Jimmy', 'Demo')
po2 = Politician('Jack', 'Repub')
po3 = Politician('Sean', 'Demo')
po4 = Politician('Jay')

print(po1.might_agree(po2))
print(po1.might_agree(po3))
print(po1.might_agree(po4))

# 다음 표현식의 값은 무엇인가?
print(isinstance('ab', str) == isinstance(str, str)) #False
# print(isinstance('as', str)) #True
# print(isinstance(str, str)) #False