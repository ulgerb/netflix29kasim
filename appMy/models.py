from django.db import models
from appUser.models import *
# Create your models here.

class Category(models.Model):
    title = models.CharField(("Kategori"), max_length=50)
    
    def __str__(self):
        return self.title
class Video(models.Model):
    category = models.ForeignKey(Category, verbose_name=("Kategori"), on_delete=models.CASCADE)
    title = models.CharField(("Video Başlığı"), max_length=50)
    image = models.FileField(("Video"), upload_to="", max_length=100)
    text = models.TextField(("Video Açıklaması"), max_length=500)
    
    def __str__(self):
        return self.title

class LikeVideo(models.Model):
    video = models.ForeignKey(Video, verbose_name=("Beğenilen Video"), on_delete=models.CASCADE)
    profil = models.ForeignKey(Profil, verbose_name=("Beğenen Profil"), on_delete=models.CASCADE)