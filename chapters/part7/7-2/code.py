# 사전에 정의된 패키지 사용하기
import math
x = 4
print(math.log(x, 3))

import calendar as cal
cal_english = cal.TextCalendar()
print(cal_english.formatmonth(1949, 3))

## 크리스마스
print(cal.day_name[cal.weekday(2033, 12, 25)])

def find_thanksgiving(year):
    month = cal.monthcalendar(year, 11)
    if month[0][cal.THURSDAY] != 0:
        thanksgiving = month[3][cal.THURSDAY]
    else:
        thanksgiving = month[4][cal.THURSDAY]
    return thanksgiving

print('2024년 미구 추수감사절은 11월', find_thanksgiving(2024), '입니다')