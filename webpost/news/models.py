from django.db import models


# Create your models here.
class Articles(models.Model):
    title = models.CharField('Название', max_length=50, default='Новый пост')
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Пост')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return f'{self.title} от {str(self.date)[11:16]}'

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
