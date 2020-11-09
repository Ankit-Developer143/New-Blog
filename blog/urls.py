from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('categories/',views.home,name='categories'),
    path('posts/',views.home,name='posts'),
    path('<int:post_ids>',views.post,name='post')
]