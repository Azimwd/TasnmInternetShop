from django.contrib import admin

from goods.models import Categories, Products

# admin.site.register(Categories)
# admin.site.register(Products)


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ['name', 'quantity', 'price', 'discount']
    list_editable = ['discount']
    search_fields = ['name', 'description']
    list_filter = ['name', 'quantity', 'price', 'discount']
    fields = [
        'name', 
        'category',
        'slug',
        'description',
        'image', 
        ('price', 'discount'),
        'quantity',
        ]

# from django.contrib import admin

# from goods.models import Categories_women,Categories_men, Products_women, Products_men

# # admin.site.register(Categories)
# # admin.site.register(Products)


# @admin.register(Categories_women)
# class Categories_womenAdmin(admin.ModelAdmin):
#     prepopulated_fields = {"slug": ("name",)}


# @admin.register(Categories_men)
# class Categories_menAdmin(admin.ModelAdmin):
#     prepopulated_fields = {"slug": ("name",)}

# @admin.register(Products_women)
# class Products_womenAdmin(admin.ModelAdmin):
#     prepopulated_fields = {"slug": ("name",)}

# @admin.register(Products_men)
# class Products_menAdmin(admin.ModelAdmin):
#     prepopulated_fields = {"slug": ("name",)}
