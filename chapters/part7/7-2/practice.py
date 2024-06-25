import calendar as cal

def find_thanksgiving(year):
    month = cal.monthcalendar(year, 11)
    if month[0][cal.THURSDAY] != 0:
        thanksgiving = month[3][cal.THURSDAY]
    else:
        thanksgiving = month[4][cal.THURSDAY]
    return thanksgiving

# 사양을 만족하는 함수
def shopping_days(year):
    """year >= 1941이다.
        미국 추수감사절과 크리스마스 사이의 일수를 반환한다."""
    thanksgiving_day = find_thanksgiving(year)
    return 30-thanksgiving_day+25-1

print(shopping_days(2022))


# 캐나다 추수감사절(10월 두번째 월요일) 크리스마스와
def find_canada_thansgiving(year):
    month = cal.monthcalendar(year,10)
    if month[0][cal.MONDAY] != 0:
        thanksgiving = month[1][cal.MONDAY]
    else:
        thanksgiving = month[2][cal.MONDAY]
    return thanksgiving

def shopping_canada_days(year):
    thanksgiving = find_canada_thansgiving(year)
    return 31-thanksgiving+30+25-1

print(shopping_canada_days(2022))
