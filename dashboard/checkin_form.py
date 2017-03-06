from django import forms

from .models import GymCheckin
from time import gmtime, strftime

class MembersCheckinForm(forms.ModelForm):

    class Meta:
        model = GymCheckin
        fields = ["gym_id"]

        # right now not working...
        def save(self, commit=True, *args, **kwargs):
            obj = super(MembersCheckinForm, self).save(commit=False, *args, **kwargs)
            obj.status = True

            if commit:
                obj.save()
            return obj
