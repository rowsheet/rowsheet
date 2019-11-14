from django.template.loader import render_to_string
from django.conf import settings
from django.core import serializers
from django.http import JsonResponse, HttpResponse

from rowsheet.cms.layouts.LandingCover import LandingCover
from rowsheet.cms.layouts.Dashboard import Dashboard

from .views_utils import rowsheet_landing_header
from .views_utils import rowsheet_landing_footer
from .views_utils import rowsheet_landing_alert
from .views_utils import rowsheet_dashboard_sidebar

def api(request):
    from storefront.models import Product
    results = Product.objects.all().order_by("-id")[0:25]
    rjson = serializers.serialize('json',results)
    return HttpResponse(rjson, content_type='application/json')

def dashboard(request):
    dashboard = Dashboard()
    dashboard.set_sidebar(rowsheet_dashboard_sidebar)
    dashboard.set_title("Dashboard")
    from affiliate_marketing.views import BrandSliderSheet
    bss = BrandSliderSheet()
    body = bss.render()
    dashboard.set_body(body)
    return dashboard.render()

def dashboard_apps(request):
    dashboard = Dashboard()
    dashboard.set_sidebar(rowsheet_dashboard_sidebar)
    dashboard.set_title("Apps")

    from rowsheet_apps.models import ClientApp
    rows = ClientApp.objects.all()
    from django.template import Template, Context
    template = Template("""
    <style>
img.image_preview {
    height: 100px;
    width: 100px;
    object-fit: contain;
}
    </style>
        {{ something }}
        {{ len }}
        {% for row in rows %}
            <h1>Row: {{ row }}</h1>
        {% endfor %}
    """)
    body = template.render(Context({
        "something": "FOO",
        "rows": rows,
        "len": len(rows),
    }))

    dashboard.set_body(body)
    return dashboard.render()

def index(request):
    page = LandingCover()
    page.set_title("RowSheet - Home")
    page.set_header(rowsheet_landing_header())
    page.set_footer(rowsheet_landing_footer())
    page.set_alert(rowsheet_landing_alert(request))
    page.set_body(
        content=render_to_string("terminal_banner.html"),
        stylesheet="rowsheet_landing/terminal_banner.css",
    )
    return page.render()
