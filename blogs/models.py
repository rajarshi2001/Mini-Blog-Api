from django.db import models

# Create your models here.


class Posts(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=200)
    desc = models.TextField()
    url_news = models.URLField() 
    post_img = models.ImageField(upload_to='pro_img', blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title