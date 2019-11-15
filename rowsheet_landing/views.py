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

def component_index(request):
    dashboard = Dashboard()
    dashboard.set_normal_sidebar(rowsheet_dashboard_sidebar)
    dashboard.set_new_alerts(3)
    dashboard.set_new_messages(5)
    dashboard.set_user_profile(
        username="Alex K",
        profile_photo="/static/headshot.png",
    )
    dashboard.set_off_canvas_sidebar()
    dashboard.set_title("Component Index")
    return dashboard.render()

def components(request):
    return HttpResponse("SOMETHING")

def dashboard(request):
    dashboard = Dashboard()
    dashboard.set_normal_sidebar(rowsheet_dashboard_sidebar)
    dashboard.set_off_canvas_sidebar()
    dashboard.set_title("Dashboard")
    return dashboard.render()

def dashboard_organizations(request):
    dashboard = Dashboard()
    dashboard.set_normal_sidebar(rowsheet_dashboard_sidebar)
    dashboard.set_off_canvas_sidebar()
    dashboard.set_title("Organizations")

    from rowsheet_apps.models import Organization
    organizations = Organization.objects.all().filter(author=request.user)
    body = render_to_string("app/organizations.html", context={
        "organizations": organizations,
    })
    dashboard.set_body(body)
    return dashboard.render()

def dashboard_apps(request):
    dashboard = Dashboard()
    dashboard.set_normal_sidebar(rowsheet_dashboard_sidebar)
    dashboard.set_off_canvas_sidebar()
    dashboard.set_title("Apps")
    from affiliate_marketing.views import BrandSliderSheet
    bss = BrandSliderSheet()
    body = bss.render()
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
