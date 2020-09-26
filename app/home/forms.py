from django import forms
from django.conf import settings


class ProfileForm(forms.Form):
    main_char = forms.CharField(max_length=32)
    main_class = forms.CharField(max_length=32)
    main_role = forms.CharField(max_length=32)
    user_description = forms.CharField(required=False)
    show_in_roster = forms.BooleanField(required=False)

    def clean_cm_rt(self):
        rt_id = Ticket.parse_rt_id(self.cleaned_data['cm_rt'])
        if rt_id:
            tracker = Ticket(settings.RT_HOST, settings.RT_USER, settings.RT_PASS, rt_id)
            if not tracker.active:
                raise forms.ValidationError('RT not active: {}'.format(rt_id))
            return int(rt_id)
