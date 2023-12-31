from rest_framework import serializers
from owner.models import Owner

class OwnerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ('nombre', 'edad', 'pais', 'dni')