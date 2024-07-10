# #модель - описание таблицы в базе данных
# #наша база данных(регистрация у нас тут да), будет содеражть данные поля:
from django.db import models

class CategoryProduct(models.Model):
    '''Категории наших товаров, они будт связаны с таблицей товаров'''
    name = models.CharField(max_length=64)
    
    def __str__(self):
        return "%s" % self.name