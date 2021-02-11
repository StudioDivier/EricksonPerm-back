from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
from django.conf import settings


# СЕО статичных страниц
class SEO(models.Model):
    path = models.CharField(name='path', verbose_name='Адрес страницы', max_length=32, unique=True,
                            choices=settings.PAGES
                            )
    title = models.CharField(name='title', verbose_name='Титульник страницы', max_length=128)
    keywords = models.CharField(name='keywords', verbose_name='Ключевые слова', max_length=1024)
    description = models.CharField(name='description', verbose_name='Описание', max_length=2048)

    class Meta:
        verbose_name = 'СЕО страницы'
        verbose_name_plural = 'СЕО страниц'

    def __str__(self):
        return str(self.title)


# заявки
class Offers(models.Model):

    name = models.CharField(name="name", max_length=128, verbose_name='Имя')
    email = models.EmailField(name='email', unique=True, verbose_name='Почта')
    form = models.CharField(name="form", max_length=128, verbose_name='Форма')

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return str(self.form)


# заявки на программы
class ProgramOffers(models.Model):

    program = models.CharField(name="program", max_length=128, verbose_name='Программа')
    name = models.CharField(name="name", max_length=128, verbose_name='Имя')
    phone = models.BigIntegerField(name="phone", verbose_name='Номер телефона')

    class Meta:
        verbose_name = 'Заявка на программу'
        verbose_name_plural = 'Заявки на программы'

    def __str__(self):
        return str(self.program)


# отзывы (_meta)
class Feeds(models.Model):

    img_detail = models.ImageField(upload_to='feeds/', verbose_name='Изображение на странице отзывов')
    img_detail_alt = models.CharField(name='img_detail_alt', max_length=128, verbose_name='Изображение на странице отзывов (Alt)')
    img_main = models.ImageField(upload_to='feeds/', verbose_name='Изображение на главной странице')
    img_main_alt = models.CharField(name='img_main_alt', max_length=128, verbose_name='Изображение на главной странице (Alt)')
    title = models.CharField(name="title", max_length=128, verbose_name='Заголовок')
    description_short = models.TextField(name="description_short", verbose_name='Описание короткое')  # preview short
    description_long = models.TextField(name="description_long", verbose_name='Описание полное')  # long
    video_review = models.URLField(name='video_review', verbose_name='Видео')

    meta_title = models.CharField(name='meta_title', verbose_name='meta_ title', max_length=128)
    meta_description = models.CharField(name='meta_description', verbose_name='meta_ description', max_length=128)
    meta_keywords = models.CharField(name='meta_keywords', verbose_name='meta_ keywords', max_length=128)

    class Meta:
        verbose_name = 'Отзывы'
        verbose_name_plural = 'Отзывы'

    def get_absolute_url(self):
        return reverse('index:feed_list', args=[self.id])

    def __str__(self):
        return str(self.title)


# тренеры (_meta)
class Trainers(models.Model):

    title = models.CharField(name="title", max_length=128, verbose_name='ФИО')
    description = models.TextField(name="description", verbose_name='Описание')
    img = models.ImageField(upload_to='coach_detail/', verbose_name='Фото')
    img_alt = models.CharField(name='img_alt', max_length=128, verbose_name='Фото альт')

    meta_title = models.CharField(name='meta_title', verbose_name='meta_ title', max_length=128)
    meta_description = models.CharField(name='meta_description', verbose_name='meta_ description', max_length=128)
    meta_keywords = models.CharField(name='meta_keywords', verbose_name='meta_ keywords', max_length=128)


    class Meta:
        verbose_name = 'Тренер'
        verbose_name_plural = 'Тренеры'

    def get_absolute_url(self):
        return reverse('index:coaches_detail', args=[self.id])

    def __str__(self):
        return str(self.title)


class Education(models.Model):
    coach = models.ForeignKey(Trainers, on_delete=models.SET_NULL, null=True, verbose_name='Тренер')
    start = models.IntegerField(name='start_ed', verbose_name='Начал')
    end = models.IntegerField(name='end_ed', verbose_name='Окончил')
    ed_title = models.CharField(name='ed_title', max_length=256, verbose_name='Наименование учреждения')

    class Meta:
        verbose_name = 'Образование'
        verbose_name_plural = 'Образования'

    def __str__(self):
        return str(self.coach.title)


