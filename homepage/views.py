# homepage/views.py
from django.shortcuts import render,redirect,get_object_or_404
from .models import BlogPost
from .models import Crop, Price
from .forms import BlogPostForm

def blog(request):
    blog_posts = BlogPost.objects.all().order_by('-pub_date')
    return render(request, 'blog.html', {'blog_posts': blog_posts})

def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage:blog')
    else:
        form = BlogPostForm()

    return render(request, 'create_blog_post.html', {'form': form}) 

def delete_blog_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)

    if request.method == 'POST':
        post.delete()
        return redirect('homepage:blog')

    return render(request, 'delete_blog_post.html', {'post': post})

def home(request):
    '''# Your view logic here
    if request.user.is_authenticated:
        # Redirect authenticated users to the state selection page
        return redirect('state_form')

    crops = Crop.objects.all()
    prices = Price.objects.all()
    context = {
        'crops': crops,
        'prices': prices,
    }'''
    return render(request, 'home.html')

def login_view(request):
    return render(request, 'login.html')

def crop_prices_prices(request):
    return render(request, 'prices/prices_home.html')

def state_form(request):
    return render(request, 'state_form.html')

def process_state(request):
    if request.method == 'POST':
        selected_state = request.POST.get('state')

        return redirect('app_name:prices')
    
    return render(request, 'state_form.html')
