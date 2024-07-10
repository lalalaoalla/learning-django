from django.contrib import admin
from .models import *# из файла odels, который находится в нашей папке импортируем все




class UserAdmin(admin.ModelAdmin):
    #list_display = ['name', 'firstname','nickname','email','password']# поля для отображения без id
    list_display = [field.name for field in User._meta.fields]# это если слишком много полей, и не хочется писать самой
    exclude = ['email']# это уже при захождении на конкретную запись, те поля, которые мы не хотим смотреть, тое сть их нельзя менять 
    #fields = []# то же самое в целом, только какие хотим видеть
    list_filter = ['firstname','name',]#в общем это наш фильтр, можно фильтровать по нескольким полям, ГЛАВНОЕ НЕ ЗАБЫТЬ , В КОНЦЕ
    search_fields = ['name', 'firstname']# это поиск по какому-то столбцу, можно набрать имя и увидеть всех с эти именем

    class Meta:
        model = User

admin.site.register(User, UserAdmin)#типа наш класс UserAdmin перезапишет с теми полями, которые нам нужны

#ЕСЛИ СИЛЬНО ЗАХОЧЕТСЯ:

#выводит лишь одно единственное поле - users, в файле registr/models.py - написано то, что мы хотим
#выводить в этом поле
#admin.site.register(User)#берем в админ сайт, регистр, говорим, что мы хотим зарегистрироваться


