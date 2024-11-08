from django.shortcuts import render, redirect, HttpResponse
from .forms import ProductForm, ImageForm, CategoryForm
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

def products_view(request):
    query = request.GET.get('q', '')
    products = Product.objects.all()
    results = list(products)
    results.reverse()
    query = query.lower().strip(' /$\\=')   
    if query == '':
        pass
    else:
        results = []
        for product in products:
            if (product.status) and ((query in str(product.name).lower())) or (query in str(product.model).lower()) or (query in str(product.brand).lower()) or (query in str(product.description).lower()):
                results.append(product)
    return render(request, 'products/products.html', {'results': results})

def publish_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        print(request.POST)
        print('\n CATEGORY FORM: \n')
        print(form.errors)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category Published', extra_tags='success')
        return redirect('login-page')
    
    else:
        return render(request, 'products/publish_category.html', {'form': CategoryForm})
