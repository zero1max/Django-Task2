from django.contrib import admin
from .models import Contact, Category
from django.utils.html import format_html

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'address', "photo_tag"]

    def photo_tag(self, obj):
        if obj.photo:
            return format_html(f'<img src="{obj.photo.url}" width=80 height=auto>')
        else:
            return format_html('-')
    photo_tag.short_description = 'Photo'

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']

admin.site.register(Contact, UserAdmin)
admin.site.register(Category, CategoryAdmin)