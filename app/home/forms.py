from django import forms


class ProfileForm(forms.Form):
    main_char = forms.CharField(max_length=32)
    main_class = forms.CharField(max_length=32)
    main_role = forms.CharField(max_length=32)
    user_description = forms.CharField(required=False)
    show_in_roster = forms.BooleanField(required=False)


class NewsForm(forms.Form):
    title = forms.CharField(max_length=64)
    display_name = forms.CharField(max_length=32)
    description = forms.CharField()
