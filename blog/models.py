from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models.fields.files import ImageFieldFile, FileField

# Create your model here
DIVISION_CHOICES = (
		("KUCHING", "Kuching"),
		("SRI AMAN", "Sri Aman"),
		("SARIKEI", "Sarikei"),
		("KAPIT", "Kapit"),
		("SIBU", "Sibu"),
		("BINTULU", "Bintulu"),
		("MIRI", "Miri"),
		("LIMBANG", "Limbang"),
		("LAWAS", "Lawas"),
	)

# Create your models here.
class Post(models.Model):
	date_written = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	title = models.CharField(max_length=250)
	division_name = models.CharField(max_length=100, choices=DIVISION_CHOICES, default='KUCHING')
	content = RichTextUploadingField()

	class Meta:
		ordering = ['-date_written']

	def __str__(self):
		return self.division_name 

	def get_absolute_url(self):
		return reverse('post_index')