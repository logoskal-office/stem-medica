from django.shortcuts import render, redirect, HttpResponse
from .forms import ProductForm, ImageForm
from .models import Image, Product, Category
from django.contrib import messages


def publish_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        image_form = request.FILES.getlist('image') # Manually Processing the images

        if form.is_valid():
            form.save()

            for image in image_form:
                print('image')  
                Image.objects.create(product=form.instance,image=image)
        messages.success(request, 'Product Published', extra_tags='success')
        return redirect('login-page')
    else:
        return render(request, 'products/publish_product.html', {'form': ProductForm, 'images': ImageForm()})

def search(request, query=''):
    if query == '':
        return HttpResponse('Welcome, Search')
    products = Product.objects.all()
    results = []
    query = query.lower().strip()
    for product in products:
        if (product.status) or ((query in product.name) or (query in product.model) or (query in product.brand) or (query in product.description)):
            results.append(product)
            print(results)
    return HttpResponse('Found: ', results)