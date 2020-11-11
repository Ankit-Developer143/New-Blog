from django.contrib import admin

from .models import Author,Post,Category
from .models import subscribe




# Register your models here.
admin.site.register((Post,Author,Category,subscribe))


