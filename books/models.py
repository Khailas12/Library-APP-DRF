from django.db import models
from author.models import Author

class Books(models.Model):
    ALPHANUMERIC_CHOICES = [(str(i), f'BOOK{i}') for i in range(1, 100)]  
    
    book_id = models.CharField(max_length=10, choices=ALPHANUMERIC_CHOICES, unique=True)
    name = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    author_email = models.EmailField()  
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        # Set the author's email
        if self.author:
            self.author_email = self.author.email

        super().save(*args, **kwargs)

    class Meta:
        db_table = 'books'
