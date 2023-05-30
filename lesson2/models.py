from django.db import models

from lesson2.validators import validate_height


class Person(models.Model):
    first_name = models.CharField('Имя', max_length=30)
    last_name = models.CharField('Фамилия', max_length=30)
    # last_update = models.DateField()
    last_update = models.DateField('Обновление профиля', auto_now=True)
    registration_date = models.DateField('Дата регистрации', auto_now_add=True)

    def __str__(self):
        return f"Person: {self.pk}-{self.first_name}-{self.last_name}"

    def __repr__(self):
        return f"Person: {self.pk}-{self.first_name}-{self.last_name}"


class PersonProfile(models.Model):
    height = models.DecimalField(
        'Рост(см.)',
        max_digits=5,
        decimal_places=2,
        validators=[
            validate_height
        ],
    )
    photo = models.ImageField('Фото', upload_to='photos/books/authors')
    owner = models.OneToOneField(
        Person,
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )

    # class Meta:
    #     verbose_name = ''
    #     verbose_name_plural = ''
    #     objects = ''
    #     ordering = ['height']
    #     order_with_respect_to = ''
    #     indexes = ''
    #     index_together = ''
    #     abstract = True


class Authors(models.Model):
    full_name = models.CharField('Ф.И.О.', max_length=75)
    birth_date = models.DateField('Дата рождения')
    photo = models.ImageField('Фото', upload_to='photos/books/authors')


class Currency(models.Model):
    name = models.CharField(max_length=200)
    html_code = models.CharField(max_length=15)


class Books(models.Model):
    name = models.CharField('Название', max_length=64)
    year = models.SmallIntegerField('Год выпуска')
    title = models.TextField('Описание')
    author = models.ForeignKey(
        Authors,
        on_delete=models.CASCADE,
        related_name='author_books',
        verbose_name='Автор'
    )


class BooksCurrency(models.Model):
    book = models.ForeignKey(
        Books,
        on_delete=models.CASCADE,
        related_name='book_currencies',
        verbose_name='книга'
    )
    currency = models.ForeignKey(
        Currency,
        on_delete=models.CASCADE,
        related_name='currency_books',
        verbose_name='Валюта'
    )
    price = models.IntegerField('Цена')


class BookPhotos(models.Model):
    photo = models.ImageField('Фото', upload_to='photos/books/previews')
    book = models.ForeignKey(
        Books,
        on_delete=models.CASCADE,
        related_name='book_photos',
        verbose_name='Книга'
    )
