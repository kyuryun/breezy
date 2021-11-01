from django.contrib import admin
from .models import MyUser, Post, Category, File, Comment

# Register your models here.
class MyUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'phone', 'email']

class PostAdmin(admin.ModelAdmin):
    list_display = ['postCode', 'category', 'title', 'author', 'text', 'published_date']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['code', 'category']

class FileAdmin(admin.ModelAdmin):
    list_display = ['fileCode', 'path', 'postCode']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['commentCode', 'author', 'postCode', 'text', 'published_date']


admin.site.register(MyUser, MyUserAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(File, FileAdmin)
admin.site.register(Comment, CommentAdmin)