from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title','created_at')
    list_display_linls = ('title',)
    ordering = ('-created_at',)


# Register your models here.
