from django.shortcuts import render, redirect
from .forms import UserForm

def registr(request):
    '''Функция вызывается из файла registr/urls.py
    возваращет render, получив от браузера запрос request, далье уже переходит на отображение 
    нашей html-странички'''
    form = UserForm(request.POST or None)
    if request.method == 'POST':
        new_form = form.save()
        #return redirect('login/')
        #print(new_form)
    return render(request,'users/register.html', locals())


