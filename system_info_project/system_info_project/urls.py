from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def redirect_to_htop(request):
    return redirect('htop')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('info.urls')),
    path('', redirect_to_htop),  # Add this line
]