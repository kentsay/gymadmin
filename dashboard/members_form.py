from django import forms

from .models import Members


class MembersForm(forms.ModelForm):

    class Meta:
        model = Members
        fields = ('gym', 'name', 'vorname', 'street1', 'city', 'postcode', 'mobile', 'email_name',
                  'birth_date', 'join_date', 'uuid', 'stu_discount', 'gym_plan', 'payment_period',
                  'teams', 'gym_act')
