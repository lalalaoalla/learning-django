from django.contrib import admin
from .models import *# из файла odels, который находится в нашей папке импортируем все

admin.site.register(Users)#берем в админ сайт, регистр, говорим, что мы хотим зарегистрироваться