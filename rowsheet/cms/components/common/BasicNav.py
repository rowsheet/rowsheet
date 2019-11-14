from django.template.loader import render_to_string

class BasicNav:

    def __init__(self, title=None, homepage_url=None, nav_links=None, logo_url=None):
        self.title = title
        self.homepage_url = homepage_url
        self.nav_links = nav_links
        self.logo_url = logo_url

    def render(self):
        return render_to_string(
            "components/common/basic_nav.html", {
                "title": self.title,
                "homepage_url": self.homepage_url,
                "nav_links": self.nav_links,
                "logo_url": self.logo_url,
            }
        )

