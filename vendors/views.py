# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Vendor
from .forms import VendorForm

def vendor_list(request):
    # Retrieve all vendors from the database
    vendors = Vendor.objects.all()
    return render(request, 'vendors/vendors_list.html', {'vendors': vendors})

def vendor_add(request):
    if request.method == 'POST':
        form = VendorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vendors:vendor_list')
    else:
        form = VendorForm()
    return render(request, 'vendors/vendors_add.html', {'form': form})

def vendor_edit(request, pk):
    vendor = get_object_or_404(Vendor, pk=pk)
    if request.method == 'POST':
        form = VendorForm(request.POST, instance=vendor)
        if form.is_valid():
            form.save()
            return redirect('vendors:vendor_list')
    else:
        form = VendorForm(instance=vendor)
    return render(request, 'vendors/vendors_edit.html', {'form': form, 'vendor': vendor})

def vendor_delete(request, pk):
    vendor = get_object_or_404(Vendor, pk=pk)
    if request.method == 'POST':
        vendor.delete()
        return redirect('vendors:vendor_list')

    context = {'vendor': vendor}
    return render(request, 'vendors/vendors_delete.html', context)