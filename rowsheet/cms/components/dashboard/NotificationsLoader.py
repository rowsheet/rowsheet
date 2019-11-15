from django.template.loader import render_to_string

class NotificationsLoader:

    def __init__(self, new_alerts=None, new_messages=None):
        self.new_alerts = new_alerts
        self.new_messages = new_messages

    def render(self):
        return render_to_string(
            "components/dashboard/notifications_loader.html", {
                "new_alerts": self.new_alerts,
                "new_messages": self.new_messages,
            })
