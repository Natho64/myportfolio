from django.shortcuts import render, get_object_or_404
from .models import Blogproj

# Create your views here.
def all_blogs(request):
    blogproj = Blogproj.objects.order_by('-date')

    return render(request, 'blog/all_blogs.html', {'blogproj':blogproj})

def detail(request, blog_id):
    
    blog = get_object_or_404(Blogproj, pk=blog_id)

    return render(request, 'blog/detail.html', {'blog':blog})