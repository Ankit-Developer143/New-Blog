from datetime import date
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Post,Author,Category, subscribe
import datetime
 

# Create your views here.
def home(request):
    
    if request.method == 'POST':
        email = request.POST.get('name')
        value = subscribe(email = email).save()
        

    
    # Trending Post
    week_ago = datetime.date.today() - datetime.timedelta(days= 7)
    trends = Post.objects.filter(time_upload__gte = week_ago).order_by('-read')
    
    #Trending Author #this is loop and store data in author and save in Authos Post
    TopAuthors = Author.objects.order_by('-rate')[:4]
    AuthorsPost = [Post.objects.filter(auther = author).first() for author in TopAuthors  ] 
    categories = Category.objects.all()
    
    
    Recentpost = Post.objects.all().order_by('-time_upload')
     
    
    posts =list( Post.objects.filter(publish = True))
    context = {
        'posts':posts,
        'trends':trends[:3],
        'author_post':AuthorsPost[:4],
        'cats':categories,
        'Recentpost':Recentpost[:3]
    }
    return render(request,'blog/garden-index.html',context)


def categories(request):
    return render(request,'blog/garden-category.html')

def post(request,post_ids):
    post_by_ids = get_object_or_404(Post,pk = post_ids) 
    Recentpost = Post.objects.all().order_by('-time_upload')
    TopAuthors = Author.objects.order_by('-rate')[:4]
    AuthorsPost = [Post.objects.filter(auther = author).first() for author in TopAuthors  ] 
    categories = Category.objects.all()
    context= {
        'posts':post_by_ids,
        'Recentpost':Recentpost[:3],
        'cats':categories,
        'author_post':AuthorsPost
        
         
    }
   
    return render(request,'blog/garden-single.html',context)