

from rest_framework import serializers
from Home.models import Note, Transaction

class Note_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'


class Transaction_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'