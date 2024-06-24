from django.contrib import admin

from goods.models import Categories, Products

class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}


class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Products, ProductsAdmin)
