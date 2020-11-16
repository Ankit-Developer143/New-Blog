from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    # path('categories/',views.categories,name='categories'),
    path('<int:post_ids>',views.post,name='post'),
    path('<int:trends_ids>',views.trends,name='trends'),
    path('like/',views.like_post,name='like_post')


    
]