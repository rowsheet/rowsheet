from django.utils.safestring import mark_safe
from django.urls import reverse

DEFAULT_IMAGE_SRC = "https://storage.googleapis.com/rowsheet/assets/img/no_image_found.jpg"

def tableview_active(active, name="", outline=False, width=None):
    button = "secondary"
    label = "NA"
    toggle = "warning"
    style = ""
    label_style = ""
    if active == True:
        label = "Enabled"
        button = "success"
        toggle = "toggle_on"
    if active == False:
        label = "Disabled"
        button = "danger"
        toggle = "toggle_off"
    if outline == True:
        style = "outline-"
    if width is not None:
        label_style = "style='width: %spx;'" % width
    # @TODO Re-enable toggle when AJAX is working.
    toggle = ""
    return mark_safe("""
    <div class="tableview_active">
    <nobr>
        <div class='tableview_subcell_key' %s>%s Status:</div>
        <span class='tableview_subcell_value'>
            <button type="button" class="btn btn-sm btn-%s%s btn-toggle">
                <i class="material-icons">
                    %s
                </i>
                %s
            </button>
        </span>
    </nobr>
    </div>
    """ % (
        label_style,
        name,
        style,
        button,
        toggle,
        label
        )
    )

def tableview_label(text, fmt="text", wrap=None, width=None, label_force=None):
    print("TEXT: " + str(text))
    html = text
    label = text
    style = ""
    # Set html to "-" and popover "Empty" if None or zero length.
    if text is None:
        label = "Empty"
        html = "-"
    if text == "":
        label = "Empty"
        html = "-"
    # Wrap if provided.
    if wrap is not None:
        html = wrap % html
    # Use css width if not custom provided.
    if width is not None:
        style = "style='width: %spx;'" % width
    # Set the label explicitly if set.
    if label_force is not None:
        label = label_force
    print("HTML: " + str(html))
    return mark_safe("""
    <div class="
            tableview_label
            tableview_label_%s
        "
        data-trigger="hover"
        data-container="body"
        data-toggle="popover"
        data-placement="right"
        data-content="%s"
        %s
    >
        %s
    </div>
    """ % (
        fmt,
        label,
        style,
        html,
        )
    )

def model_link(obj, label):
    app_label = obj._meta.app_label.lower()
    object_name = obj._meta.object_name.lower()
    link=reverse(
        "admin:%s_%s_change" % (
            app_label,
            object_name,
        ),
        args=[obj.id]
    )
    return mark_safe("""
    <div class="tableview_model_link">
    <a href="%s" class="btn btn-outline-primary">
        %s
    </a>
    </div>
    """ % (
            link,
            tableview_label(label, label_force =
                "View %s %s" % (
                    object_name, label
                )
            ),
        )
    )

def tableview_priority(number):
    return mark_safe("""
    <div class="tableview_priority">
    <div style="
        text-align: center;
        font-size: 1.25rem;
        font-weight: bold;
    ">
        %s
    </div>
    </div>
    """ % number)

def tableview_text(text):
    if text is None:
        return mark_safe("""
        <div class="tableview_text">
            -
        </div>
        """)
    if text == "":
        return mark_safe("""
        <div class="tableview_text">
            -
        </div>
        """)
    return mark_safe("""
    <div class="tableview_text">
        <i class="fas fa-quote-left"
            style="
                font-size: 1.5rem;
                color: #8b99a761;
                margin: 3px;
            "></i>
        %s
    </div>
    """ % text)

def edit_button():
    return mark_safe("""
    <div class="tableview_edit_button">
    <div class='btn btn-outline-primary'
        style="
        padding-left: 30px;
        ">
        <i class="material-icons"
            style="
            vertical-align: middle;
            margin-left: -20px;
            font-size: 15px;
            ">
            edit
        </i>
        Edit
    </div>
    </div>
    """)

def button(active, href, text, name="", outline=True):
    status = tableview_active(active, name=name, outline=outline, width=50)
    disabled = ""
    if active == False:
        disabled = "disabled"
    return mark_safe("""
    <div class="tableview_button">
    <div>
        %s
        <div style="height: 5px;"></div>
        <div class="%s">
            <a href="%s" class="button btn %s" style="width: 150px;">%s</a>
        </div>
    </div>
    </div>
    """ % (
            status,
            disabled,
            href,
            disabled,
            text
        )
    )

def tableview_href(href):
    if href is None:
        return "-"
    return mark_safe("""
    <div class="tableview_href">
    <a href="%s">
        <code>
            %s
        </code>
    </a>
    </div>
    """ % (href, href)
    )

