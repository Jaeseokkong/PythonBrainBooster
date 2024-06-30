# 1.상속
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

## MIPerson 클래스
class MIPerson(Person): # Person의 속성을 상속 받는다.

    # 클래스 변수
    # 인스턴스 생성시 새로 만들어 지지않음
    _next_id_num = 0 #식별 번호

    def __init__(self, name):
        super().__init__(name)
        self._id_num = MIPerson._next_id_num
        MIPerson._next_id_num += 1

    def get_id_num(self):
        return self._id_num
    
    def __lt__(self, other):
        return self._id_num < other._id_num
    
    def is_student(self):
        return isinstance(self, Student) 
        #isinstance : 첫 번째 인수가 두 번째 인수의 인스턴스 이면 True 반환
    
p1 = MIPerson('Barbara Beaver')
print(str(p1) + '\'s 식별번호: ' + str(p1.get_id_num()))
# MIPerson 메서드 확인 후 Person 메서드 확인

p1 = MIPerson('Mark Guttag')
p2 = MIPerson('Biily Bob Beaver')
p3 = MIPerson('Biily Bob Beaver')
p4 = Person('Billy Bob Beaver')

# p1, p2, p3 : MIPerson 타입 
# p4 : Person 타입
print('p1 < p2 = ' , p1 < p2) #True
print('p3 < p2 = ' , p3 < p2) #Flase
print('p4 < p1 = ' , p4 < p1) #True 
# p4 < p1 의 경우 p4.__lt__(p1)

# print('p1 < p4 = ', p1 < p4)
# 예외 발생 :  Person은 _id_num 이 없으므로 예외 (p1.__lt__(p4))


# 2.다단계 상속
## 두 종류의 학생
class Student(MIPerson):
    pass # 슈퍼클래스에서 상속된 속성 이외에는 다른 속성이 없음을 나타냄

class UG(Student):
    def __init__(self, name, class_year):
        super().__init__(name)
        self._year = class_year
    
    def get_class(self):
        return self._yaer
    
class Grad(Student):
    pass

# 새로운 속성이 없는 클래스를 만드는 이유
p5 = Grad('Buzz Aldrin') 
p6 = UG('Billy Beaver', 1984) 
print(p5, '는 대학원생입니다:', type(p5) == Grad) 
print(p5, '는 학부생입니다:', type(p5) == UG) 
# 두 종류의 학생을 만들고 타입으로 두 객체를 구분할 수 있음

print(p5, '는 학생입니다:', p5.is_student())  # 
print(p6, '는 학생입니다:', p6.is_student())  # UG가 Student 서브클래스이므로, p6에 바인딩 된 객체는 Student 클래스의 인스턴스이다.
print(p3, '는 학생입니다:', p3.is_student()) 

# 전학생용 클래스
class TransferStudent(Student):

    def __init__(self, name, from_school):
        MIPerson.__init__(self, name)
        self._from_school = from_school

    def get_old_school(self):
        return self._from_school
    