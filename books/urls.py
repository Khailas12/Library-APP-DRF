from django.urls import path
from . import views

urlpatterns = [
    path('create_book/', views.BooksCreateView.as_view(), name='create_book'),
    path('all_books/', views.BooksListView.as_view(), name='view_books'),
    path('book/<int:pk>/', views.BooksRetrieveUpdateDestroyView.as_view(), name='retrieve_update_destroy_book'),
    path('total_book_count/', views.TotalCountView.as_view(),'dashboard book count')
]