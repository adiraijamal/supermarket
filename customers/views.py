from django.shortcuts import render, get_object_or_404, redirect
from .models import Customer
from customers.forms import CustomerForm


def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customers/customers_list.html', {'customers': customers})


def customer_add(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customers:customer_list')
    else:
        form = CustomerForm()
    return render(request, 'customers/customers_add.html', {'form': form})


def customer_edit(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customers:customer_list')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'customers/customers_edit.html', {'form': form, 'customer': customer})


def customer_delete(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('customers:customer_list')
    return render(request, 'customers/customers_delete.html', {'customer': customer})
