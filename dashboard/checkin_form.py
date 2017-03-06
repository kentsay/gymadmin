from django import forms

from .models import GymCheckin, Members


class MembersCheckinForm(forms.ModelForm):
    class Meta:
        model = GymCheckin
        fields = ["gym_id"]

    def save(self, commit=True, *args, **kwargs):
        obj = super(MembersCheckinForm, self).save(commit=False, *args, **kwargs)
        obj.status = True# Default value

        if commit:
            obj.save()
        return obj
