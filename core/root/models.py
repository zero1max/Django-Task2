from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='images/%Y/%m/%d')
    category = models.ForeignKey("Category", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name    
    
class Category(models.Model):
    title = models.CharField(max_length=155, verbose_name="Kategoriya")
    
    def __str__(self) -> str:
        return self.title