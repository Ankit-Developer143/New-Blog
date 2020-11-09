from datetime import date
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Post,Author,Category
import datetime
 

# Create your views here.
def home(request):
    # Trending Post
    week_ago = datetime.date.today() - datetime.timedelta(days= 7)
    trends = Post.objects.filter(time_upload__gte = week_ago).order_by('-read')
    
    #Trending Author
    TopAuthors  = Author.objects.order_by('-rate')      #this is loop and store data in author and save in Authos Post
    AuthorsPost = [Post.objects.filter(auther = author).first() for author in TopAuthors  ] 
    categories = Category.objects.all()
    
    
    posts =list( Post.objects.filter(publish = True))
    context = {
        'posts':posts,
        'trends':trends[:5],
        'author_post':AuthorsPost,
        'cat':categories
    }
    return render(request,'blog/garden-category.html',context)


def categories(request):
    return HttpResponse('Hello')

def poss(request):
    return HttpResponse('Hello')

def post(request,post_ids):
    post = get_object_or_404(Post,pk = post_ids)
    print(post)
   
    return HttpResponse('Hello')