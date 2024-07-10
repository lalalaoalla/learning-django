from django.shortcuts import render

def profile(request):
    '''Функция вызывается из файла profile/urls.py
    возваращет render, получив от браузера запрос request, далье уже переходит на отображение 
    нашей html-странички'''
    return render(request,'users/profile.html', locals())


