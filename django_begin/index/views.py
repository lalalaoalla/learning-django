from django.shortcuts import render

def index(request):
    '''Функция вызывается из файла index/urls.py
    возваращет render, получив от браузера запрос request, далье уже переходит на отображение 
    нашей html-странички'''
    return render(request,'index.html', locals())

def catalog(request):
    return render(request,'products.html', locals())
