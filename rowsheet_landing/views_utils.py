from django.conf import settings

from rowsheet.cms.components.common.BasicNav import BasicNav
from rowsheet.cms.components.common.BasicFooter import BasicFooter

def rowsheet_landing_header():
    basic_nav = BasicNav(
        title = settings.RS_WEBSITE_TITLE,
        homepage_url = settings.RS_WEBSITE_HOMEPAGE_URL,
        nav_links = settings.RS_WEBSITE_NAV_LINKS,
        logo_url = settings.RS_WEBSITE_LOGO_URL,
    )
    return basic_nav.render()

def rowsheet_landing_footer():
    basic_footer = BasicFooter()
    basic_footer.add_common_links([
        {
            "href": "/",
            "title": "Home",
        },
        {
            "href": "/admin",
            "title": "Admin",
        },
        {
            "href": "/accounts/login",
            "title": "Login",
        },
        {
            "href": "/accounts/logout",
            "title": "Logout",
        },
    ])
    basic_footer.set_copyright(
        copyright_year = settings.RS_WEBSITE_COPYRIGHT_YEAR,
        copyright_author = settings.RS_WEBSITE_COPYRIGHT_AUTHOR,
        copyright_extra = settings.RS_WEBSITE_COPYRIGHT_EXTRA,
    )
    return basic_footer.render()

def rowsheet_landing_alert(request):
    alert = None
    if request.user.is_authenticated:
        alert = """Welcome back, <strong>%s</strong>!
        <a href="/dashboard" class="btn btn-sm btn-primary my-1">
            <i class="fas fa-desktop"></i>
            Dashboard
        </a>
        <a href="/accounts/logout" class="btn btn-sm btn-primary my-1">
            <i class="fas fa-sign-out-alt"></i>
            Logout
        </a>
        """ % request.user
        if request.user.is_staff:
            alert += """
            <a href="/admin" class="btn btn-sm btn-dark my-1">
                Admin
            </a>"""
    else:
        alert = """Welcome to <strong>RowSheet</strong>!
        <a href="/accounts/login" class="btn btn-sm btn-primary my-1">
            <i class="fas fa-sign-in-alt"></i>
            Sign In 
        </a>
        """
    return alert
