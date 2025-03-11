from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    
# Order items by name and adds the str representation of each item and category    
    class Meta:
        ordering = ('name' ,)
        verbose_name_plural = 'Categories'
        
    
    def __str__(self):
        return self.name
    
    
class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE) # If user deletes category, all items in that category are being deleted
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True) #uploads and create item_mage location on the server if it doesn't exist.
    is_sold = models.BooleanField(default=False)
    create_by = models.ForeignKey(User, related_name='items', on_delete = models.CASCADE) #If user deletes all items, delte all items
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name