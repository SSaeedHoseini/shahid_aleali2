# views.py
from .models import MenuItem
from rest_framework import viewsets
from .serializers import GetMenuItemSerializer, MenuItemSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = GetMenuItemSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ("title", "level", "parent__id")

    def get_serializer_class(self):
        if self.action == "list":
            return GetMenuItemSerializer
        return MenuItemSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.filter(group__in=request.user.groups.all())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
