from django.contrib import admin
from .models import Post  # Fixed import statement

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')  # Added missing comma
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)  # Added missing closing parenthesis
    date_hierarchy = 'publish'  # Fixed incorrect syntax
    ordering = ('status', 'publish')
