# #модель - описание таблицы в базе данных
# #наша база данных(регистрация у нас тут да), будет содеражть данные поля:
from django.db import models

class CategoryProduct(models.Model):
    '''Категории наших товаров, они будт связаны с таблицей товаров'''
    name = models.CharField(max_length=64)
    
    def __str__(self):
        return "%s" % self.name
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    

class Product(models.Model):#типа мы так описываем таблицу, внутри описывают поля таблицы
    ''' ТАБЛИЦА ПРОДУКТОВ
    
    model.Model связывает наш класс Users c  бд, также создаст таблицу users, также предоставляет
    возможность создания полей с определенными типами, при добавлении нового поля используются 
    миграции'''

    name = models.CharField(max_length = 256)
    price = models.FloatField()
    description = models.TextField(blank=True, null=True, default=False)
    category = models.ForeignKey(CategoryProduct,blank=True, null=True, default=False,on_delete = models.DO_NOTHING)
    is_active = models.BooleanField(default=True)#хотим ли мы показывать товары
    created = models.DateTimeField(auto_now_add=True, auto_now=False)#дата добавления заказа
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)#дата обновления чего-нибудь в таблице?


    def __str__(self):#в данном случае эта функция показывает, что должно высвечиваться в таблице
            return" %s" % self.name
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class ImagesInProduct(models.Model):
    product = models.ForeignKey(Product, blank=True, null=True, default=False, on_delete = models.DO_NOTHING)
    image = models.ImageField(upload_to='vendor/media/products_images/')
    created = models.DateTimeField(auto_now_add=True, auto_now=False)#дата добавления заказа
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)#дата обновления чего-нибудь в таблице?

    def __str__(self):
        return "Фотографии для заказа %s" % self.product.name
    class Meta:
        verbose_name = 'Фото товара'
        verbose_name_plural = 'Фото товаров'