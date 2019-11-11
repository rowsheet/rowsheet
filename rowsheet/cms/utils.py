from django.utils.safestring import mark_safe 

def compile_stylesheets(app, paths):
    return mark_safe("".join(["""
        <link href="%s" rel="stylesheet">
        """ % ("/static/" + app + path)
        for path in paths]))
