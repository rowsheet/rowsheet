from django.template.loader import render_to_string

class NormalSidebar:

    def __init__(self, config=None):
        self.config = config 

    def render(self):
        return render_to_string(
            "components/dashboard/normal_sidebar.html", {
                "sidebar": self.config,
            })
