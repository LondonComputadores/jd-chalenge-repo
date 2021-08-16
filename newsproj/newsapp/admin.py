from django.contrib import admin
from .models import Category, Articles, Authors


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

class ArticlesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ('category')
    list_display = ('title', 'category', 'authors')


admin.site.register(Articles)
admin.site.register(Category)
admin.site.register(Authors)
