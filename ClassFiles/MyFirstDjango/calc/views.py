from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.
def home(request):
    return render(request, 'home.html', {'name': 'Sweshik'})

def add(request):
    val1=int(request.POST['num1'])
    val2=int(request.POST['num2'])
    val3=val1+val2
    return render(request,'result.html',{'result':val3})

def dashboard(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()
    return render(request, 'dashboard.html', {'customers':customers, 'orders': orders})

def products(request):
    products = Product.objects.all()
    return render(request, 'product.html', {'products':products})

def customer(request, pk_test):
    customer = Customer.objects.get(id=pk_test)
    customers = Customer.objects.all()
    orders = customer.order_set.all()
    order_count = orders.count()
    context = {'customers':customers, 'cust':customer, 'orders':orders, 'ordcount':order_count}
    return render(request, 'customer.html', context)

def createOrder(request):
    form = OrderForm()

    if request.method == "POST":
        print("POST request received")
        print("Form data:", request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            print("Form is valid")
            form.save()
            return redirect('/dashboard')
        else:
            print("Form is not valid")
            print(form.errors)
        
    context = {'form': form}
    return render(request, 'order_form.html', context)

def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(request.POST, instance=order)
    if form.is_valid():
        form.save()
        return redirect('/dashboard')
    
    context = {'form': form}

    return render(request, 'order_form.html', context)

def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/dashboard')
    
    context = {'item':order}
    return render(request, 'delete.html', context)