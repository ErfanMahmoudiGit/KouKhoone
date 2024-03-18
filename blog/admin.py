from django.contrib import admin
from .models import Article, category

class categoryAdmin (admin.ModelAdmin):
    list_display = ('position', 'title', 'slug', 'status')
    list_filter = (['status'])
    search_fields = ('title','slug')
    prepopulated_fields = {'slug':('title',),}
admin.site.register(category, categoryAdmin)

class ArticleAdmin (admin.ModelAdmin):
    list_display = ('title', 'description', 'created', 'jpublish', 'status', 'category_to_str')
    list_filter = ('publish', 'status')
    search_fields = ('title','description')
    prepopulated_fields = {'slug':('title',),}
    ordering = ('status', '-publish')

    def category_to_str(self, obj):
        return "categories"
admin.site.register(Article, ArticleAdmin)
