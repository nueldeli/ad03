from django import forms
from .models import Division
from django.utils.translation import gettext_lazy as _

class UpdateFigureForm(forms.ModelForm):
	class Meta:
		model = Division
		fields = ('div_name', 'div_img', 'population', 'area', 'elevation')

		widgets = {
			'div_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Division name'}),
			'population':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Population'}),
			'area':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Area'}),
			'elevation':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Elevation'})
		}

		labels= {
			'div_name':_(''),
			'population':_(''),
			'area':_(''),
			'elevation':_(''),
		}
