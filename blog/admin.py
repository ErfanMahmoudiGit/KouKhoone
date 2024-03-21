from django.contrib import admin
from .models import Article, category

class categoryAdmin (admin.ModelAdmin):
    list_display = ('position', 'title', 'slug', 'status')
    list_filter = (['status'])
    search_fields = ('title','slug')
    prepopulated_fields = {'slug':('title',),}

class ArticleAdmin (admin.ModelAdmin):
    list_display = ('title', 'description', 'created', 'jpublish', 'status', 'category_to_str')
    list_filter = ('publish', 'status')
    search_fields = ('title','description')
    prepopulated_fields = {'slug':('title',),}
    ordering = ('status', '-publish')

    def category_to_str(self, obj):
        return ",".join([category.title for category in obj.category_published()])

    category_to_str.short_description = "دسته‌بندی ها"
admin.site.register(category, categoryAdmin)
admin.site.register(Article, ArticleAdmin)
