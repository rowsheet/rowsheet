from django.template.loader import render_to_string
from django.utils.safestring import mark_safe 
from django.http import HttpResponse

from rowsheet.cms import utils

class Dashboard:

    def __init__(self):
        self.context = {
            "title": None,
            "scripts": [],
            "stylesheets" : None,

            "header": None,
            "footer": None,
            "body": None,

            "alert": None,
            "sidebar": None,
        }
        self._stylesheets = []
        self._body_rows = []

    def render(self):
        self.context["stylesheets"] = utils.compile_stylesheets(self._stylesheets)
        return HttpResponse(render_to_string(
                "layouts/dashboard.html",
                context=self.context))

    def set_title(self, title):
        self.context["title"] = title

    def set_body(self, content=None, stylesheet=None):
        self._stylesheets.append(stylesheet)
        self.context["body"] = mark_safe(content)

    def set_alert(self, alert):
        self.context["alert"] = mark_safe(alert)

    def set_sidebar(self, sidebar):
        self.context["sidebar"] = sidebar
