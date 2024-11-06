from django.shortcuts import render

def contact_us(request):
    return render(request, 'home/contact-us.html')

def about_us(request):
    return render(request, 'home/about-us.html')
