from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Brand
from .models import BrandCategory
from .models import FeaturedAccordian
from .models import BrandSlider
from .models import TrustedBrand

from common import utils

#-------------------------------------------------------------------------------
#       ____                       ________      __                             
#      / __ )_________ _____  ____/ / ____/___ _/ /____  ____ _____  _______  __
#     / __  / ___/ __ `/ __ \/ __  / /   / __ `/ __/ _ \/ __ `/ __ \/ ___/ / / /
#    / /_/ / /  / /_/ / / / / /_/ / /___/ /_/ / /_/  __/ /_/ / /_/ / /  / /_/ / 
#   /_____/_/   \__,_/_/ /_/\__,_/\____/\__,_/\__/\___/\__, /\____/_/   \__, /  
#                                                     /____/           /____/
#-------------------------------------------------------------------------------

class BrandCategoryAdmin(admin.ModelAdmin):

    def __init__(self, *args, **kwargs):
        self._request = None
        super(BrandCategoryAdmin, self).__init__(*args, **kwargs)
        self.brands = Brand.objects.all()
        self.brands_by_category = {}
        self.slides_by_category = {}

    list_display = (
        "_edit",
        "name",
        "_brands_overview",
        "_slides_overview",
        "_enabled_brands",
        "_disabled_brands",
    )
    search_fields = (
        "name",
    )
    def _edit(self, obj):
        return utils.edit_button()
    def _enabled_brands(self, obj):
        enabled = [utils.brand_link(brand, brand.name) 
        for brand in list(filter(
            lambda brand: brand.category.name == obj.name,
            list(filter(lambda brand: brand.feature_active == True,
            self.brands))
        ))]
        if len(enabled) == 0:
            return "-"
        return mark_safe("".join(enabled))
    def _disabled_brands(self, obj):
        disabled = [utils.brand_link(brand, brand.name) 
        for brand in list(filter(
            lambda brand: brand.category.name == obj.name,
            list(filter(lambda brand: brand.feature_active != True,
            self.brands))
        ))]
        if len(disabled) == 0:
            return "-"
        return mark_safe("".join(disabled))
    def _brands_overview(self, obj):
        brands = [brand for brand in list(filter(
            lambda brand: brand.category.name == obj.name,
            self.brands))]
        total = len(brands)
        active = len(list(filter(lambda brand:
            brand.feature_active == True, brands)))
        return mark_safe("%s/%s Active" % (total, active))
    def _slides_overview(self, obj):
        slides = BrandSlider.objects.filter(brand__category__name=obj.name)
        total = len(slides)
        active = len(list(filter(lambda slide: slide.active == True, slides)))
        return mark_safe("%s/%s Active" % (total, active))
admin.site.register(BrandCategory, BrandCategoryAdmin)

#-------------------------------------------------------------------------------
#       ____                       __
#      / __ )_________ _____  ____/ /
#     / __  / ___/ __ `/ __ \/ __  / 
#    / /_/ / /  / /_/ / / / / /_/ /  
#   /_____/_/   \__,_/_/ /_/\__,_/  
#
#-------------------------------------------------------------------------------

class BrandAdmin(admin.ModelAdmin):
    #---------------------------------------------------------------------------
    # EXTRA_CHANGE_VIEW_DATA--Brand
    # Note: This is viewable in:
    #   rowsheet/templates/admin/change_form.html
    # and only when the change view for Brand is loaded.
    #---------------------------------------------------------------------------
    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['extra_change_view_data'] = "EXTRA_CHANGE_VIEW_DATA--Brand"
        return super().change_view(
            request, object_id, form_url, extra_context=extra_context,
        )
    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['extra_changelist_view_data'] = "EXTRA_CHANGE_LIST_VIEW_DATA--Brand"
        return super().changelist_view(
            request, extra_context=extra_context,
        )
    list_filter = (
        ("category"),
        ("storefront_category"),
        ("trusted_active"),
    )
    list_display = (
        "_edit",
        "_brand_info",
        "_brand_icon",
        "_priority",
        "category",
        "_homepage_url",
        "vendor_code",
        "storefront_category",
        "_trusted_priority",
    )
    search_fields = (
        "name",
        "category__name",
        "storefront_category",
        "vendor_code",
    )
    """
    fieldsets = (
        ('Status Info', {
            'fields': (
                "vendor_code",
                "storefront_category",
                "feature_active",
                "trusted_active",
                "trusted_priority",
            )
        }),
        ('Detail Info', {
            'fields': (
                "name",
                "brand_icon",
                "category",
                "homepage_url",
                "priority",
            )
        }),
    )
    """
    def _brand_info(self, obj):
        return utils.tableview_brand_info(obj.feature_active, obj.name, obj.trusted_active)
    _brand_info.admin_order_field = "feature_active"
    def _edit(self, obj):
        return utils.edit_button()
    def _priority(self, obj):
        return utils.tableview_priority(obj.priority)
    _priority.admin_order_field = "priority"
    def _trusted_priority(self, obj):
        return utils.tableview_priority(obj.trusted_priority)
    _trusted_priority.admin_order_field = "trusted_priority"
    def _brand_icon(self, obj):
        return utils.tableview_cloudfile(obj.brand_icon)
    def _homepage_url(self, obj):
        return utils.tableview_href(obj.homepage_url)
admin.site.register(Brand, BrandAdmin)

