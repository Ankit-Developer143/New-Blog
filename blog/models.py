from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models.base import ModelState
from django.utils.text import slugify
# Create your models here.
class subscribe(models.Model):
    email = models.EmailField(max_length=50,null=True)
    def __str__(self):
        return f'{self.email}' 
    
class  Author(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    rate = models.IntegerField(default = 0)
    auther_image = models.ImageField(upload_to = 'autherpic',null = True)
    def __str__(self):
        return f'{self.user}'
    
class Category(models.Model):
    title = models.CharField(max_length=20)
    def __str__(self):
        return self.title
    
class Post(models.Model):
    title = models.CharField(max_length=200)
    overview = models.TextField()
    liked = models.ManyToManyField(User,default=None,blank=True,related_name='liked')
    highlight_line = models.CharField(max_length=1000 ,blank = True)
    Highlight_explanation= models.TextField(null=True)
    Highlighttopic_img = models.ImageField(upload_to = 'Highlighttopic_img',blank = True)
    time_upload = models.DateTimeField(auto_now_add=True)
    auther = models.ForeignKey(Author,on_delete=models.CASCADE,related_name='auther')
    thumbnail = models.ImageField(upload_to = 'thumbnails')
    publish  =  models.BooleanField()
    category = models.ManyToManyField(Category)
    read = models.IntegerField(default=0)
    
    #showing latest Blog First
    class Meta:
        ordering = ['-pk']
    
    def __str__(self):
        return f'{self.title}'
    
   
        
        
class Comment(models.Model):
    post = models.ForeignKey(Post,related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    publish = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    status = models.BooleanField(default=True)
    
    
    
    class Meta:
        ordering  = ("publish",)
    def __str__(self):
        return f"commented by {self.name}"
    
@property
def num_likes(self):
    return self.liked.all().count()



LIKE_CHOICES = (
    ('Like','Like'),
    ('Unlike','Unlike'),
)


class Like(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES,default='Like',max_length=10)
    
    
    
    
    
