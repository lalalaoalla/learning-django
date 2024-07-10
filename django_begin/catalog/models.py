# #модель - описание таблицы в базе данных
# #наша база данных(регистрация у нас тут да), будет содеражть данные поля:
# from django.db import models

# class User(models.Model):#типа мы так описываем таблицу, что такое models.Model я пока хз, но внутри описывают поля таблицы
#     '''model.Model связывает наш класс Users c  бд, также создаст таблицу users, также предоставляет
#     возможность создания полей с определенными типами, при добавлении нового поля используются 
#     миграции'''
#     name = models.CharField(max_length = 100)
#     firstname = models.CharField(max_length=128)
#     nickname = models.CharField(max_length=32)
#     email = models.EmailField()
#     password = models.CharField(max_length=128)

#     def __str__(self):#в данном случае эта функция показывает, что должно высвечиваться в таблице
#             return"%s %s никнейм %s" % (self.firstname, self.name, self.nickname)#высвечивает 2(в нашем случае) и более(продолжаем %s) и наши поля после процента
        