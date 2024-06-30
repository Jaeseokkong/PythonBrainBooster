# 학생 관리를 위한 클래스
import datetime

## Person 클래스
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

me = Person('Michael Guttag') 
him = Person('Barack Hussein Obama') 
her = Person('Madonna') 
print(him.get_last_name()) 
him.set_birthday(datetime.date(1961, 8, 4)) 
her.set_birthday(datetime.date(1958, 8, 16)) 
print(him.get_name(), '의 나이는', him.get_age(), '일 입니다') 

pList = [me, him, her]
for p in pList:
    print(p)
pList.sort() # Person 클래스에 정의된 __lt__ 메서드로 리스트가 정렬된다.
for p in pList:
    print(p)