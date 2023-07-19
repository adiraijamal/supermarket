from django.shortcuts import render, get_object_or_404, redirect
from .forms import PurchaseForm
from .models import Purchase
from vendors.models import Vendor
from products.models import Product


def purchase_add(request):
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('purchases:purchase_list')
    else:
        form = PurchaseForm()
    
    return render(request, 'purchases/purchases_add.html', {'form': form})


def purchase_list(request):
    purchases = Purchase.objects.all()
    return render(request, 'purchases/purchases_list.html', {'purchases': purchases})


def purchase_edit(request, pk):
    purchase = get_object_or_404(Purchase, pk=pk)
    form = PurchaseForm(request.POST or None, instance=purchase)
    if form.is_valid():
        form.save()
        return redirect('purchases:purchase_list')
    return render(request, 'purchases/purchases_edit.html', {'form': form, 'purchase': purchase})


def purchase_delete(request, pk):
    purchase = get_object_or_404(Purchase, pk=pk)
    if request.method == 'POST':
        purchase.delete()
        return redirect('purchases:purchase_list')
    return render(request, 'purchases/purchases_delete.html', {'purchase': purchase})
