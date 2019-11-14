from django.db import models
from gcloud import storage
from oauth2client.service_account import ServiceAccountCredentials
from django.conf import settings
import uuid
from django.template.defaultfilters import slugify
from django.utils.safestring import mark_safe

class CloudFileCategory(models.Model):
	name = models.CharField(max_length=64,
		# NOT NULL, UNIQUE, no default.
		null=False, default=None, blank=False, unique=True
	)
	description = models.TextField(blank=True, null=True)
	creation_timestamp = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.name

class CloudFileTag(models.Model):
	name = models.CharField(max_length=64,
		# NOT NULL, UNIQUE, no default.
		null=False, default=None, blank=False, unique=True
	)
	description = models.TextField(blank=True, null=True)
	creation_timestamp = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.name

class CloudFile(models.Model):
	# Not actually used for anything.
	file_field = models.FileField(unique=True)
	gcloud_img_src = models.CharField(max_length=255,
		null=True, default=None, blank=True
	)
	category = models.ForeignKey(
		"CloudFileCategory",
		on_delete=models.SET_NULL,
		null=True, default=None, blank=True
	)
	tags = models.ManyToManyField(
		'CloudFileTag',
		null=True, default=None, blank=True
	)
	def save(self, *args, **kwargs):
		credentials_dict = { 
			"type": "service_account",
			"client_id": settings.GCLOUD_CLIENT_ID,
			"client_email": settings.GCLOUD_CLIENT_EMAIL,
			"private_key_id": settings.GCLOUD_PK_ID,
			"private_key": settings.GCLOUD_PK
		} 
		credentials = ServiceAccountCredentials.from_json_keyfile_dict(
			credentials_dict
		) 
		client = storage.Client(
			credentials=credentials,
			project=settings.GCLOUD_PROJECT
		)
		bucket = client.get_bucket(settings.GCLOUD_BUCKET)
		# The filename has to be both URL and FILENAME safe encoding.
		filename_slug = slugify(self.file_field.name)
		blob = bucket.blob(filename_slug)
		blob.upload_from_string(self.file_field.read())
		# In case there is a duplicate filename in gcloud, gcloud will
		# append the filename with some random chars. We need the final
		# filename returned by google to be saved into our record.
		gcloud_upload_filename = blob.public_url[len(settings.MEDIA_URL):]
		self.file_field.name = gcloud_upload_filename
		self.gcloud_img_src = blob.public_url
		super(CloudFile, self).save(*args, **kwargs)
	def __str__(self):
		return self.file_field.name
