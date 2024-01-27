from rest_framework import serializers
from .models import Author
from django.core.validators import EmailValidator
from django.db.models import Q


class AuthorSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[EmailValidator()])

    class Meta:
        model = Author
        fields = '__all__'
    

    def update(self, instance, validated_data):
        instance.is_active = validated_data.get('is_active', instance.is_active)

        instance.name = validated_data.get('name', instance.name)
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)

        updated_username = validated_data.get('username')
        updated_email = validated_data.get('email')

        if updated_username and updated_username != instance.username or updated_email and updated_email != instance.email:
            existing_author = Author.objects.filter(Q(username=updated_username) | Q(email=updated_email)).exclude(pk=instance.pk).first()
            if existing_author:
                raise serializers.ValidationError({'non_field_errors': ['An author with the same username or email already exists.']})

        instance.save()
        return instance
