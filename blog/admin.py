from django.contrib import admin

from .models import Author,Post,Category
from .models import subscribe
from .models import Comment
from .models import *




# Register your models here.
admin.site.register((Post,Author,Category,subscribe))
admin.site.register(Comment)

class CommentAdmin(admin.ModelAdmin):
    list_display = ("post","name","publish","body","status")
    list_filter = ("status","publish")
    search_fields = ("name","body")

