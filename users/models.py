from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    # overwriting the save method to add functionality
    def save(self, *args, **kawrgs):
        # running parent save
        super().save(*args, **kawrgs)

        # openning image & resizing
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            # this goes to the file path and overwrites the image
            img.save(self.image.path)
