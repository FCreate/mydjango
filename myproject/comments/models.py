from django.db import models
from myapp.models import Buyer
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
# Create your models here.
class Comment(models.Model):
    user=models.ForeignKey(Buyer)
    #product=models.ForeignKey(Product)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
    object_id = models.PositiveIntegerField(null=True)
    content_object = GenericForeignKey('content_type', 'object_id')
    content=models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True)