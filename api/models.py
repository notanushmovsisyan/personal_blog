from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='media/', null=True, default=False)
    published_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

