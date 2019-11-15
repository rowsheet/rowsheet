from django.template.loader import render_to_string

class ProfileDropdown:

    def __init__(self, username=None, profile_photo=None):
        self.username = username
        self.profile_photo = profile_photo

    def render(self):
        return render_to_string(
            "components/dashboard/profile_dropdown.html", {
                "username": self.username,
                "profile_photo": self.profile_photo,
            })
