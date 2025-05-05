from django import forms
from .models import LogoOrder


class LogoOrderForm(forms.ModelForm):
    class Meta:
        model = LogoOrder
        fields = ['full_name', 'contact', 'description']
        labels = {
            'full_name': 'Фамилия Имя',
            'contact': 'Контактный телефон или Телеграм',
            'description': 'Какие пожелания для логотипа?',
        }
        widgets = {
            'description': forms.Textarea(attrs={'rows':4}),
        }