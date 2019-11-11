from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe 

def index(request):
    context = {
        "scripts": [
        ],
        "title": settings.RS_WEBSITE_TITLE,
        "header": mark_safe(render_to_string(
            "components/landing_cover/header.html", {
                "content": render_to_string(
                    "components/common/basic_nav.html", {
                    "title":        settings.RS_WEBSITE_TITLE,
                    "homepage_url": settings.RS_WEBSITE_HOMEPAGE_URL,
                    "nav_links":    settings.RS_WEBSITE_NAV_LINKS,
                    "logo_url":     settings.RS_WEBSITE_LOGO_URL,
                    }
                ),
            },
        )),
        "body": mark_safe(render_to_string(
            "components/landing_cover/body.html", {
                "content": render_to_string(
                    "components/rowsheet/terminal_banner.html"
                ),
            },
        )),
        "footer": mark_safe(render_to_string(
            "components/landing_cover/footer.html", {
                "content": render_to_string(
                    "components/legal/copyright.html", {
                    "year":     settings.RS_WEBSITE_COPYRIGHT_YEAR,
                    "author":   settings.RS_WEBSITE_COPYRIGHT_AUTHOR,
                    "extra":    settings.RS_WEBSITE_COPYRIGHT_EXTRA,
                    },
                ),
            },
        )),
    }
    return render(request, "pages/index.html", context=context)
