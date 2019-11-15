from django.template import Template, Context

class SheetView:

    def _render_list(self):
        template = Template("""
<style>
.sheet_view_wrapper {
    overflow: scroll;
}

.sheet_view thead {
    background: #77ba40;
}
.sheet_view thead * {
    font-family: "Oswald";
    color: white;
    font-size: 14px;
    text-transform: uppercase;
}
.sheet_view tbody {
    background: white;
}
.sheet_view tbody tr {
    border-bottom: 1px solid #eeeeee;
}
.sheet_view img.image_preview {
    width: 150px;
    height: 75px;
    object-fit: contain;
}
.sheet_view tbody * {
    font-size: 15px !important;
}
.sheet_view .btn-toggle {
    font-size: 10px !important;
}
.sheet_view thead td {
    border-right: 2px solid white;
    padding-left: 5px;
    padding-right: 5px;
}
.sheet_view tbody td {
    padding-left: 10px;
    padding-right: 10px;
}
.sheet_view a.button.btn {
    border: 1px solid;
}
.sheet_view a.button.btn:hover {
    border: 1px solid;
    background: #4d73df;
    color: white;
}
.sheet_view tbody td:nth-child(even) {
    background: #77ba3f0f;
}
</style>
        <div class="sheet_view_wrapper">
            <table class="sheet_view">
                <thead>
                    <tr>
                        {% for field in fields %}
                        <td>
                            {{ field }}
                        </td>
                        {% endfor %}
                    </tr>
                </thead>
                <tbody>
                    {% for row in rows %}
                    <tr>
                        {% for column in row %}
                        <td>
                            {{ column }}
                        </td>
                        {% endfor %}
                    </tr>
                    {% endfor %}
                </tbody>
                <thead>
                    <tr>
                        {% for field in fields %}
                        <td>
                            {{ field }}
                        </td>
                        {% endfor %}
                    </tr>
                </thead>
            </table>
        </div>
        """)
        fields = self.list_display
        query = self.model.objects.all()
        rows = [
            [getattr(self, field)(item) for field in fields]
            for item in query
        ]
        context = {
            "model_name": self.model.__name__,
            "fields": fields,
            "rows": rows,
        }
        return template.render(Context(context))

    def render(self):
        # return self._render_sheet()
        return self._render_list()
