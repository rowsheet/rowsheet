from django.shortcuts import render
from django.utils.safestring import mark_safe

from .models import Brand
from .models import BrandCategory
from .models import FeaturedAccordian
from .models import BrandSlider
from .models import TrustedBrand

from common import utils
from rowsheet.admin.SheetView import SheetView

class BrandSliderSheet(SheetView):
    model = BrandSlider
    changelist_layouts = {
        "table": True,
        "cards": False
    }
    list_filter = (
        "brand__name",
        "active",
        "brand__feature_active",
        "active",
        "brand__priority",
        "priority",
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
        "_image_and_description",
        "_brand",
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
        return utils.edit_button(
            creation_timestamp = obj.creation_timestamp,
            last_changed_timestamp = obj.last_changed_timestamp,
        )
    def _image_and_description(self, obj):
        # return utils.tableview_cloudfile(obj.image)
        return utils.image_and_description(obj.image, obj.description)
    _image_and_description.admin_order_field = "description"
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
