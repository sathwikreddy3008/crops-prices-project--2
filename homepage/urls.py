# homepage/urls.py
from django.urls import path
from .views import home, blog, login_view, create_blog_post,delete_blog_post,process_state,state_form
from . import views

app_name = 'homepage'

urlpatterns = [
    path('', home, name='home'),
    path('blog/', blog, name='blog'),
    path('login/', login_view, name='login'),
    path('state/', views.state_form, name='state_form'),
    path('state_form/', state_form, name='state_form'),
    path('process_state/', process_state, name='process_state'),
    path('create_blog_post/', create_blog_post, name='create_blog_post'),
    path('delete_blog_post/<int:post_id>/', delete_blog_post, name='delete_blog_post'),
]