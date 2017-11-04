from django.contrib import admin
from .models import Category, Product

class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']
	prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug', 'category', 'price', 'starting_bid', 'available', 'created', 'updated']
	list_filter = ['available', 'created', 'updated', 'category']
	list_editable = ['price', 'starting_bid', 'available']
	prepopulated_fields = {'slug': ('name',)}
admin.site.register(Product, ProductAdmin)