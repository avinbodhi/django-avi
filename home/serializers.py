from rest_framework import fields, serializers


class VisitSerializer(serializers.Serializer):
    fromdate = serializers.CharField(max_length=30)
    todate = serializers.CharField(max_length=30)
    noofguest = serializers.CharField(max_length=30)
    typeofacc = serializers.CharField()
