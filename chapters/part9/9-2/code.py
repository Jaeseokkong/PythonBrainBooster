# 제어 흐름 메커니즘으로 예외 사용하기
## 점수 얻기
def get_grades(fname):
    grades = []
    try:
        with open(fname, 'r') as grades_file:
            for line in grades_file:
                try:
                    grades.append(float(line))
                except:
                    raise ValueError('읽어 들인 라인을 float과 바꿀 수 없다.')
    except IOError: # open 함수의 에러 발생시
        raise ValueError('get_grades가 다음 파일을 열 수 없다.:'+ fname)
    return grades
    
try:
    grades = get_grades('quiz1grades.txt')
    grades.sort()
    median = grades[len(grades)//2]
    print('점수의 중앙값:',median)
except ValueError as error_msg:
    print('에러', error_msg)