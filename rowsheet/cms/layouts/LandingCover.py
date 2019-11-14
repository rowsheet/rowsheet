from django.template.loader import render_to_string
from django.utils.safestring import mark_safe 
from django.http import HttpResponse

from rowsheet.cms import utils

class LandingCover:

    def __init__(self):
        self.context = {
            "title": None,
            "scripts": [],
            "stylesheets" : None,
            "header": None,
            "footer": None,
            "body": None,
            "alert": None,
        }
        self._stylesheets = [
            "rowsheet/layouts/landing_cover.css",
        ]
        self._body_rows = []

    def render(self):
        self.context["stylesheets"] = utils.compile_stylesheets(self._stylesheets)
        return HttpResponse(render_to_string(
                "layouts/landing_cover.html",
                context=self.context))

    def set_title(self, title):
        self.context["title"] = title

    def set_header(self, content=None, stylesheet=None):
        self._stylesheets.append(stylesheet)
        self.context["header"] = mark_safe(render_to_string(
            "components/landing_cover/header.html", {
                "content": content,
            },
        ))

    def set_footer(self, content=None, stylesheet=None):
        self._stylesheets.append(stylesheet)
        self.context["footer"] = mark_safe(render_to_string(
            "components/landing_cover/footer.html", {
                "content": content,
            },
        ))

    def set_body(self, content=None, stylesheet=None):
        self._stylesheets.append(stylesheet)
        self.context["body"] = mark_safe(render_to_string(
            "components/landing_cover/body.html", {
                "content": content,
            },
        ))

    def set_alert(self, alert):
        self.context["alert"] = mark_safe(alert)
