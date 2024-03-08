from django.shortcuts import render
from .models import Book, User
from .serializers import BookSerializer, UserSerializer
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, RetrieveAPIView
from rest_framework import status
from rest_framework.response import Response
# Create your views here.

class BookListCreateView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class=BookSerializer

class BookDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer

class UserListView(ListAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class UserDetailView(RetrieveAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class BorrowBookView(APIView):
    def post(self,request,user_id,book_id):
        user=User.objects.get(pk=user_id)
        book=Book.objects.get(pk=user_id)

        if book in user.borrowed_books.all():
            return Response({"detail":"User already borrowed this book"},status=status.HTTP_400_BAD_REQUEST)
        user.borrowed_books.add(book)
        return Response({"detail":"Book borrowed successfully"},status=status.HTTP_201_CREATED)
class ReturnBookView(APIView):
    def post(selfself,request,user_id,book_id):
        user=User.objects.get(pk=user_id)
        book=Book.objects.get(pk=book_id)

        if book not in user.borrowed_books.all():
            return Response({"detail":"User has not borrowed this book"},status=status.HTTP_400_BAD_REQUEST)
        user.borrowed_books.remove(book)
        return Response({"detail":"Book returned successfully"},status=status.HTTP_200_OK)
