from django.shortcuts import render

def login(request):
    '''Функция вызывается из файла login/urls.py
    возваращет render, получив от браузера запрос request, далье уже переходит на отображение 
    нашей html-странички'''
    return render(request,'users/login.html', locals())


