from django.shortcuts import render
from .forms import MakingAnOrderForm

def orders(request):
    '''Функция вызывается из файла orders/urls.py
    возваращет render, получив от браузера запрос request, далье уже переходит на отображение 
    нашей html-странички'''
    return render(request,'orders/orders.html', locals())

def create_order(request):
    '''Функция вызывается из файла orders/urls.py
    возваращет render, получив от браузера запрос request, далье уже переходит на отображение 
    нашей html-странички'''
    form = MakingAnOrderForm(request.POST or None)
    if request.method == 'POST':
        new_form = form.save()
    return render(request,'orders/order-create.html', locals())
