from django.shortcuts import render

def catalog(request):
    '''Функция вызывается из файла catalog/urls.py
    возваращет render, получив от браузера запрос request, далье уже переходит на отображение 
    нашей html-странички'''
    return render(request,'products.html', locals())


