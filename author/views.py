from rest_framework import generics, permissions, filters, status
from rest_framework.response import Response
from .models import Author
from .serializers import AuthorSerializer
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist


 # used the DRY principle
class BaseAuthUser:    
    permission_classes = [permissions.IsAuthenticated]
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    
    
class AuthorCreateView(BaseAuthUser, generics.CreateAPIView):
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            email = serializer.validated_data['email']
            existing_authors = Author.objects.filter(username=username, email=email)
            if existing_authors.exists():
                return Response(
                    {'detail': 'An author with the same username or email already exists.'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthorListView(BaseAuthUser, generics.ListAPIView):
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', 'email', 'name']

class AuthorRetrieveUpdateDestroyView(BaseAuthUser, generics.RetrieveUpdateDestroyAPIView):
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)

        deleted_author_data = {
            "username": instance.username,
            "email": instance.email,
            "name": instance.name,
        }
        return Response(
            {"detail": "Author deleted successfully", "deleted_author_details": deleted_author_data},
            status=status.HTTP_200_OK
        )

# Dashboard total count
class TotalCountView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        try:
            author_total_count = Author.objects.count()
            active_status_count = Author.objects.filter(is_active=True).count()
            
        except ObjectDoesNotExist:
            return Response(
                {'error': 'Authors table does not exist'}
                , status=status.HTTP_404_NOT_FOUND
            )

        return Response({'author_total_count': author_total_count, 'active_status_count': active_status_count})


# class AuthorCreateView(generics.CreateAPIView):
#     permission_classes = [permissions.IsAuthenticated]
#     queryset = Author.objects.none()
#     serializer_class = AuthorSerializer

#     def create(self, request, *args, **kwargs):
#         username = request.data.get('username')
#         email = request.data.get('email')
#         existing_authors = Author.objects.filter(username=username, email=email)

#         if existing_authors.exists():
#             return Response(
#                 {'detail': 'An author with the same username or email already exists.'},
#                 status=status.HTTP_400_BAD_REQUEST
#             )
#         return super().create(request, *args, **kwargs)

# class AuthorListView(generics.ListAPIView):
#     permission_classes = [permissions.IsAuthenticated]
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['username', 'email', 'name']

# class AuthorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [permissions.IsAuthenticated]
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer

#     def destroy(self, request, *args, **kwargs):
#         instance = self.get_object()
#         self.perform_destroy(instance)

#         deleted_author_data = {
#             "username": instance.username,
#             "email": instance.email,
#             "name": instance.name,
#         }
#         return Response(
#             {"detail": "Author deleted successfully", "deleted_author_details": deleted_author_data},
#             status=status.HTTP_200_OK)


# class AuthorDetailedView(generics.RetrieveAPIView):
#     permission_classes = [permissions.IsAuthenticated]
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer    

# class AuthorRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
#     permission_classes = [permissions.IsAuthenticated]
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer

# class AuthorDeleteView(generics.DestroyAPIView):
#     permission_classes = [permissions.IsAuthenticated]
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer

#     def destroy(self, request, *args, **kwargs):
#         instance = self.get_object()
#         self.perform_destroy(instance)

#         deleted_author_data = {
#             "username": instance.username,
#             "email": instance.email,
#             "name": instance.name,
#         }
#         return Response(
#             {"detail": "Author deleted successfully", "deleted_author_details": deleted_author_data}, 
#             status=status.HTTP_200_OK)
