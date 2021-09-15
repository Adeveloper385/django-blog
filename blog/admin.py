from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

#   Import and Export Class
class CategoryResources(resources.ModelResource):
    class Meta:
        model = Category


class AuthorResources(resources.ModelResource):
    class Meta:
        model = Author

# Register your models here.

class CategoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name', 'state', 'created_at')
    resource_class = CategoryResources

class AuthorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['name', 'last_name']
    list_diplay = ('name', 'last_name','email','state', 'created_at')
    resource_class = AuthorResources

admin.site.register(Category, CategoryAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Post)


