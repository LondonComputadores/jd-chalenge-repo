from django.contrib import admin
from .models import Category, Articles, Authors


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

class ArticlesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ('category')
    list_display = ('id', 'author', 'category', 'title', 'summary', 'firstParagraph','body')


admin.site.register(Articles)
admin.site.register(Category)
admin.site.register(Authors)
