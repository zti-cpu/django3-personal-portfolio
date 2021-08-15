from django.urls import path
from . import views

app_name = 'blog'


urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    path('<int:blog_id>/', views.detail, name='detail'),  # int:blog_id Будут  реагировать
    # на все цифровые приписки к blog/1 и фиксировать их в переменную  blog_id

]
