from django.core.validators import MinValueValidator
from rest_framework import exceptions, serializers
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    """Сериализатор для подели Product."""

    price = serializers.IntegerField(
        validators=(MinValueValidator(
            0.01,
            message='Цена продукта должна быть больше 0!'
        ),)
    )

    class Meta:
        model = Product
        fields = ('name', 'description', 'price')

    def validate_name(self, value):
        name = value
        if not name:
            raise exceptions.ValidationError(
                'Необходимо указать наименование продукта!'
            )
        return name
    
    @action(detail=False, methods=['POST'])
    def create_product(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    @action(detail=False, methods=['GET'])
    def list_products(self, request):
        serializer = ProductSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)
