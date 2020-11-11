from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('categories/',views.categories,name='categories'),
    path('<int:post_ids>',views.post,name='post')
    
]