from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import CloudFile
from .models import CloudFileTag
from .models import CloudFileCategory

class CloudFileTagAdmin(admin.ModelAdmin):
	list_display = (
		"name",
		"description",
		"creation_timestamp",
	)
admin.site.register(CloudFileTag, CloudFileTagAdmin)

class CloudFileCategoryAdmin(admin.ModelAdmin):
	list_display = (
		"name",
		"description",
		"creation_timestamp",
	)
admin.site.register(CloudFileCategory, CloudFileCategoryAdmin)

class CloudFileAdmin(admin.ModelAdmin):
	list_display = (
		"_file_field_name",
		"_gcloud_img_src",
		"category",
		"_tags",
	)
	# search_fields = (
	#	"file_field__name",
	#	"gcloud_img_src",
	#)

	def _file_field_name(self, obj):
		return obj.file_field.name

	def _tags(self, obj):
		return mark_safe("".join([
			('<div class="dash_tag">%s</div>' % tag.name) for tag in obj.tags.all()
		]))

	def _gcloud_img_src(self, obj):
		return mark_safe(u'<a target="_blank" rel="noopener noreferrer" href="%s"><img style="height: 75px;width: 75px;object-fit: cover;" src="%s"/></a>' % (obj.gcloud_img_src, obj.gcloud_img_src))
admin.site.register(CloudFile, CloudFileAdmin)
