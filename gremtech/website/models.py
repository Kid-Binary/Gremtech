from functools import reduce

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from transmeta import TransMeta

"""
Hack to order models in Django Admin. Whitespaces assigned in nested Meta
classes are concatenated with verbose_name_plural to force ordering by
whitespaces number
"""
models.options.DEFAULT_NAMES += ('order_prefix',)


class ContentBlock(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

    def get_template_block_name(self):
        return self.name.replace(' ', '_').lower()


class Intro(ContentBlock, metaclass=TransMeta):
    headline = models.CharField('Деятельность', max_length=200)
    title = models.CharField('Название компании', max_length=100)
    bottomline = models.CharField('Слоган', max_length=200)

    class Meta:
        order_prefix = ' ' * 10

        verbose_name = 'Блок "Intro"'
        verbose_name_plural = order_prefix + 'Блок "Intro"'

        translate = ('headline', 'title', 'bottomline',)


class WeAre(ContentBlock, metaclass=TransMeta):
    headline = models.CharField('Определение', max_length=200)
    title = models.CharField('Заголовок', max_length=100)
    text = models.TextField('Текст', max_length=1000)

    class Meta:
        order_prefix = ' ' * 9

        verbose_name = 'Блок "We Are"'
        verbose_name_plural = order_prefix + 'Блок "We Are"'

        translate = ('headline', 'title', 'text',)

    def get_numbers(self):
        return self.number_set.all()


class WhatWeDo(ContentBlock, metaclass=TransMeta):
    text = models.TextField('Текст', max_length=1000)

    class Meta:
        order_prefix = ' ' * 8

        verbose_name = 'Блок "What We Do"'
        verbose_name_plural = order_prefix + 'Блок "What We Do"'

        translate = ('text',)


class GetInTouch(ContentBlock, metaclass=TransMeta):
    title = models.CharField('Заголовок', max_length=100)
    text = models.TextField('Текст', max_length=1000)

    class Meta:
        order_prefix = ' ' * 7

        verbose_name = 'Блок "Get In Touch"'
        verbose_name_plural = order_prefix + 'Блок "Get In Touch"'

        translate = ('title', 'text',)


class WorkWithUs(ContentBlock, metaclass=TransMeta):
    title = models.CharField('Заголовок', max_length=100)
    text = models.CharField('Текст', max_length=1000)

    class Meta:
        order_prefix = ' ' * 6

        verbose_name = 'Блок "Work With Us"'
        verbose_name_plural = order_prefix + 'Блок "Work With Us"'

        translate = ('title', 'text',)


class Service(models.Model, metaclass=TransMeta):
    action = models.CharField('Услуга', max_length=100)
    subject = models.CharField('Объект услуги', max_length=200)

    class Meta:
        order_prefix = ' ' * 5

        verbose_name = 'Услуга'
        verbose_name_plural = order_prefix + 'Услуги'

        translate = ('action', 'subject',)

    def __str__(self):
        return "%s %s" % (self.action, self.subject)


class Employee(models.Model, metaclass=TransMeta):
    PHOTO_PATH = 'photos/'

    position = models.CharField('Должность', max_length=100)
    name = models.CharField('Имя', max_length=200)
    surname = models.CharField('Фамилия', max_length=200)
    description = models.TextField('Биография', max_length=1000)
    photo = models.ImageField('Фотография', upload_to=PHOTO_PATH)

    class Meta:
        order_prefix = ' ' * 4

        verbose_name = 'Сотрудник'
        verbose_name_plural = order_prefix + 'Сотрудники'

        translate = ('position', 'name', 'surname', 'description',)

    def __str__(self):
        return self.position

    @property
    def full_name(self):
        return ''.join([self.surname, ' ', self.name])

    def get_numbers(self):
        return self.number_set.all()

    def image_thumb(self):
        return '<img src="%s" width="400">' % (self.photo.url)
    image_thumb.allow_tags = True
    image_thumb.short_description = 'Превью'


class Stage(models.Model, metaclass=TransMeta):
    title = models.CharField('Название', max_length=200)

    class Meta:
        order_prefix = ' ' * 3

        verbose_name = 'Стадия'
        verbose_name_plural = order_prefix + 'Стадии'

        translate = ('title',)

    def __str__(self):
        return self.title


class Project(models.Model, metaclass=TransMeta):
    visual_class = models.CharField(max_length=50)
    icon = models.CharField(max_length=50)
    image = models.CharField(max_length=50)
    title = models.CharField('Название', max_length=100)
    intro_phrase = models.CharField('Вступительная фраза', max_length=200)
    description_short = models.CharField('Краткое описание', max_length=200)
    description_full = models.TextField('Подробное описание', max_length=1000)
    description_functionality = models.TextField(
        'Описание функциональности', max_length=1000,
    )
    description_scope = models.TextField(
        'Описание сферы применения', max_length=1000,
    )
    completion = models.IntegerField(
        'Готовность стадии (%)', default=0, validators=[
            MinValueValidator(1),
            MaxValueValidator(100)
        ]
    )

    stage = models.ForeignKey(
        Stage, null=False, blank=False, on_delete=models.PROTECT
    )

    class Meta:
        order_prefix = ' ' * 2

        verbose_name = 'Проект'
        verbose_name_plural = order_prefix + 'Проекты'

        translate = (
            'title',
            'intro_phrase',
            'description_short',
            'description_full',
            'description_functionality',
            'description_scope',
        )

    def __str__(self):
        return self.title

    def get_functionalities(self):
        return self.functionality_set.all()

    def get_scopes(self):
        return self.scope_set.all()


class Functionality(models.Model, metaclass=TransMeta):
    title = models.CharField('Название', max_length=500)

    project = models.ForeignKey(
        Project, null=True, blank=True, on_delete=models.SET_NULL
    )

    class Meta:
        verbose_name = 'Функциональность'
        verbose_name_plural = 'Функциональность'

        translate = ('title',)

    def __str__(self):
        return self.title


class Scope(models.Model, metaclass=TransMeta):
    title = models.CharField('Название', max_length=200)

    project = models.ForeignKey(
        Project, null=True, blank=True, on_delete=models.SET_NULL
    )

    class Meta:
        verbose_name = 'Cфера прменения'
        verbose_name_plural = 'Сферы применения'

        translate = ('title',)

    def __str__(self):
        return self.title


class Number(models.Model, metaclass=TransMeta):
    quantity = models.IntegerField('Значение', default=0)
    extra = models.BooleanField('Плюсик', default=False)
    description = models.CharField('Описание', max_length=50)

    we_are = models.ForeignKey(
        WeAre, null=True, blank=True, on_delete=models.SET_NULL
    )

    employee = models.ForeignKey(
        Employee, null=True, blank=True, on_delete=models.SET_NULL
    )

    class Meta:
        verbose_name = 'Цифра'
        verbose_name_plural = 'Цифры'

        translate = ('description',)

    def __str__(self):
        return self.description

    def get_formatted_quantity(self):
        formatters = [self.quantity_zero_fill, self.quantity_extra_plus]

        quantity = reduce(lambda x, F: F(x), formatters, self.quantity)

        return quantity

    def quantity_zero_fill(self, quantity):
        return str(quantity).zfill(2)

    def quantity_extra_plus(self, quantity):
        if self.extra:
            quantity = ''.join([quantity, '<span>+</span>'])

        return quantity


class Contact(models.Model):
    phone_first = models.CharField('Телефон', max_length=19)
    email_first = models.EmailField('E-mail #1', max_length=254)
    email_second = models.EmailField('E-mail #2', max_length=254)

    class Meta:
        order_prefix = ' ' * 1

        verbose_name = 'Контакты'
        verbose_name_plural = order_prefix + 'Контакты'

    def __str__(self):
        return self._meta.verbose_name
