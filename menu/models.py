# models.py
from django.db import models
from django.contrib.auth.models import Group
from uuid import uuid4
from mptt.models import MPTTModel  # , TreeForeignKey
from colorfield.fields import ColorField


def upload_to(instance, filename):
    ext = filename.split(".")[-1]

    return f"{uuid4()}.{ext}"


class MenuItem(MPTTModel):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to=upload_to)
    color = ColorField(default="#FF0000")
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="children",
    )
    group = models.ManyToManyField(Group, related_name="menus", null=True, blank=True)

    def __str__(self):
        return self.title

    class MPTTMeta:
        order_insertion_by = ["title"]
