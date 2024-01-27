from django.urls import path
from . import views



urlpatterns = [
    path('create_author/', views.AuthorCreateView.as_view(), name='create_author'),
    path('all_authors/', views.AuthorListView.as_view(), name='view_authors'),
    path('author/<int:pk>/', views.AuthorRetrieveUpdateDestroyView.as_view(), name='retrieve_update_destroy_author'),
    path('author_total_count/', views.TotalCountView.as_view(), name='dashboard_total_count')
]
