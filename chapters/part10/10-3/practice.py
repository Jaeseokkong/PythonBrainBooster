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

    # 다음 사양을 마족하는 제너레이터를 추가
    def get_students_above(self, grade):
        """평균 점수가 grade보다 큰 학생을 한 번에 하나씩 반환한다."""
        for s in self._students():
            grades = self.get_grades()
            if len(grades) > 0 and sum(grades)/len(grades) > grade:
                yield s