#-------------------------------------------------------------------------------
#       ____                       _______ ___     __         
#      / __ )_________ _____  ____/ / ___// (_)___/ /__  _____
#     / __  / ___/ __ `/ __ \/ __  /\__ \/ / / __  / _ \/ ___/
#    / /_/ / /  / /_/ / / / / /_/ /___/ / / / /_/ /  __/ /    
#   /_____/_/   \__,_/_/ /_/\__,_//____/_/_/\__,_/\___/_/     
#
#-------------------------------------------------------------------------------

class BrandSliderAdmin(admin.ModelAdmin):
    changelist_layouts = {
        "table": True,
        "cards": False
    }
    list_filter = (
        ("brand__name"),
        ("active"),
        ("brand__feature_active"),
        ("active"),
        ("brand__priority"),
        ("priority"),
    )
    ordering = (
        "brand",
        "brand__priority",
        "active",
        "priority",
    )
    list_display = (
        "_edit",
        "_slide_info",
        "_image",
        "_brand",
        "_description",
        "_priority",
        "c_custom_button",
        "c_homepage_button_active",
        "c_shop_button_active",
    )
    search_fields = (
        "title",
        "subtitle",
        "description",
        "button_text",
        "button_href",
        "brand__name",
        "priority",
    )
    def _edit(self, obj):
        return utils.edit_button()
    def _image(self, obj):
        return utils.tableview_cloudfile(obj.image)
    def _description(self, obj):
        return utils.tableview_text(obj.description)
    _description.admin_order_field = "description"
    def _brand(self, obj):
        return utils.brand_link(obj.brand, obj.brand.name)
    _brand.admin_order_field = "brand"
    def _name(self, obj):
        return utils.tableview_label(obj.name)
    _name.admin_order_field = "name"
    def _slide_info(self, obj):
        return utils.tableview_slide_info(obj.active, obj.title, obj.subtitle, width=300)
    _slide_info.admin_order_field = "title"
    def _priority(self, obj):
        return utils.tableview_priority(obj.priority)
    _priority.admin_order_field = "priority"
    def c_custom_button(self, obj):
        return utils.button(
            obj.button_active,
            obj.button_href,
            obj.button_text,
        )
    c_custom_button.admin_order_field = "button_active"
    def c_homepage_button_active(self, obj):
        return utils.button(
            obj.homepage_button_active,
            obj.brand.homepage_url,
            "View Homepage",
        )
    c_homepage_button_active.admin_order_field = "homepage_button_active"
    def c_shop_button_active(self, obj):
        return utils.button(
            obj.shop_button_active,
            "/brands_detail/?brand_id=%s" % obj.brand.id,
            "Shop Products",
        )
    c_shop_button_active.admin_order_field = "shop_button_active"
admin.site.register(BrandSlider, BrandSliderAdmin)

#-------------------------------------------------------------------------------
#     ______                __           ______                       __
#    /_  __/______  _______/ /____  ____/ / __ )_________ _____  ____/ /
#     / / / ___/ / / / ___/ __/ _ \/ __  / __  / ___/ __ `/ __ \/ __  / 
#    / / / /  / /_/ (__  ) /_/  __/ /_/ / /_/ / /  / /_/ / / / / /_/ /  
#   /_/ /_/   \__,_/____/\__/\___/\__,_/_____/_/   \__,_/_/ /_/\__,_/   
#
#-------------------------------------------------------------------------------

class TrustedBrandAdmin(admin.ModelAdmin):
    list_display = (
        "brand",
        "priority",
    )
    search_fields = (
        "brand",
        "priority",
    )
admin.site.register(TrustedBrand, TrustedBrandAdmin)

#-------------------------------------------------------------------------------
#       ______           __                          
#      / ____/__  ____ _/ /___  __________           
#     / /_  / _ \/ __ `/ __/ / / / ___/ _ \          
#    / __/ /  __/ /_/ / /_/ /_/ / /  /  __/          
#   /_/ ___\___/\__,_/\__/\__,_/_/   \____           
#      /   | ______________  _________/ (_)___ _____ 
#     / /| |/ ___/ ___/ __ \/ ___/ __  / / __ `/ __ \
#    / ___ / /__/ /__/ /_/ / /  / /_/ / / /_/ / / / /
#   /_/  |_\___/\___/\____/_/   \__,_/_/\__,_/_/ /_/ 
#
#-------------------------------------------------------------------------------

class FeaturedAccordianAdmin(admin.ModelAdmin):
    list_filter = (
        ("brand__category"),
        ("priority"),
        ("brand__priority"),
        ("name"),
    )
    list_display = (
        "_edit",
        "_accordian_info",
        "_image",
        "_priority",
        "_brand",
        "_brand_category",
    )
    search_fields = (
        "feature_text",
        "brand__name",
        "priority",
    )
    def _edit(self, obj):
        return utils.edit_button()
    def _image(self, obj):
        return utils.tableview_cloudfile(obj.image)
    def _accordian_info(self, obj):
        return utils.tableview_accordian_info(
                obj.active,
                obj.feature_text,
                obj.name)
    _accordian_info.admin_order_field = "feature_text"
    def _brand(self, obj):
        return utils.brand_link(obj.brand, obj.brand.name)
    _brand.admin_order_field = "brand"
    def _priority(self, obj):
        return utils.tableview_priority(obj.priority)
    _priority.admin_order_field = "priority"
    def _brand_category(self, obj):
        return obj.brand.category.name
admin.site.register(FeaturedAccordian, FeaturedAccordianAdmin)
