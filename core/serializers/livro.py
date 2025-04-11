from django.core.serializers.base import SerializationError
from attr import fields
from rest_framework.serializers import ModelSerializer

from core.models import Livro

class LivroSerializer(ModelSerializer):
    class Meta: 
        model = Livro
        fields =- "__all__"