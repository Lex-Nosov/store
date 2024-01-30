from django.contrib import admin
from django.db.models import QuerySet
from django.http import HttpRequest

from app_store.models import Product, Overview, Category, Characteristics


@admin.action(description='Archive prducts')
def mark_archived(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(archived=True)


@admin.action(description='Unarchive prducts')
def mark_unarchived(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(archived=False)


class CharacteristicsAdmin(admin.TabularInline):
    model = Characteristics
    list_display = ['article', 'country_manufacture', 'product_life', 'warranty_period', 'operating_system',
                    'case_material', 'weight', 'dimensions', 'processor', 'number_processor_cores', 'ram', 'integrated',
                    'internal_memory']
    list_editable = []
    search_fields = []


class ReviewAdmin(admin.TabularInline):
    model = Overview
    list_display = ['first_title', 'first_description', 'second_title', 'second_description']
    list_editable = []
    search_fields = []


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    actions = [
        mark_archived,
        mark_unarchived
    ]
    list_display = ['name', 'price', 'image', 'stock', 'description', 'discount', 'created', 'updated', 'archived']
    list_editable = ['price', 'stock', 'description']
    search_fields = ['name', 'price', 'stock']
    inlines = [CharacteristicsAdmin, ReviewAdmin]
    fieldsets = [(None, {
        'fields': ('name', 'stock', 'price', 'discount', 'description_for_cart', 'description', 'category_field')
    }),
                 ('hidden fields', {
                     'fields': ('image',),
                     'classes': ('wide', 'collapse')
                 })]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name_category']
    search_fields = ['name_category']
