#  캡슐화와 정보 은닉
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
## Grades 클래스
class Grades(object):

    def __init__(self):
        """빈 성적표를 만든다."""
        self._students = []
        self._grades = {}
        self._is_sorted = True

    def add_student(self, student):
        """가정: student는 Student 타입이다
            student를 성적표에 추가한다."""
        if student in self._students:
            raise ValueError('Duplicate student')
        self._students.append(student)
        self._grades[student.get_id_num()] = []
        self._is_sorted = False
    
    def add_grade(self, student, grade):
        """가정: grade는 float이다.
            grade를 student의 성적 목록에 추가한다."""
        try:
            self._grades[student.get_id_num()].append(grade)
        except:
            raise ValueError('존재하지 않은 학생이다.')
        
    def get_grades(self, student):
        """학생의 성적 목록을 반환한다."""
        try:
            return self._grades[student.get_id_num()]
        except:
            raise ValueError('존재하지 않은 학생이다.')
    
    def get_students(self):
        """알파벳 순서대로 한 번에 하나씩 학생을 반환한다."""
        if not self._is_sorted:
            self._students.sort()
            self._is_sorted = True
        for s in self._students:
            yield s


## 성적 리포트 생성하기
def grade_report(course):
    """course는 Grades 타입이라 가정한다."""
    report = ''
    for s in course.get_students():
        tot = 0.0
        num_grades = 0
        for g in course.get_grades(s):
            tot += g
            num_grades += 1
        try:
            average = tot/num_grades
            report = f"{report}\n{s}의 평균 점수는 {average}이다."
        except ZeroDivisionError:
            report = f"{report}\n{s}은(는) 받은 점수가 없다."
    return report

ug1 = UG('Jane Doe', 2021) 
ug2 = UG('Pierce Addison', 2041) 
ug3 = UG('David Henry', 2003) 
g1 = Grad('Billy Buckner') 
g2 = Grad('Bucky F. Dent') 
six_hundred = Grades() 
six_hundred.add_student(ug1) 
six_hundred.add_student(ug2) 
six_hundred.add_student(g1) 
six_hundred.add_student(g2) 
for s in six_hundred.get_students(): 
    six_hundred.add_grade(s, 75) 
six_hundred.add_grade(g1, 25) 
six_hundred.add_grade(g2, 100) 
six_hundred.add_student(ug3) 
print(grade_report(six_hundred)) 

### 캡슐화 : 데이터 속성과 이 속성에 동작하는 메서드가 함께 묵여 있음
### 정보 은닉 : 속성 이름이 __로 시작하지만 __로 끝나지 않으면 이 속성은 클래스 밖에서는 보지이 않는다.

## 클래스의 정보 은닉
class InfoHiding(object):

    def __init__(self):
        self.visible = '이 변수는 볼 수 있다.'
        self.__also_visible__ = '이 변수도 볼 수 있다.'
        self.__invisible = '이 변수는 직접 볼 수 없다.'
    
    def print_visible(self):
        print(self.visible)

    def print_invisible(self):
        print(self.__invisible)

    def __print_visible(self):
        print(self.__invisible)

    def __print_invisible__(self):
        print(self.__invisible)
    
test = InfoHiding()
print(test.visible)
print(test.__also_visible__)
#print(test.__invisible) #예외 발생 
test.print_invisible()
test.__print_invisible__()
#test.__print_visible() #예외 발생

class SubClass(InfoHiding):
    def new_print_invisible(self):
        print(self.__invisible)
    
test_sub = SubClass()
#test_sub.new_print_invisible() #예외 발생

# 제너레이터
## get_students의 새 버전
def get_students(self):
    """알파벳 순서대로 한 번에 하났기 반환한다."""
    if not self._is_sorted:
        self._students.sotr()
        self._is_sorted = True
    for s in self._students:
        yield s # 제너레이터
    # for 루프가 첫 번째 반복될 때 제너레이터가 호출되어 yield문장을 만날때 까지 실행
    # 그다음 yield문장에 잇는 표현식의 값이 반환
    # 다음번 반복에서 제너레이터는 yield바로 다음부터 실행을 재개

book = Grades()
book.add_student(Grad('Julie'))
book.add_student(Grad('Lisa'))
for s in book.get_students():
    print(s)

