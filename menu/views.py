# views.py
from .models import MenuItem
from rest_framework import viewsets
from .serializers import MenuItemSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.filter(group__in=request.user.groups.all())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)