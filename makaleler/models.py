from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class makale(models.Model):
    author=models.ForeignKey("auth.User",on_delete=models.CASCADE,verbose_name="Yazar")
    title=models.CharField(max_length=50,verbose_name="Başlık")
    content=RichTextField(verbose_name="Makale")
    datetime=models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")#makale ekleme
    def __str__(self):
        return self.title#title da ne yazıyorsa o başlıga o yazılır
class commentt(models.Model):
    article=models.ForeignKey(makale,on_delete=models.CASCADE,verbose_name="Makale",related_name="comments")
    commentauthor=models.CharField(max_length=15,verbose_name="yazan")
    commentcontent=models.CharField(max_length=200,verbose_name="icerik")
    commentdate=models.DateTimeField(auto_now_add=True,verbose_name="tarih")
    def __str__(self):
        return self.commentauthor#title da ne yazıyorsa o başlıga o yazılır