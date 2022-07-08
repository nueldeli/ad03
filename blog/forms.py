from django import forms
from .models import Post
from django.utils.translation import gettext_lazy as _

class AddPostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('author', 'title', 'division_name', 'content')

		widgets = {
			'author':forms.TextInput(attrs={'class':'form-control', 'value':'', 'id':'writer', 'type':'hidden'}),
			'title':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Post title'}),
			'division_name':forms.Select(attrs={'class':'form-control'}),
			'content':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Start writing'})
		}

		labels = {
			'author':_(''),
			'title':_(''),
			'division_name':_(''),
			'content':_('')
		}

class UpdatePostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('author', 'title', 'division_name', 'content')

		widgets = {
			'author':forms.TextInput(attrs={'class':'form-control', 'value':'', 'id':'writer', 'type':'hidden'}),
			'title':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Post title'}),
			'division_name':forms.Select(attrs={'class':'form-control'}),
			'content':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Start writing'})
		}

		labels = {
			'author':_(''),
			'title':_(''),
			'division_name':_(''),
			'content':_('')
		}