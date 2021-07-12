from django.db import models
from cloudinary.models import CloudinaryField
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    '''Class to define a user's profile.
    '''
    user = models.OneToOneField(User, on_delete=CASCADE, null=True)
    profile_pic = CloudinaryField('image', null=True)
    bio = models.TextField(null=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def save_profile(self):
        '''Method to save the profile to the database.
        '''
        self.save()

    def delete_profile(self):
        '''Method to delete the profile from the database.
        '''
        self.delete()

    @classmethod
    def update_profile(cls, id, pic):
        '''Method to update the profile in the database.
        '''
        return cls.objects.filter(id=id).update(profile_pic=pic)

    # def __str__(self) :
    #     user = User.objects.get(id=self.user_id)
    #     return user.username
class Image(models.Model):
    '''Class to define attributes of an image in the gallery, and it's methods.
    '''
    image = CloudinaryField('image', null=True)
    name = models.CharField(max_length=150)
    caption = models.TextField(null=True)
    post_date = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(Profile, on_delete=CASCADE)

    def save_image(self):
        '''Method to save the image to the database.
        '''
        self.save()

    def delete_image(self):
        '''Method to delete the image from the database.
        '''
        self.delete()

    @classmethod
    def update_image(cls, id, image):
        '''Method to update the image in the database.
        '''
        return cls.objects.filter(id=id).update(image=image)
    
    def __str__(self):
        self.name

class Likes(models.Model):
    image = models.ForeignKey(Image, on_delete=CASCADE, related_name="likes")

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes")

class Comment(models.Model):
    comment = models.TextField(null=True)


