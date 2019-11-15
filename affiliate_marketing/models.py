from django.db import models
from datetime import datetime

#-------------------------------------------------------------------------------
#       ____                       ________      __                             
#      / __ )_________ _____  ____/ / ____/___ _/ /____  ____ _____  _______  __
#     / __  / ___/ __ `/ __ \/ __  / /   / __ `/ __/ _ \/ __ `/ __ \/ ___/ / / /
#    / /_/ / /  / /_/ / / / / /_/ / /___/ /_/ / /_/  __/ /_/ / /_/ / /  / /_/ / 
#   /_____/_/   \__,_/_/ /_/\__,_/\____/\__,_/\__/\___/\__, /\____/_/   \__, /  
#                                                     /____/           /____/
#-------------------------------------------------------------------------------

class BrandCategory(models.Model):
    name = models.CharField(max_length=64,
        verbose_name = "Brand Category",
        null=True, default=None, blank=True
    )
    def __str__(self):
        return str(self.name)

#-------------------------------------------------------------------------------
#       ____                       __
#      / __ )_________ _____  ____/ /
#     / __  / ___/ __ `/ __ \/ __  / 
#    / /_/ / /  / /_/ / / / / /_/ /  
#   /_____/_/   \__,_/_/ /_/\__,_/  
#
#-------------------------------------------------------------------------------

class Brand(models.Model):
    name = models.CharField(max_length=64,
        verbose_name="Brand Name",
        null=False,
        blank=False,
        default=None,
    )
    homepage_url = models.CharField(max_length=64,
        null=True, default=None, blank=True
    )
    category = models.ForeignKey(
        "BrandCategory",
        on_delete=models.SET_NULL,
        null=True, default=None, blank=True
    )
    brand_icon = models.ForeignKey(
        "cloud_storage.CloudFile",
            related_name="brand_icon",
        on_delete=models.SET_NULL,
        null=True, default=None, blank=True
    )
    priority = models.IntegerField(
        verbose_name = "Brand Priority",
        null=False, default=0, blank=False,
    )
    vendor_code = models.CharField(max_length=64,
        null=True, default=None, blank=True
    )
    storefront_category = models.CharField(max_length=64,
        verbose_name = "Storefront Category",
        null=True, default=None, blank=True
    )
    feature_active = models.BooleanField(
        verbose_name = "Brand Enabled",
        null=False, default=True, blank=False
    )
    trusted_active = models.BooleanField(
        verbose_name = "Trusted Brand",
        null=False, default=True, blank=False
    )
    trusted_priority = models.IntegerField(
        verbose_name = "Trusted Brand Priority",
        null=False, default=0, blank=False,
    )
    def __str__(self):
        return str(self.name)

#-------------------------------------------------------------------------------
#       ____                       _______ ___     __         
#      / __ )_________ _____  ____/ / ___// (_)___/ /__  _____
#     / __  / ___/ __ `/ __ \/ __  /\__ \/ / / __  / _ \/ ___/
#    / /_/ / /  / /_/ / / / / /_/ /___/ / / / /_/ /  __/ /    
#   /_____/_/   \__,_/_/ /_/\__,_//____/_/_/\__,_/\___/_/     
#
#-------------------------------------------------------------------------------

class BrandSlider(models.Model):
    class Meta:
        unique_together = (('name', 'brand'),)
    active = models.BooleanField(
        verbose_name="Slider Enabled",
        null=False, default=True, blank=False
    )
    name = models.CharField(max_length=64,
        null=True, default=None, blank=True
    )
    title = models.CharField(max_length=64,
        null=True, default=None, blank=True
    )
    subtitle = models.CharField(max_length=64,
        null=True, default=None, blank=True
    )
    description = models.TextField(
        null=True, default=None, blank=True
    )
    brand = models.ForeignKey(
        "Brand",
        on_delete=models.CASCADE,
        null=False, blank=False,
        default=None,
    )
    image = models.ForeignKey(
        "cloud_storage.CloudFile",
            related_name="brand_slider_image",
            on_delete=models.SET_NULL,
        null=True, default=None, blank=True
    )
    priority = models.IntegerField(
        verbose_name = "Slider Priority",
        null=False, default=0, blank=False,
    )
    button_active = models.BooleanField(
        verbose_name = "Show Custom Button",
        null=False, default=True, blank=False
    )
    button_text = models.CharField(max_length=64,
        null=True, default=None, blank=True
    )
    button_href = models.CharField(max_length=64,
        null=True, default=None, blank=True
    )
    homepage_button_active = models.BooleanField(
        verbose_name = "Show Homepage Link",
        null=False, default=True, blank=False
    )
    shop_button_active = models.BooleanField(
        verbose_name = "Show Shop Link",
        null=False, default=True, blank=False
    )
    creation_timestamp = models.DateTimeField(
            default=datetime.now, blank=False)
    last_changed_timestamp = models.DateTimeField(
            default=datetime.now, blank=False)
    def __str__(self):
        return str(self.name)

#-------------------------------------------------------------------------------
#     ______                __           ______                       __
#    /_  __/______  _______/ /____  ____/ / __ )_________ _____  ____/ /
#     / / / ___/ / / / ___/ __/ _ \/ __  / __  / ___/ __ `/ __ \/ __  / 
#    / / / /  / /_/ (__  ) /_/  __/ /_/ / /_/ / /  / /_/ / / / / /_/ /  
#   /_/ /_/   \__,_/____/\__/\___/\__,_/_____/_/   \__,_/_/ /_/\__,_/   
#
#-------------------------------------------------------------------------------
    
class TrustedBrand(models.Model):
    brand = models.ForeignKey(
        "Brand",
        on_delete=models.CASCADE,
        null=False, blank=False,
        default=None,
    )
    priority = models.IntegerField(
        null=False, default=0, blank=False,
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

class FeaturedAccordian(models.Model):
    name = models.CharField(max_length=64,
        null=True, default=None, blank=True
    )
    feature_text = models.TextField(
        null=True, default=None, blank=True
    )
    brand = models.ForeignKey(
        "Brand",
        on_delete=models.CASCADE,
        null=False, blank=False,
        default=None,
    )
    image = models.ForeignKey(
        "cloud_storage.CloudFile",
            related_name="featured_accoridan_image",
            on_delete=models.SET_NULL,
        null=True, default=None, blank=True
    )
    priority = models.IntegerField(
        null=False, default=0, blank=False,
    )
    active = models.BooleanField(
        verbose_name="Accoridion Enabled",
        null=True, default=True, blank=True
    )
    def __str__(self):
        return str(self.name)
