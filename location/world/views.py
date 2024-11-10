from django.shortcuts import render
from django.urls import reverse

def home(request):
    # Generate URL for admin page using reverse
    admin_url = reverse('admin:index')
    return render(request, 'home.html', {'admin_url': admin_url})