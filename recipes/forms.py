from django import forms
from django.utils.translation import gettext as _


class ReviewForm(forms.Form):
    text = forms.CharField(label=_("Комментарий"), required=False)
    rating = forms.IntegerField(label=_("Рейтинг"), max_value=5, min_value=1)


class LoginForm(forms.Form):
    username = forms.CharField(label=_("Имя пользователя"))
    password = forms.CharField(label=_("Password"), widget=forms.PasswordInput)


class RegistrationForm(LoginForm):
    email = forms.EmailField(label=_("Email"))
