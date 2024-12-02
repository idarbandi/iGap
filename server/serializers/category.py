from rest_framework import serializers

from server.models import Category


class CategoryListSerializer(serializers.ModelSerializer):


    class Meta:
        model = Category
        fields = "__all__"