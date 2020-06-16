from rest_framework import serializers

class User(serializers.Serializers):
    class Meta:
        model=Registration
        fields='__all__'