# @TODO Support other types.
def tableview_cloudfile(cloudfile, type="image"):
    gcloud_img_src = DEFAULT_IMAGE_SRC
    if cloudfile is not None:
        gcloud_img_src = cloudfile.gcloud_img_src
    html = """
        <a target="_blank" rel="noopener noreferrer" href="%s">
            <img 
                class="image_preview"
                src="%s"/>
        </a>
    """ % (
            gcloud_img_src,
            gcloud_img_src,
        )
    return mark_safe("""
    <div class="tableview_cloudfile">
    <div class="admin_table_image_list_container">
        <div class="admin_table_image_list_content">
        %s 
        </div>
    </div>
    </div>
    """ % html)

#-------------------------------------------------------------------------------
#       ____                       __
#      / __ )_________ _____  ____/ /
#     / __  / ___/ __ `/ __ \/ __  / 
#    / /_/ / /  / /_/ / / / / /_/ /  
#   /_____/_/   \__,_/_/ /_/\__,_/  
#
#-------------------------------------------------------------------------------

def tableview_brand_info(active, name, trusted, width=300):
    status = tableview_active(active, name="Brand")
    trusted_status = tableview_active(trusted, name="Trusted")
    return mark_safe("""
    <div class="tableview_brand_info">
        %s%s%s
    </div>
    """ % (
        status,
        trusted_status,
        tableview_label(name,
            wrap="""
            <div class='tableview_subcell_key'>Brand Name:</div>
            <span class='tableview_subcell_value tableview_subtitle'>%s</span>
            """,
            width=width),
        )
    )

def brand_link(brand, label):
    status = tableview_active(brand.feature_active, name="Brand", outline=True)
    return mark_safe("""
    <div class="tableview_brand_link">
    <div style="text-align: center; display: inline-block;">
        %s
        <div style="height: 5px;"></div>
        %s
    </div>
    </div>
    """ % (
            status,
            model_link(brand, label)
        )
    )

#-------------------------------------------------------------------------------
#       ______           __                          
#      / ____/__  ____ _/ /___  __________           
#     / /_  / _ \/ __ `/ __/ / / / ___/ _ \          
#    / __/ /  __/ /_/ / /_/ /_/ / /  /  __/          
#   /_/ ___\___/\__,_/\__/\__,_/_/   \____           
#      /   | ______________  _________/ (_)___ _____ 
#     / /| |/ ___/ ___/ __ \/ ___/ __  / / __ `/ __ \
#    / ___ / /__/ /__/ /_/ / /  / /_/ / / /_/ / / / /
#   /_/  |_\___/\___/\____/_/   \__,_/_/\__,_/_/ /_/ 
#
#-------------------------------------------------------------------------------

def tableview_accordian_info(active, feature_text, name, width=400, label_width=125):
    status = tableview_active(active, name="Accordion", width=label_width)
    wrap = """
    <div class='tableview_subcell_key' style="width: """ + str(label_width) + """px;">Title:</div>
    <span class='tableview_subcell_value tableview_title'>%s</span>
    """
    wrap_name = """
    <div class='tableview_subcell_key' style="width: """ + str(label_width) + """px;">Name:</div>
    <span class='tableview_subcell_value tableview_subtitle'>%s</span>
    """
    return mark_safe("""
        <div class="tableview_accordian_info"> 
        %s%s%s
        </div>
    """ % (
            status,
            tableview_label(name,
                wrap=wrap_name,
                width=width,
            ),
            tableview_label(feature_text,
                wrap=wrap,
                width=width,
            ),
        )        
    )

#-------------------------------------------------------------------------------
#       ____                       _______ ___     __         
#      / __ )_________ _____  ____/ / ___// (_)___/ /__  _____
#     / __  / ___/ __ `/ __ \/ __  /\__ \/ / / __  / _ \/ ___/
#    / /_/ / /  / /_/ / / / / /_/ /___/ / / / /_/ /  __/ /    
#   /_____/_/   \__,_/_/ /_/\__,_//____/_/_/\__,_/\___/_/     
#
#-------------------------------------------------------------------------------

def tableview_slide_info(active, title, subtitle, width=200):
    status = tableview_active(active, name="Slide")
    return mark_safe("""
        <div class="tableview_slider_info"> 
        %s%s%s
        </div>
    """ % (
            status,
            tableview_label(title,
                wrap="""
                <div class='tableview_subcell_key'>Title:</div>
                <span class='tableview_subcell_value tableview_title'>%s</span>
                """,
                width=width),
            tableview_label(subtitle,
                wrap="""
                <div class='tableview_subcell_key'>Subtitle:</div>
                <span class='tableview_subcell_value tableview_subtitle'>%s</span>
                """,
                width=width),
        )
    )
