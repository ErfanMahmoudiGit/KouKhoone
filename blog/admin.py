from django.contrib import admin
from .models import Article

class ArticleAdmin (admin.ModelAdmin):
    list_display = ('title', 'description', 'created', 'publish', 'status')
    list_filter = ('publish', 'status')
    search_fields = ('title','description')
    prepopulated_fields = {'slug':('title',),}
    ordering = ('status', '-publish')
admin.site.register(Article, ArticleAdmin)
# Register your models here.
