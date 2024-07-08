from django.shortcuts import render

def registr(request):
    '''Функция вызывается из файла registr/urls.py
    возваращет render, получив от браузера запрос request, далье уже переходит на отображение 
    нашей html-странички'''
    return render(request,'users/register.html', locals())


