from rest_framework import generics, permissions, filters, status
from rest_framework.response import Response

from author.models import Author
from .serializers import BooksSerializer
from .models import Books
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist


 # used the DRY principle
class BaseAuthUser:    
    permission_classes = [permissions.IsAuthenticated]
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    
    
class BooksCreateView(BaseAuthUser, generics.CreateAPIView):
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        queryset = self.get_queryset()  
        
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            author = serializer.validated_data.get('author')

            existing_books = queryset.filter(name=name, author=author)

            if existing_books.exists():
                return Response(
                    {'detail': 'A book with the same Name already exists.'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            next_book_id = self.get_next_available_book_id()
            if not next_book_id:
                return Response(
                    {'detail': 'Cannot generate a unique book_id.'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            serializer.validated_data['book_id'] = next_book_id
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_next_available_book_id(self):
        for i in range(1, 100):
            choice = f'BOOK{i}'
            if not Books.objects.filter(book_id=choice).exists():
                return choice
        return None
    
    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     if serializer.is_valid():
    #         name = serializer.validated_data.get('name')
    #         author = serializer.validated_data.get('author')
    #         existing_books = Books.objects.filter(name=name, author=author)
    #         if existing_books.exists():
    #             return Response(
    #                 {'detail': 'A book with the same name and author already exists.'},
    #                 status=status.HTTP_400_BAD_REQUEST
    #             )
    #         # Find the next available choice for book_id
    #         next_book_id = None
    #         for i in range(1, 100):
    #             choice = f'BOOK{i}'
    #             if not Books.objects.filter(book_id=choice).exists():
    #                 next_book_id = choice
    #                 break
                
    #         if next_book_id is None:
    #             return Response(
    #                 {'detail': 'Cannot generate a unique book_id.'},
    #                 status=status.HTTP_400_BAD_REQUEST
    #             )

    #         serializer.validated_data['book_id'] = next_book_id
    #         serializer.save()

    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
class BooksListView(BaseAuthUser, generics.ListAPIView):
    filter_backends = [filters.SearchFilter]
    search_fields = ['author_email', 'name']

class BooksRetrieveUpdateDestroyView(BaseAuthUser, generics.RetrieveUpdateDestroyAPIView):
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)

        deleted_book_data = {
            'author_name': instance.author_name,
            "name": instance.name,
        }
        return Response(
            {"detail": "Books deleted successfully", "deleted_book_details": deleted_book_data},
            status=status.HTTP_200_OK
        )
        
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        queryset = self.get_queryset()
        
        if serializer.is_valid():
            name = serializer.validated_data.get('name', instance.name)
            author = serializer.validated_data.get('author', instance.author)
            
            # existing_books = Books.objects.filter(name=name, author=author).exclude(book_id=instance.book_id)
            
            existing_books =queryset.filter(name=name, author=author).exclude(book_id=instance.book_id)
            
            if existing_books.exists():
                return Response(
                    {'detail': 'A book with the same name and author already exists.'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Dashboard total count
class TotalCountView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        try:
            book_total_count = Books.objects.count()
            active_status_count = Books.objects.filter(is_active=True).count()
            
        except ObjectDoesNotExist:
            return Response(
                {'error': 'books table does not exist'}
                , status=status.HTTP_404_NOT_FOUND
            )

        return Response({'book_total_count': book_total_count, 'active_status_count': active_status_count})