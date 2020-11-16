from blog.forms import NewCommentForm
from datetime import date
from ckeditor import fields
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from .models import Post,Author,Category,  subscribe,Comment,Like
import datetime
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.views.generic.edit import CreateView 

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

def post(request,post_ids):
    post_by_ids = get_object_or_404(Post,pk = post_ids) 
    Recentpost = Post.objects.all().order_by('-time_upload')
    TopAuthors = Author.objects.order_by('-rate')[:4]
    AuthorsPost = [Post.objects.filter(auther = author).first() for author in TopAuthors  ] 
    categories = Category.objects.all().order_by('-title')
    #Using Read Count
    post_by_ids .read += 1
    post_by_ids.save()
    
# For Comments.....................Related Name Comments in models
    comments = post_by_ids.comments.filter(status = True)  #This is the main
    user_comment = None
    if request.method == "POST":
         comment_form = NewCommentForm(request.POST)
         if comment_form.is_valid():
             user_comment = comment_form.save(commit =False)
             user_comment.post = post_by_ids
             user_comment.save()
             return redirect('/')
             
    else:
        #this is used for html Pages
          comment_form = NewCommentForm()
    
   
    context= {
        'posts':post_by_ids,
        'Recentpost':Recentpost[:3],
        'cats':categories,
        'author_post':AuthorsPost,
        'post':post,'comments':user_comment,'comments':comments,'comment_form':comment_form
         
    }
   
    return render(request,'blog/garden-single.html',context)


def trends(request,trends_ids):
    post_by_trends = get_object_or_404(Post,pk = trends_ids)
    categories = Category.objects.all().order_by('-title')
    
    context= {
        'posts':post_by_trends,
        'Recentpost':Recentpost[:3],
        'cats':categories,
        'author_post':AuthorsPost,
        'post':post,'comments':user_comment,'comments':comments,'comment_form':comment_form
         
    }
    
    return render(request,'blog/garden-trending.html',context)



def like_post(request):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = Post.objects.get(id = post_id)
        
        if user in post_obj.liked.all():
            post_obj.liked.remove(user)
        else:
            post_obj.liked.add(user)
        like,created = Like.objects.get_or_create(user = user,post_id = post_id)
        
        if not created:
            if like.value  == 'Like':
                like.value = 'unlike'
            else:
                like.value = 'like'
        like.save()
        return redirect('/')
        
        
    return render(request,'blog/garden-index.html')
