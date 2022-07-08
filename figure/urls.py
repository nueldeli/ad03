from django.urls import path
from .views import figure_index_view, FigureDetailView, UpdateFigureView

urlpatterns = [
	path('figure_index/', figure_index_view, name='figure_index'),
	path('figure_detail/<int:pk>', FigureDetailView.as_view(), name='figure_detail'),
	path('figure_update/<int:pk>', UpdateFigureView.as_view(), name='figure_update')
]