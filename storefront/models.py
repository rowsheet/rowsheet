# All these are reqiured for actual NULL:
#     null=True, default=None, blank=True
# Goddammit.

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
import datetime
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class ProductTag(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(blank=True, null=True)
    creation_timestamp = models.DateTimeField(auto_now_add=True)
    last_changed_timestamp = models.DateTimeField(auto_now=True)
    job_timestamp = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.name)

class Carousel(models.Model):
    name = models.CharField(max_length=64,
        null=False, blank=False
    )
    active = models.BooleanField(
        "active",
        default=True
    )
    def __str__(self):
        return str(self.name)

class CarouselItem(models.Model):
    product = models.ForeignKey(
        "Product",
        on_delete=models.CASCADE,
        null=False, blank=False
    )
    carousel= models.ForeignKey(
        "Carousel",
        on_delete=models.CASCADE,
        null=False, blank=False, default=None
    )
    priority = models.IntegerField(
        null=False, default=0, blank=False,
    )
    active = models.BooleanField(
        "active",
        default=True
    )

class Product(models.Model):
    parent_product = models.ForeignKey(
        "Product",
        on_delete=models.SET_NULL,
        null=True, default=None, blank=True
    )
    visible = models.BooleanField(
        "visible",
        default=True
    )
    for_sale = models.BooleanField(
        "for_sale",
        default=True
    )
    discontinued = models.BooleanField(
        "discontinued",
        default=True
    )
    tags = models.ManyToManyField(
        "ProductTag",
        null=True, default=None, blank=True
    )
    vendor = models.CharField(max_length=64)
    name = models.CharField(max_length=64,
        null=True, default=None, blank=True
    )
    upc = models.CharField(max_length=64,
        null=True, default=None, blank=True
    )
    vendor_code = models.CharField(max_length=64,
        null=True, default=None, blank=True
    )
    # man_part_number = models.CharField(max_length=64,
    #     null=True, default=None, blank=True
    # )
    # htc_number = models.CharField(max_length=64,
    #     null=True, default=None, blank=True
    # )

    # brand = models.CharField(max_length=64,
    #     null=True, default=None, blank=True
    # )
    # model = models.CharField(max_length=64,
    #     null=True, default=None, blank=True
    # )
    # text_document = models.TextField(blank=True, null=True)
    # spec_kv = models.TextField(blank=True, null=True)
    details_kv = models.TextField(blank=True, null=True)

    # msrp = models.DecimalField(max_digits=6,decimal_places=2,
    #     null=True, default=None, blank=True
    # )
    base_price = models.DecimalField(max_digits=6,decimal_places=2)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    uofm = models.CharField(max_length=64,
        null=True, default=None, blank=True
    )
    inventory = models.IntegerField(
        null=False, default=0, blank=False
    )
    bin_date = models.DateField("date created",default=datetime.date.today,
        null=True, blank=True
    )
    weight = models.DecimalField(max_digits=6, decimal_places=2,
        null=True, default=None, blank=True
    )
    category = models.CharField(max_length=64,
        null=True, default=None, blank=True
    )
    description = models.CharField(max_length=255,
        null=True, default=None, blank=True
    )
    image = models.ManyToManyField(
        "cloud_storage.CloudFile",
        null=True, default=None, blank=True
    )
    creation_timestamp = models.DateTimeField(auto_now_add=True)
    last_changed_timestamp = models.DateTimeField(auto_now=True)
    job_timestamp = models.DateTimeField(auto_now=True)
    # Add Adilas fields
    adilas_active = models.BooleanField(
        default=False
    )
    adilas_import_timestamp = models.DateTimeField(
        null=True, default=None, blank=True
    )
    adilas_import_error = models.BooleanField(
        null=True, default=None, blank=True
    )
    def __str__(self):
        return str(self.name)

