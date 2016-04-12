from django.db import models

from transmeta import TransMeta


class Metadata(models.Model, metaclass=TransMeta):
    url_name = models.CharField('Роутинг', max_length=100)
    title = models.CharField('Название страницы', max_length=100)
    description = models.CharField('Описание страницы', max_length=250)
    robots = models.CharField('Информация для ботов', max_length=100)

    class Meta:
        verbose_name = 'Метаданные'
        verbose_name_plural = 'Метаданные'

        translate = ('title', 'description',)

    def __str__(self):
        return self.title
