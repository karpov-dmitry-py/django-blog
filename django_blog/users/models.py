from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):

        max_size_wanted = 300
        super().save(*args, **kwargs)

        image = Image.open(self.image.path)
        if image.height > max_size_wanted or image.width > max_size_wanted:
            result_size = (max_size_wanted, max_size_wanted)
            image.thumbnail(result_size)
            image.save(self.image.path)