from django.shortcuts import render
import pandas as pd
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from .models import Division
from .forms import UpdateFigureForm

# Create your views here.
def figure_index_view(request):
	div_object = Division.objects.all()
	item = div_object.values()
	df = pd.DataFrame(item)
	div_label = df.div_name.to_list()
	div_pop = df['population'].to_list()
	return render(request, 'figure/figure_index.html', {
			'div_object':div_object,
			'div_label':div_label,
			'div_pop':div_pop
		})

class FigureDetailView(DetailView):
	model = Division
	template_name = 'figure/figure_detail.html'

class UpdateFigureView(UpdateView):
	model = Division
	template_name = 'figure/figure_update.html'
	form_class = UpdateFigureForm