from django import forms
from django.core.validators import RegexValidator

from .models import User


class UserRegistrationForm(forms.ModelForm):
    '''
    форма для создания и обновления пользователя
    '''
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Подтверждение пароля',
                                widget=forms.PasswordInput)

    phone_regex = RegexValidator(regex=r'^(?:\+7|8)\d{10}$',
                                 message="Неверный формат номера телефона")
    phone_number = forms.CharField(
        label='Номер телефона',
        validators=[phone_regex],
        max_length=12,
        required=True
    )

    date_of_birth = forms.DateField(label='Дата рождения',
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email',
                  'date_of_birth', 'phone_number']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Пароли не совпадают")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


# class LoginForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('username', 'password')
