from django.contrib import admin
from django.db.models import Count
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory

from djshop.apps.catalog.models import Category, ProductClass, Option, ProductAttribute, ProductRecommendation, Product, \
    ProductAttributeValue, ProductImage


# Register your models here.
class CategoryAdmin(TreeAdmin):
    form = movenodeform_factory(Category)


admin.site.register(Option)


class ProductAttributeInline(admin.StackedInline):
    model = ProductAttribute
    extra = 2


class AttributeCountFilter(admin.SimpleListFilter):
    title = 'Attribute Count'
    parameter_name = 'attr_count'

    def lookups(self, request, model_admin):
        return [
            ('more_5', 'More Than 5'),
            ('lower_5', 'lower Than 5'),
        ]

    def queryset(self, request, queryset):
        if self.value() == "more_5":
            return queryset.annotate(attr_count=Count('attributes')).filter(attr_count__gt=5)
        if self.value() == "lower_5":
            return queryset.annotate(attr_count=Count('attributes')).filter(attr_count__lte=5)


@admin.register(ProductClass)
class ProductClassAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'require_shipping', 'track_stock', 'attribute_count')
    list_filter = ('require_shipping', 'track_stock', AttributeCountFilter)
    inlines = [ProductAttributeInline]
    actions = ['enable_track_stock']
    prepopulated_fields = {"slug": ("title",)}

    def attribute_count(self, obj):
        return obj.attributes.count()

    def enable_track_stock(self, request, queryset):
        queryset.update(track_stock=True)


class ProductRecommendationInline(admin.StackedInline):
    model = ProductRecommendation
    extra = 2
    fk_name = 'primary'


class ProductCategoryInline(admin.StackedInline):
    model = Product.categories.through
    extra = 2


class ProductAttributeValueInline(admin.TabularInline):
    model = ProductAttributeValue
    extra = 2

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 2
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug',)
    inlines = [ProductAttributeValueInline,ProductImageInline, ProductRecommendationInline]
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Category, CategoryAdmin)
