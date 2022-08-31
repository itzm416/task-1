from django.contrib import admin
from blog.models import Post, Category

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','category','add_date')
    search_fields = ('title',)
    list_filter = ('category',)
    list_per_page = 50

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    list_filter = ('title',)
    list_per_page = 50