class Experience(models.Model):
    coach = models.ForeignKey(Trainers, on_delete=models.SET_NULL, null=True, verbose_name='Тренер')
    start_exp = models.IntegerField(name='start_exp', verbose_name='Начал')
    title_exp = models.CharField(name='title_exp', max_length=256, verbose_name='Наименование учреждения')

    class Meta:
        verbose_name = 'Опыт'
        verbose_name_plural = 'Опыта'

    def __str__(self):
        return str(self.coach.title)


class WayWork(models.Model):
    coach = models.ForeignKey(Trainers, on_delete=models.SET_NULL, null=True, verbose_name='Тренер')
    way = models.CharField(name='way', max_length=64, verbose_name='Напрвление работы')

    class Meta:
        verbose_name = 'Направление работы'
        verbose_name_plural = 'Направления работы'

    def __str__(self):
        return str(self.coach.title)


# игры
class Games(models.Model):

    title = models.CharField(name="title", max_length=128, verbose_name='Заголовок')
    title_short = models.CharField(name="title_short", max_length=64, null=True, verbose_name='Заголовок короткий')
    img = models.ImageField(upload_to='games/', verbose_name='Изображение')
    img_alt = models.ImageField(name='img_alt', max_length=128, verbose_name='Изображение альт')
    price = models.DecimalField(name='price', max_digits=9, decimal_places=2, verbose_name='Цена')
    description_short = models.TextField(name="description_short", verbose_name='Описание короткое')
    couch = models.ForeignKey(Trainers, on_delete=models.SET_NULL, null=True, verbose_name='Тренер')
    date_day = models.IntegerField(name='date_day', null=True, verbose_name='День')
    date_month = models.IntegerField(name='date_month', null=True, verbose_name='Месяц')
    date_year = models.IntegerField(name='date_year', null=True, verbose_name='Год')
    long = models.CharField(name='long', max_length=64, null=True, verbose_name='Продолжительность')
    description = RichTextUploadingField(null=True, verbose_name='Описание')

    class Meta:
        verbose_name = 'Трансформационная игра'
        verbose_name_plural = 'Трансформационные игры'

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('index:games_detail', args=[self.id])


# Расписание
class WayCouch(models.Model):

    way_t = models.CharField(name='way_t', max_length=128, verbose_name='Наименование направления')

    class Meta:
        verbose_name = 'Направление коуча'
        verbose_name_plural = 'Направления коучинга'

    def __str__(self):
        return str(self.way_t)


class Timetables(models.Model):

    date_day = models.IntegerField(name='date_day', verbose_name='День')
    month = models.CharField(name='date_month', max_length=64, verbose_name='Месяц(словестно)')
    date_full = models.DateField(name='date_full', verbose_name='Дата')
    start = models.TimeField(name='time_start', verbose_name='Начало в:', blank=True, null=True)
    end = models.TimeField(name='time_end', verbose_name='Конец:', blank=True, null=True)
    long = models.CharField(name='long', max_length=64, verbose_name='Продолжительность', blank=True, null=True)
    title = models.CharField(name='title', max_length=128, verbose_name='Заголовок')
    description_short = models.TextField(name='description_short', verbose_name='Описание короткое', blank=True, null=True)
    way = models.ForeignKey(WayCouch, on_delete=models.CASCADE, verbose_name='Направление', blank=True, null=True)
    price = models.CharField(name='price', max_length=16, verbose_name='Цена', blank=True, null=True)

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписания'

    def __str__(self):
        return str(self.title)


# Статьи
class Articles(models.Model):
    img = models.ImageField(upload_to='news/', verbose_name='Изображение новости')
    img_alt = models.CharField(name='img_alt', verbose_name='alt изображение', max_length=32)
    date = models.DateField(name='date', verbose_name='Дата')
    title = models.CharField(name='title', verbose_name='Загаловок', max_length=128)
    description = models.CharField(name='description', verbose_name='Описание', max_length=256)
    keywords_seo = models.CharField(name='keywords_seo', verbose_name='Ключевые слова для СЕО', max_length=1024)
    description_seo = models.CharField(name='description_seo', verbose_name='Описание для СЕО', max_length=2048)
    text = RichTextField()

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return 'Статья {}'.format(self.title)

