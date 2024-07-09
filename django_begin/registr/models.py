#модель - описание таблицы в базе данных
#наша база данных(регистрация у нас тут да), будет содеражть данные поля:
from django.db import models

class Users(models.Model):#типа мы так описываем таблицу, что такое models.Model я пока хз, но внутри описывают поля таблицы
    '''model.Model связывает наш класс Users c  бд, также создаст таблицу users, также предоставляет
    возможность создания полей с определенными типами, при добавлении нового поля используются 
    миграции'''
    name = models.CharField(max_length = 100)
    firstname = models.CharField(max_length=128)
    nickname = models.CharField(max_length=32)
    email = models.EmailField()
    password = models.CharField(max_length=128)