from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def catalog(request):
    '''Функция вызывается из файла catalog/urls.py
    возваращет render, получив от браузера запрос request, далье уже переходит на отображение 
    нашей html-странички'''
    #номер нашей категории в строке в браузере(после "?")
    category_id = request.GET.get('category')

    categories = CategoryProduct.objects.all()# переменная, считавшая все категории
    products = Product.objects.filter(is_active=True)# переменная для продуктов(опять же она не особо нужна,наверное, для считывания)
    product_images = ImagesInProduct.objects.all()#переменная, считавшая продукты

    #Если у нас есть категории айди
    if category_id:
        #то наша category_products  получает продукты считанные с этим айди
        category_products = product_images.filter(product__category__id=category_id)
    else:
        #иначе - считываем наши новинки
        category_products = product_images.filter(product__category__id=1)

    #для пагинации
    paginator = Paginator(category_products, 6)# то есть, у нас на странице будет 6 товаров
    page_number = request.GET.get('page')#получаем номер нашей страницы

    try:
        page = paginator.page(page_number)#указание на страницу
    except PageNotAnInteger:#это если что как бы название ошибки, да, раньше я не использовала
        # Если номер страницы не целое число, используйте первую страницу
        page = paginator.page(1)
    except EmptyPage:
        # Если номер страницы слишком большой, используйте последнюю страницу
        page = paginator.page(paginator.num_pages)

    context = {
        'page_title': 'Store-каталог',
        'categories': categories,
        'products': products,
        'product_images': product_images,
        'category_products': category_products,
        'page' : page,
    }
    return render(request, 'products.html', context)
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