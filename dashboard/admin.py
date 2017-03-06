from django.contrib import admin

import models
# Register your models here.

admin.site.register(models.Members)
admin.site.register(models.Gym)
admin.site.register(models.GymPlan)
admin.site.register(models.PaymentPeriod)
admin.site.register(models.GymActivity)
admin.site.register(models.FightTeam)
admin.site.register(models.PaymentRecord)
admin.site.register(models.GymCheckin)
