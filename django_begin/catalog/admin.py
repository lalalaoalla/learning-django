from django.contrib import admin
from .models import *# из файла odels, который находится в нашей папке импортируем все




class CategoryProductAdmin(admin.ModelAdmin):
#     #list_display = ['name', 'firstname','nickname','email','password']# поля для отображения без id
    list_display = [field.name for field in CategoryProduct._meta.fields]# это если слишком много полей, и не хочется писать самой
#     exclude = ['email']# это уже при захождении на конкретную запись, те поля, которые мы не хотим смотреть, тое сть их нельзя менять 
#     #fields = []# то же самое в целом, только какие хотим видеть
#     list_filter = ['firstname','name',]#в общем это наш фильтр, можно фильтровать по нескольким полям, ГЛАВНОЕ НЕ ЗАБЫТЬ , В КОНЦЕ
#     search_fields = ['name', 'firstname']# это поиск по какому-то столбцу, можно набрать имя и увидеть всех с эти именем

    class Meta:
        model = CategoryProduct

class ProductAdmin(admin.ModelAdmin):
#     #list_display = ['name', 'firstname','nickname','email','password']# поля для отображения без id
    list_display = [field.name for field in Product._meta.fields]# это если слишком много полей, и не хочется писать самой
#     exclude = ['email']# это уже при захождении на конкретную запись, те поля, которые мы не хотим смотреть, тое сть их нельзя менять 
#     #fields = []# то же самое в целом, только какие хотим видеть
#     list_filter = ['firstname','name',]#в общем это наш фильтр, можно фильтровать по нескольким полям, ГЛАВНОЕ НЕ ЗАБЫТЬ , В КОНЦЕ
#     search_fields = ['name', 'firstname']# это поиск по какому-то столбцу, можно набрать имя и увидеть всех с эти именем

    class Meta:
        model = Product


class ImagesInProductAdmin(admin.ModelAdmin):
#     #list_display = ['name', 'firstname','nickname','email','password']# поля для отображения без id
    list_display = [field.name for field in ImagesInProduct._meta.fields]# это если слишком много полей, и не хочется писать самой
#     exclude = ['email']# это уже при захождении на конкретную запись, те поля, которые мы не хотим смотреть, тое сть их нельзя менять 
#     #fields = []# то же самое в целом, только какие хотим видеть
#     list_filter = ['firstname','name',]#в общем это наш фильтр, можно фильтровать по нескольким полям, ГЛАВНОЕ НЕ ЗАБЫТЬ , В КОНЦЕ
#     search_fields = ['name', 'firstname']# это поиск по какому-то столбцу, можно набрать имя и увидеть всех с эти именем

    class Meta:
        model = ImagesInProduct
# admin.site.register(User, UserAdmin)#типа наш класс UserAdmin перезапишет с теми полями, которые нам нужны

# #ЕСЛИ СИЛЬНО ЗАХОЧЕТСЯ:

# #выводит лишь одно единственное поле - users, в файле registr/models.py - написано то, что мы хотим
# #выводить в этом поле
# admin.site.register(CategoryProduct)#берем в админ сайт, регистр, говорим, что мы хотим зарегистрироваться
# admin.site.register(Product)
# admin.site.register(ImagesInProduct)

