from django.shortcuts import render, redirect
from .forms import ProductForm, ImageForm
from .models import Image
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
