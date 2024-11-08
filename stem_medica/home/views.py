from django.shortcuts import render
from django.http import FileResponse, Http404
from products.models import Product, Category

import os
from django.conf import settings

def home(request, ):
    return render(request, 'home/main.html',{'products':Product.objects.all(), 'categories': Category.objects.all(),'categories_active': Category.objects.all()[0:3],'categories_rest': Category.objects.all()[3:7] })

def latest_section(request, ):
    product_list = list(Product.objects.all())
    product_list.reverse()
    return render(request, 'home/latest.html',{'products':Product.objects.all(), 'categories': Category.objects.all(),'categories_active': Category.objects.all()[0:3],'categories_rest': Category.objects.all()[3:7] })

def contact_us(request, ):
    return render(request, 'home/contact-us.html')

def about_us(request):
    return render(request, 'home/about-us.html')

def download(request):
        return render(request, 'home/download.html')

def download_link(request, file_name):
    file_path = os.path.join(settings.MEDIA_ROOT, 'files/'+ file_name)
    
    if not os.path.exists(file_path):
        raise Http404('Requested File Not Found')
    
    response = FileResponse(open(file_path, 'rb'))
    response['Content-Type'] = 'application/octet-stream'  # Optional: to force download
    return response

