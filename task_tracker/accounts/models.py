from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.forms import ValidationError


class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed')
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    assigned_to = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)

    def clean(self):
        today = timezone.localdate() 

        if self.start_date and self.end_date:
            if self.start_date > self.end_date:
                raise ValidationError('Дата начала не может быть позже даты окончания!')

            if self.end_date < today:
                raise ValidationError('Дата окончания не может быть в прошлом!')
            
            
    def __str__(self):
        return self.title

