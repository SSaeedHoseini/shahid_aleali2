# serializers.py
from rest_framework import serializers
from .models import MenuItem
# from rest_framework_recursive.fields import RecursiveField


class GetMenuItemSerializer(serializers.ModelSerializer):
    # children = RecursiveField(many=True)

    class Meta:
        model = MenuItem
        fields = ["id", "title", "image", "parent" ,"color", "level"]


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ["title", "image", "parent", "color"]
