from django.urls import path
from .views import PostIndexView , PostDetailView, PostAddView, PostUpdateView, PostDeleteView

urlpatterns = [
	path('post_index/', PostIndexView.as_view(), name='post_index'),
	path('post_add/', PostAddView.as_view(), name='post_add'),
	path('post_detail/<int:pk>', PostDetailView.as_view(), name='post_detail'),
	path('post_update/<int:pk>', PostUpdateView.as_view(), name='post_update'),
	path('post_delete/<int:pk>', PostDeleteView.as_view(), name='post_delete')
]