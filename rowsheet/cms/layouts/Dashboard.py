from django.template.loader import render_to_string
from django.utils.safestring import mark_safe 
from django.http import HttpResponse

from rowsheet.cms import utils
from rowsheet.cms.components.dashboard.NormalSidebar import NormalSidebar
from rowsheet.cms.components.dashboard.OffCanvasSidebar import OffCanvasSidebar
from rowsheet.cms.components.dashboard.NotificationsLoader import NotificationsLoader
from rowsheet.cms.components.dashboard.ProfileDropdown import ProfileDropdown

class Dashboard:

    def __init__(self):
        self.context = {
            "title": None,
            "scripts": [],
            "stylesheets" : None,

            "body": None,

            "normal_sidebar": None,
            "off_canvas_sidebar": None,
        }
        self.new_alerts = None
        self.new_messages = None
        self.username = None
        self.profile_photo = None
        self._stylesheets = []
        self._body_rows = []

    def render(self):

        self.context["stylesheets"] = utils.compile_stylesheets(self._stylesheets)

        notifications_loader = NotificationsLoader(
            new_alerts = self.new_alerts,
            new_messages = self.new_messages,
        )
        self.context["notifications_loader"] = mark_safe(notifications_loader.render())

        profile_dropdown = ProfileDropdown(
            username = self.username,
            profile_photo = self.profile_photo,
        )
        self.context["profile_dropdown"] = mark_safe(profile_dropdown.render())

        return HttpResponse(render_to_string(
                "layouts/dashboard.html",
                context=self.context))

    def set_title(self, title):
        self.context["title"] = title

    def set_body(self, content=None, stylesheet=None):
        self._stylesheets.append(stylesheet)
        self.context["body"] = mark_safe(content)

    def set_off_canvas_sidebar(self, config=None):
        off_canvas_sidebar = OffCanvasSidebar(config=config)
        self.context["off_canvas_sidebar"] = mark_safe(off_canvas_sidebar.render())

    def set_normal_sidebar(self, config=None):
        normal_sidebar = NormalSidebar(config=config)
        self.context["normal_sidebar"] = mark_safe(normal_sidebar.render())

    def set_new_alerts(self, new_alerts):
        self.new_alerts = new_alerts

    def set_new_messages(self, new_messages):
        self.new_messages= new_messages

    def set_user_profile(self, username=None, profile_photo=None):
        self.username = username
        self.profile_photo = profile_photo
