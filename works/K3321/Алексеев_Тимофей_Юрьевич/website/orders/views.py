from django.shortcuts import render, redirect
from .forms import LogoOrderForm


def home(request):
    return render(request, 'orders/home.html')


def order_logo(request):
    if request.method == 'POST':
        form = LogoOrderForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'orders/order_success.html')
    else:
        form = LogoOrderForm()
    return render(request, 'orders/order_logo.html', {'form': form})