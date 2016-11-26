from .models import PaymentRecord
import datetime
from dateutil.relativedelta import relativedelta

def months_between(date1, date2):
    if date1 > date2:
        date1, date2 = date2, date1
    m1 = date1.year * 12 + date1.month
    m2 = date2.year * 12 + date2.month
    months = m2 - m1
    if date1.day > date2.day:
        months -= 1
    return months


class PaymentGenerator:

    @staticmethod
    def generateRecord(member):
        # auto generate the payment record from the join date to current date
        joinDate = member.join_date
        period = member.payment_period
        now = datetime.datetime.now().date()
        num_of_records = months_between(joinDate, now)

        for index in range(num_of_records):
            date_after_month = joinDate + relativedelta(months=1)
            record = PaymentRecord(uid=member,
                                   invoice_number=index,
                                   begin_period=joinDate.strftime('%Y-%m-%d'),
                                   end_period=date_after_month.strftime('%Y-%m-%d'),
                                   member_fee=100,
                                   pay_status=False)
            record.save()
            joinDate = joinDate + relativedelta(months=1)
