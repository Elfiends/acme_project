from django import forms


from .models import Birthday, Congratulation


from django.core.exceptions import ValidationError

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()


BEATLES = {'Джон Леннон', 'Пол Маккартни', 'Джордж Харрисон', 'Ринго Старр'}


class BirthdayForm(forms.ModelForm):

    class Meta:
        def clean_first_name(self):
        # Получаем значение имени из словаря очищенных данных.
            first_name = self.cleaned_data['first_name']
        # Разбиваем полученную строку по пробелам 
        # и возвращаем только первое имя.
            return first_name.split()[0]

        def clean(self):
        # Получаем имя и фамилию из очищенных полей формы.
            super().clean()
            first_name = self.cleaned_data['first_name']
            last_name = self.cleaned_data['last_name']
        # Проверяем вхождение сочетания имени и фамилии во множество имён.
            if f'{first_name} {last_name}' in BEATLES:
                raise ValidationError(
                    'Мы тоже любим Битлз, но введите, пожалуйста, настоящее имя!'
                )
        model = Birthday
        exclude = ('author',)
        widgets = {
            'birthday': forms.DateInput(
                attrs={'type': 'date'},
                format='%Y-%m-%d',
            )               
        }


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User


class CongratulationForm(forms.ModelForm):

    class Meta:
        model = Congratulation
        fields = ('text',)
