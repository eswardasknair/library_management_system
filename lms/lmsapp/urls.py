# urls.py
from django.urls import path
from .views import BookListCreateView, BookDetailView, UserListView, UserDetailView, BorrowBookView, ReturnBookView

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('borrow/<int:user_id>/<int:book_id>/', BorrowBookView.as_view(), name='borrow-book'),
    path('return/<int:user_id>/<int:book_id>/', ReturnBookView.as_view(), name='return-book'),
]
