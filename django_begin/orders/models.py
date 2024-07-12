#модель - описание таблицы в базе данных
#наша база данных(корзина короче у нас тут да), будет содеражть данные поля:
from django.db import models
from catalog.models import Product
from django.db.models.signals import post_save




class Status(models.Model):
    '''Статус заказа'''
    name = models.CharField(max_length=24)
    is_avtive = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)#дата добавления заказа
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)#дата обновления чего-нибудь в таблице?

    def __str__(self):
        return "%s" % self.name
    
    class Meta:
        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Статусы заказа'



class MakingAnOrder(models.Model):#таблица с оформленным заказом
    ''' ОФОРМЛЕНИЕ ЗАКАЗА
    
    model.Model связывает наш класс Users c  бд, также создаст таблицу users, также предоставляет
    возможность создания полей с определенными типами, при добавлении нового поля используются 
    миграции'''

    name = models.CharField(max_length = 100)
    firstname = models.CharField(max_length=128)
    email = models.EmailField()
    address = models.CharField(max_length=512)
    status = models.ForeignKey(Status, default=True, on_delete=models.DO_NOTHING)
    total_price_in_order = models.FloatField(default=0)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)#дата добавления заказа
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)#дата обновления чего-нибудь в таблице?


    def __str__(self):#в данном случае эта функция показывает, что должно высвечиваться в таблице
            return"Заказ %s" % self.id#self.status)
    
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
    def save(self,*args,**kwargs):
        super(MakingAnOrder, self).save(*args,**kwargs)
        
class ProductInBasket(models.Model):#здесь я еще подумаю, стоит может order перенести в другой класс
    '''СОДЕРЖИМОЕ КОРЗИНЫ
    содержит связь с оформлением заказа, а также мы берем названия из таблицы с товарами'''
    order = models.ForeignKey(MakingAnOrder, blank=True, null=True, default=None, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.DO_NOTHING)#модели товара еще нет, но они связаны
    quantity = models.IntegerField(blank=True, null=True, default=1)
    price_one_product =models.FloatField(default=1)
    total_price = models.FloatField(default=1)#price* quantity
    is_active = models.BooleanField(default=True)#типа что заказ можем отменить ес что
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.product.name

    class Meta:
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товары в корзине'
    def save(self,*args,**kwargs):
        price_one_product = self.product.price
        self.price_one_product = price_one_product
        self.total_price = self.quantity* price_one_product
        super(ProductInBasket, self).save(*args,**kwargs)

def product_in_order_post_save(sender, instance,created,**kwargs):
        order = instance.order#вместо self надо писать instance
        all_products_in_order = ProductInBasket.objects.filter(order = order,is_active=True)

        total_price_in_order = 0
        for item in all_products_in_order:
            total_price_in_order+=item.total_price

        order.total_price_in_order = total_price_in_order
        order.save(force_update=True)

post_save.connect(product_in_order_post_save, sender = ProductInBasket)

    
