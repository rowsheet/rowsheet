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

        self.body_loaders = []
        self.active_loader = None
    def render(self):

        # Set the stylesheets.
        self.context["stylesheets"] = utils.compile_stylesheets(self._stylesheets)

        # Set the notification loaders (notify if any new "unread" alerts
        # or messages exist).
        notifications_loader = NotificationsLoader(
            new_alerts = self.new_alerts,
            new_messages = self.new_messages,
        )
        self.context["notifications_loader"] = mark_safe(notifications_loader.render())

        # Set the username and profile picture for the profile dropdown.
        profile_dropdown = ProfileDropdown(
            username = self.username,
            profile_photo = self.profile_photo,
        )
        self.context["profile_dropdown"] = mark_safe(profile_dropdown.render())

        # Set body loaders from config. Set the active loader to the first
        # if no active loader is set.
        if self.context["body"] is None:
            self.context["body_loaders"] = self.body_loaders
            self.context["active_loader"] = self.active_loader
            if self.active_loader not in [loader["safe_title"] for loader in self.body_loaders]:
                self.context["active_loader"] = self.body_loaders[0]["safe_title"]
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

    def set_loader(self, title, path):
        self.body_loaders.append({
            # Set "safe_title" so we can compare the get request with the
            # id from the loader (hopefully unique).
            "safe_title": title.replace(" ",""),
            "title": title,
            "path": path,
        })

    def set_active_loader(self, title):
        self.active_loader = title
