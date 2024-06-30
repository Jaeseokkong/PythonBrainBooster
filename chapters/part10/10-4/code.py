# 고급 예제
def find_payment(loan, r, m):
    """가정: loan과 r은 floats, m은 int이다.
        m 개월 동안 월이자가 r일 때 모기지 금액 loan의 월 상환액을 반환한다."""
    return loan*((r*(1+r)**m)/((1+r)**m -1))

class Mortgage(object):
    """여러 종류의 모기지를 만드는 추상 클래스"""
    def __init__(self, loan, ann_rate, months):
        """가정: loan과 ann_rate는 float, month는 int이다.
            대출금 loan, 대출 기간 months, 연이율 ann_rate인 모기지를 만든다."""
        self._loan = loan
        self._rate = ann_rate/12
        self._months = months
        self._paid = [0.0]
        self._outstanding = [loan]
        self._payment = find_payment(loan, self._rate, months)
        self._legend = None #모기지 설명

    def make_payment(self):
        """월 상환액을 납입한다."""
        self._paid.append(self._payment)
        reduction = self._payment - self._outstanding[-1]*self._rate
        self._outstanding.append(self._outstanding[-1] - reduction)

    def get_total_paid(self):
        """지금까지 납입한 총금액을 반환한다."""
        return sum(self._paid)
    
    def __str__(self):
        return self._legend