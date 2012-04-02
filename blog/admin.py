from django.contrib import admin
from blog.models import Post

class PostAdmin(admin.ModelAdmin):
    fields = ('title', 'content', 'created', 'modified')
    readonly_fields = ('created', 'modified')
    list_display = ('id', 'title', 'created', 'modified')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')

admin.site.register(Post, PostAdmin)