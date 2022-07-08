from django.db import models
from django.urls import reverse

# Create your models here.
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

class Division(models.Model):
	div_name = models.CharField(max_length=100, choices=DIVISION_CHOICES, default='KUCHING')
	div_img = models.ImageField('Division image', null=True, blank=True, upload_to='div_img/')
	population = models.IntegerField()
	area = models.FloatField(null=True)
	elevation = models.FloatField(null=True)

	class Meta:
		ordering = ['-population']

	def __str__(self):
		return self.div_name

	def get_absolute_url(self):
		return reverse('figure_index')