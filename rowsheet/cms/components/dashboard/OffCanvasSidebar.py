from django.template.loader import render_to_string

class OffCanvasSidebar:

    def __init__(self, config=None):
        self.config = config 

    def render(self):
        return render_to_string(
            "components/dashboard/off_canvas_sidebar.html", {
                "sidebar": self.config,
            })
