from django.shortcuts import render
from .models import *

def catalog(request):
    '''Функция вызывается из файла catalog/urls.py
    возваращет render, получив от браузера запрос request, далье уже переходит на отображение 
    нашей html-странички'''
    
    category_id = request.GET.get('category')#строка в браузере

    category_one = category_id==1#пока не рабочая фигня
    category_two = category_id==2

    categories = CategoryProduct.objects.all()#для считывания названий категорий

    products = Product.objects.filter(is_active=True)#сейчас уже не нужен вроде но пусть будет

    product_images = ImagesInProduct.objects.all()#для считывания товаров и фоток и всего их

    category_new_products = product_images.filter(product__category__id=1)# переменные для использования категорий товаов
    category_clothes = product_images.filter(product__category__id=2)

    #title = 'Store-каталог'
    
    context = {'page_title' : 'Store-каталог','categories' : categories, 'products' : products, 'product_images' : product_images,
               'category_clothes' : category_clothes,'category_new_products' : category_new_products,
               'category_one' : category_one, 'category_two' : category_two}
    return render(request,'products.html', context)
#Почему-то с отдельными функциями не работает, может ей не нравится, что я ссылаюсь на одну и ту же страницу
#что вполне может быть

# def products(request):
#     '''Функция для выводы товаров'''
#     products = Product.objects.filter(is_active=True)# выводим только активные объекты
#     return render(request, 'products.html', locals())

# def categories(request):
#     '''Функция для вывода категорий'''
#     categories = CategoryProduct.objects.all()
#     context = {'categories' : categories}
#     return render(request, 'products.html', context)