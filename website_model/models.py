from django.db import models

# Create your models here.
class Member(models.Model):
    Name=models.CharField(max_length =26)
    Email=models.EmailField()
    HomeTown=models.CharField(max_length=26)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    def __str__(self):
          return self.Name

class ordr(models.Model):
    Article_num=models.CharField(max_length =200)
    sizes=models.CharField(max_length =200)
    delivery_location=models.CharField(max_length =200)
    payment_mode=models.CharField(max_length =200)
    email_id=models.EmailField()
    phone_number=models.IntegerField()
    date=models.DateTimeField()
