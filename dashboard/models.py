from __future__ import unicode_literals
from django.db import models


class Gym(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=400)

    def __str__(self):
        return self.name + ": " + self.address


class Members(models.Model):
    gym = models.ForeignKey(Gym, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    vorname = models.CharField(max_length=200)
    street1 = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    postcode = models.CharField(max_length=10)
    email_name = models.EmailField()
    mobile = models.CharField(max_length=50, blank=True)
    uuid = models.CharField(max_length=200, unique=True, null=False)
    birth_date = models.DateField(null=True, blank=True)
    join_date = models.DateField()
    gym_plan = models.CharField(max_length=50)
    payment_period = models.IntegerField(default=12)
    teams = models.CharField(max_length=200, null=True, blank=True)
    gym_act = models.CharField(max_length=500, null=True, blank=True)
    member_pic = models.ImageField(upload_to='images/', default='images/no-image-available.jpg')

    def __str__(self):
        return '{} {}'.format(self.vorname, self.name)


class GymCheckin(models.Model):
    gym_id = models.CharField(max_length=200, null=False)
    checkin_time = models.DateTimeField(auto_now=True, auto_now_add=False)
    status = models.BooleanField()

    def __str__(self):
        return 'ID: {}, Checkin: {}, Status: {}'.format(self.gym_id, self.checkin_time, self.status)


class GymPlan(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=300, null=True)
    price = models.CharField(max_length=300, null=True)

    def __str__(self):
        return 'Plan {}: {}'.format(self.name, self.price)


class PaymentPeriod(models.Model):
    one = '1'
    three = '3'
    six = '6'
    year = '12'
    PERIOD = (
        (one, '1 month'),
        (three, '3 months'),
        (six, '6 months'),
        (year, '12 months'),
    )
    period = models.CharField(
        max_length=2,
        choices=PERIOD,
        default=one,
    )

    def __str__(self):
        return '{}'.format(self.period)


class GymActivity(models.Model):
    plan = models.ForeignKey(GymPlan, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=300, null=True)

    def __str__(self):
        return '{}'.format(self.name)


class FightTeam(models.Model):
    team = models.CharField(max_length=100)
    desc = models.CharField(max_length=300, null=True)

    def __str__(self):
        return '{}'.format(self.team)


class PaymentRecord(models.Model):
    uid = models.ForeignKey(Members)
    invoice_number = models.CharField(max_length=10)
    begin_period = models.DateField(auto_now=False)
    end_period = models.DateField(auto_now=False)
    member_fee = models.FloatField(default=0)
    pay_status = models.BooleanField(default=None)

    def __str__(self):
        return '{}: {}-{}'.format(self.uid, self.begin_period, self.end_period)


class InvoiceNumber(models.Model):
    invoiceId = models.PositiveIntegerField(default=10000001)