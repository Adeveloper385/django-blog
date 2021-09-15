from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    posts = Post.objects.filter(state = True)

    paginator = Paginator(posts, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'index.html', {"posts": posts})

def publicity(request):
    return render(request, 'publicity.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')


def post(request, slug):
    post = get_object_or_404(Post, slug = slug)
    return render(request, 'post.html', {"post": post})
