from django.db import models

# Create your models here.
# admin = kalemz, password = kalemz

class Articles(models.Model):
    title = models.CharField('Name', max_length=100)
    anons = models.CharField('Anons', max_length=250)
    text = models.TextField('Article')
    date = models.DateTimeField('CreatedAt')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'