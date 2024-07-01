# 고급 예제
## Mortgage 클래스
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
    
## Mortgage 서브 클래스
class Fixed(Mortgage):
    def __init__(self, loan, r, months):
        Mortgage.__init__(self, loan, r, months)
        self._legend = f'고정, {r*100:.1f}5'

class FixedWithPts(Mortgage):
    def __init__(self, loan, r, months, pts):
        Mortgage.__init__(self, loan, r, months)
        self._pts = pts
        self._paid = [loan*(pts/100)]
        self._legend = f'고정, {r*100:.1f}%, {pts} 포인트'
    
class TwoRate(Mortgage):
    def __init__(self, loan, r, months, teaser_rate, teaser_months):
        Mortgage.__init__(self, loan, teaser_rate, months)
        self._teaser_months = teaser_months
        self._teaser_rate = teaser_rate
        self._nextRate = r/12
        self._legend = (f'{self._teaser_months}달 동안 {100*teaser_rate:1f}%, 그다음엔 {100*r:.1f}%')

    def make_payment(self):
        if len(self._paid) == self._teaser_months + 1:
            self._rate = self._nextRate
            self._payment = find_payment(self._outstanding[-1], self._rate, self._months - self._teaser_months)

def compare_mortgages(amt, years, fixed_rate, pts, pts_rate, var_rate1, var_rate2, var_months):
    tot_months = years*12
    fixed1 = Fixed(amt, fixed_rate, tot_months)
    fixed2 = FixedWithPts(amt, pts_rate, tot_months, pts)
    two_rate = TwoRate(amt, var_rate2, tot_months, var_rate1, var_months)
    morts = [fixed1, fixed2, two_rate]
    for m in range(tot_months):
        for mort in morts:
            mort.make_payment()
    for m in morts:
        print(m)
        print(f'총상환액 = ${m.get_total_paid():,.0f}')


compare_mortgages(amt=200000, years=30, fixed_rate=0.035, 
                  pts = 2, pts_rate=0.03, var_rate1=0.03, 
                  var_rate2=0.05, var_months=60) 