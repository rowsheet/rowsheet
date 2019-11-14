from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.template import Template, Context

from .models import Brand
from .models import BrandCategory
from .models import FeaturedAccordian
from .models import BrandSlider
from .models import TrustedBrand

from common import utils

class SheetView:

    def _render_sheet(self):
        template = Template("""
<style>
td {
    border: 1px solid black;
}
.table_wrapper {
    overflow: scroll;
}
</style>
<h1>{{ model_name }}</h1>
<div class="row">
    <div class="col-12 table_wrapper">
        <table>
            <thead>
                <tr>
                    {% for field in fields %}
                    <td>
                        {{ field }}
                    </td>
                    {% endfor %}
                </tr>
            </thead>
            <tbody>
                {% for row in rows %}
                <tr>
                    {% for column in row %}
                    <td>
                        {{ column }}
                    </td>
                    {% endfor %}
                </tr>
                {% endfor %}
            </tbody>
        </table>
    </div>
</div>
        """)
        fields = [field.name for field in self.model._meta.get_fields()]
        query = self.model.objects.all()
        rows = [
            [getattr(item, field) for field in fields]
            for item in query
        ]
        context = {
            "model_name": self.model.__name__,
            "fields": fields,
            "rows": rows,
        }
        return template.render(Context(context))

    def _render_list(self):
        template = Template("""
<style>
tbody {
    background: white;
}
#content {
    background: #eee;
}
tbody tr {
    border-bottom: 1px solid #eeeeee;
}
.table_wrapper {
    overflow: scroll;
}
img.image_preview {
    width: 100px;
    height: 100px;
    object-fit: contain;
}
</style>
<div class="row">
    <div class="col-12 table_wrapper">
        <table>
            <thead>
                <tr>
                    {% for field in fields %}
                    <td>
                        {{ field }}
                    </td>
                    {% endfor %}
                </tr>
            </thead>
            <tbody>
                {% for row in rows %}
                <tr>
                    {% for column in row %}
                    <td>
                        {{ column }}
                    </td>
                    {% endfor %}
                </tr>
                {% endfor %}
            </tbody>
        </table>
    </div>
</div>
        """)
        fields = self.list_display
        query = self.model.objects.all()
        rows = [
            [getattr(self, field)(item) for field in fields]
            for item in query
        ]
        context = {
            "model_name": self.model.__name__,
            "fields": fields,
            "rows": rows,
        }
        return template.render(Context(context))

    def render(self):
        # return self._render_sheet()
        return self._render_list()

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
