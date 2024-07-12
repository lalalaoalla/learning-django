from django import forms 
from .models import *


class MakingAnOrderForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите имя'}))
    firstname = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите фамилию'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'you@example.com'}))
    address = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Россия, Москва, ул. Мира 6'}))
    
    class Meta:
        model = MakingAnOrder
        fields = ['name','firstname','email', 'address']

# class UserForm(forms.ModelForm):

#     name = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'form-control py-4', 'placeholder': 'Введите имя'}))
#     firstname = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'form-control py-4', 'placeholder': 'Введите фамилию'}))
#     nickname = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'form-control py-4', 'placeholder': 'Введите имя пользователя'}))
#     email = forms.CharField(widget=forms.EmailInput(attrs={
#         'class': 'form-control py-4', 'placeholder': 'Введите адрес эл. почты'}))
#     password = forms.CharField(widget=forms.PasswordInput(attrs={
#         'class': 'form-control py-4', 'placeholder': 'Введите пароль'}))

#     class Meta:
#         model = User
#         #fields = [''] - поля которые нужно включить
#         exclude = ['']#поля которые нужно исключить, пишем обычно что-то одно