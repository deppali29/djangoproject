from django.shortcuts import render
from app1.models import Product
# Create your views here.

def home(request):
    all_products=Product.objects.all()

    item_name=request.POST.get('data')#item_name="shirt"
    if item_name!='' and item_name is not None:
        all_products=all_products.filter(title__contains=item_name)

    context={
        'all_products':all_products
    }
    return render(request,"home.html",context)
    
def display_one_data(request,slug):
    one_product_data=Product.objects.get(slug=slug)
    context={
        'one_product_data':one_product_data
    }
    return render(request,"data.html",context)

def login(request):
    return render(request,"login.html")   