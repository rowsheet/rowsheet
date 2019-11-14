from django.template.loader import render_to_string
from django.utils.safestring import mark_safe 

class BasicFooter:

    def __init__(self):
        self._footer_rows = []

    def set_copyright(self, copyright_year=None, copyright_author=None, copyright_extra=None):
        self._footer_rows.append(render_to_string(
            "components/legal/copyright.html", {
                "year": copyright_year,
                "author": copyright_author,
                "extra": copyright_extra,
            },
        ))

    def add_common_links(self, common_links = None):
        self._footer_rows.append((" | ".join(
            ("""<a href="%s">%s</a>""" % (link["href"], link["title"]))
            for link in common_links
        )))

    def render(self):
        return mark_safe("<br>".join(self._footer_rows))