#===============================================================================
#
# MAYBE LATER
#
#===============================================================================
class MembershipPlan(models.Model):
    name = models.CharField(max_length=64,
        null=True, default=None, blank=True
    )
    price = models.DecimalField(max_digits=6,decimal_places=2,
        null=True, default=None, blank=True
    )
    DAILY = 'daily'
    MONTHLY = 'monthly'
    QUARTERLY = 'quarterly'
    YEARLY = 'yearly'
    PERIOD = ( 
        (DAILY, 'daily'),
        (MONTHLY, 'monthly'),
        (QUARTERLY, 'quarterly'),
        (YEARLY, 'yearly'),
    )   
    period = models.CharField(
        max_length=32,
        choices=PERIOD,
        # NOT NULL, no default.
        null=False, default=MONTHLY
    )
    short_description = models.TextField(blank=True, null=True)
    long_description = models.TextField(blank=True, null=True)
    creation_timestamp = models.DateTimeField(auto_now_add=True)
    last_changed_timestamp = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.name)

class UserMembership(models.Model):
    class Meta:
        unique_together= ("user", "plan")
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True, default=None, blank=True
    )
    plan = models.ForeignKey(
        MembershipPlan,
        on_delete=models.SET_NULL,
        null=True, default=None, blank=True
    )
    start_date = models.DateField("User Membership Start Date",default=datetime.date.today,
        null=True, blank=True
    )
    end_date = models.DateField("User Membership End Date",default=datetime.date.today,
        null=True, blank=True
    )
    creation_timestamp = models.DateTimeField(auto_now_add=True)
    last_changed_timestamp = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.user.username)

class ProductPromotion(models.Model):
    product = models.ForeignKey(
        "Product",
        on_delete=models.SET_NULL,
        null=True, default=None, blank=True
    )
    category = models.ForeignKey(
        "ProductPromotionCategory",
        on_delete=models.SET_NULL,
        null=True, default=None, blank=True
    )
    tags = models.ManyToManyField(
        "ProductTag",
        null=True, default=None, blank=True
    )
    active = models.BooleanField(
        "active",
        default=True
    )
    title = models.CharField(max_length=32)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField("Start Date",default=datetime.date.today,
        null=True, blank=True
    )
    end_date = models.DateField("End Date",default=datetime.date.today,
        null=True, blank=True
    )
    promo_code = models.CharField(max_length=32, unique=True,
        null=True, default=None, blank=True
    )
    selling_price = models.DecimalField(max_digits=6,decimal_places=2,
        null=True, default=None, blank=True
    )
    discount = models.FloatField(default=0.5,
        validators=[MinValueValidator(0.0), MaxValueValidator(1.0)]
    )
    creation_timestamp = models.DateTimeField(auto_now_add=True)
    last_changed_timestamp = models.DateTimeField(auto_now=True)
    job_timestamp = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.title)

class EmployeeProductQA(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True, default=None, blank=True
    )
    product = models.ForeignKey(
        "Product",
        on_delete=models.SET_NULL,
        null=True, default=None, blank=True
    )
    date_assigned = models.DateTimeField(
        null=True, default=None, blank=True
    )
    date_submitted = models.DateTimeField(
        null=True, default=None, blank=True
    )
    date_due = models.DateTimeField(
        null=True, default=None, blank=True
    )
    comments = models.TextField(blank=True, null=True)
    rating_one = models.IntegerField(
        null=True, default=None, blank=True,
        validators=[MaxValueValidator(100), MinValueValidator(1)]
    )
    rating_two = models.IntegerField(
        null=True, default=None, blank=True,
        validators=[MaxValueValidator(100), MinValueValidator(1)]
    )
    creation_timestamp = models.DateTimeField(auto_now=True)
    def clean(self):
        if self.id is None:
            if self.product is None:
                raise ValidationError({
                    "product": ["Product is required for new QA assignments."]
                })
            if self.user is None:
                raise ValidationError({
                    "user": ["User is required for new QA assignments."]
                })

class ProductPromotionCategory(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(blank=True, null=True)
    creation_timestamp = models.DateTimeField(auto_now_add=True)
    last_changed_timestamp = models.DateTimeField(auto_now=True)
    job_timestamp = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.name)
