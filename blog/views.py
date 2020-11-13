from datetime import date
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Post,Author,Category, subscribe
import datetime
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
 

# Create your views here.
def home(request):
    
    if request.method == 'POST':
        email = request.POST.get('email')
        value = subscribe(email = email)
        value.save()
        

    
    # Trending Post
    week_ago = datetime.date.today() - datetime.timedelta(days= 7)
    trends = Post.objects.filter(time_upload__gte = week_ago).order_by('-read')
    
    #Trending Author #this is loop and store data in author and save in Authos Post
    TopAuthors = Author.objects.order_by('-rate')[:4]
    AuthorsPost = [Post.objects.filter(auther = author).first() for author in TopAuthors  ] 
    categories = Category.objects.all()
    Recentpost = Post.objects.all().order_by('-time_upload')
    #posts =list( Post.objects.filter(publish = True))
    
    #pagination
    all_post = Paginator(Post.objects.filter(publish = True),3)
    #get pages
    page = request.GET.get('page')
    try:
        posts = all_post.page(page)
    except PageNotAnInteger:
        posts = all_post.page(1)
    except EmptyPage:
        posts = all_post.page(all_post.num_pages)
        
    
    
     
    
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
    #Using Read Count
    post_by_ids .read += 1
    post_by_ids.save()
    context= {
        'posts':post_by_ids,
        'Recentpost':Recentpost[:3],
        'cats':categories,
        'author_post':AuthorsPost
        
         
    }
   
    return render(request,'blog/garden-single.html',context)