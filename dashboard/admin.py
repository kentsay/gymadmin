from django.contrib import admin

# Register your models here.
from models import Members, Gym, GymPlan, PaymentPeriod, GymActivity, FightTeam

admin.site.register(Members)
admin.site.register(Gym)
admin.site.register(GymPlan)
admin.site.register(PaymentPeriod)
admin.site.register(GymActivity)
admin.site.register(FightTeam)
