from django.shortcuts import render, redirect
from datetime import datetime
from .forms import LogoOrderForm
from .models import LogoOrder


def home(request):
    return render(request, 'orders/home.html', {'current_year': datetime.now().year})


def about(request):
    logo_order_count = LogoOrder.objects.count()

    context = {
        'logo_order_count': logo_order_count,
        'current_year': datetime.now().year,
    }
    return render(request, 'orders/about.html', context)


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