from rest_framework import serializers

from ap1.models import Reteta


class RetetaSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reteta
        fields = ['id', 'nume', 'timp_executie']
