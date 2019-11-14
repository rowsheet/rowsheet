from django.utils.safestring import mark_safe 

def compile_stylesheets(paths):
    # Only take unique cases for where the path is not None.
    paths = list(set(list(filter(lambda x: x is not None, [ x for x in paths ]))))
    return mark_safe("".join(["""
        <link href="%s" rel="stylesheet">
        """ % ("/static/" + path)
        for path in paths]))
