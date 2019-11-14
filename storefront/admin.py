from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils import timezone

from .models import Product
from .models import ProductTag
from .models import CarouselItem
from .models import Carousel

class CarouselAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "active",
    )
    search_fields = (
        "name",
        "active",
    )
admin.site.register(Carousel, CarouselAdmin)

class CarouselItemAdmin(admin.ModelAdmin):
    list_display = (
        "product",
        "carousel",
        "priority",
        "active",
    )
    search_fields = (
        "product",
        "carousel",
        "priority",
        "active",
    )
admin.site.register(CarouselItem, CarouselItemAdmin)

class ProductTagAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'creation_timestamp',
        'last_changed_timestamp',
        'job_timestamp'
    )
    search_fields = (
        'name',
        'description',
        'creation_timestamp',
        'last_changed_timestamp',
        'job_timestamp'
    )
admin.site.register(ProductTag, ProductTagAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_filter = (
        ('visible', admin.BooleanFieldListFilter),
        ('adilas_active', admin.BooleanFieldListFilter),
    )
    list_display = (
        'name',
        'description',
        'adilas_active',
        'adilas_import_timestamp',
        'adilas_import_error',
        'visible',
        'for_sale',
        'discontinued',
        '_tags',
        'parent_product',
        '_vendor',
        'upc',
        'vendor_code',
    #     'man_part_number',
    #     'htc_number',

    #     'model',
    #     'brand',
    #     'text_document',
    #     'spec_kv',
        'details_kv',

    #     'msrp',
        'base_price',
        'price',

        '_image',
        'uofm',
        'inventory',
        'bin_date',
        'weight',
        'category',
        'creation_timestamp',
        'last_changed_timestamp',
        'job_timestamp'
    )
    search_fields = (
        'vendor',
        'name',
        'upc',
        'base_price',
        'price',
        'uofm',
        'inventory',
        'bin_date',
        'weight',
        'category',
        'description',
        'creation_timestamp'
    )

    def _visible(self, obj):
        return format_bool(obj.visible)

    def _for_sale(self, obj):
        return format_bool(obj.for_sale)

    def _discontinued(self, obj):
        return format_bool(obj.discontinued)

#    def _adilis_active(self, obj):
#        return format_bool(obj.adilas_active)

    def _adilas_import_timestamp(self, obj):
        return mark_safe("""
        <code>%s</code>
        """ % obj.adilas_import_timestamp)

    def _adilas_import_error(self, obj):
        return format_bool(obj.adilas_import_error)

    def _vendor(self, obj):
        return mark_safe("""
            <div style='width: 200px'>%s</div>
        """ % obj.vendor)

    def _image(self, obj):
        image_links_html = "".join([
            ("""
            <a target="_blank" rel="noopener noreferrer" href="%s">
                <img 
                    style="height: 75px;width: 75px;object-fit: cover;"
                    src="%s"/>
            </a>
            """ % (img.gcloud_img_src, img.gcloud_img_src)) for img in obj.image.all()
        ]) 
        if len(obj.image.all()) == 0:
            image_links_html = "<div class='admin_no_images_message'>No images</div>"
        return mark_safe("""
        <div class="admin_table_image_list_container">
            <div class="admin_table_image_list_content">
            %s 
            </div>
        </div>
        """ % image_links_html)
    def _tags(self, obj):
        return format_tags(obj.tags)
admin.site.register(Product, ProductAdmin)

def format_bool(value):
    if (value):
        return mark_safe("""
            <div class="td_true">True</div>
        """)
    return mark_safe("""
        <div class="td_false">False</div>
    """)

def format_tags(tags):
    if tags is None:
        return mark_safe("""
            <div class="no_tags"><nobr>No tags<nobr></div>
        """)
    tags_html = ",".join([
        ("""
        <div class="has_tags"><nobr>%s</nobr></div>
        """ % (tag.name)) for tag in tags.all()
    ]) 
    if tags_html == "":
        return mark_safe("""
            <div class="no_tags"><nobr>No tags<nobr></div>
        """)
    return mark_safe(tags_html)
