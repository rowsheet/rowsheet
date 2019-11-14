from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

import numpy as np

register = template.Library()

def rs_card_label(label):
    if label[0:2] != "c_":
        return ""
    return """
    <div class="rs_card_label">
        <span>
            %s
        </span>
    </div>
    """ % label[2:].replace("_", " ")

def rs_card_item(item):
    return """
    <div class="rs_card_item">
    %s
    </div>""" % item

def rs_card_column(item):
    return """
    <div class="rs_card_column">
    %s
    </div>""" % item

def rs_card_row(columns):
    return """
    <div class="rs_card_row">
    %s
    </div>""" % columns 

@register.simple_tag
def rs_card_items(result, list_display):
    return  mark_safe("""
<div class="card-container">
    <div class="card my-2 mx-2 rs_card">
        <div class="front">
            <div class="card-header">
                %s
            </div>
            <div class="card-body">
                %s
            </div>
            <div class="card-footer">
                %s
            </div>
        </div>
        <div class="back">
            <div class="card-header">
                %s
            </div>
            <div class="card-body">
                %s
            </div>
            <div class="card-footer">
                %s
            </div>
        </div>
    </div>
</div>
    """ % (
            rs_card_item(
                rs_card_row ("".join([
                    rs_card_column(result[i])
                    for i in list(filter(lambda i: (
                        (i == 0) or 
                        (list_display[i] == "_priority") or 
                        (list_display[i] == "_edit")
                    ),list(range(len(list_display)))))])
                )
            ),
            "<hr>".join(
                "".join([
                    rs_card_label(list_display[i]),
                    rs_card_item(result[i]),
                ]) for i in list(filter(lambda i: [
                    (i != 0) and
                    [
                        (list_display[i] != "_priority") and
                        (list_display[i] != "_edit")
                    ]
                ],list(range(len(list_display)))))
            ),
            """
            <i class="material-icons">
                flip_camera_android
            </i>
            """,
            "back","back","back"
        )
    )

@register.simple_tag
def whatthefuck(cl):
    return  mark_safe("""WHATTHEFUCK""")
