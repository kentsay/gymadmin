from .models import PaymentRecord, Members, InvoiceNumber
import datetime
import math
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


def get_gym_fee(gym_plan):
    print("gym plan ", gym_plan)
    return 100


class PaymentGenerator:

    @staticmethod
    def generateRecord():
        # auto generate the payment record from the join date to current date
        member_list = Members.objects.all()
        invoice_object = InvoiceNumber.objects.get()
        invoice_id = invoice_object.invoiceId

        for member in member_list:
            join_date = member.join_date
            period = member.payment_period
            now = datetime.datetime.now().date()
            num_of_records = months_between(join_date, now)/period
            if num_of_records == 0:
                num_of_records = 1
            exist_records = PaymentRecord.objects.filter(uid=member.id).count()

            if exist_records == num_of_records:
                pass
            else:
                for index in range(exist_records, num_of_records):
                    date_after_month = join_date + relativedelta(months=period)
                    record = PaymentRecord(uid=member,
                                       invoice_number=invoice_id,
                                       begin_period=join_date.strftime('%Y-%m-%d'),
                                       end_period=date_after_month.strftime('%Y-%m-%d'),
                                       member_fee=get_gym_fee(member.gym_plan),
                                       pay_status=False)
                    record.save()
                    invoice_id += 1
                    join_date = join_date + relativedelta(months=period)

        # update the latest invoice number into database
        invoice_object.invoiceId = invoice_id
        invoice_object.save()