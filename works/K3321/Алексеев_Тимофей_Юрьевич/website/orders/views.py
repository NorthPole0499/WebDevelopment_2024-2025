from django.shortcuts import render, redirect
from datetime import datetime
from .forms import LogoOrderForm


def home(request):
    return render(request, 'orders/home.html', {'current_year': datetime.now().year})


def about(request):
    return render(request, 'orders/about.html', {'current_year': datetime.now().year})


def order_logo(request):
    if request.method == 'POST':
        form = LogoOrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_success')
    else:
        form = LogoOrderForm()

    return render(request, 'orders/order_logo.html', {'form': form, 'current_year': datetime.now().year})


def order_success(request):
    return render(request, 'orders/order_success.html', {'current_year': datetime.now().year})