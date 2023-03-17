from django.db import models


# Create your models here.
class Profile(models.Model):
    
    First_Name = models.CharField(max_length=20)
    Last_Name = models.CharField(max_length=30)
    E_mail = models.EmailField(max_length=20)
    Phon_number = models.PositiveIntegerField()
    Age = models.PositiveIntegerField()
    Gender = models.CharField(max_length=30)
    NID_Number = models.PositiveIntegerField()
    Address = models.TextField(max_length=50)
    Image = models.ImageField(upload_to='prof_pic/',default='default/default.jpg') ##use to profile show without use image. if blank but show on html file//

    def __str__(self):
        return str(self.First_Name)
