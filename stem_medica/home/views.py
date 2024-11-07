from django.shortcuts import render
from django.http import FileResponse, Http404

import os
from django.conf import settings

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

