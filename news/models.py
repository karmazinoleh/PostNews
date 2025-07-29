from django.contrib.auth.models import User
from django.db import models

# Create your models here.
# admin = kalemz, password = kalemz

class Articles(models.Model):
    title = models.CharField('Name', max_length=100)
    anons = models.CharField('Anons', max_length=250)
    text = models.TextField('Article')
    date = models.DateTimeField('CreatedAt')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

class Comment(models.Model):
    article = models.ForeignKey('Articles', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField('Comment text')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author.username} on {self.article.title}: \n{self.text}'

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'